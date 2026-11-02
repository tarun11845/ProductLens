# User Interface — Satish Kumar (244CA046)

## Role
Built the main Streamlit interface: the page header, the category sidebar and the product
listing shown as cards.

## Project Workflow

```
 Product data (JSON)  ──►  seed_db.py  ──►  MongoDB  ◄──  db.py  ◄──  Streamlit UI  ◄──  User
   [Shubham]               [Prince]                       [Prince]    [Satish, Tarun]
```

| Step | What happens | Done by |
|---|---|---|
| 1 | Product data for 50 products is prepared in `products.json` | Shubham |
| 2 | `seed_db.py` loads the data into MongoDB | Prince |
| 3 | **User opens the app and sees the five categories** | **Satish** |
| 4 | **User selects a category** or types in the search box | **Satish** / Tarun |
| 5 | `db.py` fetches matching products from MongoDB | Prince |
| 6 | **Products are shown as cards** | **Satish** |
| 7 | **User clicks "View Details"** and the details and images are shown | **Satish** / Tarun |

## Files

| File | Purpose |
|---|---|
| `home.py` | Header, category sidebar and product cards |

## Functions in `home.py`

| Function | What it does |
|---|---|
| `show_header()` | Shows the ProductLens title and subtitle |
| `select_category()` | Shows the five categories as a sidebar radio button and returns the selected one |
| `show_product_grid(products)` | Shows products in a 3-column grid of cards with image, name, brand, price and a "View Details" button |
| `open_product(product_id)` | Saves the clicked product in `st.session_state` so the details page opens |

## How the Screens Change
Streamlit runs the whole script again on every click, so the app remembers the current page in
`st.session_state["selected_product"]`:

- `None`: show the home page (header, search, product grid)
- a product id: show the details page for that product

Clicking "View Details" sets the product id. Changing the category in the sidebar resets it to
`None`, so the user goes back to the listing.

## Work Done
- Designed the page layout (wide layout, sidebar for categories, main area for products)
- Built the category navigation for Mobile, Laptop, Tablet, Headphone and Smartwatch
- Built the product cards with the first product image, name, brand and price
- Handled switching between the listing and the details page with session state
- Showed a message when no products are found
