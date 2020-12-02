# jupyter-env-whitelist

[![Latest PyPI version](https://img.shields.io/pypi/v/jupyter-env-whitelist?logo=pypi)](https://pypi.python.org/pypi/jupyter-env-whitelist)
[![TravisCI build status](https://img.shields.io/travis/com/dtaniwaki/jupyter-env-whitelist?logo=travis)](https://travis-ci.com/dtaniwaki/jupyter-env-whitelist)
[![Test coverage of code](https://codecov.io/gh/dtaniwaki/jupyter-env-whitelist/branch/main/graph/badge.svg)](https://codecov.io/gh/dtaniwaki/jupyter-env-whitelist)

Protect Jupyter Kernel with Whitelist Env.

## Installation

```bash
$ pip install jupyter-env-whitelist
```

## Usage

You can enabled the server extension by the following command.

```bash
$ jupyter serverextension enable --py jupyter-env-whitelist
```

Alternatively, you can enable it by adding the following setting in your `jupyter_notebook_config.py`.

```python
c.NotebookApp.nbserver_extensions = {
    'jupyter_env_whitelist': True,
}
```
