from pathlib import Path

OTTASA_HOME = Path.home() / ".ottasa"
MODELS_DIR = OTTASA_HOME / "models"

def ensure_directories() -> None:
    MODELS_DIR.mkdir(parents=True,exist_ok=True)

def get_model_path(model: str) -> Path:
    return MODELS_DIR / model

def model_exists(model: str) -> bool:
    return get_model_path(model).is_dir()

def get_model_size(model: str) -> int:
    model_path = get_model_path(model)

    if not model_path.exists():
        return 0

    return sum(
        file.stat().st_size
        for file in model_path.rglob("*")
        if file.is_file()
    )


def get_model_modified(model: str) -> float:
    return get_model_path(model).stat().st_mtime