# jupyter-whitelist-env

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
