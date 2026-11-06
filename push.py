"""Push the contents of this folder to GitHub, honoring .gitignore.

Usage:
    python push.py                      # commit message defaults to a timestamp
    python push.py "Add whole-state fills"

On first run (no .git folder) it connects this folder to the existing remote
history without touching your files, so the push lands on top of what's on
GitHub instead of overwriting it.
"""

import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_URL = "https://github.com/GC-BCSA/zip_map.git"
REMOTE = "origin"

ROOT = Path(__file__).resolve().parent


def git(*args, check=True, capture=False):
    # The folder lives on a network share whose owner differs from the Windows
    # user, which trips git's "dubious ownership" check. Trust it for these
    # commands only, without changing global git config.
    cmd = ["git", "-c", "safe.directory=*", *args]
    result = subprocess.run(
        cmd, cwd=ROOT, text=True,
        stdout=subprocess.PIPE if capture else None,
    )
    if check and result.returncode != 0:
        sys.exit(f"\nFailed: git {' '.join(args)}")
    return result.stdout.strip() if capture else result.returncode


def default_branch():
    out = git("ls-remote", "--symref", REMOTE, "HEAD", capture=True)
    for line in out.splitlines():
        if line.startswith("ref:"):
            return line.split()[1].removeprefix("refs/heads/")
    return "main"


def setup_repo():
    print("No git repo here yet; connecting to", REPO_URL)
    git("init", "--quiet")
    git("remote", "add", REMOTE, REPO_URL)
    branch = default_branch()
    git("fetch", "--quiet", REMOTE, branch)
    git("symbolic-ref", "HEAD", f"refs/heads/{branch}")
    # Point the branch at the remote history but keep the files on disk as-is.
    git("reset", "--quiet", f"{REMOTE}/{branch}")
    git("branch", "--quiet", f"--set-upstream-to={REMOTE}/{branch}")


def main():
    message = " ".join(sys.argv[1:]) or f"Update {datetime.now():%Y-%m-%d %H:%M}"

    if not (ROOT / ".git").exists():
        setup_repo()

    branch = git("rev-parse", "--abbrev-ref", "HEAD", capture=True)

    # Stage everything not excluded by .gitignore (including deletions).
    git("add", "--all")
    if git("diff", "--cached", "--quiet", check=False) == 0:
        print("Nothing to commit.")
    else:
        git("status", "--short")
        git("commit", "--quiet", "-m", message)
        print(f'Committed: "{message}"')

    # Pick up anything pushed from elsewhere before pushing.
    git("pull", "--rebase", "--quiet", REMOTE, branch)
    git("push", REMOTE, branch)
    print(f"Pushed to {REMOTE}/{branch}.")


if __name__ == "__main__":
    main()
