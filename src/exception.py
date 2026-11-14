class ProjectError(Exception):
    """Base exception for the tournament project."""
    pass


class InputFileError(ProjectError):
    """Raised when an input file has a problem."""
    pass


class ValidationError(ProjectError):
    """Raised when input data is invalid."""
    pass


class ProcessingError(ProjectError):
    """Raised when tournament processing fails."""
    pass