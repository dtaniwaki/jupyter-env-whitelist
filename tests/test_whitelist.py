import os
from unittest.mock import patch

from jupyter_env_whitelist.whitelist import filter_env


def test_filter_env():
    with patch.dict(os.environ, {"foo": "1", "bar": "2", "PWD": "pwd"}, clear=True):
        filter_env()
        assert os.environ == {"PWD": "pwd"}

    with patch.dict(os.environ, {"JUPYTER_ENV_WHITELIST": "foo,bar", "foo": "1", "bar": "2", "PWD": "pwd"}, clear=True):
        filter_env()
        assert os.environ == {"foo": "1", "bar": "2"}


def test_filter_env_with_extra_whitelist():
    with patch.dict(
        os.environ, {"JUPYTER_ENV_EXTRA_WHITELIST": "foo", "foo": "1", "bar": "2", "PWD": "pwd"}, clear=True
    ):
        filter_env()
        assert os.environ == {"foo": "1", "PWD": "pwd"}

    with patch.dict(
        os.environ,
        {"JUPYTER_ENV_WHITELIST": "foo", "JUPYTER_ENV_EXTRA_WHITELIST": "bar", "foo": "1", "bar": "2", "PWD": "pwd"},
        clear=True,
    ):
        filter_env()
        assert os.environ == {"foo": "1", "bar": "2"}
