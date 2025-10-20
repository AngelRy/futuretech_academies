import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="FutureTech Academies",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM STYLES ---
st.markdown("""
<style>
    /* Overall theme */
    body {
        background-color: #0A192F;
        color: #E6E6E6;
    }
    .main {
        background-color: #0A192F;
        color: #E6E6E6;
    }
    h1, h2, h3, h4 {
        color: #64FFDA;
    }
    p, li {
        color: #CCD6F6;
    }
    hr {
        border: 1px solid #233554;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #112240;
        border-radius: 10px;
        padding: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #CCD6F6;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: #233554;
        color: #64FFDA;
    }

    /* Buttons */
    .stButton>button {
        background-color: #64FFDA;
        color: #0A192F;
        border: none;
        padding: 0.6em 1.4em;
        border-radius: 6px;
        font-weight: bold;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #52E0C4;
        color: #0A192F;
        transform: scale(1.02);
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 5rem 2rem 3rem 2rem;
        background: radial-gradient(circle at top left, #112240, #0A192F 70%);
        border-radius: 16px;
        margin-bottom: 3rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .hero h3 {
        color: #A8B2D1;
        font-weight: 400;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Robot-icon.svg/512px-Robot-icon.svg.png", width=150)
    st.title("🌐 FutureTech Academies")
    st.markdown("""
    **Empowering the next generation of innovators**  
    within the **Technology Park** ecosystem.
    
    ---
    **Focus Sectors:**
    - Artificial Intelligence  
    - Robotics & Automation  
    - Cybersecurity  
    - MedTech  
    - Smart Solutions  
    
    ---
    **Contact**  
    📧 info@futuretech-park.com  
    🌍 www.futuretech-park.com
    """)
    st.markdown("---")
    st.caption("© 2025 FutureTech Academies")

# --- HERO SECTION ---
st.markdown("""
<div class="hero">
    <h1>🎓 FutureTech Academies</h1>
    <h3>Empowering AI talent within the Technology Park ecosystem</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    explore = st.button("🚀 Explore Academies")

# When the user clicks the button, jump to content
if explore:
    st.session_state["show_content"] = True
else:
    st.session_state.setdefault("show_content", False)

# --- MAIN CONTENT ---
if st.session_state["show_content"]:
    st.markdown("""
    ### Transforming Talent for the AI-Powered Economy
    **FutureTech Academies** bridge education, innovation, and industry —  
    preparing learners for the **fastest-growing technology careers**.

    ---
    """)

    with st.expander("📘 Common Program Structure"):
        st.markdown("""
        | Level | Duration | Focus | Outcome |
        |:------|:----------|:-------|:---------|
        | **Level 1 – Foundations** | 6–8 weeks | Core principles, key tools, essential workflows | Certificate of Completion |
        | **Level 2 – Applied Specialization** | 12–16 weeks | Advanced concepts, real-world projects, teamwork | Professional Diploma |
        | **Level 3 – Capstone & Industry Residency** | 8–12 weeks | Industry collaboration, applied innovation | Industry-Validated Certification |
        """)

    st.markdown("---")
    st.subheader("🧩 Explore the Academy Portfolio")

    # --- TABS FOR EACH ACADEMY ---
    tabs = st.tabs([
        "Applied AI & MLOps",
        "Generative & Multimodal AI",
        "Data Engineering & Analytics",
        "AI Product, Governance & Ethics",
        "AI for Industry & Human-Augmentation"
    ])

    with tabs[0]:
        st.header("🤖 Applied AI & MLOps Academy")
        st.caption("**Motto:** From Model to Production")
        st.markdown("""
        **Duration:** ~8 months  
        - **Level 1:** *Foundations of AI Systems Engineering*  
        - **Level 2:** *Deployment & Automation*  
        - **Level 3:** *Capstone Residency* — deploy a production-grade AI solution.  
        """)
        st.info("Outcome: Ready to manage the full AI lifecycle — from data to deployment.")

    with tabs[1]:
        st.header("🎨 Generative & Multimodal AI Academy")
        st.caption("**Motto:** Create with Models")
        st.markdown("""
        **Duration:** ~7 months  
        - **Level 1:** *Fundamentals of Generative Models*  
        - **Level 2:** *Domain Applications* — text, image, audio, robotics.  
        - **Level 3:** *Capstone Residency* — build a multimodal AI system.  
        """)
        st.info("Outcome: Create advanced AI tools across multiple data modalities.")

    with tabs[2]:
        st.header("📊 Data Engineering & Analytics Academy")
        st.caption("**Motto:** Make Data Usable")
        st.markdown("""
        **Duration:** ~6–7 months  
        - **Level 1:** *Data Systems Foundations*  
        - **Level 2:** *Infrastructure for AI* — data streams, governance, analytics.  
        - **Level 3:** *Capstone Residency* — build an end-to-end analytics system.  
        """)
        st.info("Outcome: Specialists in data infrastructure for scalable AI systems.")

    with tabs[3]:
        st.header("⚖️ AI Product, Governance & Ethics Academy")
        st.caption("**Motto:** Lead AI Responsibly")
        st.markdown("""
        **Duration:** ~6 months  
        - **Level 1:** *Responsible AI Fundamentals*  
        - **Level 2:** *Governance & Ethics* — fairness, compliance, AI Act.  
        - **Level 3:** *Capstone Residency* — design a responsible AI policy.  
        """)
        st.info("Outcome: Professionals who ensure ethical and compliant AI deployment.")

    with tabs[4]:
        st.header("🤝 AI for Industry & Human-Augmentation Academy")
        st.caption("**Motto:** AI Applied to Real-World Systems")
        st.markdown("""
        **Duration:** ~9 months  
        - **Level 1:** *Foundations of Robotics & Smart Systems*  
        - **Level 2:** *Industrial & Assistive Applications*  
        - **Level 3:** *Capstone Residency* — prototype an intelligent system.  
        """)
        st.info("Outcome: Integrating AI into robotics, automation, and assistive technologies.")

    st.markdown("---")
    st.subheader("🧭 Progression & Flexibility")
    st.markdown("""
    - Learners may start directly at **Level 2** with prior knowledge.  
    - Each level provides a **microcredential**, stackable toward a **Full Academy Diploma**.  
    - Includes **corporate fast-tracks** and **joint research residencies** with Technology Park startups.
    """)

    st.success("FutureTech Academies — Powering the Next Generation of AI Talent 🚀")

else:
    st.markdown("<div style='text-align:center; color:#A8B2D1;'>Scroll or click 'Explore Academies' to continue ↓</div>", unsafe_allow_html=True)
