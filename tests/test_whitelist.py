import os
from unittest.mock import patch

from jupyter_env_whitelist.whitelist import filter_env


def test_filter_env():
    pass

    with patch.dict(os.environ, {"foo": "1", "bar": "2", "PWD": "pwd"}, clear=True):
        filter_env()
        assert os.environ == {"PWD": "pwd"}

    with patch.dict(os.environ, {"JUPYTER_ENV_WHITELIST": "foo,bar", "foo": "1", "bar": "2", "PWD": "pwd"}, clear=True):
        filter_env()
        assert os.environ == {"foo": "1", "bar": "2"}
