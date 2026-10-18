import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SCIENCE-LAB AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Visual design ----------
st.markdown("""
<style>
    .block-container {padding-top: 1.4rem; padding-bottom: 2.5rem; max-width: 1100px;}
    .hero {
        padding: 1.7rem 1.5rem; border-radius: 22px;
        background: linear-gradient(120deg, #102a43 0%, #176b87 58%, #27a6a1 100%);
        color: white; margin-bottom: 1.1rem;
    }
    .hero h1 {color: white; font-size: clamp(2rem, 5vw, 3.2rem); margin: 0;}
    .hero p {color: #e5f6ff; font-size: 1.08rem; margin: .55rem 0 0 0;}
    .eyebrow {text-transform: uppercase; letter-spacing: .14em; font-size: .76rem; font-weight: 700; color: #b9f3ee;}
    .lab-card {
        border: 1px solid rgba(120,140,160,.32); border-radius: 17px;
        padding: 1.1rem; min-height: 155px; margin-bottom: .35rem;
        background: rgba(128,128,128,.045);
    }
    .lab-icon {font-size: 1.8rem;}
    .lab-card h3 {margin: .45rem 0 .35rem 0; font-size: 1.12rem;}
    .lab-card p {font-size: .91rem; opacity: .82; margin-bottom: .7rem;}
    .small-note {font-size: .86rem; opacity: .78;}
    div.stButton > button {border-radius: 11px; min-height: 2.65rem; font-weight: 600;}
</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page):
    st.session_state.page = page

def show_header():
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">Explore • Experiment • Understand</div>
      <h1>🔬 SCIENCE-LAB AI</h1>
      <p>Your interactive virtual science laboratory — discover science by changing variables, testing ideas and learning from results.</p>
    </div>
    """, unsafe_allow_html=True)

def ohms_lab():
    if st.button("← Back to Science Lab Home"):
        go("home")
        st.rerun()

    st.title("⚡ Electricity Lab")
    st.subheader("Experiment 01 · Ohm's Law")
    st.write("Investigate how voltage and resistance affect current in an ideal ohmic conductor.")
    st.info("**Ohm's Law:** Current = Voltage ÷ Resistance  |  **I = V / R**")

    left, right = st.columns([1, 1.35], gap="large")
    with left:
        st.markdown("### Experiment controls")
        voltage = st.slider("Voltage (V)", min_value=0.0, max_value=24.0, value=12.0, step=1.0)
        resistance = st.slider("Resistance (Ω)", min_value=1.0, max_value=100.0, value=6.0, step=1.0)
        st.caption("Change one control at a time to observe its effect.")
    current = voltage / resistance
    power = voltage * current
    with right:
        st.markdown("### Live results")
        a, b = st.columns(2)
        a.metric("Current", f"{current:.3f} A")
        b.metric("Power", f"{power:.3f} W")
        a, b = st.columns(2)
        a.metric("Voltage", f"{voltage:.1f} V")
        b.metric("Resistance", f"{resistance:.1f} Ω")
        st.success(f"I = V / R = {voltage:.1f} / {resistance:.1f} = **{current:.3f} A**")

    st.markdown("### Explore the graph")
    st.write("Current versus voltage while resistance remains constant.")
    volts = list(range(0, 25))
    data = pd.DataFrame({
        "Voltage (V)": volts,
        "Current (A)": [v / resistance for v in volts],
    }).set_index("Voltage (V)")
    st.line_chart(data, y="Current (A)")
    with st.expander("🧠 What did we learn?"):
        st.markdown(
            "- At fixed resistance, increasing voltage increases current proportionally.\n"
            "- At fixed voltage, increasing resistance decreases current.\n"
            "- At 0 V, the ideal circuit current is 0 A."
        )
    st.caption("Scientific note: This model assumes an ideal ohmic conductor at constant physical conditions. Real components have limits, and resistance may change with temperature.")

def coming_soon(title, description, examples):
    if st.button("← Back to Science Lab Home"):
        go("home")
        st.rerun()
    st.title(title)
    st.info("This lab module is planned for a future update. The working Electricity Lab is available now.")
    st.write(description)
    st.markdown("**Planned experiments**")
    for item in examples:
        st.markdown(f"- {item}")
    st.button("Open Electricity Lab instead", on_click=go, args=("electricity",))

if st.session_state.page == "electricity":
    show_header()
    ohms_lab()
elif st.session_state.page == "chemistry":
    show_header()
    coming_soon("🧪 Chemistry Lab", "Explore substances, indicators, reactions and safe virtual investigations.", ["Acid–base indicator explorer", "Reaction and equation balancing", "pH scale explorer"])
elif st.session_state.page == "biology":
    show_header()
    coming_soon("🧬 Biology Lab", "Explore living systems with interactive models and guided observations.", ["Cell explorer", "Human body systems", "Photosynthesis investigation"])
elif st.session_state.page == "physics":
    show_header()
    coming_soon("🚀 Physics Lab", "Discover motion, forces, light, sound and energy through simulations.", ["Motion and speed simulator", "Reflection and refraction", "Energy transformations"])
elif st.session_state.page == "mentor":
    show_header()
    coming_soon("🤖 AI Science Mentor", "A guided science assistant will help students ask questions, understand concepts and interpret experiment results.", ["Ask science questions in simple language", "Get experiment-specific explanations", "English and Punjabi support"])
else:
    show_header()
    st.markdown("## Choose your laboratory")
    st.write("Pick a lab to begin. Electricity is ready to use; other modules will be added in future updates.")

    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown('<div class="lab-card"><div class="lab-icon">⚡</div><h3>Electricity Lab</h3><p>Explore voltage, current, resistance and live graphs.</p><span>READY · 1 experiment</span></div>', unsafe_allow_html=True)
        st.button("Open Electricity Lab →", key="electricity_btn", use_container_width=True, on_click=go, args=("electricity",))
    with c2:
        st.markdown('<div class="lab-card"><div class="lab-icon">🧪</div><h3>Chemistry Lab</h3><p>Investigate indicators, reactions and the pH scale.</p><span>COMING SOON</span></div>', unsafe_allow_html=True)
        st.button("Explore Chemistry plans", key="chemistry_btn", use_container_width=True, on_click=go, args=("chemistry",))
    c3, c4 = st.columns(2, gap="medium")
    with c3:
        st.markdown('<div class="lab-card"><div class="lab-icon">🚀</div><h3>Physics Lab</h3><p>Explore motion, forces, light, sound and energy.</p><span>COMING SOON</span></div>', unsafe_allow_html=True)
        st.button("Explore Physics plans", key="physics_btn", use_container_width=True, on_click=go, args=("physics",))
    with c4:
        st.markdown('<div class="lab-card"><div class="lab-icon">🧬</div><h3>Biology Lab</h3><p>Discover cells, body systems and living processes.</p><span>COMING SOON</span></div>', unsafe_allow_html=True)
        st.button("Explore Biology plans", key="biology_btn", use_container_width=True, on_click=go, args=("biology",))
    st.markdown("---")
    mentor_left, mentor_right = st.columns([2, 1], gap="medium")
    with mentor_left:
        st.markdown("### 🤖 AI Science Mentor")
        st.write("A future learning companion for explanations, experiment guidance and bilingual science support.")
    with mentor_right:
        st.button("Preview AI Mentor plans", key="mentor_btn", use_container_width=True, on_click=go, args=("mentor",))

    st.markdown("---")
    st.markdown("### How SCIENCE-LAB AI works")
    s1, s2, s3 = st.columns(3)
    s1.markdown("**1 · Predict**\n\nMake a prediction before changing a variable.")
    s2.markdown("**2 · Experiment**\n\nChange a setting and observe the results.")
    s3.markdown("**3 · Understand**\n\nUse evidence and scientific principles to explain what happened.")
    st.caption("Built for curious students • SCIENCE-LAB AI")
