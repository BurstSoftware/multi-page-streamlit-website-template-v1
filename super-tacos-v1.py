# app.py
# Super Tacos Streamlit Website App
# Python 3.14

import streamlit as st

# Page Config
st.set_page_config(
    page_title="Super Tacos",
    page_icon="🌮",
    layout="wide"
)

# Header
st.title("🌮 Super Tacos")
st.subheader("Fresh • Delicious • Authentic Tacos")

st.markdown("---")

# Contact Info
st.header("📞 Contact Us")
st.write("**Phone:** (555) 123-4567")
st.write("**Email:** contact@supertacos.com")

st.markdown("---")

# Menu Section
st.header("📋 Taco Menu")

menu = [
    {
        "name": "Chicken Taco",
        "price": "$3.50",
        "ingredients": [
            "Grilled chicken",
            "Onions",
            "Cilantro",
            "Lettuce",
            "Cheese",
            "Salsa"
        ]
    },
    {
        "name": "Beef Taco",
        "price": "$4.00",
        "ingredients": [
            "Seasoned beef",
            "Onions",
            "Tomatoes",
            "Cheese",
            "Lettuce",
            "Sour cream"
        ]
    },
    {
        "name": "Pastor Taco",
        "price": "$4.25",
        "ingredients": [
            "Marinated pork",
            "Pineapple",
            "Onions",
            "Cilantro",
            "Salsa verde"
        ]
    }
]

for taco in menu:
    with st.container():
        st.subheader(f"{taco['name']} - {taco['price']}")
        st.write("**Ingredients:**")
        for item in taco["ingredients"]:
            st.write(f"- {item}")
        st.markdown("---")

# Footer
st.success("Thank you for visiting Super Tacos!")
