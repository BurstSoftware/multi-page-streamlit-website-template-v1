To view keyboard shortcuts, press question mark
View keyboard shortcuts

History

Share
New chat
create a streamlit website called AcuHub.  AcuHub is an Ai tools company for acupuncture specialists

Thought for 37s
I'll create a complete, professional Streamlit app for AcuHub — an AI tools platform for acupuncture specialists.

The app includes:

Clean branding and navigation
Interactive AI tool demos (symptom-based point recommendations, treatment plan generator, and patient notes assistant)
About and contact sections
Modern, clinical aesthetic
You can run it locally with:

bash
pip install streamlit pandas
streamlit run acuhub.py
Here’s the full app code:


Thought
The Streamlit app has been created. Here’s the complete code (also saved as acuhub.py in this environment):

python
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="AcuHub",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a clean, professional look
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 0;
    }
    .tagline {
        font-size: 1.3rem;
        color: #4a6fa5;
        margin-top: -10px;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background-color: #2d6a4f;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
    }
    .stButton>button:hover {
        background-color: #1b4332;
    }
    .tool-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2d6a4f;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("AcuHub")
st.sidebar.markdown("### AI for Acupuncture")
page = st.sidebar.radio("Navigate", ["Home", "AI Tools", "About", "Contact"])

# --- HOME ---
if page == "Home":
    st.markdown('<p class="main-header">AcuHub</p>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">AI-powered tools designed exclusively for acupuncture specialists</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Precision. Intelligence. Tradition.
        
        AcuHub combines classical acupuncture knowledge with modern AI to help practitioners:
        - Generate point recommendations from patient symptoms
        - Create structured treatment plans in seconds
        - Analyze and organize clinical notes
        - Support better clinical decision-making
        
        Built by practitioners, for practitioners.
        """)
        st.info("All tools are designed as clinical aids. Final decisions remain with the licensed practitioner.")
    
    with col2:
        st.image("https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?auto=format&fit=crop&w=800", caption="Supporting clinical excellence")

    st.markdown("---")
    st.subheader("Featured Tools")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="tool-card"><h4>Point Recommender</h4><p>Input symptoms → suggested points & meridians</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="tool-card"><h4>Treatment Planner</h4><p>Generate multi-session protocols</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="tool-card"><h4>Notes Assistant</h4><p>Structure SOAP notes from free text</p></div>', unsafe_allow_html=True)

# --- AI TOOLS ---
elif page == "AI Tools":
    st.markdown('<p class="main-header">AI Tools</p>', unsafe_allow_html=True)
    tool = st.selectbox("Select a tool", ["Point Recommender", "Treatment Plan Generator", "Clinical Notes Assistant"])
    
    # Point Recommender
    if tool == "Point Recommender":
        st.subheader("Symptom-Based Point Recommendations")
        symptoms = st.text_area("Describe the patient's chief complaint and symptoms", 
                               placeholder="e.g. Frontal headache, stress, insomnia, neck tension...")
        if st.button("Generate Recommendations"):
            if symptoms:
                # Mock knowledge base (in production this would call an LLM or expert system)
                knowledge = {
                    "headache": ["LI4", "GB20", "Taiyang", "Yintang"],
                    "stress": ["HT7", "PC6", "LV3", "Yintang"],
                    "insomnia": ["HT7", "SP6", "Anmian", "Yintang"],
                    "neck": ["GB20", "GB21", "BL10", "SI3"],
                    "back": ["BL23", "BL40", "GV4", "Yaoyan"],
                    "fatigue": ["ST36", "SP6", "CV6", "BL20"]
                }
                recs = set()
                text = symptoms.lower()
                for key, points in knowledge.items():
                    if key in text:
                        recs.update(points)
                if not recs:
                    recs = ["ST36", "SP6", "LV3", "LI4"]  # general support
                
                st.success("Recommended points (clinical judgment required):")
                for p in sorted(recs):
                    st.write(f"• **{p}**")
                st.caption("These are educational suggestions based on common patterns. Always assess the individual patient.")
            else:
                st.warning("Please enter symptoms.")
    
    # Treatment Plan Generator
    elif tool == "Treatment Plan Generator":
        st.subheader("Treatment Plan Generator")
        col1, col2 = st.columns(2)
        with col1:
            condition = st.selectbox("Primary pattern / condition", 
                                    ["Liver Qi Stagnation", "Kidney Yin Deficiency", "Spleen Qi Deficiency", 
                                     "Wind-Cold Invasion", "Blood Stasis", "General Wellness"])
            sessions = st.slider("Number of sessions", 1, 12, 6)
        with col2:
            frequency = st.selectbox("Frequency", ["2x/week", "1x/week", "Every other week"])
            focus = st.multiselect("Additional focus", ["Pain relief", "Stress reduction", "Sleep", "Digestion", "Energy"])
        
        if st.button("Create Plan"):
            st.success(f"**{sessions}-session protocol** for {condition}")
            plan = []
            for i in range(1, sessions + 1):
                phase = "Initial" if i <= 2 else "Core" if i <= sessions-2 else "Consolidation"
                plan.append({
                    "Session": i,
                    "Phase": phase,
                    "Focus": condition,
                    "Key Points": "LI4, LV3, ST36 + local points",
                    "Notes": f"{frequency} • Reassess after session {i}"
                })
            df = pd.DataFrame(plan)
            st.dataframe(df, use_container_width=True)
            st.download_button("Download Plan (CSV)", df.to_csv(index=False), "acuhub_plan.csv")
    
    # Notes Assistant
    elif tool == "Clinical Notes Assistant":
        st.subheader("Clinical Notes Assistant")
        raw_notes = st.text_area("Paste free-form notes", height=150,
                                placeholder="Patient reports frontal headache for 3 days, worse with stress. Tongue pale with thin coat. Pulse wiry...")
        if st.button("Structure as SOAP"):
            if raw_notes:
                st.markdown("#### Structured Note")
                st.write("**Subjective:** " + raw_notes[:200] + "...")
                st.write("**Objective:** Tongue & pulse findings noted. Further examination recommended.")
                st.write("**Assessment:** Pattern differentiation pending full evaluation.")
                st.write("**Plan:** Acupuncture + lifestyle recommendations. Follow-up in 1 week.")
                st.info("Review and edit before adding to the patient record.")
            else:
                st.warning("Enter notes first.")

# --- ABOUT ---
elif page == "About":
    st.markdown('<p class="main-header">About AcuHub</p>', unsafe_allow_html=True)
    st.markdown("""
    **AcuHub** was created to give acupuncture specialists practical AI tools that respect the depth of the medicine.
    
    We believe technology should support clinical judgment, not replace it. Every feature is built with practitioners who understand both classical theory and modern practice.
    
    ### Our Approach
    - Grounded in classical point indications and pattern differentiation
    - Transparent recommendations (no black-box claims)
    - Privacy-first: no patient data is stored on our servers in this demo
    - Continuously refined with feedback from licensed acupuncturists
    """)
    st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=1200", caption="Supporting the practice of acupuncture")

# --- CONTACT ---
elif page == "Contact":
    st.markdown('<p class="main-header">Contact Us</p>', unsafe_allow_html=True)
    st.markdown("Interested in AcuHub for your clinic or school?")
    with st.form("contact"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        clinic = st.text_input("Clinic / Organization")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you! We'll be in touch soon.")
            st.balloons()

st.sidebar.markdown("---")
st.sidebar.caption(f"AcuHub • {datetime.now().year}")
How to run it
Save the code above as acuhub.py
Install dependencies:
bash
pip install streamlit pandas
Launch:
bash
streamlit run acuhub.py
What’s included
Home — Branding, value proposition, and tool highlights
AI Tools:
Point Recommender — Symptom input → suggested points (rule-based demo; ready for real LLM integration)
Treatment Plan Generator — Creates multi-session protocols with downloadable CSV
Clinical Notes Assistant — Structures free text into SOAP format
About and Contact pages
Professional medical-aesthetic styling
Would you like me to expand any of the tools (e.g., add real LLM calls via API, more point data, multi-page structure, or authentication)? Or generate a custom logo/branding image for the site?




Ask anything
No file chosen
