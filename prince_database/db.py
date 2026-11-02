import os
import re

from bson import ObjectId
from pymongo import MongoClient

import streamlit as st

try:
    MONGO_URI = st.secrets["MONGO_URI"]
except Exception:
    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017"
    )
DB_NAME = "product_lens"
COLLECTION_NAME = "products"

CATEGORIES = ["Mobile", "Laptop", "Tablet", "Headphone", "Smartwatch"]

_client = None


def get_collection():
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URI)
    return _client[DB_NAME][COLLECTION_NAME]


def get_products_by_category(category):
    return list(get_collection().find({"category": category}).sort("name", 1))


def search_products(text):
    pattern = {"$regex": re.escape(text.strip()), "$options": "i"}
    query = {"$or": [{"name": pattern}, {"brand": pattern}, {"category": pattern}]}
    return list(get_collection().find(query).sort("name", 1))


def get_product(product_id):
    return get_collection().find_one({"_id": ObjectId(product_id)})
