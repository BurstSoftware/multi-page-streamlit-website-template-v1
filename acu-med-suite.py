import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="AcuHub",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling — text forced to black on light cards
st.markdown("""
<style>
    .hero {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a4f 100%);
        padding: 4rem 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .hero h1 { font-size: 3.2rem; margin-bottom: 0.5rem; font-weight: 700; color: white; }
    .hero p { font-size: 1.4rem; opacity: 0.95; color: white; }
    .peace { font-size: 1.6rem; font-weight: 500; color: #d8f3dc; margin-top: 1rem; }

    .service-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2d6a4f;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #000000 !important;
    }
    .service-card h4 { 
        margin-top: 0; 
        color: #1e3a5f !important; 
    }
    .service-card p { 
        color: #000000 !important; 
    }

    .highlight { 
        background-color: #d8f3dc; 
        padding: 1.5rem; 
        border-radius: 10px; 
        color: #000000 !important;
    }
    .highlight h3, 
    .highlight p, 
    .highlight li, 
    .highlight ul,
    .highlight strong {
        color: #000000 !important;
    }
    .highlight strong {
        color: #1e3a5f !important;
    }

    .cta-box {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d6a4f 100%);
        padding: 3rem 2rem;
        border-radius: 12px;
        text-align: center;
        color: white;
        margin-top: 2rem;
    }
    .cta-box h2 { color: white; margin-bottom: 0.5rem; }
    .cta-box p { color: #e8f5e9; font-size: 1.15rem; margin-bottom: 1.5rem; }
    .book-btn {
        display: inline-block;
        background-color: #ffffff;
        color: #1e3a5f !important;
        font-weight: 700;
        font-size: 1.15rem;
        padding: 0.9rem 2.2rem;
        border-radius: 8px;
        text-decoration: none;
        transition: all 0.2s ease;
    }
    .book-btn:hover {
        background-color: #d8f3dc;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <h1>AcuHub</h1>
    <p>An AI tools company for acupuncturists</p>
    <p class="peace">AI does the work you don’t want to do.<br>Bringing peace to acupuncturists’ lives.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Built for solo practitioners — whether you accept insurance or not.")

# CORE MESSAGE
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="highlight">
    <h3>What we do</h3>
    <p>We handle the administrative burden so you can focus on patients.</p>
    <ul>
        <li>Claims & medical billing</li>
        <li>Insurance payments, status & documents</li>
        <li>Bookkeeping & certified tax support</li>
        <li>EHR, scheduling, notes & billing</li>
        <li>Document hub & communications</li>
        <li>HIPAA compliance & data encryption</li>
        <li>Legal support for liability protection</li>
        <li>Work comp & reference systems</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight">
    <h3>The outcome</h3>
    <p><strong>Peace of mind.</strong></p>
    <p>Track insurance payments and claim status without chasing anyone.</p>
    <p>Your own EHR system that pulls what you need — easy for you, powerful for your admin team.</p>
    <p>Quality service, strong presence, and tools designed so the AI (and the team) do the work.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Everything bundled in one place")

# Service cards
services = [
    ("Claims & Medical Billing", "Dedicated billers who submit, track, and follow up on claims."),
    ("Insurance Payments & Status", "Real-time visibility into payments, denials, and required docs."),
    ("Accountant & Tax Specialists", "Certified tax support and bookkeeping tailored for acupuncturists."),
    ("Attorney & Liability Support", "Legal help focused on reducing malpractice exposure."),
    ("EHR + Scheduling + Notes", "Your own system — scheduling, clinical notes, and billing integrated."),
    ("Doc Hub & Comms", "Secure document storage and client communication platform."),
    ("HIPAA & Encryption", "Certified compliance and strong data encryption."),
    ("Admin & Work Comp", "Administrative support and workers’ compensation handling."),
]

cols = st.columns(4)
for i, (title, desc) in enumerate(services):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="service-card">
            <h4>{title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")  # spacing

st.markdown("---")
st.markdown("""
### Designed for ease of use
- **Practitioners** get a simple interface and peace of mind.  
- **Administrative staff** can track insurance payments, claim status, and documents efficiently.  
- Everything is pulled together so you don’t have to manage multiple vendors or systems.

**Core outcome:** Providing a service for the things you don’t want to do — so you can bring more peace into your practice and your life.
""")

# Slick CTA — Book a presentation
st.markdown("""
<div class="cta-box">
    <h2>See AcuMed Suite in Action</h2>
    <p>Book a short software presentation and discover how AcuHub removes the administrative load<br>so you can focus on your patients — and your peace of mind.</p>
    <a class="book-btn" href="https://book.squareup.com/appointments/6kib7afaj4d9tv/location/LBDGTAVYB2WK6?buttonTextColor=ffffff&color=212121&locale=en&referrer=so&service_id=C6SYSXTTBBVJIMRL5VI2IMDS" target="_blank">
        Book Your Presentation
    </a>
</div>
""", unsafe_allow_html=True)

st.caption(f"AcuHub • An AI tools company for acupuncturists • {datetime.now().year}")
