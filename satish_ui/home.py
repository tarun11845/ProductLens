import streamlit as st

from prince_database.db import CATEGORIES


def show_header():
    st.title("ProductLens")
    st.caption("An Electronic Product Information System")


def open_product(product_id):
    st.session_state["selected_product"] = product_id


def select_category():
    st.sidebar.header("Categories")
    return st.sidebar.radio(
        "Choose a category",
        CATEGORIES,
        label_visibility="collapsed",
        on_change=open_product,
        args=(None,),
    )


def show_product_grid(products, columns=3):
    if not products:
        st.info("No products found.")
        return

    cols = st.columns(columns)
    for i, product in enumerate(products):
        with cols[i % columns]:
            with st.container(border=True):
                if product.get("images"):
                    st.image(product["images"][0])
                st.subheader(product["name"])
                st.write(f"{product['brand']}  |  {product['category']}")
                st.write(f"**₹{product['price']:,}**")
                st.button(
                    "View Details",
                    key=f"view_{product['_id']}",
                    on_click=open_product,
                    args=(str(product["_id"]),),
                )
