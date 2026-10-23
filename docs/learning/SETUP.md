# Setup: source first, tests before models

Use Python **3.12** and an isolated environment. Setup/test execution needs no UCI download, API key,
cloud account, GPU or bundled pretrained model. Installing packages does require network access.
Review downloaded code/dependencies; this guide is not a security guarantee.

## macOS or Linux

From a directory where you keep learning projects:

```bash
git clone https://github.com/haiqalzne/predictive-maintenance-ml-learning.git
cd predictive-maintenance-ml-learning
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install "pip==26.2.1"
python -m pip install -c requirements/constraints-py312.txt -e ".[dev]"
```

If Python 3.12 is not installed and you already use `uv`, replace the environment-creation and
installation steps with:

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -c requirements/constraints-py312.txt -e ".[dev]"
```

`uv` may download a managed Python runtime. Do not reuse or overwrite an unrelated environment.

## Windows PowerShell

```powershell
git clone https://github.com/haiqalzne/predictive-maintenance-ml-learning.git
cd predictive-maintenance-ml-learning
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install "pip==26.2.1"
.\.venv\Scripts\python.exe -m pip install -c requirements/constraints-py312.txt -e ".[dev]"
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest -q
```

## Verify the environment

With the macOS/Linux environment active:

```bash
python --version
python -m pip check
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m predictive_maintenance --help
```

For an environment created without pip by `uv`, use `uv pip check` instead of `python -m pip check`.
Tests use synthetic temporary fixtures. API tests run in process, without a live server or external
requests. Tests may train tiny fixture models; that is not the AI4I baseline experiment.

See [verification](VERIFICATION.md) for observed results and gaps. A passing suite does not prove
security, statistical validity on new data, or readiness for industrial use.

## Start a separate learning run

Do not run default data/training commands from the repository root when reproducing the project:
some default paths overlap the retained upstream manifests and receipts. From the repository root,
with the environment active, create a new, named directory:

```bash
mkdir -p learning-runs/baseline-01
cd learning-runs/baseline-01
python -m predictive_maintenance download
python -m predictive_maintenance validate
python -m predictive_maintenance split
```

These steps contact UCI and create local data/metadata; they are for [Lab 1](LAB_01.md), not required
for setup verification. On Windows, create the folder with `New-Item -ItemType Directory` and use
the activated environment, or invoke its Python executable by its absolute path.

The installed package is accessible from the run directory, so relative output paths stay there.
The entire `learning-runs/` directory is ignored. Never disable checksum checks to accommodate a
changed download; investigate and document a genuinely new dataset revision instead.

After reviewing the training partition and the evaluation protocol, later commands are:

```bash
python -m predictive_maintenance eda
python -m predictive_maintenance train
```

Training selects models and thresholds using training/development data. Do not run
`evaluate-holdout --confirm-final-evaluation` until the final evaluation protocol is frozen.
Do not run `machine-failure-app` yet: the service deliberately requires a consistent, evaluated
local bundle. The later service lab will create and verify that bundle before startup.

## Common setup issues

- Wrong Python: the package deliberately requires 3.12, not 3.11/3.13/3.14. Check the active executable.
- No pip in a uv-created environment: use `uv pip` commands; this is not a broken model package.
- Editable import missing on macOS despite successful installation: inspect `python -v` output.
  If it explicitly says it is skipping hidden `.pth` files, inspect their flags with `ls -lO` and
  clear the hidden flag only on the affected files in **this** virtual environment. For this package:

  ```bash
  chflags nohidden .venv/lib/python3.12/site-packages/__editable__.machine_failure_risk_classifier-1.0.1.pth
  chflags nohidden .venv/lib/python3.12/site-packages/_virtualenv.pth
  ```

  The second file exists only in some environment tools. Do not run a recursive flag change or
  change unrelated system files. Verify the import again after the targeted repair.
- Matplotlib cache permission issue: set `MPLCONFIGDIR` to a writable local cache directory.
- Dependency or wheel failure: retain the error, OS, architecture and versions. Do not silently
  remove constraints or change the global Python installation; propose a tested compatibility change.
- Model/receipt mismatch: do not edit hashes or reuse upstream receipts for a new local artifact.
  Keep each run separate, record its environment and follow the evaluation contract.

## Publication boundaries

Default CI runs source checks/tests only. The upstream Dockerfile and archived README show a
different path that loads a bundled Joblib model; it is not the recommended learning setup. No
public deployment, paid service or automatic retraining is configured by this fork.
