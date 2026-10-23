"""Check that the learning setup does not deserialize the upstream model."""

from pathlib import Path

import joblib
import pytest


def test_bundled_artifacts_are_blocked_before_deserialization() -> None:
    artifact = (
        Path(__file__).resolve().parents[1]
        / "artifacts"
        / "m3"
        / "b15bab7b54bc2e1f"
        / "pipeline.joblib"
    )
    with pytest.raises(RuntimeError, match="must not load bundled"):
        joblib.load(artifact)


def test_locally_created_fixture_can_round_trip(tmp_path: Path) -> None:
    artifact = tmp_path / "fixture.joblib"
    joblib.dump({"purpose": "locally generated test fixture"}, artifact)
    assert joblib.load(artifact) == {"purpose": "locally generated test fixture"}
