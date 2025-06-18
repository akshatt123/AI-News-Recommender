import pandas as pd
import json
import os

def load_articles():
    path = os.path.join("data", "sample_articles.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data)
