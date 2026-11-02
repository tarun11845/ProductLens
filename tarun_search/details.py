import streamlit as st


def go_back():
    st.session_state["selected_product"] = None


def show_product_details(product):
    st.button("← Back to products", on_click=go_back)

    if product is None:
        st.error("Product not found.")
        return

    st.title(product["name"])
    st.write(f"**Brand:** {product['brand']}  |  **Category:** {product['category']}")
    st.header(f"₹{product['price']:,}")
    st.write(product.get("description", ""))

    images = product.get("images", [])
    if images:
        st.subheader("Images")
        cols = st.columns(len(images))
        for col, image in zip(cols, images):
            col.image(image)

    specs_tab, features_tab, review_tab, box_tab = st.tabs(
        ["Specifications", "Key Features", "Pros & Cons", "In the Box"]
    )

    with specs_tab:
        sections = list(product.get("specifications", {}).items())
        left, right = st.columns(2)
        for i, (section, specs) in enumerate(sections):
            with left if i % 2 == 0 else right:
                st.markdown(f"#### {section}")
                st.table({"Details": specs})

    with features_tab:
        for feature in product.get("features", []):
            st.write(f"✔ {feature}")

    with review_tab:
        pros_col, cons_col = st.columns(2)
        with pros_col:
            st.markdown("####  Pros")
            for pro in product.get("pros", []):
                st.success(pro)
        with cons_col:
            st.markdown("####  Cons")
            for con in product.get("cons", []):
                st.error(con)

    with box_tab:
        for item in product.get("in_the_box", []):
            st.write(f"- {item}")
