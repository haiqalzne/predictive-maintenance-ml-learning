# Provenance and fork boundaries

Prepared 23 October 2026.

- Original: [xSkyLiN3/predictive-maintenance-ml](https://github.com/xSkyLiN3/predictive-maintenance-ml).
- Author: Cristóbal Vergara.
- Reviewed starting commit: `20371f21a15ef59598bc2d63be298b3925e434be` (upstream v1.0.1-era source).
- Learning fork: [haiqalzne/predictive-maintenance-ml-learning](https://github.com/haiqalzne/predictive-maintenance-ml-learning).
- Code and documentation license: [MIT](../../LICENSE). The original copyright notice is unchanged.
- Dataset: synthetic UCI AI4I 2020, DOI `10.24432/C5HS5C`, CC BY 4.0; see
  [data attribution](../DATA_ATTRIBUTION.md). Data licensing is separate from the code license.

## What this fork adds

- A learner-facing entry point, environment instructions, code-reading map and milestone roadmap.
- A first lab, experiment template, contribution guidance and explicit verification status.
- A test guard against loading shipped Joblib artifacts, plus regression tests for that guard.
- A narrowly bounded floating-point tolerance in the API test's Wilson interval comparison,
  discovered during local Mac verification; production statistics are unchanged.
- Automatic source/test CI on Linux, macOS and Windows. Original release/container validation is
  manual, with bundled-model execution requiring an explicit input.
- Ignored local learning-run/cache directories and clear separation of original results from
  new learning evidence.

The ML algorithms, model settings, dataset contract, model artifact, upstream reports and original
evaluation receipts are not changed in this initial preparation. Existing completion statements in
`docs/ROADMAP.md`, `CHANGELOG.md` and reports describe the original author's work.

## Assistance and evidence

Initial source review, environment preparation, documentation and verification were AI-assisted
using Codex at the maintainer's request. This does not establish independent learner competence.
Only checks actually run are marked as verified. Do not relabel an imported result as an original
experiment. The planned threshold experiment is intentionally left for a future learning session.

The public repository contains project material only, not private conversation history, personal
study schedules or local machine paths. Git history retains upstream provenance. The original
bundled model is retained as upstream material but is not loaded by the default learning tests;
it is not newly endorsed as safe by this fork.

## Updating from upstream

Keep the `upstream` remote pointed to the original project and `origin` to your fork. Fetching is
not an instruction to merge or run new code automatically. Compare changes, inspect new dependencies
and executable paths, preserve your notes, and rerun checks before adopting an update. Record the
new base revision if the learning baseline changes.
