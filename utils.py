import json
import pandas as pd

def save_to_json(products, path="data/products.json"):
    with open(path, "w") as f:
        json.dump(products, f, indent=4)

def save_to_csv(products, path="data/products.csv"):
    df = pd.DataFrame(products)
    df.to_csv(path, index=False)
