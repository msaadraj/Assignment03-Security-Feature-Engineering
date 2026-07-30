import pandas as pd
import hashlib

df = pd.read_json("sample_raw_events.jsonl", lines=True)

df["user_hash"] = df["user"].apply(
    lambda x: hashlib.sha256(x.encode()).hexdigest()
)

features = df.groupby("user_hash").agg(
    total_events=("event","count"),
    failed_logins=("event",lambda x:(x=="login_failed").sum()),
    total_bytes=("bytes","sum"),
    unique_ips=("ip","nunique")
).reset_index()

features.to_csv("sample_features.csv",index=False)
features.to_json("sample_features.json",orient="records",indent=4)

print("Features generated.")