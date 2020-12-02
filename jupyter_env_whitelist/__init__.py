import os

from IPython.core.interactiveshell import InteractiveShell
from notebook.notebookapp import NotebookWebApplication

from .whitelist import filter_env

__version__ = "0.2.0"


def load_jupyter_server_extension(_nb_server_app: NotebookWebApplication) -> None:
    filter_env()


def load_ipython_extension(ipython: InteractiveShell) -> None:
    filter_env()


def unload_ipython_extension(ipython: InteractiveShell) -> None:
    pass
