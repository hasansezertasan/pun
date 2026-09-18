"""Smoke tests for pun package."""


def test_smoke() -> None:
    """Test that the package can be imported."""
    import pun  # noqa: PLC0415

    assert pun is not None
