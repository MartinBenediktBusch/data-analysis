from pathlib import Path
import pandas as pd


DATA_DIR = Path(__file__).resolve().parent / "data"


def read_data(file_name: str, data_dir: Path | str | None = None, **kwargs) -> pd.DataFrame:
    """Load a dataset from the repository data directory into a DataFrame."""
    base_dir = Path(data_dir) if data_dir is not None else DATA_DIR
    file_path = base_dir / file_name

    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    suffix = file_path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(file_path, **kwargs)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(file_path, **kwargs)
    if suffix == ".json":
        return pd.read_json(file_path, **kwargs)
    if suffix == ".parquet":
        return pd.read_parquet(file_path, **kwargs)

    supported_types = ".csv, .xlsx, .xls, .json, .parquet"
    raise ValueError(
        f"Unsupported file type '{suffix}'. Supported file types: {supported_types}"
    )
