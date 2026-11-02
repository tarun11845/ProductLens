# Database Module — Prince Kumar (244CA036)

## Role
Set up MongoDB for ProductLens, wrote all the functions that read product data from the
database, and wrote the script that loads the product data into MongoDB.

## Project Workflow

```
 Product data (JSON)  ──►  seed_db.py  ──►  MongoDB  ◄──  db.py  ◄──  Streamlit UI  ◄──  User
   [Shubham]               [Prince]                       [Prince]    [Satish, Tarun]
```

| Step | What happens | Done by |
|---|---|---|
| 1 | Product data for 50 products is prepared in `products.json` | Shubham |
| 2 | **`seed_db.py` loads the data into MongoDB** | **Prince** |
| 3 | User opens the app and sees the five categories | Satish |
| 4 | User selects a category or types in the search box | Satish / Tarun |
| 5 | **`db.py` fetches matching products from MongoDB** | **Prince** |
| 6 | Products are shown as cards | Satish |
| 7 | User clicks a product; **`db.py` fetches it by id** and its details and images are shown | **Prince** / Tarun |

## Files

| File | Purpose |
|---|---|
| `db.py` | MongoDB connection and query functions used by the app |
| `seed_db.py` | Reads `shubham_data/products.json` and inserts all products into MongoDB |

## Functions in `db.py`

| Function | What it does | Used by |
|---|---|---|
| `get_collection()` | Connects to MongoDB (once) and returns the `products` collection | All functions below |
| `get_products_by_category(category)` | Returns all products of a category, sorted by name | Category listing (Satish) |
| `search_products(text)` | Case-insensitive search on name, brand and category | Search (Tarun) |
| `get_product(product_id)` | Returns a single product by its MongoDB `_id` | Details page (Tarun) |

`CATEGORIES` holds the five category names and is used by the sidebar.

## Database Design

- Database: `product_lens`
- Collection: `products`
- Index on `category` for faster category filtering

Each document has the following fields:

```json
{
  "name": "iPhone 15",
  "brand": "Apple",
  "category": "Mobile",
  "price": 69900,
  "description": "...",
  "specifications": {
    "General": { "Launch": "September 2023", "Operating System": "iOS 17" },
    "Display": { "Size": "6.1 inches", "Type": "Super Retina XDR OLED", "...": "..." },
    "...": { }
  },
  "features": ["...", "..."],
  "pros": ["...", "..."],
  "cons": ["...", "..."],
  "in_the_box": ["...", "..."],
  "images": ["shubham_data/images/iphone_15_1.jpg", "..."]
}
```

`specifications` is a nested document: each key is a section (Display, Performance, Camera
and so on), and each section holds its own specification fields.

## Work Done
- Designed the MongoDB document structure along with Shubham
- Wrote the connection logic, with the server address read from the `MONGO_URI` environment variable
- Wrote the category, search and single-product queries
- Escaped user input in search so that special characters like `(` or `+` do not break the query
- Wrote the seed script that clears old data and inserts the 50 products

## How to Run
```
python -m prince_database.seed_db
```
