from pathlib import Path
import os

class Program:
    def __init__(self, path: Path, name: str) -> None:
        self.path = path
        self.name = name

TEST_DATA_DIR = Path(__file__).resolve().parent

def load_program(name: str) -> Program:
    path = Path.joinpath(TEST_DATA_DIR, name)
    if not os.path.isdir(path):
        raise RuntimeError("test program {name} could not be found at {path}")

    return Program(path, name)
