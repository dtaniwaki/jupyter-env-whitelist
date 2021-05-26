import os

default_whitelist = [
    "PWD",
    "KERNEL_USERNAME",
    "KERNEL_HUB_USERNAME",
    "HOME",
    "LANG",
    "SHLVL",
    "KERNEL_LANGUAGE",
    "TERM",
    "CLICOLOR",
    "PAGER",
    "NO_PROXY",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "LD_LIBRARY_PATH",
    "PATH",
]


def filter_env() -> None:
    whitelist_str = os.environ.get("JUPYTER_ENV_WHITELIST", None)
    if whitelist_str is not None:
        whitelist = [s.strip().upper() for s in whitelist_str.split(",") if s]
    else:
        whitelist = default_whitelist

    whitelist_extra_str = os.environ.get("JUPYTER_ENV_EXTRA_WHITELIST", "")
    whitelist.extend([s.strip().upper() for s in whitelist_extra_str.split(",") if s])

    for name in os.environ:
        if name.upper() not in whitelist:
            del os.environ[name]
