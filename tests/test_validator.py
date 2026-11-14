import pandas as pd
import pytest

from src.validator import validate_required_columns


def test_valid_columns():

    data = pd.DataFrame({
        "team_id": ["T01"],
        "team_name": ["Alpha"],
        "seed": [1]
    })

    required = ["team_id", "team_name", "seed"]

    assert validate_required_columns(data, required) == True


def test_missing_columns():

    data = pd.DataFrame({
        "team_id": ["T01"],
        "team_name": ["Alpha"]
    })

    required = ["team_id", "team_name", "seed"]

    with pytest.raises(ValueError):
        validate_required_columns(data, required)