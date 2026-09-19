from pathlib import Path

OTTASA_HOME = Path.home() / ".ottasa"
MODELS_DIR = OTTASA_HOME / "models"

def ensure_directories() -> None:
    MODELS_DIR.mkdir(parents=True,exist_ok=True)

def get_model_path(model: str) -> Path:
    return MODELS_DIR / model

def model_exists(model: str) -> bool:
    return get_model_path(model).is_dir()
