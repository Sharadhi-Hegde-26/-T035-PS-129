import pytest

from src.exception import (
    ProjectError,
    InputFileError,
    ValidationError,
    ProcessingError
)


def test_validation_error():

    with pytest.raises(ValidationError):
        raise ValidationError("Invalid data")


def test_input_file_error():

    with pytest.raises(InputFileError):
        raise InputFileError("File missing")


def test_processing_error():

    with pytest.raises(ProcessingError):
        raise ProcessingError("Processing failed")


def test_custom_errors_inherit_from_project_error():

    assert issubclass(ValidationError, ProjectError)
    assert issubclass(InputFileError, ProjectError)
    assert issubclass(ProcessingError, ProjectError)