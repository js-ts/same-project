
from test.testdata.program import load_program
from click.testing import CliRunner
from cli.main import program_compile

def test_compile_helloword():
    program = load_program("helloworld")

    runner = CliRunner()
    result = runner.invoke(program_compile, args=[str(program.path)])
    assert result.exit_code == 0
