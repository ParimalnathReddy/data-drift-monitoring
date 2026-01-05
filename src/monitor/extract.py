import pandas as pd

KEEP_COLS = [
    "tpep_pickup_datetime", "tpep_dropoff_datetime",
    "passenger_count", "trip_distance",
    "PULocationID", "DOLocationID",
    "RatecodeID", "payment_type",
    "fare_amount", "total_amount",
]

def load_data(path: str, n: int = 20_000, seed: int = 42) -> pd.DataFrame:
    path_lower = path.lower()
    if path_lower.endswith((".parquet", ".pq")):
        df = pd.read_parquet(path, columns=KEEP_COLS)
    elif path_lower.endswith(".csv"):
        df = pd.read_csv(path, usecols=KEEP_COLS)
    else:
        raise ValueError(f"Unsupported data format for path: {path}")

    # Downsample for local runs (deterministic)
    if len(df) > n:
        df = df.sample(n=n, random_state=seed)

    # Basic cleanup
    df["passenger_count"] = pd.to_numeric(df["passenger_count"], errors="coerce")
    df["trip_distance"] = pd.to_numeric(df["trip_distance"], errors="coerce")
    df["fare_amount"] = pd.to_numeric(df["fare_amount"], errors="coerce")
    df["total_amount"] = pd.to_numeric(df["total_amount"], errors="coerce")
    return df
