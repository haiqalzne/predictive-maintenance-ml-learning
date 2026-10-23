# Contributing to the learning fork

This repository welcomes explanations, small exercises, regression tests and reproducible
experiments. Start with [the roadmap](docs/learning/ROADMAP.md). Prefer one learning objective per
change; a negative result with sound evaluation is useful.

Before proposing a change:

1. Follow [setup](docs/learning/SETUP.md), then run dependency checks, Ruff and pytest.
2. Describe the question, baseline, split, selection method and result. Use the
   [experiment template](docs/learning/EXPERIMENT_TEMPLATE.md).
3. Keep preprocessing and threshold tuning inside training/development data. Never select an
   improvement from repeated final-test scores. Disclose any prior exposure to the benchmark.
4. Preserve original attribution and license notices. Clearly distinguish upstream code/results
   from your own changes and record AI assistance when material.
5. Do not commit secrets, personal/customer data, virtual environments, raw/processed datasets,
   serialized models or local experiment directories. Share a reviewed, aggregate report instead.
6. Do not weaken validation, artifact checks or leakage tests just to make a demonstration work.
   Explain any changed contract and test its failure cases.

Open an issue for a proposed larger change and a pull request for a small reviewed change. Keep
learning material in `docs/learning/`; original methodology is historical context, not a completion
record for this fork. Contributions are offered under this repository's MIT license; dataset terms
remain separate. Do not upload course assignment solutions that violate their rules.

There is no supported industrial deployment, security-response service or uptime commitment.
Please do not put credentials or private data into an issue. If accidentally exposed, revoke the
credential and address the exposure rather than assuming deleting the message removes its history.
