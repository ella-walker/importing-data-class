from pathlib import Path

def project_paths():
    base = Path(__file__).resolve().parents[1]
    return {
        "base": base,
        "demo": base / "data" / "demo",
        "practice": base / "data" / "practice",
    }
