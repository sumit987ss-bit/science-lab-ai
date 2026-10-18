import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SCIENCE-LAB AI | Electricity Lab",
    page_icon="⚡",
    layout="centered",
)

st.title("⚡ SCIENCE-LAB AI")
st.subheader("Electricity Lab: Ohm's Law")
st.write("Explore how voltage and resistance affect electric current in an ideal ohmic conductor.")

st.info("**Ohm's Law:** Current = Voltage ÷ Resistance  |  **I = V / R**")

st.header("1. Set up your virtual experiment")
voltage = st.slider("Voltage (V)", min_value=0.0, max_value=24.0, value=12.0, step=1.0)
resistance = st.slider("Resistance (Ω)", min_value=1.0, max_value=100.0, value=6.0, step=1.0)

current = voltage / resistance
power = voltage * current

st.header("2. Your results")
c1, c2, c3 = st.columns(3)
c1.metric("Voltage", f"{voltage:.1f} V")
c2.metric("Resistance", f"{resistance:.1f} Ω")
c3.metric("Current", f"{current:.3f} A")
st.metric("Electrical power", f"{power:.3f} W")

st.success(f"Calculation: I = V / R = {voltage:.1f} / {resistance:.1f} = **{current:.3f} A**")

st.header("3. See the relationship")
st.write("This graph shows how current changes with voltage when resistance stays constant.")
voltages = list(range(0, 25, 1))
currents = [v / resistance for v in voltages]
chart_data = pd.DataFrame({"Voltage (V)": voltages, "Current (A)": currents}).set_index("Voltage (V)")
st.line_chart(chart_data, y="Current (A)")

st.header("4. Try these discoveries")
st.markdown(
    "- **Increase voltage** while keeping resistance fixed: current increases proportionally.\n"
    "- **Increase resistance** while keeping voltage fixed: current decreases.\n"
    "- **Set voltage to 0 V**: the ideal circuit current is 0 A."
)

st.subheader("Quick challenge")
challenge_voltage = 9
challenge_resistance = 3
with st.expander("Can you predict the current?"):
    st.write(f"If voltage is {challenge_voltage} V and resistance is {challenge_resistance} Ω, what is the current?")
    st.write("**Answer:** I = V / R = 9 / 3 = **3 A**.")

st.caption(
    "Scientific note: This simulator uses I = V/R for an ideal ohmic conductor. "
    "In a real experiment, resistance can change with temperature and components have limits. "
    "This is a learning simulation, not a real electrical circuit."
)
st.divider()
st.write("Built for student exploration • SCIENCE-LAB AI")
