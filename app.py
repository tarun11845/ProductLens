import streamlit as st

from prince_database.db import get_product, get_products_by_category, search_products
from satish_ui.home import select_category, show_header, show_product_grid
from tarun_search.details import show_product_details
from tarun_search.search import search_bar

st.set_page_config(page_title="ProductLens", page_icon="🔍", layout="wide")

if "selected_product" not in st.session_state:
    st.session_state["selected_product"] = None

category = select_category()

if st.session_state["selected_product"]:
    show_product_details(get_product(st.session_state["selected_product"]))
else:
    show_header()
    query = search_bar()
    if query:
        products = search_products(query)
        st.subheader(f"Search results for \"{query}\" ({len(products)})")
    else:
        products = get_products_by_category(category)
        st.subheader(f"{category} ({len(products)})")
    show_product_grid(products)
