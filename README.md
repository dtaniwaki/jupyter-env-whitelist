# jupyter-whitelist-env

[![Latest PyPI version](https://img.shields.io/pypi/v/jupyter-whitelist-env?logo=pypi)](https://pypi.python.org/pypi/jupyter-whitelist-env)
[![TravisCI build status](https://img.shields.io/travis/com/dtaniwaki/jupyter-whitelist-env?logo=travis)](https://travis-ci.com/dtaniwaki/jupyter-whitelist-env)
[![Test coverage of code](https://codecov.io/gh/dtaniwaki/jupyter-whitelist-env/branch/master/graph/badge.svg)](https://codecov.io/gh/dtaniwaki/jupyter-whitelist-env)

Protect Jupyter Kernel with Whitelist Env.

## Installation

```bash
$ pip install jupyter-whitelist-env
```

## Usage

You can enabled the server extension by the following command.

```bash
$ jupyter serverextension enable --py jupyter-whitelist-env
```

Alternatively, you can enable it by adding the following setting in your `jupyter_notebook_config.py`.

```python
c.NotebookApp.nbserver_extensions = {
    'jupyter_whitelist_env': True,
}
```
