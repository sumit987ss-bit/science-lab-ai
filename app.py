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
    st.subheader("Experiment 01
    st.button("🔌 Open Virtual Circuit Lab", key="open_circuit_from_ohms", use_container_width=True, on_click=go, args=("circuit",)) · Virtual Circuit: Ohm's Law")
    st.write("Adjust the battery voltage and resistor value. Watch the ideal circuit readings update.")
    st.info("**Ohm's Law:** I = V / R  ·  This is a mathematical simulation, not a physical electrical circuit.")

    left, right = st.columns([0.9, 1.3], gap="large")
    with left:
        st.markdown("### 🎛️ Circuit controls")
        voltage = st.slider("Battery voltage (V)", min_value=0.0, max_value=24.0, value=12.0, step=1.0, key="circuit_voltage")
        resistance = st.slider("Resistance (Ω)", min_value=1.0, max_value=100.0, value=6.0, step=1.0, key="circuit_resistance")
        st.caption("Try changing one control at a time.")
        st.markdown("**Prediction challenge**")
        prediction = st.selectbox("If voltage stays the same and resistance doubles, current will…", [
            "Choose a prediction", "Double", "Stay the same", "Become half"
        ], key="circuit_prediction")
        if prediction != "Choose a prediction":
            if prediction == "Become half":
                st.success("Correct! Since I = V/R, doubling R halves the current when V is fixed.")
            else:
                st.warning("Not quite. With fixed voltage, doubling resistance makes current half as large.")

    current = voltage / resistance
    power = voltage * current
    # Draw a schematic with an ammeter in series and a voltmeter connected in parallel.
    svg = f"""
    <div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">
    <svg viewBox="0 0 700 285" role="img" aria-label="Schematic of an ideal battery, ammeter in series, resistor and voltmeter in parallel" style="width:100%;height:auto;display:block;">
      <g fill="none" stroke="#168b91" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
        <path d="M95 75 H210 M270 75 H340 M450 75 H590 V220 H95 V75"/>
        <path d="M340 75 l15 -12 l15 24 l15 -24 l15 24 l15 -24 l15 24 l20 -12"/>
        <path d="M95 125 V220"/>
        <path d="M340 75 V140 M450 75 V140"/>
        <path d="M340 140 H365 M425 140 H450"/>
      </g>
      <g stroke="#168b91" stroke-width="4" fill="none">
        <circle cx="240" cy="75" r="30" fill="rgba(22,139,145,.08)"/>
        <circle cx="395" cy="140" r="30" fill="rgba(22,139,145,.08)"/>
        <path d="M76 145 H114 M84 164 H106" />
      </g>
      <g fill="currentColor" font-family="Arial,sans-serif" font-size="16" text-anchor="middle">
        <text x="240" y="81" font-weight="700">A</text>
        <text x="395" y="146" font-weight="700">V</text>
        <text x="395" y="36">Resistor</text>
        <text x="240" y="36">Ammeter</text>
        <text x="395" y="194">Voltmeter</text>
        <text x="95" y="112">Battery</text>
        <text x="350" y="258">Ideal circuit schematic · readings shown at right</text>
      </g>
      <g fill="#e0a52b">
        <path d="M155 214 l16 6 l-16 6 z"/>
        <path d="M560 105 l6 16 l6 -16 z"/>
      </g>
    </svg>
    </div>
    """
    with right:
        st.markdown("### 🔌 Virtual circuit")
        st.markdown(svg, unsafe_allow_html=True)
        m1, m2 = st.columns(2)
        m1.metric("Ammeter reading", f"{current:.3f} A")
        m2.metric("Voltmeter reading", f"{voltage:.2f} V")
        m3, m4 = st.columns(2)
        m3.metric("Resistance", f"{resistance:.1f} Ω")
        m4.metric("Power", f"{power:.3f} W")
        st.success(f"Calculated current: I = V / R = {voltage:.1f} / {resistance:.1f} = **{current:.3f} A**")

    st.markdown("### 📈 Current–voltage graph")
    st.write(f"The resistance is fixed at {resistance:.1f} Ω for this graph.")
    volts = list(range(0, 25))
    data = pd.DataFrame({
        "Voltage (V)": volts,
        "Current (A)": [v / resistance for v in volts],
    }).set_index("Voltage (V)")
    st.line_chart(data, y="Current (A)")
    with st.expander("🧠 Explain the circuit"):
        st.markdown(
            "- **Ammeter:** connected in series to measure current.\n"
            "- **Voltmeter:** connected in parallel across the resistor to measure potential difference.\n"
            "- **Resistor:** limits current in the ideal model.\n"
            "- **Prediction:** when voltage is fixed, increasing resistance reduces current.\n"
            "- The simulator calculates ideal readings; it does not model wire resistance, meter loading or component heating."
        )
    st.caption("Safety and accuracy: This is a virtual schematic only, not a wiring guide for mains electricity. The model assumes an ohmic resistor at constant physical conditions.")

def virtual_circuit_lab():
    if st.button("← Back to Electricity Lab"):
        go("electricity")
        st.rerun()

    st.title("🔌 Virtual Circuit Lab")
    st.write("Change battery voltage and resistance, open or close the switch, and observe the virtual meters.")
    st.info("Ideal model: ammeter in series, voltmeter in parallel across the resistor.")

    left, right = st.columns([1, 1.2], gap="large")
    with left:
        st.markdown("### Circuit controls")
        voltage = st.slider("Battery voltage (V)", 0.0, 24.0, 12.0, 1.0, key="circuit_voltage")
        resistance = st.slider("Resistor (Ω)", 1.0, 100.0, 6.0, 1.0, key="circuit_resistance")
        closed = st.checkbox("Close the switch", value=True, key="circuit_closed")
        st.caption("An open switch breaks the circuit, so no current flows.")

    current = voltage / resistance if closed else 0.0
    resistor_voltage = voltage if closed else 0.0
    power = resistor_voltage * current

    with right:
        st.markdown("### Live circuit diagram")
        wire = "#22a06b" if closed else "#d97706"
        switch_label = "SWITCH CLOSED" if closed else "SWITCH OPEN"
        switch_symbol = '<line x1="215" y1="55" x2="255" y2="55" stroke="' + wire + '" stroke-width="5"/>' if closed else '<line x1="215" y1="55" x2="252" y2="36" stroke="' + wire + '" stroke-width="5"/>'
        svg = (
            '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:8px;background:rgba(128,128,128,.035);">'
            '<svg viewBox="0 0 520 300" width="100%" role="img" aria-label="Virtual battery resistor circuit with ammeter and voltmeter">'
            '<g fill="none" stroke="' + wire + '" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M70 55 H190"/>' + switch_symbol +
            '<path d="M255 55 H340 V105"/><path d="M340 175 V245 H70 V165"/>'
            '<path d="M70 55 V112"/><path d="M70 165 V245"/>'
            '<path d="M340 105 H390"/><path d="M340 175 H390"/>'
            '</g>'
            '<g fill="none" stroke="#64748b" stroke-width="4">'
            '<circle cx="285" cy="55" r="25" fill="rgba(128,128,128,.08)"/>'
            '<rect x="315" y="105" width="50" height="70" rx="5" fill="rgba(128,128,128,.08)"/>'
            '<circle cx="390" cy="140" r="25" fill="rgba(128,128,128,.08)"/>'
            '<line x1="50" y1="118" x2="90" y2="118"/><line x1="58" y1="132" x2="82" y2="132"/><line x1="50" y1="146" x2="90" y2="146"/>'
            '</g>'
            '<g fill="currentColor" font-size="14" text-anchor="middle">'
            '<text x="285" y="61" font-weight="700">A</text><text x="340" y="144" font-weight="700">R</text>'
            '<text x="390" y="146" font-weight="700">V</text><text x="70" y="184">Battery</text>'
            '<text x="285" y="22">Switch</text><text x="340" y="194">' + f'{resistance:.0f} Ω' + '</text>'
            '<text x="390" y="184">Across R</text><text x="260" y="278">' + switch_label + '</text>'
            '</g></svg></div>'
        )
        st.markdown(svg, unsafe_allow_html=True)

    st.markdown("### Meter readings")
    m1, m2, m3 = st.columns(3)
    m1.metric("Ammeter", f"{current:.3f} A")
    m2.metric("Voltmeter across resistor", f"{resistor_voltage:.1f} V")
    m3.metric("Resistor power", f"{power:.3f} W")
    if closed:
        st.success(f"Switch closed: I = V/R = {voltage:.1f}/{resistance:.1f} = **{current:.3f} A**.")
    else:
        st.warning("Switch open: the circuit is broken, so the ideal current is **0 A**. This simplified model shows zero voltage across the resistor.")
    with st.expander("🧠 Understand the circuit"):
        st.markdown(
            "- The **ammeter** is connected in series and measures current.\n"
            "- The **voltmeter** is connected in parallel across the resistor.\n"
            "- With the switch closed, the ideal resistor follows Ohm's law: I = V/R.\n"
            "- This is a simulation, not a physical circuit. Real components have limits."
        )
    st.caption("Ideal DC learning model only. Use real low-voltage classroom equipment with teacher supervision.")

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

if st.session_state.page == "circuit":
    show_header()
    virtual_circuit_lab()
elif st.session_state.page == "electricity":
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
