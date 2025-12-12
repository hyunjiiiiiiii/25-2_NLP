from __future__ import annotations
import re
import pandas as pd

_WS_RE = re.compile(r"\s+")

def safe_str(x) -> str:
    if pd.isna(x):
        return ""
    return str(x)

def normalize_whitespace(text: str) -> str:
    text = text.replace("\u00a0", " ")  # non-breaking space
    return _WS_RE.sub(" ", text).strip()

def build_text(row: pd.Series) -> str:
    q = safe_str(row.get("QuestionText"))
    a = safe_str(row.get("MC_Answer"))
    e = safe_str(row.get("Student Explanation"))  # 컬럼명 정확히 맞추기
    text = f"[Q] {q} [A] {a} [E] {e}"
    return normalize_whitespace(text)

def add_text_column(df: pd.DataFrame, out_col: str = "text") -> pd.DataFrame:
    df = df.copy()
    df[out_col] = df.apply(build_text, axis=1)
    return df