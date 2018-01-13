"""Core workflow for Image Annotator Lite by Red@."""

PROJECT_NAME = "Image Annotator Lite"
DOMAIN_THEME = "image tooling"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
