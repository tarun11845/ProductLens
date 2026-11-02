import streamlit as st


def search_bar():
    return st.text_input(
        "Search products",
        placeholder="Search by name, brand or category (e.g. iPhone, Samsung, Laptop)",
    ).strip()
