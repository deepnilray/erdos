# Teach me: the Seshadri project and the J060000 star, from the ground up

Written 2026-11-20 by Claude for Deepnil Ray. Part A is the cosmology project (primordial magnetic fields, Seshadri's 2018
model, and why 2025-2026 data now test it). Part B is the star (ASASSN-V J060000.76-310027.83 and its infrared brightening).
Each section only uses ideas explained before it. Anything marked CONJECTURED is my reasoning, not a checked result.

---

# Part A. Primordial magnetic fields and the project

## A1. The question in one paragraph

Every galaxy we can measure is magnetised, at about a microgauss. Nobody knows where the first, weak "seed" fields came from.
One answer is that they were made in the very early universe, during inflation, and have been there ever since. Seshadri,
with Ramkishor Sharma and Kandaswamy Subramanian, wrote a model in 2018 that makes such fields and predicts how strong they
are today and over what length they are coherent. Separately, primordial fields leave a fingerprint on how matter clumps on
small scales, and in 2025-2026 three measurements of small-scale clumping (the Lyman-alpha forest, JWST's early galaxies, and
gravitationally lensed quasars) have started to put numbers on that fingerprint. The project is to ask: given those
measurements, which versions of Seshadri's model survive, and does the tentative 0.2 nanogauss signal in the Lyman-alpha forest
correspond to a particular version of it? The one piece of new theory needed is the clumping produced by a *helical* field,
which is what his model makes and which the 2024-2026 papers explicitly leave out.

The rest of Part A builds every piece of that sentence.

## A2. Units and the language of cosmology

**Gauss and nanogauss.** The gauss (G) is the CGS unit of magnetic field. Earth's field is about 0.5 G. A nanogauss (nG) is
$10^{-9}$ G and a microgauss is $10^{-6}$ G. The energy density of a field is $\rho_B = B^2/8\pi$ in CGS units, so a 1 nG
field holds about $4\times10^{-20}$ erg cm$^{-3}$. The cosmic microwave background (CMB) today holds about
$4\times10^{-13}$ erg cm$^{-3}$, so a 1 nG field carries roughly $10^{-7}$ of the CMB's energy. Primordial fields are tiny in
energy, which is why they can exist without having wrecked the early universe, and why they are hard to detect.

**Scale factor and redshift.** The universe expands uniformly. The scale factor $a(t)$ says how big distances are compared with
today: $a=1$ now, $a=1/2$ when distances were half as big. Light emitted when the scale factor was $a$ arrives stretched by
$1/a$, and astronomers call $1+z = 1/a$ the redshift. Recombination, when the universe became transparent, happened at
$z\approx1100$, so $a_{\rm rec}\approx 1/1100$.

**Comoving versus physical.** A comoving length is a length measured on the expanding grid, scaled to today's size. Two galaxies
sitting still on the grid keep a fixed comoving distance while their physical distance grows as $a$. In this project every length
and every field strength is comoving unless stated otherwise: "0.6 Mpc" means 0.6 megaparsec as it would be today.
A megaparsec (Mpc) is $3.09\times10^{24}$ cm, about 3.26 million light-years; a kiloparsec (kpc) is $10^{-3}$ Mpc.

**Conformal time.** Instead of clock time $t$ it is often easier to use conformal time $\eta$, defined by $d\eta = dt/a$. Light
moves one comoving unit of distance per unit of $\eta$, so in $(\eta, \text{comoving } x)$ coordinates light rays are 45-degree
lines, exactly as in flat spacetime. The metric becomes $ds^2 = a^2(\eta)\,(-d\eta^2 + d\vec x^2)$: flat spacetime multiplied
by $a^2$.

**Wavenumbers.** Cosmologists describe structure by Fourier modes. A wavenumber $k$ corresponds to a wavelength
$\lambda = 2\pi/k$, so $k = 10\ \text{Mpc}^{-1}$ means wavelength about 0.63 Mpc. Large $k$ means small scales. Throughout,
"small scales" means roughly $k \sim 5$ to $100\ \text{Mpc}^{-1}$, which is the scale of dwarf-galaxy halos (masses
$10^6$ to $10^{10}$ solar masses).

**Dex.** "One dex" is a factor of 10 in a logarithm: $\log_{10}$ of a ratio equal to 0.3 means a factor of 2, 1 dex means a
factor of 10, 1.37 dex means a factor of $10^{1.37}\approx 23$.

## A3. Why anyone thinks the fields could be primordial

Galaxies have microgauss fields, clusters of galaxies have fields of order a microgauss, and gamma-ray observations of distant
blazars suggest that even the near-empty voids between galaxies hold fields of at least about $10^{-17}$ to $10^{-15}$ G.
(The argument: TeV photons from a blazar make electron-positron pairs on the way to us; those pairs should produce a halo of GeV
photons by scattering CMB photons; the halo is missing, which is explained if a magnetic field deflects the pairs.) Galactic
fields can be amplified by a dynamo, turbulent motions that stretch and fold field lines, but a dynamo amplifies a field that
already exists. It needs a seed. Fields in voids are especially hard to explain by galaxies leaking magnetised gas, because
voids are far from galaxies. A field made everywhere in the early universe would explain voids naturally. That is the
"primordial magnetic field" (PMF) hypothesis.

## A4. Flux freezing: how a field evolves after it is made

The early universe is an extremely good electrical conductor. In a perfect conductor, magnetic field lines are tied to the
fluid ("frozen in"): the magnetic flux through any surface moving with the fluid is constant. Take a comoving square of side
$L$. Its physical area grows as $a^2$, the flux $B_{\rm phys}\times\text{area}$ is fixed, so $B_{\rm phys}\propto a^{-2}$.
The quantity $B_{\rm comoving} = a^2 B_{\rm phys}$ is therefore constant, which is why papers quote "the comoving field": it is
the field you would see today if nothing but expansion had acted. The energy density $B^2/8\pi$ then falls as $a^{-4}$, the same
as radiation, so the ratio of magnetic to radiation energy stays fixed. This is the "flux-frozen" evolution in Seshadri's paper.

Flux freezing is not the whole story, because magnetic fields push on the plasma and drive turbulence. Turbulence destroys
small-scale structure in the field. Section A7 covers what that does to a helical field.

## A5. Inflation, and why it does not normally make magnetic fields

**Inflation** is a proposed phase, before the hot Big Bang, during which the universe expanded exponentially,
$a\propto e^{Ht}$ with nearly constant Hubble rate $H$. During that phase, quantum fluctuations of fields get stretched to
astronomical sizes and become classical. This is how inflation makes the density fluctuations that grew into galaxies. The
"horizon" is the length $c/H$; a mode is "inside the horizon" when its physical wavelength is shorter than that and "outside"
when longer. The ratio $k/(aH)$ measures this: much bigger than 1 inside, much smaller than 1 outside. During inflation $aH$
grows, so every mode starts inside and ends outside ("horizon exit").

**Why ordinary electromagnetism does not join in.** The Maxwell action is
$$S = -\frac{1}{16\pi}\int d^4x\,\sqrt{-g}\,F_{\mu\nu}F^{\mu\nu},$$
where $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ is the field-strength tensor built from the vector potential $A_\mu$.
Rescale the metric by a position-dependent factor, $g_{\mu\nu}\to\Omega^2 g_{\mu\nu}$. Then $\sqrt{-g}\to\Omega^4\sqrt{-g}$
(four dimensions), while $F^{\mu\nu} = g^{\mu\alpha}g^{\nu\beta}F_{\alpha\beta}$ picks up $\Omega^{-4}$ from the two inverse
metrics, and $F_{\mu\nu}$ itself does not change. The factors cancel: the action is unchanged. This is called conformal
invariance. The expanding universe in conformal time is $a^2\times$(flat spacetime), which is exactly such a rescaling with
$\Omega=a$. So Maxwell's equations in an expanding universe are identical to those in flat spacetime when written in comoving
variables. In flat spacetime, the vacuum does not spontaneously produce photons, so the electromagnetic field is not amplified;
each mode just oscillates, and the physical field dilutes as $a^{-2}$. Any field made early is diluted by the enormous expansion
of inflation to nothing. To make a field during inflation you must break conformal invariance.

## A6. The Ratra-type coupling, step by step

The standard way (Ratra 1992) is to multiply the Maxwell term by a function of time:
$$S = -\frac{1}{16\pi}\int d^4x\,\sqrt{-g}\,f^2(\eta)\,F_{\mu\nu}F^{\mu\nu}.$$
In a real model $f$ depends on the inflaton field, which changes with time, so $f$ is a function of time. Physically, $f$ sets
the strength of electromagnetism: the coupling of charges to this field is $e/f$, so the effective charge is $e_{\rm eff}=e/f$.

**The equation of motion.** Work in Coulomb gauge ($A_0=0$, $\nabla\cdot\vec A=0$) in conformal time. The action reduces to
$S=\frac{1}{8\pi}\int d\eta\,d^3x\,f^2\left[(\vec A')^2-(\nabla\times\vec A)^2\right]$, where a prime is $d/d\eta$. Varying
with respect to $\vec A$ gives $(f^2\vec A')' - f^2\nabla^2\vec A = 0$. For one Fourier mode of wavenumber $k$ this reads
$$A_k'' + 2\frac{f'}{f}A_k' + k^2A_k = 0.$$
The friction-like middle term is the whole effect of the coupling. Remove it by defining $\mathcal A_k = fA_k$. Then
$A_k=\mathcal A_k/f$, and differentiating twice:
$A_k' = \mathcal A_k'/f - \mathcal A_k f'/f^2$,
$A_k'' = \mathcal A_k''/f - 2\mathcal A_k' f'/f^2 - \mathcal A_k f''/f^2 + 2\mathcal A_k f'^2/f^3$.
Substitute into the equation: the $\mathcal A_k'$ terms cancel ($-2f'/f^2 + 2f'/f^2$), the $f'^2$ terms cancel
($+2/f^3 - 2/f^3$), and what is left, multiplied by $f$, is
$$\mathcal A_k'' + \left(k^2 - \frac{f''}{f}\right)\mathcal A_k = 0.$$
This is a harmonic oscillator with a time-dependent frequency. Inside the horizon $k^2$ dominates and the mode oscillates. Outside,
$f''/f$ dominates and, if it is positive and large, $\mathcal A_k$ grows. Growth means many photons produced from the vacuum:
the field is amplified.

**Power-law coupling in de Sitter.** During inflation $a = -1/(H\eta)$ with $\eta<0$ running toward 0 (check:
$da/d\eta = 1/(H\eta^2) = Ha^2$, and $dt = a\,d\eta$ gives $da/dt = Ha$, exponential growth). Take $f\propto a^\alpha$, so
$f\propto(-\eta)^{-\alpha}$. Differentiating twice, $f''/f = \alpha(\alpha+1)/\eta^2$. The equation becomes Bessel's equation,
and the solution that starts as the quantum vacuum deep inside the horizon ($\mathcal A_k\to e^{-ik\eta}/\sqrt{2k}$, the
Bunch-Davies state) is
$$\mathcal A_k = \frac{\sqrt{\pi}}{2}e^{i\pi(\nu+1/2)/2}\sqrt{-\eta}\,H^{(1)}_\nu(-k\eta),\qquad \nu = \alpha+\tfrac12,$$
where $H^{(1)}_\nu$ is a Hankel function. Outside the horizon, $x=-k\eta = k/(aH)\ll1$, and for $\nu>0$ the Hankel function behaves
as $H^{(1)}_\nu(x)\approx -\frac{i}{\pi}\Gamma(\nu)(2/x)^\nu$. So
$|\mathcal A_k|^2 \propto (-\eta)\,(-k\eta)^{-2\nu}\propto k^{-2\nu}$ at fixed time.

**The magnetic spectrum.** The magnetic energy per logarithmic interval of $k$ is, up to constants,
$\frac{d\rho_B}{d\ln k}\propto \frac{f^2k^5|A_k|^2}{a^4} = \frac{k^5|\mathcal A_k|^2}{a^4}\propto k^{5-2\nu} = k^{4-2\alpha}$.
(The $k^5$ is $k^3$ from the phase-space volume of a log interval times $k^2$ from $B=\nabla\times A$.) For $\alpha=2$ the
magnetic spectrum during inflation is scale invariant ($k^0$): equal energy in every decade of scale.

**Two problems, and Seshadri's fix.**
1. *Strong coupling.* The classic models let $f$ decrease during inflation and end at $f=1$ (normal electromagnetism today). Then
   $f$ was tiny at the start, $e_{\rm eff}=e/f$ was enormous, and perturbation theory (the basis of every calculation) fails.
2. *Backreaction.* If the electromagnetic energy grows bigger than the energy driving inflation, it spoils inflation itself.

Sharma, Jagannathan, Seshadri & Subramanian (PRD 96, 083511, 2017; arXiv:1708.08119) let $f$ *grow* during inflation from 1, so
$e_{\rm eff}\le e$ and there is no strong coupling, and then *decrease* after inflation, during a matter-dominated reheating
phase, back to $f=1$ at reheating. Reheating is when the inflaton's energy turns into the hot plasma of the Big Bang, at
temperature $T_r$. The post-inflation fall of $f$ converts the electric field built up during inflation into magnetic field, and
the final spectrum at reheating is (from the paper) $d\rho_B/d\ln k \propto k^{8-2\alpha}$, which is $k^4$ for $\alpha=2$. Avoiding
backreaction puts an upper limit on the reheating temperature: about $1.7\times10^4$ GeV in the 2017 non-helical model.

## A7. Helicity, the inverse cascade, and Seshadri's 2018 numbers

**Helicity.** Magnetic helicity, $\int \vec A\cdot\vec B\,d^3x$, measures how twisted and linked the field lines are. A field
made of circularly polarised waves of only one handedness is fully helical. Sharma, Subramanian & Seshadri (PRD 97, 083503, 2018;
arXiv:1802.04847) added a parity-violating term $f^2F_{\mu\nu}\tilde F^{\mu\nu}$ ($\tilde F$ is the dual tensor). This term
amplifies one circular polarisation more than the other, so the resulting field is almost fully helical. With $f\propto a^2$ the
spectrum is again blue, $d\rho_B/d\ln k\propto k^4$, and backreaction now requires $T_r \lesssim 4000$ GeV.

**Why helicity matters later: the inverse cascade.** In a turbulent plasma, magnetic energy decays, but magnetic helicity is
very nearly conserved. A helical field cannot just lose energy at fixed scale without losing helicity, so instead its energy moves
to larger scales as it decays. This is the inverse cascade. Its rule of thumb: helicity $\sim B^2L$ is conserved, so as the
coherence length $L$ grows, $B\propto L^{-1/2}$. The 2018 paper applies this between reheating and matter-radiation equality and
uses $B_0^{NL} = B_0\,(a_m/a_r)^{-1/3}$ for the field strength ($a_m$ is the scale factor at equality), with the coherence length
growing correspondingly. That is why helical fields end up both stronger on large scales and more coherent than non-helical ones.

**The numbers (Table 1 of 1802.04847, read from the LaTeX source).** These are the *maximal* fields, which assume the
electromagnetic energy reaches the inflaton energy at reheating ($\epsilon=1$):

| Reheating temperature $T_r$ | Field today $B_0$ | Coherence length $L_c$ |
|---|---|---|
| 5 MeV | 6.4 nG | 1.6 Mpc |
| 150 MeV (QCD scale) | 0.99 nG | 0.58 Mpc |
| 100 GeV (electroweak scale) | 0.039 nG | 0.068 Mpc |
| 1000 GeV | 0.0071 nG | 0.032 Mpc |

If only a fraction $\epsilon$ of the inflaton energy goes into the electromagnetic field, $B$ is smaller by $\sqrt\epsilon$ and
$L_c$ is unchanged (stated in the paper). From the table, $L_c\propto T_r^{-1/3}$ and roughly $B\propto T_r^{-1/2}$ across the
middle rows. The $L_c$ scaling has a simple origin (CONJECTURED reading): the field is born coherent on roughly the horizon at
reheating, whose comoving size scales as $1/T_r$, and the inverse cascade then stretches it by a factor that grows as $T_r$ falls
(more time before equality), giving $T_r^{-1}\times T_r^{2/3} = T_r^{-1/3}$.

**Why low reheating temperatures are the interesting corner.** Lower $T_r$ gives stronger, larger fields. The strongest cases
(near 0.1 to a few nG over 0.1 to 1 Mpc) are exactly the fields that small-scale structure now tests. The project is to find
where the line between "allowed" and "excluded" falls in $T_r$ and $\epsilon$.

## A8. Power spectra: how cosmologists measure clumpiness

Write the matter density as $\rho(\vec x) = \bar\rho\,[1+\delta(\vec x)]$; $\delta$ is the density contrast. Fourier transform it
to $\delta(\vec k)$. If the fluctuations are statistically the same everywhere and in every direction, then
$\langle\delta(\vec k)\delta^*(\vec k')\rangle = (2\pi)^3\delta_D(\vec k-\vec k')P(k)$, where $\delta_D$ is the Dirac delta and
$P(k)$ is the power spectrum (units of volume, Mpc$^3$). The dimensionless version
$$\Delta^2(k) = \frac{k^3P(k)}{2\pi^2}$$
is the contribution to the variance $\langle\delta^2\rangle$ from one logarithmic interval of $k$. $\Delta^2\sim1$ at some $k$ means
structures of that size are just becoming nonlinear (collapsing into halos).

In the standard model (ΛCDM, cold dark matter plus a cosmological constant), $\Delta^2$ rises toward small scales only very slowly,
roughly logarithmically, above $k\sim0.1$ Mpc$^{-1}$. The reason: modes that entered the horizon while the universe was dominated
by radiation could barely grow until matter took over (the Mészáros effect), so small scales lost out. This slow rise is
important: anything that adds a *rising* (blue) spectrum on small scales stands out there, even if it is invisible on large scales.

## A9. How a magnetic field makes matter clump after recombination

Before recombination, baryons (ordinary matter: protons, electrons) are glued to photons and cannot move much. After
$z\approx1100$ they decouple, and a magnetic field can push on the ionised part of the gas through the Lorentz force
$\vec F = \frac{1}{4\pi}(\nabla\times\vec B)\times\vec B$ per unit volume. Where the field pushes gas together, the density goes
up. Only the part of the force that compresses or expands gas matters, its divergence. Ralegankar, Pavicevic & Viel (2024,
arXiv:2402.14079) write the baryon density equation as
$$a^2\frac{\partial^2\delta_b}{\partial a^2}+\frac32 a\frac{\partial\delta_b}{\partial a}-\frac32\frac{\Omega_b}{\Omega_m}\delta_b
=-\frac{S_0}{a^3H^2}+\frac32\frac{\Omega_{dm}}{\Omega_m}\delta_{dm},\qquad
S_0 = \frac{\nabla\cdot[(\nabla\times\vec B)\times\vec B]}{4\pi a^3\rho_b},$$
with the dark-matter equation the same but without $S_0$. ($\Omega_b$, $\Omega_{dm}$, $\Omega_m$ are the fractions of the critical
density in baryons, dark matter and total matter.) In the matter era the source $S_0/(a^3H^2)$ is constant in time, because the
comoving field is constant (A4), $a^3\rho_b$ is constant, and $a^3H^2$ is constant when $H^2\propto a^{-3}$. So the source acts
like a steady push switched on at recombination.

What happens next: at first gravity is negligible and $\delta_b$ grows only logarithmically, $\delta_b\approx 2\frac{S_0}{a^3H^2}\ln(a/a_{\rm rec})$.
Once $\frac32\frac{\Omega_b}{\Omega_m}\delta_b$ catches up with the source, self-gravity takes over and the perturbation grows like
any other ($\propto a$). That happens at $a_{\rm gr}\approx a_{\rm rec}e^{\Omega_m/3\Omega_b}\approx 10\,a_{\rm rec}$, so by $z\approx100$
gravity is in charge. Dark matter has no Lorentz force, but baryons pull it along gravitationally, so it lags and then catches up.
The paper packages the time dependence into numbers $\xi_b(a)$ and $\xi_{dm}(a)$ with $\delta^{\rm PMF}=-\xi\,S_0/(a^3H^2)$,
quoting $\xi_b(a=0.01)\approx2.5$. Our code integrates these two coupled equations from recombination and gets
$\xi_b(0.01)=2.27$, close enough that we know the equations are typed correctly (a control).

**Why the result is quartic in $B$.** $S_0$ is quadratic in $B$ (one $B$ from the current $\nabla\times B$, one from the field).
The power spectrum of $S_0$ is the average of a product of two $S_0$'s, so it involves four $B$'s. For a Gaussian random field,
the average of four factors splits into a sum of products of pairs (Wick's theorem), and each pair is a magnetic power
spectrum $P_B$. So the induced matter power is an integral of $P_B(q)\,P_B(|\vec k-\vec q|)$ over all $\vec q$: a convolution.
That is the paper's equation
$$P_b^{\rm PMF}(k) = \xi_b^2\frac{k^4}{8(4\pi a^3\rho_b\,[a^3H^2])^2}\int\frac{d^3q}{(2\pi)^3}\frac{P_B(q)P_B(|\vec k-\vec q|)}{|\vec k-\vec q|^2}[\ldots],$$
where $[\ldots]$ is an angular factor. The $k^4$ in front comes from the two derivatives in $\nabla\cdot[(\nabla\times\vec B)\times\vec B]$
(each $\nabla$ is a factor $k$ in amplitude, so $k^2$ in amplitude and $k^4$ in power).

**Scaling with $k$.** Describe the field by a power law, $P_B(k)\propto k^{n_B}$. Note the convention: $d\rho_B/d\ln k\propto k^3P_B\propto k^{3+n_B}$,
so $n_B=-3$ is scale invariant, $n_B=-2.9$ is nearly so, and Seshadri's $k^4$ spectrum is $n_B=+1$. When $-3<n_B<-1.5$ the convolution
is dominated by $q\sim k$, so it scales as (volume $k^3$)$\times$($P_B^2\sim k^{2n_B}$)$\times$($1/k^2$)$\times$(bracket $k^2$) $= k^{2n_B+3}$.
Multiply by the $k^4$ in front and the $k^3$ in $\Delta^2$: $\Delta^2_{\rm PMF}\propto B^4k^{2n_B+10}$. For $n_B=-2.9$ that is
$k^{4.2}$, steeply rising, against ΛCDM's nearly flat $\Delta^2$. That is why magnetic fields show up on small scales.

**Where it stops: the damping scale.** On small enough scales the field itself is destroyed: magnetic stresses drive plasma motions
that cascade and dissipate the field. The paper models this as a cutoff $e^{-k^2\lambda_D^2}$ in $P_B$, with
$\lambda_D = 0.1\,\kappa\,(B/\text{nG})$ Mpc. It is proportional to $B$ because a stronger field drives faster motions (the Alfvén
speed $v_A=B/\sqrt{4\pi\rho}$ is proportional to $B$), so it can stir and erase larger scales. $\kappa$ is an order-one number that is
not known well; the paper shows the peak height of the induced power scales as $\kappa^{-4}$, so a factor 3 in $\kappa$ moves it by a
factor 100. That is one of the main theoretical uncertainties, and an honest part of the project.

**The peak.** Rising as $k^{2n_B+10}$, cut off at $1/\lambda_D$, the induced spectrum peaks at
$k_{\rm peak}\approx\sqrt{(n_B+5)/2}\,/\lambda_D$. For $n_B=-2.9$ and $\kappa=0.88$: 0.2 nG peaks at 48 Mpc$^{-1}$, 0.5 nG at 20 Mpc$^{-1}$
(our code reproduces both to 0.5 percent). Stronger fields peak at larger scales (smaller $k$). A curious fact from the paper: the
*height* of the peak, $\Delta^2\sim$ order 1 at $z\approx100$, is the same for every $B$; $B$ only moves where it is. Physically, the
damping scale is by definition where the field makes the gas nonlinear.

**Blue spectra are different.** For $n_B>-1.5$, which includes Seshadri's $n_B=+1$, the convolution is no longer dominated by
$q\sim k$; it is dominated by the scale where the field has most of its energy (the peak of the field spectrum, near $1/L_c$, or
the damping scale). Then for $k$ below that peak the induced matter power goes as $P\propto k^4$ ("white noise" from many
independent small kicks). Ralegankar et al. explicitly decline to treat this case ("we do not focus on scenarios with
$n_B>-3/2$"), because the answer depends on exactly how the field spectrum ends at small scales. That is a gap the project fills
for one physically motivated case: Seshadri's.

## A10. The three ways the sky now measures small-scale clumping

**Lyman-alpha forest.** A distant quasar shines through the intergalactic gas. Neutral hydrogen absorbs at the Lyman-alpha
wavelength, 1216 Å in its own rest frame, and because each gas cloud sits at a different redshift, the quasar's spectrum shows a
dense "forest" of absorption lines. The transmitted flux is $F=e^{-\tau}$ with optical depth $\tau$ tracing the gas density along
the line of sight. The power spectrum of $F$ along the line (one-dimensional, in units of velocity, s/km) is sensitive to matter
clumping down to $k$ of tens of Mpc$^{-1}$. The difficulty: the gas is hot, so its lines are blurred by thermal motions, and pressure
smooths the gas; both erase small-scale power and can mimic or hide extra power. Pavicevic et al. (PRL 2025; arXiv:2501.06299) used
about a quarter million simulated models varying the thermal history and found extra small-scale power fitted by
$B_{1\rm Mpc}=0.2\pm0.05$ nG ($n_B=-2.9$), with ΛCDM disfavoured at about $3\sigma$ ($\Delta\chi^2=-12.2$ for one extra parameter).
When they model the instrument noise more conservatively, or drop the smallest-scale data, it becomes an upper limit,
$B<0.30$ nG at $3\sigma$. So: a hint, not a detection. ($B_{1\rm Mpc}$ means the field smoothed over 1 Mpc.) One detail we caught:
the paper's abstract says $k_{\rm peak}\sim20$ Mpc$^{-1}$ for the hint, but its body says 0.2 nG corresponds to 48 Mpc$^{-1}$, and our
calculation agrees with the body.

**JWST and reionisation.** Extra small halos make galaxies earlier, those galaxies reionise the universe earlier, and earlier
reionisation increases the optical depth $\tau$ that CMB photons see when scattering off free electrons. Planck measures $\tau$. Fairbairn
et al. (arXiv:2604.24835, April 2026) calibrate galaxy formation on JWST's ultraviolet luminosity function and find that strong fields
give a "double reionisation" near $z\approx24$, incompatible with Planck. Result: $\sqrt{\langle B^2\rangle}<0.27$ nG for $n_B=-2$ and
$<0.18$ nG for $n_B=+2$ (95 percent), "in Gaussian, non-helical scenarios". The $n_B=+2$ number is close to Seshadri's $n_B=+1$, which
already suggests his strongest cases (about 1 nG) are in trouble, but the helical case has not been done.

**Strong gravitational lensing.** A galaxy between us and a quasar can split it into four images (a "quad"). The brightness ratios of
the images are very sensitive to small dark-matter clumps near the light paths, so "flux-ratio anomalies" count small halos.
Gilman et al. (arXiv:2112.03293) used 11 quads to infer the matter power spectrum relative to ΛCDM:
$\log_{10}(P/P_{\Lambda\rm CDM}) = 0.0\pm0.4$ at $k=10$, $0.1^{+0.7}_{-0.6}$ at $k=25$, $0.2^{+1.0}_{-0.9}$ at $k=50$ Mpc$^{-1}$ (68 percent).
These are honest but wide: a factor of 2.5 to 10.

## A11. What our pilot calculation did, and how to read it

Two scripts live in `pmf_lensing/`.

**`pmf_vs_lensing.py` (lensing alone).** It computes the extra power from $n_B=-2.9$ fields of 0.05 to 0.5 nG and compares with the
lensing numbers above. Result: even 0.5 nG, which the Lyman-alpha forest strongly excludes, sits within 0.7 sigma of the lensing
constraints. So lensing alone cannot yet test the hint (status EMPTY). It will matter once JWST-era lens samples shrink the errors.

**`helical_model_pilot.py` (Seshadri's model).** Step by step:
1. Solve the two-fluid equations of A9 for the growth factor $\xi_m$ (control: $\xi_b(0.01)=2.27$ versus about 2.5 in the paper).
2. Evaluate the convolution integral numerically for any field spectrum, using variables $x=q/k$ and $u=|\vec k-\vec q|/k$, which keep
   the integrable singularity at $\vec q=\vec k$ under control.
3. Fix the overall constant by matching the paper's closed formula for pure power laws. Control: the paper's dimensionless number
   $G_{n_B}$ is reproduced to 3 percent for $n_B=-2.5$ and 0.6 percent for $n_B=-2.0$, and the two calibrations agree to 3 percent.
   For $n_B=-2.9$ the integrand behaves like $x^{-0.9}$ near zero and converges too slowly for the grid, so those reference models use
   the closed formula instead. (This is the kind of trap worth knowing about: a quantity can be finite and still badly computed.)
4. Build Seshadri's spectrum today: $d\rho_B/d\ln k\propto k^4$ below $k_c=2\pi/L_c$ and $\propto k^{-2/3}$ above (the small-scale tail
   is my assumption, a Kolmogorov-like turbulent spectrum), normalised to the table's $B_0$, cut off at $\lambda_D$ with $\kappa=0.88$.
5. Compare with ΛCDM from the CAMB code at $z=30$ (where both grow alike), and report $\log_{10}(P_{\rm total}/P_{\Lambda\rm CDM})$.

**The table, read aloud** (numbers in dex at $k=10$, 20, 30, 50 Mpc$^{-1}$):
- Reference fields with $n_B=-2.9$: 0.2 nG (the hint) gives 0.01, 0.13, 0.33, 0.47; 0.3 nG (the $3\sigma$ bound) 0.06, 0.34, 0.50, 0.23;
  0.5 nG (strongly excluded) 0.26, 0.55, 0.28, 0.00. These calibrate the eye: around 0.5 dex near $k\sim20$-30 is already at the edge.
- Seshadri's model at $T_r=150$ MeV with the maximal field: 0.28, 1.37, 1.08, 0.01. At $k=20$ that is $10^{1.37}\approx23$ times ΛCDM,
  against 3.5 times for the excluded 0.5 nG reference. **Worked example.** $B_0=0.99$ nG gives $\lambda_D=0.1\times0.88\times0.99=0.087$
  Mpc, so the cutoff is at $1/\lambda_D\approx11.5$ Mpc$^{-1}$; the field's energy peaks at $k_c=2\pi/0.58=10.8$ Mpc$^{-1}$. Both say the
  action is near $k\sim10$-30, exactly where the forest is sensitive, and the amplitude is far above anything allowed. Conclusion
  (CONJECTURED): this corner is very likely excluded.
- $T_r=150$ MeV with $\epsilon=10^{-2}$ ($B=0.10$ nG): 0.00, 0.01, 0.06, 0.25, and 0.56 at $k=80$: similar to the hint.
- $T_r=5$ MeV with $\epsilon=10^{-2}$: 0.67, 1.23, 1.21, 0.39: very likely excluded. (With $\epsilon=1$ the 6.4 nG field has
  $\lambda_D=0.56$ Mpc, so it is damped above $k\approx2$ and shows 0.35 dex at $k=5$; that case needs a large-scale treatment.)
- $T_r\ge100$ GeV: no visible effect. Those versions are untouched by these data.

So the picture is: small-scale structure already bites on the low-reheating, high-$\epsilon$ corner of his model, and the Lyman-alpha
hint, if real, would sit around QCD-to-GeV reheating, depending on $\epsilon$.

**What could change the answer, biggest first.** (1) The helical contribution is missing from the kernel. (2) $\kappa$ for blue spectra
is unknown and enters as $\kappa^{-4}$. (3) The small-scale tail of the field after the inverse cascade was assumed. (4) Mapping a
peaked spectrum onto bounds derived for $n_B=-2.9$ is approximate (Pavicevic and arXiv:2609.39399 say models with the same $k_{\rm peak}$
behave alike, which supports the mapping but does not prove it for this shape).

## A12. Why helicity changes the calculation

For a non-helical, statistically isotropic field, the two-point function is
$\langle B_i(\vec k)B_j^*(\vec k')\rangle = (2\pi)^3\delta_D(\vec k-\vec k')\left(\delta_{ij}-\hat k_i\hat k_j\right)\frac{P_B(k)}{2}$
(the bracket keeps $\vec B$ perpendicular to $\vec k$, which is $\nabla\cdot\vec B=0$). A helical field has an extra antisymmetric piece,
$+\,i\,\epsilon_{ijl}\hat k_l\,\frac{P_H(k)}{2}$, where $\epsilon_{ijl}$ is the Levi-Civita symbol and $P_H$ is the helical spectrum
($|P_H|\le P_B$, with equality for a fully helical field). When you compute the four-point average for the Lorentz-force power with
Wick's theorem, products of two antisymmetric pieces give new terms proportional to $P_H(q)P_H(|\vec k-\vec q|)$ with their own angular
factor. For a fully helical field this term is as large as the non-helical one, so it can change the answer by an order-one factor
in either direction (CONJECTURED until computed). Seshadri has done the same type of calculation for the CMB with helical fields
(Jagannathan, Sharma & Seshadri, arXiv:2010.08836), which is why this is home ground for him. The second, probably larger, effect
of helicity is indirect: the inverse cascade sets the spectrum's shape and $L_c$, which we already used.

## A13. The project, as you would do it

1. **Derive** the scalar Lorentz-force power spectrum including the helical term, for general $P_B$ and $P_H$. Check it against the
   non-helical result (set $P_H=0$) and against the paper's $G_{n_B}$ (our code already does this second check).
2. **Model** Seshadri's field today over a grid in $(T_r,\epsilon)$, using the 2018 paper's formulas, with the tail and $\kappa$
   varied to show the theoretical spread.
3. **Confront** each case with the Lyman-alpha bound and hint, the JWST bound, and the lensing numbers, by matching $k_{\rm peak}$ and
   amplitude. Output: a figure in the $(T_r,\epsilon)$ plane with excluded, allowed and "explains the hint" regions.
4. **Forecast** what more Lyman-alpha data (ESPRESSO, DESI) and larger JWST lens samples would add.

What to learn first, in order: Fourier transforms and power spectra; Gaussian random fields and Wick's theorem; the Subramanian review
(Rep. Prog. Phys. 79, 076901, 2016; arXiv:1504.02311) sections on MHD in the expanding universe, inflationary generation and
structure formation; then 1708.08119, 1802.04847, 2402.14079 and 2501.06299 in that order.

## A14. Questions you will be asked, answered now

**Is the Lyman-alpha hint real?** Unknown. It weakens to an upper limit under conservative noise modelling. That is fine for the
project: either way you get a bound on his model, and if the hint survives, the model says which reheating temperature it means.

**Would this kill his model?** No. It removes a corner (low $T_r$, large $\epsilon$) and leaves the rest. A model that makes a
falsifiable prediction which data then test is a good outcome for its authors.

**Why would he say yes?** It extends his own paper, the new piece of theory is a calculation of the type he has done before, and it
ends in a quotable number. Nothing in it argues against his work.

**Why has nobody done it?** The 2024-2026 papers chose non-helical, nearly scale-invariant fields because the blue, helical case depends
on details (the damping and the tail) that are uncertain. That uncertainty is real; the project's job is to show how much the answer
moves with it, not to hide it.

**Who could beat you to it?** His former student Ramkishor Sharma and Subramanian are active on low-scale magnetogenesis
(arXiv:2611.19721, November 2026), and the Trieste group (Viel, Pavicevic, Ralegankar) owns the matter-power pipeline. Proposing it
through Seshadri makes the first group potential collaborators rather than competitors.

**What is $\epsilon$ physically?** The fraction of the inflaton's energy at reheating that ended up in the electromagnetic field. $\epsilon=1$
is the most the model allows before backreaction; real values could be smaller.

**Can I do this without being a theorist?** Steps 2 to 4 are numerical and data comparison, which you already do well. Step 1 is a
careful page or two of Fourier algebra; do it with him.

---

# Part B. The star J060000: what we saw and why it matters

## B1. The object

ASASSN-V J060000.76-310027.83 is a K-type dwarf star (cooler and smaller than the Sun; ATel 13361 fits $T_{\rm eff}=4500\pm100$ K),
157 pc away (Gaia parallax 6.39 mas; distance in parsecs is 1000 divided by the parallax in milliarcseconds). In October 2019 the
ASAS-SN survey saw it fade by about 0.9 magnitude, irregularly, for about 580 days. The leading idea from the 2019-2021 reports is that
something dusty passed in front of it: a "patchy dust ring", possibly around an unseen companion (Kenworthy on the AAVSO campaign page),
with the dimming deeper in blue light than red (Schaefer, ATel 13450), as small dust grains would produce.

## B2. Magnitudes and colours

Astronomers measure brightness in magnitudes: $m = -2.5\log_{10}(F) + \text{constant}$, so brighter means a smaller number, and a change
$\Delta m$ corresponds to a flux ratio $10^{-0.4\Delta m}$. Our star brightened by 0.161 mag in W2: flux ratio $10^{0.4\times0.161}=1.16$,
a 16 percent increase. In W1 it brightened 0.055 mag: 5.2 percent.

W1 and W2 are the two infrared bands of the WISE satellite, at 3.4 and 4.6 micrometres. NEOWISE is WISE's 2014-2024 extension, which
scanned the whole sky every six months, so every star has about 20 snapshots. "W1-W2" is a colour: the magnitude difference between the
bands. A larger W1-W2 means relatively more light at the longer wavelength, which is "redder". A star's photosphere at these wavelengths
is in the Rayleigh-Jeans tail and has W1-W2 near zero. Dust at a few hundred to a thousand kelvin emits mostly in the infrared and much more
at 4.6 than at 3.4 micrometres, so new warm dust makes a star both brighter and redder in W1-W2, which is exactly what we saw (from -0.065 to
+0.04).

## B3. The dust temperature, worked through

Convert magnitudes to flux with the WISE zero points (the flux of a magnitude-0 source): 309.54 Jy in W1 and 171.787 Jy in W2
(1 Jy $=10^{-23}$ erg s$^{-1}$ cm$^{-2}$ Hz$^{-1}$).
- Baseline W1 = 10.524: $F_1 = 309.54\times10^{-0.4\times10.524} = 0.0191$ Jy. The extra light is $F_1(10^{0.4\times0.055}-1)=0.0191\times0.052=0.99$ mJy.
- Baseline W2 = 10.591: $F_2 = 171.787\times10^{-0.4\times10.591}=0.00997$ Jy. The extra light is $0.00997\times(10^{0.4\times0.161}-1) = 1.59$ mJy.
- Ratio of the extra light, W1 to W2: 0.62.

A blackbody at temperature $T$ has $F_\nu\propto\nu^3/(e^{h\nu/kT}-1)$. Evaluating the ratio at 3.35 and 4.60 micrometres gives 0.59 at
800 K and 0.69 at 900 K, so 0.62 means about 820 K. With the W1 measurement error the range is roughly 750 to 900 K. This assumes the new
light is a single-temperature blackbody (CONJECTURED as physics, VERIFIED as arithmetic).

## B4. Why 800 K dust is a clue

Dust in equilibrium with starlight, absorbing and emitting like a blackbody, sits at $T\approx278\,\text{K}\,(L/L_\odot)^{1/4}(r/\text{au})^{-1/2}$,
where $L$ is the star's luminosity and $r$ the distance. For a K dwarf with radius about 0.7 solar and 4500 K, $L\approx0.7^2(4500/5772)^4\approx0.18\,L_\odot$,
so at 1 au the dust would be about 180 K. To be 820 K it must be at $r\approx(180/820)^2\approx0.05$ au (small grains run hotter than blackbodies,
so perhaps a few times farther, still well inside 1 au). A cold ring around a companion orbiting at au-scale distances would be a couple of
hundred kelvin, not 800 K. Hot dust appearing at the same time as the occultation therefore suggests fresh dust close to the star, the kind made
in a collision or a disruption event. This is CONJECTURED; it is the argument a short note would make, with a supervisor checking it.

## B5. Why we trust the brightening is real and belongs to this star

- It is a step between two consecutive six-month visits, then a smooth decline over three years: not one bad measurement.
- The 75 other stars within 15 arcminutes, observed in the same scans, show no such step (largest 0.057 mag, in a fainter star). So it is
  not an instrumental change in that part of the sky.
- The measured position of the source moves smoothly with the star's proper motion and does not jump when it brightens. If a neighbour a few
  arcseconds away had brightened instead, the light centroid would have shifted toward it.
- No Gaia star lies within 6 arcseconds (the WISE beam), and the nearest infrared neighbours are 26 to 27 arcseconds away and 6 to 7 magnitudes fainter.
- The shape of each detection matches a point source (normal fit quality), and the star is far from saturating the detector.

## B6. What is still unchecked, and what to do

The literature check covered all ATels on the star, the AAVSO campaign page, Kenworthy's code repository and six related papers; none mentions
the infrared brightening. ADS, the astronomy paper database, blocks automated searching, so do it by hand: search full text for
"J060000" or "J0600-31" together with "WISE", "NEOWISE" or "infrared". If nothing comes up, the result is a short research note: the light curve,
the 800 K estimate, the timing coincidence with the optical fade, and the argument of B4, written with a supervisor (Seshadri has published
variable-star photometry himself, 2010, so he can judge it).
