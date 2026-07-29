"""Initial package smoke tests."""

import racing_line


def test_package_version() -> None:
    """The package should expose its initial version."""
    assert racing_line.__version__ == "0.1.0"
