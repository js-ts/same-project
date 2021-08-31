from pathlib import Path
import click
from .config import load_config

@click.group()
def main():
    """Project SAME CLI"""

@main.group()
def program():
    """Work with a SAME program"""

@program.command('compile')
@click.argument('path', type=click.Path(exists=True, file_okay=True, dir_okay=True, path_type=Path))
def program_compile(path: Path):
    """Compile a SAME program without running"""

    config = load_config(path)
    nodes

@program.command('run')
@click.argument('path')
def program_run():
    """Run a SAME program"""

if __name__ == "__main__":
    main()
