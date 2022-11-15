from typer.testing import CliRunner
from aleph_client.commands.aggregate import forget

runner = CliRunner()
from .main import app

def test_app():

    result = runner.invoke(app, ["Camila", "--city", "Berlin"])

