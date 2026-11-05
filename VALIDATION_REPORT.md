# Release verification status

- [x] Parsed nine substantive code cells and nine markdown sections from the supplied JupyterLab HTML export.
- [x] Generated three valid Jupyter notebooks without saved execution outputs.
- [x] Python source cells compiled successfully.
- [x] Removed literal desktop paths and embedded notebook audio/image outputs.
- [x] Kept the source's original model hyperparameters and 2,000-bootstrap default.
- [x] Tested the stochastic synthetic CKD generator locally (1,000 rows, 25 columns, reproducible seed).
- [x] Identified and addressed incompatible Seaborn categorical-plot calls.
- [ ] Complete UCI branch on freshly downloaded official UCI data with every original model/stacking metric checked against the published tables.
- [ ] Complete synthetic branch with all classification and stacking models at original settings, verifying all paper scores.
- [ ] Confirm copyright permissions from all relevant code contributors for the MIT software release.
- [x] Upload nine web-optimized publication figures (paper Figures 2–6, 11, 16, 21 and 26), with manifest and explicit attribution/rights notes; do not redistribute KDIGO Figure 1 without permission.
- [x] Run automated GitHub Actions code checks; the 5 November 2026 run completed successfully ([workflow result](https://github.com/beingrazuahmed/ckd-risk-factors-stacking-ml/actions/runs/42018467389)).

**Status:** Professional *code release candidate*; not a fully verified exact numerical replica. Individual smoke-test results may be recorded below if available.