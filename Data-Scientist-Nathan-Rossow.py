import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Nathan Rossow | Burst Software Development", layout="wide")

TOTAL_APPS = 301

CATEGORIES = {
    "Data Science & Analytics": 65,
    "Machine Learning & AI": 40,
    "Business & Finance Tools": 55,
    "Project Management": 30,
    "Developer Tools & Frameworks": 45,
    "Automation & Utilities": 35,
    "Industry-Specific Apps": 31
}

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Dashboard", "Contact"])

# -----------------------------
# Home Page
# -----------------------------
if page == "Home":
    st.title("🚀 Nathan Rossow")
    st.subheader("Data Scientist | Streamlit Specialist | Burst Software Development")

    st.write(
        "I specialize in Streamlit and Streamlit Cloud development, building fast, production-ready data applications using Python (3.7 – 3.14)."
    )

    st.metric("📊 Total Published Streamlit Apps", TOTAL_APPS)

    st.info("📈 4-Year Contribution Summary: 2,753 contributions")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Core Expertise")
        st.write("- Streamlit & Streamlit Cloud Applications")
        st.write("- Rapid Prototyping in Python (3.7 – 3.14)")
        st.write("- Machine Learning & AI Systems")
        st.write("- Data Visualization & Dashboards")
        st.write("- Backend APIs & Automation")

    with col2:
        st.subheader("App Categories")
        for category, count in CATEGORIES.items():
            st.write(f"- {category}: {count}")

# -----------------------------
# About Page
# -----------------------------
elif page == "About":
    st.title("📖 About Me")

    st.write(
        "I'm Nathan Rossow, a data scientist and software developer specializing in Streamlit ecosystems and high-speed Python development."
    )

    st.subheader("Specializations")
    st.write("- Streamlit & Streamlit Cloud Frameworks")
    st.write("- Rapid MVP Development")
    st.write("- Python (3.7 – 3.14)")

# -----------------------------
# Projects Page
# -----------------------------
elif page == "Projects":
    st.title("💼 Projects Overview")

    st.write(f"Total Apps Built: {TOTAL_APPS}")

    st.subheader("📂 Categories Breakdown")
    st.bar_chart(CATEGORIES)

# -----------------------------
# Dashboard Page
# -----------------------------
elif page == "Dashboard":
    st.title("📊 Interactive Dashboard")

    name = st.text_input("Enter your name")
    value = st.slider("Select a value", 0, 100, 50)

    if name:
        st.success(f"Welcome {name}! Selected value: {value}")

    st.subheader("Apps Distribution")
    st.bar_chart(CATEGORIES)

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
            st.success("Thanks for reaching out! I'll get back to you soon.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("© 2026 Nathan Rossow | Burst Software Development | Streamlit Specialist")
