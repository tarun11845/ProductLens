"""Load the product data from shubham_data/products.json into MongoDB.

Run from the project folder:  python -m prince_database.seed_db
"""
import json
from pathlib import Path

from prince_database.db import get_collection

DATA_FILE = Path(__file__).resolve().parent.parent / "shubham_data" / "products.json"


def seed():
    with open(DATA_FILE, encoding="utf-8") as f:
        products = json.load(f)

    collection = get_collection()
    collection.delete_many({})
    collection.insert_many(products)
    collection.create_index("category")
    print(f"Inserted {len(products)} products into MongoDB.")


if __name__ == "__main__":
    seed()
