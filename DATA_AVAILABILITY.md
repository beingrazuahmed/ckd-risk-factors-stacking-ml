# Data sources, privacy and access permissions

### UCI Chronic Kidney Disease benchmark

- **Source:** UCI Machine Learning Repository, dataset 336: <https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease>.
- **Source creators:** L. Rubini, P. Soundarapandian, P. Eswaran.
- **Citation:** Rubini, Soundarapandian, and Eswaran (2015), Chronic Kidney Disease [Dataset], UCI ML Repository, DOI <https://doi.org/10.24432/C5G020>.
- **Original dataset license:** CC BY 4.0, attribution required. This dataset is not covered by the repository's MIT *code* license.
- **Distribution:** We do **not** bundle the CKD source records. `scripts/fetch_uci_ckd.py` provides a reproducible download from the official source into the untracked local `data/` directory.

### Synthetic data

Synthetic CKD records are generated locally by the original study's simulation code (1,000 samples, random state 42 by default). They are **simulated biomedical profiles, not real people**, and should not be interpreted as independent clinical evidence. Generated CSVs are excluded by `.gitignore`; users can regenerate them as needed.

### User-supplied clinical datasets

Do not commit identifiable information, personal health records, patient-level hospital data or other restricted records. Users are responsible for appropriate consent, legal basis and local ethical/regulatory requirements. A compatible substitute dataset will not necessarily reproduce the published UCI results.

### Figures and published paper

Full article: <https://doi.org/10.3329/ijss.v25i2.85732>. The publisher lists CC BY-NC-SA 4.0 for the article. Images reproduced from it, or third-party graphics credited therein, require their appropriate attribution and applicable permissions; the MIT software license does not override these rights.