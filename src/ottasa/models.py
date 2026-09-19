MODELS = {
    "kokoro": {
        "type": "tts",
    }
}

def get_model(model: str) -> dict | None:
    return MODELS.get(model)

def model_supported(model: str) -> bool:
    return model in MODELS

