# Provenance and conversion notes

**Source received:** `Untitled98 (5).html`, a JupyterLab HTML export supplied by the study's first author. It contained eight substantial Python code cells, markdown section titles and many embedded output images. The HTML source is **not** committed because it is not portable, is unusually large, and may contain saved outputs. This code-only release reconstructs the nine research code cells from that export and removes executed outputs.

**Changes to permit public execution:**

1. Removed absolute paths like `C:\Users\RAZU\Downloads\...` and substituted `CKD_UCI_CSV` (default `data/uci_ckd.csv`) and `CKD_SYNTHETIC_CSV` (default `data/simulated_ckd_data.csv`). The generator creates the parent directory before exporting CSV.
2. Updated categorical Seaborn `countplot` and `barplot` calls to provide an explicit hue and hide the duplicate legend; this avoids failures on modern Seaborn/Matplotlib without changing data or plotted category groups.
3. Made the original `N_BOOT=2000` default controllable via `CKD_BOOTSTRAP_REPS` to support quicker software smoke tests (the original default remains 2,000).
4. Split the source into two independent analysis notebooks plus a complete chronological notebook. No original cell output or dataset was bundled.

**Scientific method preservation:** Original seeds, default bootstrap iterations, modeling parameters, predictors, synthetic-data assumptions, feature selection, and stacking architecture were **not** otherwise altered. `METHODS_AND_LIMITATIONS.md` identifies remaining methodological limitations so the publication's numerical workflow is not silently redesigned.

**Validation:** Syntax checking and a direct simulation data-generation run have passed; see `VALIDATION_REPORT.md` for what was and was not independently rerun. This is not an assertion of exact paper-performance replication.