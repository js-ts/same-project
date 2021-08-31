from pathlib import Path

class Config:
    def __init__(self, path: Path, values: dict) -> None:
        self.path = path
        self.values = values

    def notebook_path(self) -> Path:
        relative_path = str(self.values['pipeline']['package'])
        return self.path.joinpath(relative_path)

