"""Shared offline fixtures for the M1 data contract."""

import os
from pathlib import Path

import joblib
import pandas as pd
import pytest


@pytest.fixture(autouse=True)
def block_bundled_model_loading(monkeypatch: pytest.MonkeyPatch) -> None:
    """Learning-fork safety: tests may load local fixtures, not shipped pickle artifacts."""
    artifact_root = (Path(__file__).resolve().parents[1] / "artifacts").resolve()
    original_load = joblib.load

    def guarded_load(filename, *args, **kwargs):
        candidate = filename if isinstance(filename, (str, os.PathLike)) else filename.name
        if Path(candidate).resolve().is_relative_to(artifact_root):
            raise RuntimeError("Learning tests must not load bundled model artifacts.")
        return original_load(filename, *args, **kwargs)

    monkeypatch.setattr(joblib, "load", guarded_load)


@pytest.fixture
def valid_frame() -> pd.DataFrame:
    """Return a small frame that follows the raw-source contract."""
    return pd.DataFrame(
        {
            "UDI": [1, 2, 3],
            "Product ID": ["L00001", "M00002", "H00003"],
            "Type": ["L", "M", "H"],
            "Air temperature [K]": [295.3, 300.0, 304.5],
            "Process temperature [K]": [305.7, 310.0, 313.8],
            "Rotational speed [rpm]": [1168, 1500, 2886],
            "Torque [Nm]": [3.8, 40.0, 76.6],
            "Tool wear [min]": [0, 100, 253],
            "Machine failure": [0, 1, 0],
            "TWF": [0, 0, 0],
            "HDF": [0, 1, 0],
            "PWF": [0, 0, 0],
            "OSF": [0, 0, 0],
            "RNF": [0, 0, 0],
        }
    )
