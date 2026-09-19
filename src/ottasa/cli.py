import typer

app = typer.Typer()


@app.command("list")
def list_models():
    print("Listing models...")


@app.command()
def pull(model: str):
    print(f"Pulling {model}...")


@app.command()
def run(model: str):
    print(f"Running {model}...")


@app.command()
def stop(model: str):
    print(f"Stopping {model}...")


@app.command()
def rm(model: str):
    print(f"Removing {model}...")


if __name__ == "__main__":
    app()