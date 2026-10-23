# Verification record

23 October 2026 · initial learning-fork preparation.

## Observed environment

- macOS, Apple Silicon (`arm64`).
- CPython 3.12.13 in an isolated virtual environment.
- Editable source installation with `requirements/constraints-py312.txt` completed.
- Dependency consistency, Ruff lint and formatting checks passed on the unchanged source.

## Checks actually run

| Check | Observed result |
|---|---|
| Dependency consistency (`uv pip check`) | 41 packages checked; compatible |
| Ruff lint | Passed |
| Ruff formatting | 57 files already formatted |
| Full suite after learning-fork changes | **230 passed** in 9.93 seconds on the local host |
| CLI entry point (`python -m predictive_maintenance --help`) | Passed |
| Local links in README/contributing/learning documents | 9 documents checked; no broken local links |
| Diff whitespace checks | Passed |
| Ignore rules | Local learning runs, caches, environment and `.env` excluded |

Durations are an observed run, not a performance promise. Upstream model metrics have not been
reproduced by these tests. Cross-platform GitHub CI status is published separately in Actions;
it was not yet observed at the time this local preparation record was written.

## Portability findings and repairs

The first unchanged-source test run had 227 passes and one failure: two Wilson confidence-interval
values differed in their final floating-point digits on this host. The API shape test now permits
an absolute `1e-15` tolerance only for those interval values, with relative tolerance disabled.
Keys, other fields and the production calculation are unchanged. This is a test portability fix,
not a model improvement.

A subsequent interpreter launch skipped the environment's `.pth` files because those specific
files had macOS hidden flags. Clearing the flags on the two environment files restored the editable
import; no global Python configuration or source import path was changed. See setup troubleshooting.

## Not established by preparation

- No full UCI training run or final holdout evaluation has been performed for this learning fork.
- No bundled serialized model has been loaded as part of the learning setup.
- No live local service, Docker image or public demonstration has been verified for the fork.
- No threshold improvement, real-world generalisation or independent learner competency is claimed.
- Package installation and tests do not constitute a complete dependency/security audit.

The automatic learning workflow runs on Linux, macOS and Windows. Its badge describes the latest
GitHub run, not every historical commit or an industrial safety certification. See the actual run
results before claiming a platform passed.
