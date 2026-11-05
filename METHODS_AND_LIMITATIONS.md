# Methods and limitations: scientific provenance

The original notebook uses the UCI CKD 400-record benchmark and a 1,000-record simulated dataset. Original computations are preserved as separate branches; dependency/path/Seaborn fixes are documented in `CONVERSION_NOTES.md`.

## Workflow summary

Stratified split (70% train/30% test; seed 42); median/mode imputation on outer training only; categorical recoding; numeric Z-score capping and min–max scaling learned from outer training; SMOTE; six individual feature selectors (logistic regression, RFE, random forest, mutual information, chi-square, PCA); majority-vote consensus; tuned model baselines; stacking ensemble; test-set bootstrap intervals. Read notebook code for exact implementation details.

## Important qualification 1: stacking CV preprocessing

Although the **outer held-out test set** is not used to fit the preprocessing in the source workflow, the stacking pipeline fits StandardScaler and applies SMOTE before the `StackingClassifier` performs its own 5-fold internal cross-validation to construct meta-features. This means SMOTE samples and global outer-training scaling can leak information between the internal meta-CV folds. Likewise the selected feature list is not re-derived inside each inner fold. Avoid the absolute claim that this particular stacking pipeline is "leakage-free at every validation stage." A rigorously fold-isolated alternative would require refactoring the internal folds, repeating feature selection/preprocessing inside folds and rerunning the analyses; this is a proposed *future improvement*, not the same published numerical protocol.

## Important qualification 2: interpolation of binary clinical features

The source performs SMOTE after mapping nominal/binary variables to numeric 0/1, so synthetic interpolations can take non-binary values on nominal fields. The paper's original protocol is preserved, but future methodological improvements should assess SMOTENC/appropriate categorical handling rather than treating interpolated medical categories as meaningful measurements.

## Important qualification 3: bootstrap uncertainty

The notebook resamples prediction pairs on the **same held-out data split** and does not repeat the entire training, tuning, feature selection or validation scheme for each bootstrap draw. These intervals thus quantify a narrower form of held-out prediction-sample variability, not full end-to-end model-selection uncertainty.

## Important qualification 4: small observational data and synthetic validation

The UCI dataset is small (400 samples) and is not a multi-centre clinical validation study. The simulation generates CKD labels and biomarker values with assumptions determined by the synthetic data generator; its accuracy is not evidence of real-world patient-level performance on a separate clinical cohort. Numerical comparison must be interpreted within these limitations.

## Important qualification 5: tuning and test set

Model hyperparameters and seed are taken as provided in the saved source. The HTML export alone does not prove how all tuning was performed or whether exploratory decisions were made after viewing held-out performance. This package does not add a retrospective claim of prospectively locked hyperparameters.

## Medical-use restriction

Not a diagnostic device. The study and repository code must not be used to make patient diagnosis or treatment decisions without clinical oversight, relevant validation and approvals.