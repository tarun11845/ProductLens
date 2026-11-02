# Search and Product Details — Tarun Dhote (244CA057)

## Role
Built the search option and the product details page that shows the full information and
images of the selected product.

## Project Workflow

```
 Product data (JSON)  ──►  seed_db.py  ──►  MongoDB  ◄──  db.py  ◄──  Streamlit UI  ◄──  User
   [Shubham]               [Prince]                       [Prince]    [Satish, Tarun]
```

| Step | What happens | Done by |
|---|---|---|
| 1 | Product data for 50 products is prepared in `products.json` | Shubham |
| 2 | `seed_db.py` loads the data into MongoDB | Prince |
| 3 | User opens the app and sees the five categories | Satish |
| 4 | User selects a category or **types in the search box** | Satish / **Tarun** |
| 5 | `db.py` fetches matching products from MongoDB | Prince |
| 6 | Products are shown as cards | Satish |
| 7 | User clicks a product and **its details and images are shown** | **Tarun** |

## Files

| File | Purpose |
|---|---|
| `search.py` | Search box |
| `details.py` | Product details page |

## Functions

| Function | File | What it does |
|---|---|---|
| `search_bar()` | `search.py` | Shows the search box and returns the typed text |
| `show_product_details(product)` | `details.py` | Shows name, brand, category, price, description, images, specifications table and features list |
| `go_back()` | `details.py` | Clears the selected product so the user returns to the listing |

## How Search Works
1. The user types text, for example `samsung`, `laptop` or `pixel`.
2. The text is sent to `search_products()` in `prince_database/db.py`.
3. MongoDB matches the text against the product **name**, **brand** and **category**, ignoring case.
4. Matching products from all categories are shown, along with the number of results.
5. Clearing the search box shows the selected category again.

## Details Page Layout
- "← Back to products" button
- Product name, brand, category and price
- Short description
- Three product images side by side
- Four tabs:
  - **Specifications**: one table per section (Display, Performance, Camera and so on), in two columns
  - **Key Features**: list of the main features
  - **Pros & Cons**: strengths in green and weaknesses in red, side by side
  - **In the Box**: items included with the product

## Work Done
- Built the search box and connected it to the database search function
- Made search work across all categories, so the user doesn't have to open each one
- Built the product details page with images and tabs for specifications, features,
  pros and cons, and box contents
- Displayed the grouped specifications as separate tables, one per section
- Added the Back button and handled the case where a product is not found
