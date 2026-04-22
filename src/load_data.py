import pandas as pd
from src.config import DATA_RAW_DIR, YEARS


def load_year_file(year: int) -> pd.DataFrame:
    file_path = DATA_RAW_DIR / f"{year}.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"Missing file: {file_path}")

    df = pd.read_csv(file_path)
    df["Year"] = year
    return df


def load_all_years() -> pd.DataFrame:
    dfs = []

    for year in YEARS:
        df = load_year_file(year)
        dfs.append(df)

    combined = pd.concat(dfs, ignore_index=True)
    return combined


if __name__ == "__main__":
    df = load_all_years()
    print("\nLoaded data successfully.")
    print("\nShape:")
    print(df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())