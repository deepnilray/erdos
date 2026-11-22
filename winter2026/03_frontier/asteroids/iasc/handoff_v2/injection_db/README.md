# IASC tracker training database (PS1 practice set XY54_p10)
Built 2026-11-21 from the real ps1-NewPractice_3 images.
- tracker.py: detection + linking with tunable Params (same logic as iasc_hunt.py at defaults; verified to reproduce T000/T001).
- build_db.py: injects trailed synthetic movers (Moffat PSF per-image FWHM, Poisson noise, 0.05-15 "/min, w 19-24) into the real images; truth in injections.csv; tracklet features + labels (1 injected/real-known, 0 false, -1 real unknown) in tracklets_features.csv; SQLite iasc_train.db. Train region = left half of image, test region = right half.
- tune.py: threshold grid on train region (mag 21-23.5), final check on held-out test region.
Results: see tune_*.json. Limits: one field only; injected objects are a model; nothing recovered fainter than w 22 in any setting.
