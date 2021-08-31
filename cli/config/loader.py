from pathlib import Path
import errno
import os
import yaml
from .config import Config

def load_config(path: Path) -> Config:
    """Loads a same.yaml given the exact path to the file or a directory path. Will also tolerate same.yml."""

    if not path.exists():
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), str(path))
    
    if path.is_file():
        return _read(path)

    if path.is_dir() and path.joinpath('same.yaml').exists():
        return _read(path.joinpath('same.yaml'))

    if path.is_dir() and path.joinpath('same.yml'):
        return _read(path.joinpath('same.yml'))

    raise RuntimeError("could not find a same.yaml or same.yml in directory {path}")

def _read(path: Path) -> Config:
    with open(str(path), 'r', encoding='utf8') as stream:
        doc = yaml.safe_load(stream)
        return Config(doc)
