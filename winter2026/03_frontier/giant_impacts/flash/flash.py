"""Giant-impact FLASH detector for Gaia epoch photometry (DR4).
Signature (Tanna et al. 2026, arXiv:2606.26026): near-instant brightening of 1-10 %, then roughly
exponential decay, half-life 1-2000 d.  Model in relative flux: f = c + A*exp(-(t-t_k)/tau) for t >= t_k.
The onset date inside a gap is degenerate with A, so t_k is the first post-onset visit and A is the
excess at first detection.  Score = delta-chi2(flash vs flat) minus delta-chi2(best sinusoid vs flat),
so rotation and pulsation cannot pass.  Extra cuts: A > 0, >= 2 separate post-onset visits above 3 sigma,
>= 3 pre-onset visits (a flat baseline must be seen).  Negative-A fits are returned as 'fade' (side scan).
Input: t (days), G mag, mag error.  Usage: score_lc(t, mag, err) -> dict."""
import numpy as np

TAUS = np.geomspace(1.0, 3000.0, 28)
FREQS = np.geomspace(1/3000., 2.0, 4000)

def _visits(t, gap=1.0):
    """visit index for each epoch (transits within `gap` days form one visit)."""
    o = np.argsort(t); v = np.zeros(len(t), int)
    v[o[1:]] = np.cumsum(np.diff(t[o]) > gap)
    return v

def _lin2(y, w, g):
    """weighted LS of y = c + A g for many templates g (n_tmpl, n). returns A, delta-chi2 vs constant."""
    W = w.sum(); ybar = (w*y).sum()/W
    gbar = (g*w).sum(1)/W
    gc = g - gbar[:, None]
    sgg = (w*gc*gc).sum(1); sgy = (w*gc*(y-ybar)).sum(1)
    ok = sgg > 0
    A = np.where(ok, sgy/np.where(ok, sgg, 1), 0.0)
    return A, np.where(ok, sgy**2/np.where(ok, sgg, 1), 0.0)

def sinus_dchi2(t, y, w):
    ph = 2*np.pi*FREQS[:, None]*t[None, :]
    best = 0.0
    for s in range(0, len(FREQS), 500):  # chunked: 2-template LS via orthogonalised sin/cos
        S, C = np.sin(ph[s:s+500]), np.cos(ph[s:s+500])
        A1, d1 = _lin2(y, w, S)
        r = y[None, :] - A1[:, None]*S
        W = w.sum()
        # second template on residual (Gram-Schmidt approximation, adequate for ranking)
        Cc = C - ((w*C).sum(1)/W)[:, None]
        Sc = S - ((w*S).sum(1)/W)[:, None]
        Cp = Cc - ((w*Cc*Sc).sum(1)/np.maximum((w*Sc*Sc).sum(1), 1e-30))[:, None]*Sc
        rc = r - ((w*r).sum(1)/W)[:, None]
        d2 = (w*Cp*rc).sum(1)**2/np.maximum((w*Cp*Cp).sum(1), 1e-30)
        best = max(best, float((d1+d2).max()))
    return best

def score_lc(t, mag, err, min_pre=3):
    t = np.asarray(t, float); mag = np.asarray(mag, float); err = np.asarray(err, float)
    m = np.isfinite(t) & np.isfinite(mag) & np.isfinite(err) & (err > 0)
    t, mag, err = t[m], mag[m], err[m]
    y = 10**(-0.4*(mag-np.median(mag))) - 1.0      # relative flux
    sig = 0.921*err; w = 1/sig**2
    v = _visits(t); nv = v.max()+1
    vt = np.array([t[v == i].min() for i in range(nv)])
    ks = np.arange(min_pre, nv-1)                     # onset visit; need >=2 visits after
    if len(ks) == 0:
        return dict(score=0., n=len(t), nvis=nv)
    dt = t[None, None, :] - vt[ks][:, None, None]
    g = np.where(dt >= 0, np.exp(-np.clip(dt, 0, None)/TAUS[None, :, None]), 0.0)
    g = g.reshape(-1, len(t))
    A, d = _lin2(y, w, g)
    kk = np.repeat(ks, len(TAUS)); tt = np.tile(TAUS, len(ks))
    out = {}
    for sign, name in ((1, 'flash'), (-1, 'fade')):
        dd = np.where(sign*A > 0, d, 0.0); i = int(dd.argmax())
        out[name] = (float(dd[i]), float(A[i]), float(tt[i]), float(vt[kk[i]]), int(kk[i]))
    dflash, A1, tau1, t0, k = out['flash']
    # >= 2 separate post-onset visits individually above 3 sigma of baseline
    base = y[v < k]; bmu = np.average(base, weights=w[v < k])
    bsd = max(np.std(base), np.median(sig))
    vis_hi = sum(1 for i in range(k, nv) if np.median(y[v == i]) - bmu > 3*bsd/np.sqrt((v == i).sum()))
    dsin = sinus_dchi2(t, y - np.average(y, weights=w), w)
    good = A1 > 0 and vis_hi >= 2
    return dict(score=(dflash - dsin) if good else 0., dchi2_flash=dflash, dchi2_sin=dsin, A=A1, tau=tau1,
                t0=t0, post_vis_hi=vis_hi, fade_dchi2=out['fade'][0], fade_A=out['fade'][1],
                n=len(t), nvis=int(nv))
