import json
import pandas as pd

with open("data/dataset samples.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.to_csv("data/train.csv", index=False, encoding="utf-8-sig")

print(df.head())
print(df.shape)