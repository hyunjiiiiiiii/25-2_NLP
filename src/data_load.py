import pandas as pd
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

def load_train(path: str | Path = DATA_DIR / "train.csv") -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Train file not found: {path}")
    return pd.read_csv(path)

def load_test(path: str | Path = DATA_DIR / "test.csv") -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Train file not found: {path}")
    return pd.read_csv(path)