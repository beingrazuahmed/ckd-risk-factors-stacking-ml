# Code validation environment

**Local software audit:** 5 November 2026.

| Package | Local version |
|---|---|
| Python | 3.13.5 |
| NumPy | 2.3.5 |
| pandas | 2.2.3 |
| SciPy | 1.17.0 |
| scikit-learn | 1.8.0 |
| imbalanced-learn | 0.14.1 |
| XGBoost | 3.1.3 |
| matplotlib | 3.10.8 |
| seaborn | 0.13.2 |
| nbformat | 5.10.4 |

The test environment also included the system's normal Python scientific dependencies. The fresh-data retrieval dependency `ucimlrepo` was not installed here and was not remotely fetched because local network access was unavailable. The `fetch_uci_ckd.py` normalization logic was tested against correctly-shaped test data, but actual remote retrieval remains unverified.

Both end-to-end analysis branches passed **software smoke tests** using synthetic data and reduced model workloads (bootstrap draws set to 20, 35 RF/XGBoost estimators for tests, MLP 70 iterations for tests and internal stack CV reduced to 3 folds). The actual distributed research notebooks **retain the original** 500/600 estimator counts where used, MLP max_iter=800, stack CV=5 and N_BOOT=2000 by default. Smoke-test metrics are not valid independent reproductions of the paper's reported accuracies.

For rigorous scientific reproducibility, run the original settings against the official 400-row UCI data and separately regenerate the simulation, recording all software versions, selected features, metrics, confidence intervals and any deviations. See `REPRODUCIBILITY.md`.