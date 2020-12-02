import os

import invoke

root_dir = os.path.dirname(__file__)

exclude_regex = "/(protos?|modules)/"
exclude_glob = "**/proto/**,**/protos/**,**/modules/**"
mypy_paths = "jupyter_env_whitelist"


@invoke.task()
def lint(ctx):
    """
    Check lint issues.
    """
    with ctx.cd(root_dir):
        ctx.run("isort -c .")
        ctx.run("brunette --config=setup.cfg --check --exclude '%s' ." % exclude_regex)
        ctx.run(
            "autoflake --check --recursive --exclude '%s' --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports . > /dev/null && echo 'No issues detected!'"
            % exclude_glob
        )
        ctx.run("mypy %s" % mypy_paths)


@invoke.task(name="fix-lint")
def fix_lint(ctx):
    """
    Fix lint issues.
    """
    with ctx.cd(root_dir):
        ctx.run("isort .")
        ctx.run("brunette --config=setup.cfg --exclude '%s' ." % exclude_regex)
        ctx.run(
            "autoflake --in-place --recursive --exclude '%s' --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports ."
            % exclude_glob
        )
        ctx.run("mypy %s" % mypy_paths)


@invoke.task(name="fix-lint-diff")
def fix_lint_diff(ctx):
    """
    Show diff of lint issue fixing.
    """
    with ctx.cd(root_dir):
        ctx.run("isort -df .")
        ctx.run("brunette --config=setup.cfg --diff --exclude '%s' ." % exclude_regex)
        ctx.run(
            "autoflake --recursive --exclude '%s' --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports ."
            % exclude_glob
        )
        ctx.run("mypy %s" % mypy_paths)
