# Reproducibility and execution guide

## What is reproducible?

This release provides transparent computational procedures for the public UCI dataset and an independent synthetic generation procedure. Exact numeric reproduction of published scores has **not been independently certified** by this release. Random seeds and fixed hyperparameters are carried over from the exported HTML. Results depend on package versions and on using the same 400-row UCI CKD source, not a different CKD CSV.

## 1. Setup

From repository root, run `python -m pip install -r requirements.txt`. Start Jupyter from this folder so `data/` resolves correctly. Install Jupyter if necessary (`jupyter notebook`). Python 3.11–3.13 is supported by the packages used during preparation; older versions may need appropriate dependency versions.

## 2. UCI (real-data benchmark)

The data are *not bundled*. Run `python scripts/fetch_uci_ckd.py` to fetch UCI dataset ID 336 via `ucimlrepo` and save `data/uci_ckd.csv` with all 24 predictors and the `class` target. This needs internet and should be checked against the published study source. UCI metadata and citation: <https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease>.

Run `python scripts/verify_dataset.py --path data/uci_ckd.csv --expected-rows 400` before opening `notebooks/CKD_UCI_Benchmark.ipynb`. If using your own compatible CKD CSV, explicitly set `CKD_UCI_CSV`; its **25 columns must be in the original order**, and class labels must correspond to CKD / not CKD. The notebook renames columns positionally to preserve the historical paper workflow.

## 3. Synthetic data

Open `notebooks/CKD_Synthetic_Study.ipynb` and run all cells **in order**. The generator writes `data/simulated_ckd_data.csv` with `N=1000`, `TARGET_PREV=0.55`, and seed 42, as in the source HTML. It creates simulated profiles and conditionally generated clinical variables; **these are not independent real patients**. You can redirect output with `CKD_SYNTHETIC_CSV`.

The original code sets several synthetic measurement distributions conditionally on the generated CKD state; this can produce strong prediction even in synthetic data. It does not establish out-of-hospital generalization.

## 4. Separate studies and state

Each branch has its own standalone notebook to prevent accidentally reusing variables left over from the other branch. For direct provenance, the full original-order workflow is also provided in `notebooks/CKD_Full_Research_Workflow.ipynb`. Do not execute the simulation-selection cells after the UCI preprocessing without rerunning the simulation preprocessing first.

## 5. Statistical outputs

Preprocessing uses the original held-out stratified 70:30 split and seed 42, with imputation and z-cap/scaling learned only from the outer training set. Six feature selectors operate on the outer training data and feed model development. Base model comparisons and stacking code produce accuracy, weighted precision, weighted recall, weighted F1 and MCR. Bootstrap confidence intervals resample **fixed held-out (y_true, y_pred) pairs**, rather than repeating all model fitting or selection. The original run uses 2,000 draws; `CKD_BOOTSTRAP_REPS` can be temporarily reduced for development tests.

**Known methodological caveat:** The original StackingClassifier outer pipeline uses scale → SMOTE → stack, so all of its meta-learning CV folds see data scaled and balanced on the *entire outer training set*. This is not a fully nested, fold-isolated preprocessing design. See `METHODS_AND_LIMITATIONS.md`. We preserve this exact study-procedure choice here for provenance, rather than silently replacing it with a changed experiment. Published results should not be treated as an independent external clinical validation.

## 6. Privacy, permissions and dataset credit

UCI CKD data are under CC BY 4.0 and should be attributed to Rubini, Soundarapandian and Eswaran (2015). Do not publish uploaded local medical records or unlicensed modified datasets. Generated simulation CSVs and all notebook outputs are excluded from version control. If you distribute publication figures, follow the article's separate CC BY-NC-SA 4.0 requirements and any third-party figure credit.

## 7. Suggested validation protocol before claiming exact reproduction

(1) Record Python and dependency versions. (2) Verify 400 original UCI rows, 25 columns, and class counts. (3) Rerun the UCI branch from a clean kernel. (4) Rerun the simulated branch separately from a clean kernel. (5) Compare selected predictors and metrics to paper tables, not merely headline accuracy. (6) Re-run with independent seeds and consider a stronger nested-CV protocol as a *new* analysis. Record deviations transparently.