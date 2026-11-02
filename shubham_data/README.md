# Product Data — Shubham Shashwat (244CA053)

## Role
Collected and prepared the information for all 50 products in the catalogue: specifications,
features, price, description and image links.

## Project Workflow

```
 Product data (JSON)  ──►  seed_db.py  ──►  MongoDB  ◄──  db.py  ◄──  Streamlit UI  ◄──  User
   [Shubham]               [Prince]                       [Prince]    [Satish, Tarun]
```

| Step | What happens | Done by |
|---|---|---|
| 1 | **Product data for 50 products is prepared in `products.json`** | **Shubham** |
| 2 | `seed_db.py` loads the data into MongoDB | Prince |
| 3 | User opens the app and sees the five categories | Satish |
| 4 | User selects a category or types in the search box | Satish / Tarun |
| 5 | `db.py` fetches matching products from MongoDB | Prince |
| 6 | Products are shown as cards | Satish |
| 7 | User clicks a product and its details and images are shown | Tarun |

## Files

| File | Purpose |
|---|---|
| `products.json` | All 50 products, 10 in each category |
| `images/` | 150 product photos, 3 per product, named `<product_name>_1.jpg` to `_3.jpg` |

## Products Included

| Category | Products |
|---|---|
| Mobile | iPhone 15, iPhone 15 Pro, Samsung Galaxy S24, Samsung Galaxy A55, Google Pixel 8, OnePlus 12, OnePlus Nord CE 4, Redmi Note 13 Pro, Nothing Phone (2a), Vivo V30 |
| Laptop | MacBook Air M2, MacBook Pro 14 M3, Dell XPS 13, Dell Inspiron 15, HP Pavilion 15, HP Victus 15, Lenovo ThinkPad E14, Lenovo IdeaPad Slim 5, ASUS ROG Strix G16, ASUS Vivobook 15 |
| Tablet | iPad (10th Gen), iPad Air M2, iPad Pro M4, Samsung Galaxy Tab S9, Galaxy Tab S9 FE, Galaxy Tab A9+, Xiaomi Pad 6, OnePlus Pad, Lenovo Tab M10 (3rd Gen), Realme Pad 2 |
| Headphone | Sony WH-1000XM5, Sony WH-CH720N, Bose QuietComfort Ultra, Apple AirPods Max, Apple AirPods Pro 2, Sennheiser Momentum 4, JBL Tune 760NC, boAt Rockerz 550, Samsung Galaxy Buds2 Pro, OnePlus Buds 3 |
| Smartwatch | Apple Watch Series 9, Apple Watch SE (2nd Gen), Apple Watch Ultra 2, Samsung Galaxy Watch6, Galaxy Watch6 Classic, Google Pixel Watch 2, OnePlus Watch 2, Amazfit GTR 4, Noise ColorFit Pro 5, Fire-Boltt Phoenix Pro |

## Specification Sections per Category

Specifications are grouped into sections. Each product has about 15–38 specification fields
(28 on average).

| Category | Sections |
|---|---|
| Mobile | General, Display, Performance, Camera, Battery & Charging, Connectivity, Design, Security |
| Laptop | General, Display, Performance, Battery & Power, Ports & Connectivity, Audio & Camera, Keyboard & Input, Design |
| Tablet | General, Display, Performance, Camera, Battery & Charging, Connectivity, Audio, Design, Security & Accessories |
| Headphone | General, Audio, Noise Control, Battery & Charging, Connectivity, Calls, Controls, Design |
| Smartwatch | General, Display, Performance, Health & Fitness, Battery, Connectivity, Design (plus Smart Features for some) |

Examples of what is recorded: launch date, display size/type/resolution/refresh rate/brightness,
chipset, CPU, GPU, RAM, storage options, camera details, battery capacity, charging speed,
Wi-Fi/Bluetooth versions, ports, dimensions, weight, water resistance and colours.

## Other Fields per Product

| Field | Content |
|---|---|
| `name`, `brand`, `category` | Basic product identity |
| `price` | Price in ₹ |
| `description` | 2–3 sentence overview of the product |
| `features` | 6–8 key features |
| `pros` / `cons` | 3 strengths and 3 weaknesses |
| `in_the_box` | Items included in the retail box |
| `images` | 3 photos |

## Work Done
- Selected 10 popular products in each of the five categories across budget, mid-range and premium price levels
- Collected detailed specifications, key features, pros and cons, box contents and Indian
  prices (₹) for each product
- Grouped specifications into the same sections for every product in a category, so all
  products look consistent
- Collected three photos per product, checked that each one shows the correct model, and
  resized them all to 800×600 so the product cards look uniform
- Worked with Prince on the JSON structure so it can be inserted directly into MongoDB

## Updating the Data
Edit `products.json`, then reload it into MongoDB:
```
python -m prince_database.seed_db
```
