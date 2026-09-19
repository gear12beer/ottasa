import typer
import shutil

from ottasa.models import model_supported
from ottasa.storage import (
    MODELS_DIR,
    ensure_directories,
    get_model_path,
)

app = typer.Typer()


@app.command("list")
def list_models():
    ensure_directories()

    models = [
        path.name
        for path in MODELS_DIR.iterdir()
        if path.is_dir()
    ]

    if not models:
        print("No models installed.")
        return

    for model in models:
        print(model)


@app.command()
def pull(model: str):
    ensure_directories()

    if not model_supported(model):
        print(f"Unknown model: {model}")
        raise typer.Exit(code=1)

    model_path = get_model_path(model)

    if model_path.exists():
        print(f"{model} is already installed.")
        return

    model_path.mkdir(parents=True)

    print(f"✓ {model} initialized")


@app.command()
def run(model: str):
    print(f"Running {model}...")


@app.command()
def stop(model: str):
    print(f"Stopping {model}...")


@app.command()
def rm(model: str):
    model_path = get_model_path(model)

    if not model_path.exists():
        print(f"{model} is not installed.")
        return

    shutil.rmtree(model_path)

    print(f"✓ Removed {model}")


if __name__ == "__main__":
    app()