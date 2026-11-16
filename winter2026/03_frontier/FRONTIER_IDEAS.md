# Frontier physics / astronomy ideas: ledger, first results, next steps

Written 2026-11-16 by Claude for Deepnil Ray. Read `../README.md` first.

Labels: PROVED (closed symbolically), VERIFIED (computed here, with a control that fired), CONJECTURED (argued, not checked),
OCCUPIED (someone has published it), DEAD (killed, with the reason). Every number below was produced by a script in this
folder unless a source is named.

## 0. Verdict first

- No result in this folder is a discovery. Two ideas were carried to a first computation; both came back without a signal.
- Idea A (radio polarisation alignment, section 2) is the one to keep working on. The pipeline runs, the planted-signal control
  fires, one trap that produces a fake 4 sigma detection has been found and removed, and the decisive data set
  (SPICE-RACS DR2 / POSSUM, about 10^4 to 10^5 sources) has apparently not been used for this test yet (search depth: two
  extended web searches on 2026-11-16, so CONJECTURED open, not confirmed).
- Idea B (Gaia stellar streams as a test of the primordial-magnetic-field fix for the Hubble tension, section 3) is EMPTY with
  today's stream data and becomes a forecast paper. It is still the natural bridge to Prof. Seshadri's field
  (see `../01_seshadri/SESHADRI_DOSSIER.md`).
- Risks, most worrying first: (1) instrumental polarisation leakage can fake alignment inside one telescope field;
  (2) components of one radio galaxy fake alignment unless one source per 10 arcmin is kept; (3) the alignment anomaly being
  tested rests on optical samples of a few hundred quasars and may simply not exist; (4) the PMF-to-subhalo chain in idea B uses
  a fit to one set of simulations.

## 0b. Update 2026-11-17
- Idea A was run on the real SPICE-RACS DR1 catalogue (5,818 reliable RMs): NULL, as forecast. See `askap_alignment/RESULT.md`.
- Black-hole masses from Gaia DR4 astrometric microlensing: OCCUPIED. The Warsaw group (Wyrzykowski, Kruszyńska, Rybicki and
  others) has dark-lens candidates from DR3 and is preparing DR4 analyses; predictions papers exist (arXiv:2609.10705,
  arXiv:2403.14612, arXiv:2412.14844, arXiv:2301.00822). Do not race them.
- New flagship: systematic search for planetary-collision afterglows, VarWISE x Gaia DR4 x ZTF. See `giant_impacts/PLAN.md`.

## 1. Ledger of ideas considered

| # | Idea | Status | Reason |
|---|---|---|---|
| A | Large-scale alignment of intrinsic radio polarisation angles as a test of the cosmological principle and of axion-photon mixing in cosmic magnetic fields, using the new ASKAP catalogues | CARRIED, pilot NULL | section 2 |
| B | Stream-inferred subhalo counts (GD-1, Pal 5, Gaia) as a bound on primordial magnetic fields at the Hubble-tension strength | CARRIED, EMPTY today, forecast possible | section 3 |
| C | Cosmic birefringence tomography with radio galaxies (polarisation angle minus jet axis as a function of redshift) | OCCUPIED | Naokawa et al., arXiv:2504.06709 (method, PRL 2025); arXiv:2610.39449 (first constraints, using Battye, Jackson and Browne 2026 data). Seen in search results on 2026-11-16, abstracts only. |
| D | A "time-dilation dipole": our motion should modulate observed variability timescales of supernovae and quasars across the sky | DEAD | Observed timescales scale with (1 + z_observed), and z_observed is measured spectroscopically, so after the standard correction nothing is left. It is the redshift dipole in different clothes. CONJECTURED from a two-line argument, not searched. |
| E | Asteroid-mass primordial black holes detected through the oscillations they excite when crossing stars (Kepler/TESS asteroseismology) | DEAD by rate | For a 10^21 g black hole the crossing rate is about 6e-8 per year for a Sun-like star and about 1.4e-6 per year for a 10 solar-radius giant (dark matter density 0.4 GeV/cm^3, v = 250 km/s, gravitational focusing included). Kepler has about 10^6 dwarf star-years and 6e4 giant star-years, so fewer than 0.1 events are expected. Hand estimate, not checked by code. |
| F | Self-lensing black holes: Gaia DR4 orbits predict the time of the lensing flash, TESS checks it | PARKED | A 10 solar-mass black hole at 1 au magnifies a Sun-like companion by about 3.6 percent (Einstein radius 0.135 solar radii), but only about 0.5 percent of orbits are aligned, so a Gaia-guided search expects fewer than one event. A blind TESS search is a discovery project, not new physics. Hand estimate. |
| G | Pulsating stars or eclipsing binaries as clocks for the Galactic acceleration field | DEAD | Galactic acceleration gives a fractional period drift of about 3e-19 per second; the intrinsic drift of the most stable pulsating white dwarf is about 2e-17 per second. Hand estimate. |
| H | A supersymmetric-quantum-mechanics treatment of inflationary magnetogenesis | PARKED, partly known | The f to 1/f duality is Giovannini (arXiv:0911.0896). The open question that survives is in the Seshadri dossier ("is k^4 a theorem?"). |

## 2. Idea A: is the polarised radio sky statistically isotropic?

### 2.1 Why it matters
Optical polarisation vectors of quasars were reported to be aligned over gigaparsec regions (Hutsemekers 1998 and later papers).
If real, that violates the cosmological principle or signals new physics on the line of sight; photon mixing with axion-like
particles in a large-scale magnetic field is one proposed mechanism, which makes a null result a joint limit on the coupling and
the intergalactic field. Radio tests so far: JVAS/CLASS at 8.4 GHz, 4290 sources, no alignment (Joshi et al., arXiv:0705.2548);
Tiwari and Jain 2013 and Pelgrims and Hutsemekers (arXiv:1503.03482) reported alignment in sub-samples at about 150 Mpc;
Tiwari and Jain (arXiv:1809.01270) found isotropy in millimetre sources. The status is unsettled. Sources: search-result
abstracts read on 2026-11-16; none of these papers was read in full, and the attribution of each result must be checked
against the paper before it is cited anywhere.

What is new now: broadband surveys give Faraday-derotated (intrinsic) angles for far more sources than before. SPICE-RACS DR1
has 5818 rotation measures over 1300 square degrees (Thomson et al., arXiv:2307.07207); a DR2 exists (mentioned in
arXiv:2606.07919, not opened); POSSUM is building towards about a million.

### 2.2 What was done here (VERIFIED)
Script `polarisation_alignment/align_pilot.py`, data: Van Eck et al. consolidated RM catalogue v1.2.0
(github.com/CIRADA-Tools/RMTable, 59,530 rows, of which only about 2,400 carry a derotated angle).
Statistic: for each source, the length of the mean of exp(2i psi) over its n_v nearest neighbours after parallel transport
along the great circle; S_D is the average over sources. Significance by shuffling angles among positions (2000 shuffles).

| Sample (galactic latitude above 20 degrees, non-Galactic) | N | z at n_v = 20 | p |
|---|---|---|---|
| all, one source per 2 arcmin | 1454 | +4.4 | 0.0005 |
| all, one source per 10 arcmin | 1045 | +1.1 | 0.13 |
| all, one source per 60 arcmin | 736 | +0.3 | 0.36 |
| Tabara-Inoue 1980 + Simard-Normandin 1981 only, one per 60 arcmin | 513 | +1.1 | 0.14 |

Controls: random angles give z = -0.8 (not significant, as required); a planted alignment of 130 sources inside a 30 degree cap
gives z = +7.5 (fires, as required). Outputs: `pilot_output.txt`, `diagnostics_output.txt`.

Reading: the 4 sigma in the first row is produced by several catalogue rows belonging to the same radio galaxy (lobes and
repeated entries within a few arcminutes share an angle). It disappears when one source per 10 arcmin is kept. The pilot is
therefore NULL at N of about 700 to 1000, which is a smaller and more heterogeneous sample than JVAS/CLASS. It does not test
the anomaly; it shows the pipeline works and documents the trap.

### 2.3 Next steps (in order)
1. Prior-art gate, properly: search ADS for alignment tests on SPICE-RACS, POSSUM, LoTSS, MeerKAT and VLASS polarisation
   catalogues; read Joshi 2007, Tiwari and Jain 2013, Pelgrims and Hutsemekers 2015 in full and record exactly which statistic
   and scale each used.
2. Get SPICE-RACS DR1 (CASDA, ASKAP data portal) and DR2 if public. The cloud sandbox cannot reach CASDA; run on Deepnil's PC
   or in a GitHub Actions workflow that pushes results to a branch (the method already used for SearchChev).
3. Forecast before running: with N sources and intrinsic scatter, state the smallest alignment fraction detectable. Write it
   down before looking at the data.
4. Run with one source per 10 arcmin, then per 60 arcmin; add redshifts where available and repeat in three dimensions.
5. Leakage control: repeat with angles shuffled only within each telescope field, and test whether alignment correlates with
   position in the beam. A signal that lives inside single fields is instrumental.
6. If null: convert to an upper limit on the aligned fraction as a function of angular scale, then to a limit on the
   axion-photon coupling times field strength. If positive: do nothing public until step 5 and an independent catalogue agree.

## 3. Idea B: do Gaia stellar streams test the magnetic fix for the Hubble tension?

### 3.1 The chain
A primordial magnetic field of about 0.05 nG is one proposed fix for the Hubble tension (Jedamzik and Pogosian,
arXiv:2004.09487; not re-read today, strength quoted from memory and to be checked). After recombination such a field adds
small-scale matter power and raises the number of dark-matter halos below about 10^9 solar masses. Sanati et al.
(arXiv:2005.05401, read in full) simulated this and fitted the halo-mass-function ratio (their Eq. 12, Table 2). Banik et al.
(arXiv:1911.02663, read in full) measured the subhalo abundance in the inner Milky Way from the GD-1 and Pal 5 streams with
Gaia and Pan-STARRS and published the posterior in closed form (their Eqs. 2.2 to 2.4), noting it can be reused for any model.

### 3.2 What was done here (VERIFIED numerics on a CONJECTURED chain)
Script `pmf_streams/pmf_streams_first_pass.py`. Bin-averaged boost of the subhalo count over cold dark matter, n_B = -2.9:

| B (nG) | 10^5 to 10^6 | 10^6 to 10^7 | 10^7 to 10^8 | 10^8 to 10^9 solar masses |
|---|---|---|---|---|
| 0.05 | 2.9 | 1.9 | 1.1 | 1.0 |
| 0.10 | 2.8 | 4.2 | 2.0 | 1.0 |
| 0.20 | 1.2 | 2.7 | 3.7 | 1.7 |
| 0.50 | 1.0 | 1.0 | 1.8 | 3.6 |

Result with today's stream measurement (two bins, 10^7 to 10^9): no field strength between 0.02 and 2 nG is disfavoured by
more than a factor 2.6, under any of three priors on the subhalo survival fraction. Verdict EMPTY.
Forecast: if four decade bins from 10^5 to 10^9 were each measured to 0.15 dex and agreed with cold dark matter, fields from
0.045 to 0.68 nG would be disfavoured at relative posterior below 0.05; at 0.20 dex only a sliver near 0.1 nG; at 0.30 dex
nothing. Controls: zero-field limit returns a boost of 1; a planted 30-fold boost is rejected (delta lnL = -7.2).

### 3.3 What is assumed (each item can change the answer)
- The Sanati fit is for field halos in a small box at z = 0, applied here to Milky Way subhalos.
- Interpolation between their four field strengths, and extrapolation of the peak mass below 0.05 nG, is my choice.
- Only n_B = -2.9 is covered; the field definition is their B_lambda at 1 Mpc, and the mapping from the pre-recombination
  field of the Hubble-tension papers to B_lambda today was not done.
- Halos formed early from magnetic perturbations are denser, survive tides better and hit streams harder; this would
  strengthen the signal and is not modelled.
- Sanati et al. already used Milky Way satellite counts, so the satellite route is OCCUPIED; they state the mini-halos are out
  of reach of lensing and do not mention streams.
- Prior art for streams specifically: see `../01_seshadri/notes/` if the background search finished; otherwise UNCHECKED.

### 3.4 Next steps
1. Finish the prior-art gate (streams or strong-lensing substructure used for primordial fields).
2. Replace the fit with a direct calculation: magnetic matter power spectrum from MagCAMB (github.com/alexzucca90/MagCAMB),
   then an extended Press-Schechter subhalo function, for a grid in B and n_B.
3. Map the pre-recombination field of the Hubble-tension solution to today's B_lambda using the recent MHD recombination
   papers, and mark that value on the forecast plot.
4. Ask what Gaia DR4, Rubin and the S5 stream sample will deliver per mass decade, and state when 0.15 dex is reachable.
