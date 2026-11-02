# ProductLens

An Electronic Product Information System built with **Python**, **Streamlit** and **MongoDB**.

Users can browse 50 electronic products across five categories (Mobile, Laptop, Tablet,
Headphone, Smartwatch), search for products, and open a product to see its specifications,
features, price and images.

## Team Contribution

| Folder | Member | Roll No. | Work |
|---|---|---|---|
| `prince_database/` | Prince Kumar | 244CA036 | MongoDB connection, queries and loading data into the database |
| `shubham_data/` | Shubham Shashwat | 244CA053 | Preparing product data for all 50 products (specs, features, price, images) |
| `satish_ui/` | Satish Kumar | 244CA046 | Streamlit interface, category navigation and product listing |
| `tarun_search/` | Tarun Dhote | 244CA057 | Search option and product details page with images |

`app.py` connects all four parts together. Each folder has its own `README.md` that shows the
full project workflow and that member's work.

## Project Structure

```
ProductLens/
├── app.py                  # Main Streamlit app
├── requirements.txt
├── prince_database/
│   ├── db.py               # MongoDB connection and query functions
│   └── seed_db.py          # Loads products.json into MongoDB
├── shubham_data/
│   ├── products.json       # 50 products (10 per category)
│   └── images/             # 3 photos per product
├── satish_ui/
│   └── home.py             # Header, category sidebar, product cards
└── tarun_search/
    ├── search.py           # Search box
    └── details.py          # Product details page
```

## How to Run

1. Install and start MongoDB (running on `mongodb://localhost:27017`).
2. Install the Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Load the product data into MongoDB (only needed once):
   ```
   python -m prince_database.seed_db
   ```
4. Start the app:
   ```
   streamlit run app.py
   ```

To use a different MongoDB server (for example MongoDB Atlas), set the `MONGO_URI`
environment variable before steps 3 and 4.

## Product Images

Each product has three photos stored in `shubham_data/images/` (150 photos in total, 800×600 JPEG).
`products.json` refers to them by path, e.g. `shubham_data/images/iphone_15_1.jpg`, so always
start the app from the project folder. To change a photo, replace the file with the same name.
Photos belong to their respective brands and are used here for academic purposes only.
