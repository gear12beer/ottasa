import hashlib


def get_model_id(model: str) -> str:
    return hashlib.sha256(model.encode()).hexdigest()[:12]