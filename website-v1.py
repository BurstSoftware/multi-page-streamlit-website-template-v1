import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="My Multi-Page App", layout="wide")

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Dashboard", "Contact"])

# -----------------------------
# Home Page
# -----------------------------
if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to your multi-page Streamlit website!")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Features")
        st.write("- Multi-page layout")
        st.write("- Interactive widgets")
        st.write("- Clean UI")

    with col2:
        st.image("https://via.placeholder.com/400", caption="Sample Image")

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
    st.title("📖 About")
    st.write("This app is built using Streamlit.")

    st.subheader("Our Mission")
    st.write("To build simple and powerful data apps quickly.")

    st.subheader("Team")
    st.write("- Developer 1")
    st.write("- Developer 2")

# -----------------------------
# Dashboard Page
# -----------------------------
elif page == "Dashboard":
    st.title("📊 Dashboard")

    st.subheader("User Input")
    name = st.text_input("Enter your name")
    age = st.slider("Select your age", 1, 100, 25)

    if name:
        st.success(f"Hello {name}, you are {age} years old!")

    st.subheader("Sample Data Visualization")
    data = {
        "A": [10, 20, 30, 40],
        "B": [5, 15, 25, 35]
    }
    st.line_chart(data)

# -----------------------------
# Contact Page
# -----------------------------
elif page == "Contact":
    st.title("📬 Contact")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Thanks for reaching out! We'll get back to you soon.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("© 2026 My Streamlit App")
