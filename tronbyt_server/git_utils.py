"""Git utilities using GitPython."""

import logging
from pathlib import Path

from git import InvalidGitRepositoryError, NoSuchPathError, Repo

logger = logging.getLogger(__name__)


def get_repo(path: Path) -> Repo | None:
    """Get a GitPython Repo object for the given path."""
    try:
        return Repo(path)
    except (InvalidGitRepositoryError, NoSuchPathError):
        return None
