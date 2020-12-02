import os
from unittest.mock import patch

from jupyter_env_whitelist import __version__, load_jupyter_server_extension


def test_version():
    assert __version__ == "0.1.1"


def test_load_jupyter_server_extension():
    app = None

    with patch.dict(os.environ, {"foo": "1", "bar": "2", "PWD": "pwd"}, clear=True):
        load_jupyter_server_extension(app)
        assert os.environ == {"PWD": "pwd"}

    with patch.dict(os.environ, {"JUPYTER_ENV_WHITELIST": "foo,bar", "foo": "1", "bar": "2", "PWD": "pwd"}, clear=True):
        load_jupyter_server_extension(app)
        assert os.environ == {"foo": "1", "bar": "2"}
