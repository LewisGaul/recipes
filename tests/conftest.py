"""
Configuration for tests, including mocking out some of the real behaviour to avoid interfering with
the data we store.
"""

from unittest import mock

import pytest


@pytest.fixture(scope="session", autouse=True)
def open_fixture():
    """
    A fixture to mock the builtin 'open' function to use mock_data.json rather than data.json.
    """
    orig_open = open

    def mock_open(*args, **kwargs):
        if args[0] == "data.json":
            args = ["tests/mock_data.json"] + list(args)[1:]
            if args[1][0] == "w":
                return mock.MagicMock()  # Do nothing
        return orig_open(*args, **kwargs)

    patcher = mock.patch("builtins.open", side_effect=mock_open)
    patcher.start()
    yield
    patcher.stop()


@pytest.fixture
def mock_json_dump():
    """A mock for json.dump()."""
    with mock.patch("json.dump") as m:
        yield m
