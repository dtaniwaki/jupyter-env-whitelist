from unittest.mock import patch

from jupyter_env_whitelist import (
    __version__,
    load_ipython_extension,
    load_jupyter_server_extension,
    unload_ipython_extension,
)


def test_version():
    assert __version__ == "0.3.0"


def test_load_jupyter_server_extension():
    with patch("jupyter_env_whitelist.filter_env") as m:
        load_jupyter_server_extension(None)
    m.assert_called_once_with()


def test_load_ipython_extension():
    with patch("jupyter_env_whitelist.filter_env") as m:
        load_ipython_extension(None)
    m.assert_called_once_with()


def test_unload_ipython_extension():
    # Ensure no error.
    unload_ipython_extension(None)
