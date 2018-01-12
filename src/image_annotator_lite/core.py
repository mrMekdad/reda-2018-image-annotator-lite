"""Core workflow for Image Annotator Lite by Red@."""

PROJECT_NAME = "Image Annotator Lite"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": "image tooling"}
