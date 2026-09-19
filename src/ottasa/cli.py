from datetime import datetime
from rich.console import Console
from rich.table import Table
import typer

from ottasa.identity import get_model_id
from ottasa.models import model_supported
from ottasa.storage import (
    MODELS_DIR,
    ensure_directories,
    get_model_path,
    get_model_size,
)

app = typer.Typer()
console = Console()

def format_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(size)

    for unit in units:
        if value < 1024:
            return f"{value:.1f} {unit}"

        value /= 1024

    return f"{value:.1f} PB"

@app.command("list")
def list_models():
    ensure_directories()

    models = [
        path
        for path in MODELS_DIR.iterdir()
        if path.is_dir()
    ]

    if not models:
            print("No models installed.")
            return
    
    table = Table(show_header=True)

    table.add_column("NAME")
    table.add_column("ID")
    table.add_column("SIZE")
    table.add_column("MODIFIED")

    for model_path in sorted(models):
        model = model_path.name

        model_id = get_model_id(model)
        size = get_model_size(model)

        modified = model_path.stat().st_mtime

        modified_time = datetime.fromtimestamp(modified)

        table.add_row(
            model,
            model_id,
            format_size(size),
            modified_time.strftime("%Y-%m-%d %H:%M"),
        )

    console.print(table)


@app.command()
def pull(model: str):
    ensure_directories()

    if not model_supported(model):
        print(f"Model not supported, request support: {model}")
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
    import shutil
    model_path = get_model_path(model)

    if not model_path.exists():
        print(f"{model} is not installed.")
        return

    shutil.rmtree(model_path)

    print(f"✓ Removed {model}")


if __name__ == "__main__":
    app()