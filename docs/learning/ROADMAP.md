# Project-led learning roadmap

Purpose: deepen familiar ML concepts through an existing implementation. Prior study is useful,
but familiarity, passing tests and independent skill are different kinds of evidence. There is no
required whole-course restart or fixed calendar.

## First project: a trustworthy predictive ML service

| Stage | Work | Revise/deepen | Evidence |
|---|---|---|---|
| 0. Prepare | Inspect source, license and dependencies; isolate and test | Python project structure, environments, provenance and artifact trust | Working setup and an explanation of the code map |
| 1. Frame the problem | Trace features/target, verify data and partition | Distributions, base rates, leakage, units and split assumptions | Data card and justified feature allowlist |
| 2. Reproduce | Compare Dummy, logistic regression and random forest on identical folds | Vectors, scaling, sigmoid/log loss, regularisation, optimisation, trees and bias–variance | Reproducible development metrics and reload parity |
| 3. Change one decision | Compare F1 threshold to a predeclared cost-sensitive threshold | Precision/recall, expected loss and decision thresholds | Controlled comparison and honest trade-offs |
| 4. Serve | Verify a locally produced model bundle and prediction API | Input contracts, train–serve consistency, testing and latency | Valid/invalid request tests; offline/API agreement |
| 5. Challenge | Investigate errors, subgroup support and simulated shift | Uncertainty, calibration, robustness and monitoring limits | Failure cases, limitations and a teach-back/change task |

Use short targeted revision when a gap appears. Calculate a small confusion matrix by hand; trace
one scaled feature vector through logistic regression; explain why changing a threshold does not
retrain the model. If gradient mechanics are unclear, use a tiny numerical/analytic check rather
than treating framework output as an explanation.

## Evaluation rules

- Preserve upstream code/results; label a reproduction separately from a new experiment.
- Use the explicit feature allowlist. Never use failure-mode targets or identifiers as predictors.
- Learn preprocessing inside training folds. Compare models using the same development partitions.
- Select models, features, thresholds and calibration using development data only. Freeze the
  protocol before a final test. If test outcomes drive a change, disclose the contamination and seek
  a new independent check; repeatedly resplitting the public benchmark is not external validation.
- Primary ranking metric: average precision; also report prevalence, precision, recall and counts
  of missed failures/false alarms. Accuracy alone is insufficient.
- A possible learning-only cost is `10 * false_negatives + false_positives`. Declare the ratio before
  comparing and do not present it as measured industrial cost. Retain the F1 reference point.
- A score from `predict_proba` is not automatically calibrated. Fit any calibration without the
  final test; otherwise explicitly describe the output as an uncalibrated score.
- Random splits of synthetic observations are limited evidence. Consider ordered-block sensitivity
  later, without claiming real future-time validation. Report subgroup counts and uncertainty.
- Drift in inputs is not itself measured performance loss. Outcome labels are needed; no automatic
  retraining is justified merely by a shifted input distribution.

The first threshold experiment is planned, not implemented here. Preserve the upstream frozen run
and protocol. A changed threshold needs a new named configuration and result; do not mutate old
receipts or use old final-test results to select the new threshold.

## Later integrated projects

1. **Grounded workflow assistant:** compare keyword/classical retrieval with pretrained embeddings
   on held-out questions; evaluate citations, abstention and bounded tool use. Add a small neural
   adaptation only when a measured limitation warrants it.
2. **Reasoning/planning lab:** model explicit constraints for a small scheduling/allocation problem,
   compare an exhaustive tiny baseline with a heuristic, and test infeasibility.

Model operation is embedded in the first two projects, not a separate full project. A small PyTorch
exercise can fill a neural implementation gap, but do not force neural networks into a tabular
problem simply to claim deep-learning coverage. These projects do not equal an entire AI degree;
vision, RL, robotics and other specialist branches remain optional later study.

## Completion standard

Explain the mechanism, predict the effect of a change, make/direct one justified modification,
test valid/invalid/failure cases and diagnose an error. Record the help used. Negative results are
valid; unexplained accuracy gains and copied demos are not the objective.
