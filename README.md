# CKD Risk Factors and Stacking Machine Learning

[![Published paper](https://img.shields.io/badge/Published-IJSS%202025-245E78)](https://doi.org/10.3329/ijss.v25i2.85732)
[![Article DOI](https://img.shields.io/badge/DOI-10.3329%2Fijss.v25i2.85732-blue)](https://doi.org/10.3329/ijss.v25i2.85732)
[![Dataset: UCI 336](https://img.shields.io/badge/UCI%20Dataset-336-2e7d32)](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)
[![Research code license](https://img.shields.io/badge/Code%20license-MIT-informational)](LICENSE)

Public research-code companion for the peer-reviewed article:

> **Ahmed, M. R., Rakib, M. A., Shiddik, A. B., & Reza, M. S. (2025).** Identification of Predisposing Risk Factors for Chronic Kidney Disease and Optimizing Disease Prediction Using a Stacking Machine Learning Algorithm. *International Journal of Statistical Sciences*, **25**(2), 1–32. <https://doi.org/10.3329/ijss.v25i2.85732>

**Maintainer:** [Md. Razu Ahmed](https://orcid.org/0009-0001-8646-1881) · [Email](mailto:razuahmed038@gmail.com) · [Academic portfolio](https://beingrazuahmed.github.io/projects.html#ckd-prediction-project).

## Research overview

This study investigates chronic kidney disease (CKD) indicators and binary disease-status prediction using a **real-world public UCI CKD benchmark** and a **separate synthetic simulation**. The research code demonstrates missing-value handling, train/test separation, clinical-feature recoding, numeric outlier capping, feature selection, classification models, stacking ensembles, and confidence intervals. It is a *retrospective research benchmark*, **not an approved clinical decision system**.

| Research branch | Dataset | Sample size | Reported stacking test accuracy |
|---|---|---:|---:|
| UCI CKD | [UCI Machine Learning Repository, dataset 336](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease) | 400 | **100.0%** |
| Simulated CKD | Independently generated study-specific synthetic records | 1,000 | **96.7%** |

These figures are **reported in the published article**, *not* independently verified full-run results for this release. Synthetic results are not external clinical validation; perfect accuracy on a small public benchmark must not be interpreted as clinical diagnostic performance. Reproducing exact values depends on data, software versions and the original experimental procedure.

### Core methods

- Median/mode imputation; harmonized categorical labels and clinically interpretable encoding.
- Train-derived Z-score capping and min–max scaling of numeric variables.
- SMOTE-based balancing of the outer training set.
- **Six selectors:** logistic regression, recursive feature elimination, random forest, mutual information, chi-square, and PCA-based ranking; majority-vote feature consensus.
- Individual model baselines including KNN, SVM, Random Forest, Gaussian NB, Logistic Regression, MLP, and optional XGBoost.
- Stacking ensemble and bootstrap confidence intervals for held-out prediction metrics.

**Methodological qualification:** The source code keeps the published stacking structure, in which scaling and SMOTE precede internal `StackingClassifier` CV. Accordingly it should not be characterized as *fully fold-isolated* nested preprocessing. Additional limitations appear in [METHODS_AND_LIMITATIONS.md](METHODS_AND_LIMITATIONS.md). The study also applies original feature selection once on the outer training split, rather than within every inner stacking fold.

## Repository structure

```text
.
├── notebooks/
│   ├── CKD_Full_Research_Workflow.ipynb
│   ├── CKD_UCI_Benchmark.ipynb
│   └── CKD_Synthetic_Study.ipynb
├── scripts/
│   ├── fetch_uci_ckd.py
│   ├── verify_dataset.py
│   └── check_release.py
├── tests/
├── figures/README.md             # Figure documentation; optimized images in upload package
├── data/.gitkeep                 # No patient-record CSV files committed
├── README.md, REPRODUCIBILITY.md, METHODS_AND_LIMITATIONS.md
├── DATA_AVAILABILITY.md, AUTHORS.md, CITATION.cff, CITATION.bib
├── LICENSING.md, LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md
└── requirements.txt, environment.yml, .github/workflows/quality.yml
```

## Quick start

**Python 3.11 or later recommended.** Open a terminal inside the extracted repository directory.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Official UCI data citation: [Rubini, Soundarapandian and Eswaran (2015), DOI 10.24432/C5G020](https://doi.org/10.24432/C5G020).

**Option A — Public UCI data (requires internet once):**

```bash
python scripts/fetch_uci_ckd.py
python scripts/verify_dataset.py --path data/uci_ckd.csv --expected-rows 400
jupyter notebook notebooks/CKD_UCI_Benchmark.ipynb
```

**Option B — Synthetic study (no original patient-record CSV needed):**

```bash
jupyter notebook notebooks/CKD_Synthetic_Study.ipynb
```

The first synthetic notebook code cell generates `data/simulated_ckd_data.csv` locally with random state 42; run the remaining analysis cells in order. These locally generated files are excluded from GitHub by `.gitignore`.

**Option C — Complete source workflow:** use `notebooks/CKD_Full_Research_Workflow.ipynb` after preparing the UCI dataset.

**Custom data:** set environment variable `CKD_UCI_CSV` to a compatible, authorized CSV with the same **25 columns and column order** as the original notebook; set `CKD_SYNTHETIC_CSV` to customize simulation output location. Please review [REPRODUCIBILITY.md](REPRODUCIBILITY.md) for full details.

**Fast test:** `CKD_BOOTSTRAP_REPS=50` can reduce bootstrap draws for local code checks, **not for reproducing the published study**. The original default remains 2,000. Hyperparameters and model fits may take time on CPU hardware.

## Research visuals

The complete **figure-ready upload package** includes nine optimized study figures (2–6, 11, 16, 21 and 26), plus a detailed figure manifest and third-party rights notices. Figure 1 (KDIGO 2024) is excluded pending separate permission. The hosted gallery will display once the figure assets are uploaded.

## Reproducibility status and limitations

The exported notebook was converted to valid `.ipynb` files, outputs removed, and the code adjusted for local file portability and modern Seaborn. The stochastic simulation generator was tested. A full rerun of all reported models and both stacking analyses is **not yet certified**; see [VALIDATION_REPORT.md](VALIDATION_REPORT.md). Do not claim the paper's two exact accuracies were independently reproduced by this release.

- [Detailed reproduction guide](REPRODUCIBILITY.md)
- [Dataset provenance and data rights](DATA_AVAILABILITY.md)
- [Methodological qualifications](METHODS_AND_LIMITATIONS.md)
- [Conversion and code changes](CONVERSION_NOTES.md)
- [Validated environment and smoke tests](TESTED_ENVIRONMENT.md)
- [Code versus paper/figure licensing](LICENSING.md)
- [Citation instructions](CITATION.cff)
- [GitHub repository About metadata](GITHUB_ABOUT.md)

## Citation

Please **cite the published article** whenever using or describing the CKD analysis, and **cite the UCI dataset separately** if using its records: <https://doi.org/10.24432/C5G020>. See [CITATION.bib](CITATION.bib). When reusing code, retain copyright notices and comply with the code license.

## Authors and contact

Original paper: **Md. Razu Ahmed**, **Md. Abdur Rakib**, **Abu Bakar Shiddik**, **Md. Shamim Reza**. For code inquiries and corrections: **Md. Razu Ahmed** · `razuahmed038@gmail.com` · [ORCID](https://orcid.org/0009-0001-8646-1881). All authorship and attribution details are in [AUTHORS.md](AUTHORS.md).

## License, ethics and disclaimer

- **Software:** [MIT](LICENSE), intended for public research code, subject to confirmation of coauthor/contributor permissions.
- **Public UCI dataset:** [CC BY 4.0](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease), with its own attribution requirement; download from source.
- **Published article and any publisher figures:** [CC BY-NC-SA 4.0](https://www.banglajol.info/index.php/ijss/article/view/85732); not covered by this repository's MIT code license.
- **Locally supplied clinical data:** never included in this repository; only use data you are authorized to process.

The code provides an educational/research benchmark and **must not be used to diagnose, triage, or recommend treatment for patients** without independent, appropriately validated clinical evaluation and regulatory approval where required.