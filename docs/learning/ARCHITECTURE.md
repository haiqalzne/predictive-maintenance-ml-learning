# Read the system before changing it

The existing implementation separates data, model selection, final evaluation and inference.

```text
Official UCI snapshot -> checksum/schema validation -> feature allowlist -> fixed split
                                                                            |
                                      training -> EDA -> CV model selection  |
                                                    -> OOF threshold -> fit |
                                                                            v
                                             frozen choice -> final holdout check
                                                               |
                                               model + manifests + receipts
                                                               |
                                               verified loader -> API
```

The final holdout is not an input to model/threshold selection. The service does not read training
data. An artifact checksum binds bytes to a record; it does not establish that its author is trusted.

Paths below are relative to the repository root:

| Read in this order | Responsibility | Question to answer |
|---|---|---|
| `src/predictive_maintenance/cli.py` | Routes data/experiment commands and paths | Where will this command write its files? |
| `dataset.py`, `validation.py` in the same package | Source identity, schema and allowed features | What is rejected, and what information would leak the target? |
| `splitting.py`, `config.py` | Partition and fixed experiment settings | What can the training code access? |
| `modeling.py` | Pipeline, shared folds, selection and threshold | Which parameters are learned, and on which rows? |
| `evaluation.py` | Guarded final evaluation and receipts | When does the holdout become visible, and what is immutable? |
| `inference.py`, `schemas.py`, `api.py` | Verified bundle, input contracts and serving | Does an API request receive the same preprocessing as offline inference? |
| `tests/` | Synthetic fixture, integrity and API checks | Which failures are caught and which claims are not tested? |

Follow one request: six JSON inputs → strict schema → dataset-name mapping → reference-envelope
check → trained preprocessing/model → score → threshold decision → response with warnings.

The reference envelope is a narrow marginal-range check from the original training data, not a
physical operating limit or complete out-of-distribution detector. A changed dataset/split may
require reviewing that contract rather than silently retaining its bounds.

Read `tests/test_modeling.py` beside `modeling.py`, `tests/test_api.py` beside `api.py`, and
`tests/test_inference.py` beside `inference.py`. The tests build local temporary fixture models;
the learning guard in `tests/conftest.py` prevents loading the original bundled artifacts.
