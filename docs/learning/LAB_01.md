# Lab 1 — Understand the data and reproduce a baseline

Prerequisites: [setup verification](SETUP.md), basic Python/dataframe reading and prior introductory
ML exposure. This lab is not marked completed by downloading the repository or passing its tests.

## Before running a model

1. Read the feature definitions in `validation.py` and the parameters in `config.py`.
2. State the target, intended input and what a positive prediction would mean. Why can this dataset
   not establish a promise to predict failure a day in advance?
3. Explain why `TWF`, `HDF`, `PWF`, `OSF`, `RNF`, `UDI` and `Product ID` are excluded.
4. Predict what an always-negative classifier would get right and wrong on an imbalanced dataset.
   Why can its accuracy be high while it misses every failure?
5. Trace the split and preprocessing code. Identify where scaling is fitted and which rows it sees.

## Practice

Use the isolated `learning-runs/baseline-01` directory and commands in [setup](SETUP.md). Download,
validate and split the public dataset, then inspect **training-only** EDA. Record the source hash,
feature list, versions, split settings and any data-contract anomalies. Do not overwrite upstream
reports or inspect the final test to decide your model.

Before training, predict which of Dummy, logistic regression and random forest will handle
nonlinear feature interactions best, and why more complexity might still fail. Then run the
training/development comparison and record what happened; prediction and observation may differ.

Use the [experiment template](EXPERIMENT_TEMPLATE.md). Explain average precision, precision,
recall and the confusion matrix in your own words. Separate a classifier's ranking from the
decision made by its threshold.

## Exit check

- Trace one data row from input through preprocessing to score and decision.
- Explain one way leakage could create a misleading improvement.
- Explain why a constant baseline belongs in the comparison.
- Explain why choosing a threshold on the final test would compromise that test.
- Re-run an unchanged development experiment and explain any discrepancy without editing old
  metrics or claiming byte-identical model files across platforms.

Do not consume the final holdout or implement the threshold extension merely to finish this lab.
Review the protocol first. A course section or a worked example may support the explanation;
record that assistance. The next lab will change one threshold-selection objective while preserving
the same development comparison and a separate, frozen final-check policy.
