import streamlit as st
import pandas as pd

st.set_page_config(page_title="SCIENCE-LAB AI", page_icon="🔬", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.block-container{padding-top:1.2rem;padding-bottom:2.5rem;max-width:1100px}
.hero{padding:1.5rem;border-radius:20px;background:linear-gradient(120deg,#102a43,#176b87 58%,#27a6a1);color:white;margin-bottom:1rem}
.hero h1{color:white;font-size:clamp(2rem,5vw,3rem);margin:0}
.hero p{color:#e5f6ff;font-size:1.03rem;margin:.5rem 0 0}
.lab-card{border:1px solid rgba(120,140,160,.32);border-radius:16px;padding:1rem;min-height:135px;background:rgba(128,128,128,.04)}
div.stButton>button{border-radius:11px;min-height:2.55rem;font-weight:600}
</style>
""", unsafe_allow_html=True)

T = {
"en": {
"tagline":"Explore • Experiment • Understand",
"intro":"Your interactive virtual science laboratory. Change variables, test ideas and learn from results.",
"home":"Science Lab Home","choose":"Choose your laboratory","choose_desc":"Select a lab to begin. Electricity Lab has the first class-wise experiment collection.",
"electricity":"Electricity Lab","chemistry":"Chemistry Lab","physics":"Physics Lab","biology":"Biology Lab","mentor":"AI Science Mentor",
"electricity_desc":"Explore circuits, current, voltage, resistance and magnetic effects.",
"chemistry_desc":"Investigate indicators, reactions, mixtures and pH.",
"physics_desc":"Discover motion, forces, light, sound and energy.",
"biology_desc":"Explore cells, body systems and living processes.",
"mentor_desc":"Ask questions and get guided science explanations.",
"open":"Open","planned":"Planned for a future update","class":"Select class","experiment":"Select experiment",
"aim":"Aim","how":"How to explore","controls":"Interactive controls","result":"Live observations","conclusion":"Conclusion","back":"← Back to Science Lab Home",
"voltage":"Battery voltage (V)","resistance":"Resistance (Ω)","switch":"Close the switch","material":"Test material",
"predict":"Prediction challenge","predict_q":"If voltage stays the same and resistance doubles, current will…",
"select_prediction":"Choose a prediction","double":"Double","same":"Stay the same","half":"Become half","correct":"Correct! With fixed voltage, doubling resistance halves current.",
"incorrect":"Try again. With fixed voltage, doubling resistance halves current.",
"current":"Current","power":"Electrical power","circuit":"Circuit state","closed":"Closed — current flows","open_circuit":"Open — no current flows",
"conductivity":"Conductivity result","conductor":"Conducts in this model","insulator":"Does not conduct in this model",
"graph":"Current–voltage graph","graph_note":"Ideal model: the resistance stays constant.",
"note":"Learning note","safe":"This is a virtual learning model, not a real electrical circuit. Never use household mains electricity for experiments.",
"exp_count":"25 class-wise experiments","home_note":"Choose a subject. Each lab will eventually have Classes 6–10, with five experiments per class.",
"planned_items":"Planned topics","language":"Language / ਭਾਸ਼ਾ","en_name":"English","pa_name":"ਪੰਜਾਬੀ",
"units":"Units","magnetic":"Relative magnetic effect (illustrative)","turns":"Coil turns","current_control":"Current (A)",
"liquid":"Choose a liquid","water":"Distilled water","salt":"Salt solution","sugar":"Sugar solution","lemon":"Lemon juice",
"temp":"Temperature (°C)","time":"Time (hours)","turns_label":"Number of turns","bulbs":"Number of bulbs",
"amount":"Amount (illustrative)","ph":"pH value","light":"Light intensity","distance":"Distance","speed":"Speed",
"formula":"Model formula","feedback":"Try changing one control at a time and explain the result in your own words.","bulb_on":"Bulb is glowing","bulb_off":"Bulb is off","complete_path":"Complete circuit path","broken_path":"Circuit path is broken","visual_circuit":"Interactive circuit diagram","battery":"Cell / battery","bulb":"Bulb","wire":"Connecting wires","switch_label":"Switch",
},
"pa": {
"tagline":"ਖੋਜੋ • ਪ੍ਰਯੋਗ ਕਰੋ • ਸਮਝੋ",
"intro":"ਤੁਹਾਡੀ ਇੰਟਰਐਕਟਿਵ ਵਰਚੁਅਲ ਵਿਗਿਆਨ ਪ੍ਰਯੋਗਸ਼ਾਲਾ। ਮੁੱਲ ਬਦਲੋ, ਵਿਚਾਰ ਪਰਖੋ ਅਤੇ ਨਤੀਜਿਆਂ ਤੋਂ ਸਿੱਖੋ।",
"home":"ਵਿਗਿਆਨ ਲੈਬ ਦਾ ਮੁੱਖ ਪੰਨਾ","choose":"ਆਪਣੀ ਪ੍ਰਯੋਗਸ਼ਾਲਾ ਚੁਣੋ","choose_desc":"ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਲੈਬ ਚੁਣੋ। ਬਿਜਲੀ ਲੈਬ ਵਿੱਚ ਜਮਾਤ ਅਨੁਸਾਰ ਪ੍ਰਯੋਗਾਂ ਦਾ ਪਹਿਲਾ ਸੰਗ੍ਰਹਿ ਹੈ।",
"electricity":"ਬਿਜਲੀ ਲੈਬ","chemistry":"ਰਸਾਇਣ ਵਿਗਿਆਨ ਲੈਬ","physics":"ਭੌਤਿਕ ਵਿਗਿਆਨ ਲੈਬ","biology":"ਜੀਵ ਵਿਗਿਆਨ ਲੈਬ","mentor":"AI ਵਿਗਿਆਨ ਮਾਰਗਦਰਸ਼ਕ",
"electricity_desc":"ਸਰਕਟ, ਕਰੰਟ, ਵੋਲਟੇਜ, ਰੋਧ ਅਤੇ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵਾਂ ਦੀ ਖੋਜ ਕਰੋ।",
"chemistry_desc":"ਸੂਚਕਾਂ, ਰਸਾਇਣਕ ਕਿਰਿਆਵਾਂ, ਮਿਸ਼ਰਣਾਂ ਅਤੇ pH ਦੀ ਜਾਂਚ ਕਰੋ।",
"physics_desc":"ਗਤੀ, ਬਲ, ਪ੍ਰਕਾਸ਼, ਧੁਨੀ ਅਤੇ ਊਰਜਾ ਬਾਰੇ ਜਾਣੋ।",
"biology_desc":"ਕੋਸ਼ਿਕਾਵਾਂ, ਸਰੀਰਕ ਪ੍ਰਣਾਲੀਆਂ ਅਤੇ ਜੀਵਨ ਪ੍ਰਕਿਰਿਆਵਾਂ ਦੀ ਖੋਜ ਕਰੋ।",
"mentor_desc":"ਸਵਾਲ ਪੁੱਛੋ ਅਤੇ ਵਿਗਿਆਨ ਦੀ ਸੌਖੀ ਵਿਆਖਿਆ ਲਵੋ।",
"open":"ਖੋਲ੍ਹੋ","planned":"ਅਗਲੇ ਅੱਪਡੇਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕੀਤਾ ਜਾਵੇਗਾ","class":"ਜਮਾਤ ਚੁਣੋ","experiment":"ਪ੍ਰਯੋਗ ਚੁਣੋ",
"aim":"ਉਦੇਸ਼","how":"ਕਿਵੇਂ ਪ੍ਰਯੋਗ ਕਰੋ","controls":"ਇੰਟਰਐਕਟਿਵ ਕੰਟਰੋਲ","result":"ਤੁਰੰਤ ਨਿਰੀਖਣ","conclusion":"ਸਿੱਟਾ","back":"← ਵਿਗਿਆਨ ਲੈਬ ਦੇ ਮੁੱਖ ਪੰਨੇ ਤੇ ਜਾਓ",
"voltage":"ਬੈਟਰੀ ਵੋਲਟੇਜ (V)","resistance":"ਰੋਧ (Ω)","switch":"ਸਵਿੱਚ ਬੰਦ ਕਰੋ","material":"ਜਾਂਚਣ ਲਈ ਪਦਾਰਥ",
"predict":"ਅਨੁਮਾਨ ਲਗਾਓ","predict_q":"ਜੇ ਵੋਲਟੇਜ ਇੱਕੋ ਰਹੇ ਅਤੇ ਰੋਧ ਦੁੱਗਣਾ ਹੋ ਜਾਵੇ, ਤਾਂ ਕਰੰਟ…",
"select_prediction":"ਅਨੁਮਾਨ ਚੁਣੋ","double":"ਦੁੱਗਣਾ ਹੋਵੇਗਾ","same":"ਇੱਕੋ ਰਹੇਗਾ","half":"ਅੱਧਾ ਰਹਿ ਜਾਵੇਗਾ","correct":"ਬਿਲਕੁਲ ਠੀਕ! ਵੋਲਟੇਜ ਇੱਕੋ ਹੋਣ ਤੇ ਰੋਧ ਦੁੱਗਣਾ ਕਰਨ ਨਾਲ ਕਰੰਟ ਅੱਧਾ ਹੋ ਜਾਂਦਾ ਹੈ।",
"incorrect":"ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰੋ। ਵੋਲਟੇਜ ਇੱਕੋ ਹੋਣ ਤੇ ਰੋਧ ਦੁੱਗਣਾ ਕਰਨ ਨਾਲ ਕਰੰਟ ਅੱਧਾ ਹੋ ਜਾਂਦਾ ਹੈ।",
"current":"ਕਰੰਟ","power":"ਬਿਜਲੀ ਸ਼ਕਤੀ","circuit":"ਸਰਕਟ ਦੀ ਸਥਿਤੀ","closed":"ਬੰਦ — ਕਰੰਟ ਵਹਿੰਦਾ ਹੈ","open_circuit":"ਖੁੱਲ੍ਹਾ — ਕਰੰਟ ਨਹੀਂ ਵਹਿੰਦਾ",
"conductivity":"ਚਾਲਕਤਾ ਦਾ ਨਤੀਜਾ","conductor":"ਇਸ ਮਾਡਲ ਵਿੱਚ ਚਾਲਕ ਹੈ","insulator":"ਇਸ ਮਾਡਲ ਵਿੱਚ ਚਾਲਕ ਨਹੀਂ ਹੈ",
"graph":"ਕਰੰਟ–ਵੋਲਟੇਜ ਗ੍ਰਾਫ","graph_note":"ਆਦਰਸ਼ ਮਾਡਲ: ਰੋਧ ਸਥਿਰ ਰਹਿੰਦਾ ਹੈ।",
"note":"ਸਿੱਖਣ ਲਈ ਨੋਟ","safe":"ਇਹ ਸਿਰਫ਼ ਵਰਚੁਅਲ ਸਿੱਖਣ ਮਾਡਲ ਹੈ, ਅਸਲੀ ਬਿਜਲੀ ਸਰਕਟ ਨਹੀਂ। ਘਰੇਲੂ ਮੇਨ ਬਿਜਲੀ ਨਾਲ ਪ੍ਰਯੋਗ ਕਦੇ ਨਾ ਕਰੋ।",
"exp_count":"ਜਮਾਤ ਅਨੁਸਾਰ 25 ਪ੍ਰਯੋਗ","home_note":"ਵਿਸ਼ਾ ਚੁਣੋ। ਅੱਗੇ ਹਰ ਲੈਬ ਵਿੱਚ ਜਮਾਤ 6ਵੀਂ ਤੋਂ 10ਵੀਂ ਤੱਕ, ਹਰ ਜਮਾਤ ਲਈ ਪੰਜ ਪ੍ਰਯੋਗ ਹੋਣਗੇ।",
"planned_items":"ਯੋਜਨਾਬੱਧ ਵਿਸ਼ੇ","language":"ਭਾਸ਼ਾ / Language","en_name":"English","pa_name":"ਪੰਜਾਬੀ",
"units":"ਇਕਾਈਆਂ","magnetic":"ਸਾਪੇਖ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ (ਸਮਝਾਉਣ ਲਈ)","turns":"ਕੋਇਲ ਦੇ ਚੱਕਰ","current_control":"ਕਰੰਟ (A)",
"liquid":"ਤਰਲ ਚੁਣੋ","water":"ਡਿਸਟਿਲਡ ਪਾਣੀ","salt":"ਨਮਕ ਦਾ ਘੋਲ","sugar":"ਚੀਨੀ ਦਾ ਘੋਲ","lemon":"ਨਿੰਬੂ ਦਾ ਰਸ",
"temp":"ਤਾਪਮਾਨ (°C)","time":"ਸਮਾਂ (ਘੰਟੇ)","turns_label":"ਚੱਕਰਾਂ ਦੀ ਗਿਣਤੀ","bulbs":"ਬਲਬਾਂ ਦੀ ਗਿਣਤੀ",
"amount":"ਮਾਤਰਾ (ਸਮਝਾਉਣ ਲਈ)","ph":"pH ਮੁੱਲ","light":"ਰੋਸ਼ਨੀ ਦੀ ਤੀਬਰਤਾ","distance":"ਦੂਰੀ","speed":"ਗਤੀ",
"formula":"ਮਾਡਲ ਦਾ ਸੂਤਰ","feedback":"ਇੱਕ ਵਾਰ ਵਿੱਚ ਇੱਕ ਕੰਟਰੋਲ ਬਦਲੋ ਅਤੇ ਨਤੀਜੇ ਨੂੰ ਆਪਣੇ ਸ਼ਬਦਾਂ ਵਿੱਚ ਸਮਝਾਓ।","bulb_on":"ਬਲਬ ਜਗ ਰਿਹਾ ਹੈ","bulb_off":"ਬਲਬ ਬੰਦ ਹੈ","complete_path":"ਸਰਕਟ ਦਾ ਰਸਤਾ ਪੂਰਾ ਹੈ","broken_path":"ਸਰਕਟ ਦਾ ਰਸਤਾ ਟੁੱਟਿਆ ਹੋਇਆ ਹੈ","visual_circuit":"ਇੰਟਰਐਕਟਿਵ ਸਰਕਟ ਚਿੱਤਰ","battery":"ਸੈੱਲ / ਬੈਟਰੀ","bulb":"ਬਲਬ","wire":"ਜੋੜਨ ਵਾਲੀਆਂ ਤਾਰਾਂ","switch_label":"ਸਵਿੱਚ",
}
}

# Class-wise Electricity Lab experiments: English title, Punjabi title, aim EN, aim PA, type, concept note EN, concept note PA
EXPERIMENTS = {
6: [
("Build a Simple Electric Circuit","ਸਧਾਰਨ ਬਿਜਲੀ ਸਰਕਟ ਬਣਾਓ","Connect a cell, wires, bulb and switch to make a complete path.","ਸੈੱਲ, ਤਾਰਾਂ, ਬਲਬ ਅਤੇ ਸਵਿੱਚ ਜੋੜ ਕੇ ਪੂਰਾ ਰਸਤਾ ਬਣਾਓ।","circuit","A bulb glows only when the conducting path is complete.","ਬਲਬ ਤਦ ਹੀ ਜਗਦਾ ਹੈ ਜਦੋਂ ਚਾਲਕ ਰਸਤਾ ਪੂਰਾ ਹੋਵੇ।"),
("How Does a Bulb Glow?","ਬਲਬ ਕਿਵੇਂ ਜਗਦਾ ਹੈ?","Explore the bulb terminals and the need for a complete conducting path.","ਬਲਬ ਦੇ ਟਰਮੀਨਲ ਅਤੇ ਪੂਰੇ ਚਾਲਕ ਰਸਤੇ ਦੀ ਲੋੜ ਸਮਝੋ।","circuit","Both bulb terminals must connect appropriately in a complete circuit.","ਪੂਰੇ ਸਰਕਟ ਵਿੱਚ ਬਲਬ ਦੇ ਦੋਵੇਂ ਟਰਮੀਨਲ ਠੀਕ ਤਰ੍ਹਾਂ ਜੁੜੇ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।"),
("Conductors and Insulators","ਚਾਲਕ ਅਤੇ ਕੁਚਾਲਕ","Test virtual materials and see whether they complete a circuit.","ਵਰਚੁਅਲ ਪਦਾਰਥਾਂ ਦੀ ਜਾਂਚ ਕਰੋ ਕਿ ਕੀ ਉਹ ਸਰਕਟ ਪੂਰਾ ਕਰਦੇ ਹਨ।","conductors","Metals usually conduct electricity; rubber and plastic usually insulate.","ਧਾਤਾਂ ਆਮ ਤੌਰ ਤੇ ਬਿਜਲੀ ਚਲਾਉਂਦੀਆਂ ਹਨ; ਰਬੜ ਅਤੇ ਪਲਾਸਟਿਕ ਆਮ ਤੌਰ ਤੇ ਕੁਚਾਲਕ ਹਨ।"),
("Open and Closed Circuits","ਖੁੱਲ੍ਹੇ ਅਤੇ ਬੰਦ ਸਰਕਟ","Operate a virtual switch and observe the bulb and current.","ਵਰਚੁਅਲ ਸਵਿੱਚ ਚਲਾਓ ਅਤੇ ਬਲਬ ਤੇ ਕਰੰਟ ਦਾ ਨਿਰੀਖਣ ਕਰੋ।","circuit","An open switch breaks the path; a closed switch completes it.","ਖੁੱਲ੍ਹਾ ਸਵਿੱਚ ਰਸਤਾ ਤੋੜਦਾ ਹੈ; ਬੰਦ ਸਵਿੱਚ ਰਸਤਾ ਪੂਰਾ ਕਰਦਾ ਹੈ।"),
("Magnetic Materials","ਚੁੰਬਕੀ ਪਦਾਰਥ","Compare magnetic and non-magnetic objects in a simple model.","ਸਧਾਰਨ ਮਾਡਲ ਵਿੱਚ ਚੁੰਬਕੀ ਅਤੇ ਗੈਰ-ਚੁੰਬਕੀ ਚੀਜ਼ਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।","magnet","Iron and steel are commonly attracted by magnets; many other materials are not.","ਲੋਹਾ ਅਤੇ ਸਟੀਲ ਆਮ ਤੌਰ ਤੇ ਚੁੰਬਕ ਵੱਲ ਖਿੱਚੇ ਜਾਂਦੇ ਹਨ; ਕਈ ਹੋਰ ਪਦਾਰਥ ਨਹੀਂ।")
],
7: [
("Circuit Components and Symbols","ਸਰਕਟ ਦੇ ਭਾਗ ਅਤੇ ਚਿੰਨ੍ਹ","Identify cells, bulbs, switches and wires in a circuit diagram.","ਸਰਕਟ ਚਿੱਤਰ ਵਿੱਚ ਸੈੱਲ, ਬਲਬ, ਸਵਿੱਚ ਅਤੇ ਤਾਰਾਂ ਪਛਾਣੋ।","circuit","Circuit symbols make electrical diagrams easier to read.","ਸਰਕਟ ਚਿੰਨ੍ਹ ਬਿਜਲੀ ਦੇ ਚਿੱਤਰ ਸਮਝਣੇ ਆਸਾਨ ਬਣਾਉਂਦੇ ਹਨ।"),
("Heating Effect of Current","ਕਰੰਟ ਦਾ ਤਾਪੀ ਪ੍ਰਭਾਵ","Explore how current and resistance affect heating in a safe model.","ਸੁਰੱਖਿਅਤ ਮਾਡਲ ਵਿੱਚ ਵੇਖੋ ਕਿ ਕਰੰਟ ਅਤੇ ਰੋਧ ਤਾਪ ਨੂੰ ਕਿਵੇਂ ਪ੍ਰਭਾਵਿਤ ਕਰਦੇ ਹਨ।","heating","Electrical energy can be converted into heat in a resistor.","ਰੋਧਕ ਵਿੱਚ ਬਿਜਲੀ ਊਰਜਾ ਤਾਪ ਵਿੱਚ ਬਦਲ ਸਕਦੀ ਹੈ।"),
("Make a Virtual Electromagnet","ਵਰਚੁਅਲ ਬਿਜਲੀ-ਚੁੰਬਕ ਬਣਾਓ","Change coil turns and current to explore magnetic strength.","ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ ਸਮਝਣ ਲਈ ਕੋਇਲ ਦੇ ਚੱਕਰ ਅਤੇ ਕਰੰਟ ਬਦਲੋ।","electromagnet","In this illustrative model, more coil turns or current increase relative strength.","ਇਸ ਸਮਝਾਉਣ ਵਾਲੇ ਮਾਡਲ ਵਿੱਚ ਚੱਕਰ ਜਾਂ ਕਰੰਟ ਵਧਾਉਣ ਨਾਲ ਸਾਪੇਖ ਤਾਕਤ ਵਧਦੀ ਹੈ।"),
("Why Is a Fuse Needed?","ਫਿਊਜ਼ ਦੀ ਲੋੜ ਕਿਉਂ ਹੈ?","Model how a protective fuse interrupts excessive current.","ਸਮਝੋ ਕਿ ਸੁਰੱਖਿਆ ਫਿਊਜ਼ ਬਹੁਤ ਜ਼ਿਆਦਾ ਕਰੰਟ ਨੂੰ ਕਿਵੇਂ ਰੋਕਦਾ ਹੈ।","fuse","A fuse is a safety device designed to break a circuit under specified overcurrent conditions.","ਫਿਊਜ਼ ਇੱਕ ਸੁਰੱਖਿਆ ਯੰਤਰ ਹੈ ਜੋ ਨਿਰਧਾਰਤ ਹੱਦ ਤੋਂ ਵੱਧ ਕਰੰਟ ਹੋਣ ਤੇ ਸਰਕਟ ਤੋੜਨ ਲਈ ਬਣਿਆ ਹੈ।"),
("Magnetic Effect of Current","ਕਰੰਟ ਦਾ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ","Visualise a magnetic field produced by current in a wire.","ਤਾਰ ਵਿੱਚ ਕਰੰਟ ਕਾਰਨ ਬਣਨ ਵਾਲੇ ਚੁੰਬਕੀ ਖੇਤਰ ਨੂੰ ਸਮਝੋ।","magnetic_field","Electric current produces a magnetic field around a conductor.","ਬਿਜਲੀ ਕਰੰਟ ਚਾਲਕ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਚੁੰਬਕੀ ਖੇਤਰ ਬਣਾਉਂਦਾ ਹੈ।")
],
8: [
("Can Liquids Conduct Electricity?","ਕੀ ਤਰਲ ਬਿਜਲੀ ਚਲਾ ਸਕਦੇ ਹਨ?","Compare the conductivity of different virtual liquid samples.","ਵੱਖ-ਵੱਖ ਵਰਚੁਅਲ ਤਰਲਾਂ ਦੀ ਚਾਲਕਤਾ ਦੀ ਤੁਲਨਾ ਕਰੋ।","liquids","Conductivity depends on mobile ions; the sample model is qualitative.","ਚਾਲਕਤਾ ਚਲਣਯੋਗ ਆਇਨਾਂ ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ; ਇਹ ਮਾਡਲ ਗੁਣਾਤਮਕ ਹੈ।"),
("Chemical Effects of Electric Current","ਬਿਜਲੀ ਕਰੰਟ ਦੇ ਰਸਾਇਣਕ ਪ੍ਰਭਾਵ","Explore how current through a suitable solution can cause chemical change.","ਜਾਣੋ ਕਿ ਢੁਕਵੇਂ ਘੋਲ ਵਿੱਚੋਂ ਕਰੰਟ ਲੰਘਣ ਨਾਲ ਰਸਾਇਣਕ ਤਬਦੀਲੀ ਹੋ ਸਕਦੀ ਹੈ।","electrolysis","Electrolysis involves chemical changes driven by electric current.","ਇਲੈਕਟ੍ਰੋਲਾਈਸਿਸ ਵਿੱਚ ਬਿਜਲੀ ਕਰੰਟ ਕਾਰਨ ਰਸਾਇਣਕ ਤਬਦੀਲੀਆਂ ਹੁੰਦੀਆਂ ਹਨ।"),
("Understand Electroplating","ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਨੂੰ ਸਮਝੋ","Simulate metal coating and learn why it is used.","ਧਾਤ ਦੀ ਪਰਤ ਚੜ੍ਹਾਉਣ ਦਾ ਮਾਡਲ ਵੇਖੋ ਅਤੇ ਇਸ ਦੀ ਵਰਤੋਂ ਸਮਝੋ।","electroplating","Electroplating deposits a thin layer of one metal on another object.","ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਵਿੱਚ ਇੱਕ ਧਾਤ ਦੀ ਪਤਲੀ ਪਰਤ ਦੂਜੀ ਵਸਤੂ ਉੱਤੇ ਜਮਾਈ ਜਾਂਦੀ ਹੈ।"),
("Electricity Can Produce Magnetism","ਬਿਜਲੀ ਨਾਲ ਚੁੰਬਕਤਾ ਪੈਦਾ ਹੋ ਸਕਦੀ ਹੈ","Investigate the relationship between current and magnetic effects.","ਕਰੰਟ ਅਤੇ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵਾਂ ਵਿਚਕਾਰ ਸਬੰਧ ਸਮਝੋ।","electromagnet","A coil carrying current can behave like a magnet.","ਕਰੰਟ ਵਾਲੀ ਕੋਇਲ ਚੁੰਬਕ ਵਾਂਗ ਵਰਤਾਅ ਕਰ ਸਕਦੀ ਹੈ।"),
("How Does a Cell Supply Electricity?","ਸੈੱਲ ਬਿਜਲੀ ਕਿਵੇਂ ਦਿੰਦਾ ਹੈ?","Explore the conversion of chemical energy into electrical energy.","ਰਸਾਇਣਕ ਊਰਜਾ ਦੇ ਬਿਜਲੀ ਊਰਜਾ ਵਿੱਚ ਬਦਲਣ ਨੂੰ ਸਮਝੋ।","cell","A cell converts stored chemical energy into electrical energy.","ਸੈੱਲ ਵਿੱਚ ਸੰਭਾਲੀ ਰਸਾਇਣਕ ਊਰਜਾ ਬਿਜਲੀ ਊਰਜਾ ਵਿੱਚ ਬਦਲਦੀ ਹੈ।")
],
9: [
("Explore Electric Charge","ਬਿਜਲਈ ਚਾਰਜ ਦੀ ਖੋਜ","Model positive and negative charges and their attraction or repulsion.","ਧਨਾਤਮਕ ਅਤੇ ਰਿਣਾਤਮਕ ਚਾਰਜਾਂ ਦਾ ਖਿੱਚ ਅਤੇ ਵਿਕਰਸ਼ਣ ਮਾਡਲ ਰਾਹੀਂ ਸਮਝੋ।","charge","Like charges repel and unlike charges attract in the basic model.","ਮੂਲ ਮਾਡਲ ਵਿੱਚ ਇੱਕੋ ਕਿਸਮ ਦੇ ਚਾਰਜ ਦੂਰ ਧੱਕਦੇ ਹਨ ਅਤੇ ਵੱਖਰੀ ਕਿਸਮ ਦੇ ਖਿੱਚਦੇ ਹਨ।"),
("Voltage, Current and Resistance","ਵੋਲਟੇਜ, ਕਰੰਟ ਅਤੇ ਰੋਧ","Change circuit values and explore their relationship in a resistor.","ਸਰਕਟ ਦੇ ਮੁੱਲ ਬਦਲ ਕੇ ਰੋਧਕ ਵਿੱਚ ਉਨ੍ਹਾਂ ਦਾ ਸਬੰਧ ਸਮਝੋ।","ohms","For an ohmic resistor at constant conditions, current is proportional to voltage.","ਸਥਿਰ ਹਾਲਤਾਂ ਵਿੱਚ ਓਮਿਕ ਰੋਧਕ ਲਈ ਕਰੰਟ ਵੋਲਟੇਜ ਦੇ ਅਨੁਪਾਤ ਵਿੱਚ ਹੁੰਦਾ ਹੈ।"),
("Series and Parallel Circuits","ਲੜੀਵਾਰ ਅਤੇ ਸਮਾਂਤਰ ਸਰਕਟ","Compare bulb behaviour and current paths in two arrangements.","ਦੋ ਬਣਤਰਾਂ ਵਿੱਚ ਬਲਬਾਂ ਦੇ ਵਰਤਾਅ ਅਤੇ ਕਰੰਟ ਦੇ ਰਸਤੇ ਦੀ ਤੁਲਨਾ ਕਰੋ।","series_parallel","Series has one path; parallel circuits have branches.","ਲੜੀਵਾਰ ਸਰਕਟ ਵਿੱਚ ਇੱਕ ਰਸਤਾ ਹੁੰਦਾ ਹੈ; ਸਮਾਂਤਰ ਸਰਕਟ ਵਿੱਚ ਕਈ ਸ਼ਾਖਾਂ ਹੁੰਦੀਆਂ ਹਨ।"),
("Electrical Power and Energy","ਬਿਜਲੀ ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ","Explore how electrical energy changes into light, heat or motion in everyday devices.","ਰੋਜ਼ਾਨਾ ਉਪਕਰਣਾਂ ਵਿੱਚ ਬਿਜਲੀ ਊਰਜਾ ਦੇ ਰੋਸ਼ਨੀ, ਤਾਪ ਜਾਂ ਗਤੀ ਵਿੱਚ ਬਦਲਣ ਨੂੰ ਸਮਝੋ।","power","Electrical power describes how quickly energy is transferred; devices transform electrical energy into useful forms.","ਬਿਜਲੀ ਸ਼ਕਤੀ ਊਰਜਾ ਦੇ ਤਬਾਦਲੇ ਦੀ ਦਰ ਦਰਸਾਉਂਦੀ ਹੈ; ਉਪਕਰਣ ਬਿਜਲੀ ਊਰਜਾ ਨੂੰ ਲਾਭਦਾਇਕ ਰੂਪਾਂ ਵਿੱਚ ਬਦਲਦੇ ਹਨ।"),
("Static Electricity","ਸਥਿਰ ਬਿਜਲੀ","Explore how electric charge can attract light objects in a model.","ਮਾਡਲ ਰਾਹੀਂ ਸਮਝੋ ਕਿ ਬਿਜਲਈ ਚਾਰਜ ਹਲਕੀਆਂ ਵਸਤੂਆਂ ਨੂੰ ਖਿੱਚ ਸਕਦਾ ਹੈ।","charge","Static charge can exert forces without a continuous circuit.","ਸਥਿਰ ਚਾਰਜ ਲਗਾਤਾਰ ਸਰਕਟ ਤੋਂ ਬਿਨਾਂ ਵੀ ਬਲ ਲਗਾ ਸਕਦਾ ਹੈ।")
],
10: [
("Verify Ohm's Law","ਓਮ ਦੇ ਨਿਯਮ ਦੀ ਪੁਸ਼ਟੀ","Investigate the relationship between voltage, current and resistance.","ਵੋਲਟੇਜ, ਕਰੰਟ ਅਤੇ ਰੋਧ ਵਿਚਕਾਰ ਸਬੰਧ ਦੀ ਜਾਂਚ ਕਰੋ।","ohms","For a fixed resistor, I = V/R. The app's circuit model is ideal.","ਸਥਿਰ ਰੋਧ ਲਈ I = V/R। ਐਪ ਦਾ ਸਰਕਟ ਮਾਡਲ ਆਦਰਸ਼ ਹੈ।"),
("Resistance in Series and Parallel","ਲੜੀਵਾਰ ਅਤੇ ਸਮਾਂਤਰ ਰੋਧ","Compare equivalent resistance and current for different arrangements.","ਵੱਖ-ਵੱਖ ਬਣਤਰਾਂ ਲਈ ਸਮਤੁੱਲ ਰੋਧ ਅਤੇ ਕਰੰਟ ਦੀ ਤੁਲਨਾ ਕਰੋ।","series_parallel","Series resistances add; parallel equivalent resistance is lower than either branch resistance.","ਲੜੀਵਾਰ ਰੋਧ ਜੋੜੇ ਜਾਂਦੇ ਹਨ; ਸਮਾਂਤਰ ਸਮਤੁੱਲ ਰੋਧ ਹਰ ਸ਼ਾਖਾ ਦੇ ਰੋਧ ਤੋਂ ਘੱਟ ਹੁੰਦਾ ਹੈ।"),
("Calculate Electrical Power","ਬਿਜਲੀ ਸ਼ਕਤੀ ਦੀ ਗਣਨਾ","Explore P = VI and electrical energy use in an ideal model.","ਆਦਰਸ਼ ਮਾਡਲ ਵਿੱਚ P = VI ਅਤੇ ਬਿਜਲੀ ਊਰਜਾ ਦੀ ਵਰਤੋਂ ਸਮਝੋ।","power","Power in watts equals voltage in volts multiplied by current in amperes.","ਵਾਟ ਵਿੱਚ ਸ਼ਕਤੀ, ਵੋਲਟੇਜ ਅਤੇ ਐਂਪੀਅਰ ਵਿੱਚ ਕਰੰਟ ਦੇ ਗੁਣਨਫਲ ਦੇ ਬਰਾਬਰ ਹੈ।"),
("Magnetic Field Around a Wire","ਤਾਰ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਚੁੰਬਕੀ ਖੇਤਰ","Explore how current direction affects the magnetic field direction.","ਕਰੰਟ ਦੀ ਦਿਸ਼ਾ ਬਦਲਣ ਨਾਲ ਚੁੰਬਕੀ ਖੇਤਰ ਦੀ ਦਿਸ਼ਾ ਕਿਵੇਂ ਬਦਲਦੀ ਹੈ, ਸਮਝੋ।","magnetic_field","Reversing current reverses the magnetic field direction.","ਕਰੰਟ ਦੀ ਦਿਸ਼ਾ ਉਲਟਣ ਨਾਲ ਚੁੰਬਕੀ ਖੇਤਰ ਦੀ ਦਿਸ਼ਾ ਵੀ ਉਲਟ ਜਾਂਦੀ ਹੈ।"),
("Explore a Simple Electric Motor","ਸਧਾਰਨ ਬਿਜਲੀ ਮੋਟਰ ਦੀ ਖੋਜ","Explore how magnetic forces can produce rotation in a motor model.","ਮੋਟਰ ਦੇ ਮਾਡਲ ਵਿੱਚ ਚੁੰਬਕੀ ਬਲਾਂ ਨਾਲ ਘੁੰਮਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਸਮਝੋ।","motor","A motor converts electrical energy into mechanical motion.","ਮੋਟਰ ਬਿਜਲੀ ਊਰਜਾ ਨੂੰ ਮਕੈਨੀਕਲ ਗਤੀ ਵਿੱਚ ਬਦਲਦੀ ਹੈ।")
]
}

def tr(key):
    return T[st.session_state.language].get(key, T["en"].get(key, key))

if "language" not in st.session_state:
    st.session_state.language = "en"
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_class" not in st.session_state:
    st.session_state.selected_class = 10
if "selected_experiment" not in st.session_state:
    st.session_state.selected_experiment = 0

def go(page):
    st.session_state.page = page

def show_header():
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f'<div class="hero"><div style="font-size:.78rem;letter-spacing:.12em;color:#b9f3ee;font-weight:700">{tr("tagline")}</div><h1>🔬 SCIENCE-LAB AI</h1><p>{tr("intro")}</p></div>', unsafe_allow_html=True)
    with c2:
        st.selectbox(tr("language"), ["en", "pa"], format_func=lambda x: "English" if x == "en" else "ਪੰਜਾਬੀ", key="language")

def electricity_lab():
    if st.button(tr("back")):
        go("home")
        st.rerun()
    st.title("⚡ " + tr("electricity"))
    st.caption(tr("exp_count") + " · PSEB 2026–27 syllabus alignment reviewed by the project owner")
    classes = [6, 7, 8, 9, 10]
    selected_class = st.selectbox(tr("class"), classes, index=classes.index(st.session_state.selected_class), format_func=lambda x: f"Class {x}" if st.session_state.language == "en" else f"{x}ਵੀਂ ਜਮਾਤ", key="class_picker")
    st.session_state.selected_class = selected_class
    exp_list = EXPERIMENTS[selected_class]
    exp_index = st.selectbox(tr("experiment"), list(range(5)), format_func=lambda i: f"EXPERIMENT {i+1} · {exp_list[i][0 if st.session_state.language == 'en' else 1]}", key=f"exp_picker_{selected_class}")
    en_title, pa_title, en_aim, pa_aim, kind, en_note, pa_note = exp_list[exp_index]
    title = en_title if st.session_state.language == "en" else pa_title
    aim = en_aim if st.session_state.language == "en" else pa_aim
    note = en_note if st.session_state.language == "en" else pa_note
    st.markdown("---")
    st.header(f"EXPERIMENT {exp_index+1}")
    st.subheader(title)
    st.markdown(f"**{tr('aim')}:** {aim}")
    st.markdown(f"**{tr('how')}:** {tr('feedback')}")
    magnetic_experiment = kind == "magnet" and selected_class == 6 and exp_index == 4
    symbol_experiment = selected_class == 7 and exp_index == 0
    heating_experiment = selected_class == 7 and exp_index == 1 and kind == "heating"
    electromagnet_experiment = selected_class == 7 and exp_index == 2 and kind == "electromagnet"
    wide_experiment = magnetic_experiment or symbol_experiment or heating_experiment or electromagnet_experiment
    if wide_experiment:
        left, right = st.container(), st.container()
    else:
        left, right = st.columns([1, 1.2], gap="large")
    with left:
        if not wide_experiment:
            st.markdown("### " + tr("controls"))
        # Keep controls aligned with the class level: Classes 6–9 use qualitative models.
        # Numerical voltage, resistance, coil-turn and current controls are shown only
        # for relevant Class 10 quantitative experiments.
        quantitative_class10 = selected_class == 10 and (kind in ("ohms", "series_parallel", "power", "heating") or (kind == "magnetic_field" and exp_index == 3) or (kind == "motor" and exp_index == 4))
        voltage = st.slider(tr("voltage"), 0, 24, 12, 1, key=f"v_{selected_class}_{exp_index}") if quantitative_class10 else 12
        resistance = st.slider(tr("resistance"), 1, 100, 6, 1, key=f"r_{selected_class}_{exp_index}") if quantitative_class10 else 6
        # Class 7 Experiment 4 uses a current-condition selector, not a switch checkbox.
        fuse_current_condition = "normal"
        if selected_class == 7 and exp_index == 3 and kind == "fuse":
            is_pa_fuse = st.session_state.language != "en"
            fuse_current_condition = st.selectbox(
                "ਕਰੰਟ ਦੀ ਸਥਿਤੀ" if is_pa_fuse else "Current condition",
                ["normal", "high"],
                format_func=lambda x: (
                    ("ਆਮ ਕਰੰਟ" if x == "normal" else "ਬਹੁਤ ਜ਼ਿਆਦਾ ਕਰੰਟ")
                    if is_pa_fuse else
                    ("Normal current" if x == "normal" else "Excessive current")
                ),
                key=f"class7_fuse_condition_{st.session_state.language}",
            )
        closed = st.checkbox(tr("switch"), value=True, key=f"sw_{selected_class}_{exp_index}") if ((kind in ("circuit", "motor", "electromagnet", "magnetic_field", "ohms", "series_parallel", "power", "heating") or (selected_class == 8 and exp_index == 4 and kind == "cell")) and not (selected_class == 6 and exp_index == 1) and not (selected_class == 9 and exp_index == 2 and kind == "series_parallel")) else True
        turns = 10
        current_control = 1.0
        material = None
        liquid = None
        heat_current_level = "Medium" if st.session_state.language == "en" else "ਦਰਮਿਆਨਾ"
        heat_resistance_level = "Medium" if st.session_state.language == "en" else "ਦਰਮਿਆਨਾ"
        if heating_experiment:
            level_options = ["Low", "Medium", "High"] if st.session_state.language == "en" else ["ਘੱਟ", "ਦਰਮਿਆਨਾ", "ਵੱਧ"]
            heat_current_level = st.selectbox(
                "Current level / ਕਰੰਟ ਦਾ ਪੱਧਰ",
                level_options,
                index=1,
                key=f"class7_heat_current_level_{st.session_state.language}",
            )
            heat_resistance_level = st.selectbox(
                "Resistance level / ਰੋਧ ਦਾ ਪੱਧਰ",
                level_options,
                index=1,
                key=f"class7_heat_resistance_level_{st.session_state.language}",
            )
        class9_voltage_level = "Medium"
        class9_resistance_level = "Medium"
        class9_power_device = "bulb"
        if selected_class == 9 and exp_index == 3 and kind == "power":
            is_pa_power_control = st.session_state.language != "en"
            power_devices = ["bulb", "fan", "heater"]
            power_device_labels = {
                "bulb": "ਬਲਬ" if is_pa_power_control else "Bulb (light and some heat)",
                "fan": "ਪੱਖਾ" if is_pa_power_control else "Fan (motion)",
                "heater": "ਹੀਟਰ" if is_pa_power_control else "Heater (heat)",
            }
            class9_power_device = st.selectbox(
                "ਉਪਕਰਣ ਚੁਣੋ" if is_pa_power_control else "Choose an electrical device",
                power_devices,
                format_func=lambda x: power_device_labels[x],
                key=f"class9_power_device_{st.session_state.language}",
            )
        if selected_class == 9 and exp_index == 1 and kind == "ohms":
            is_pa_ohms_control = st.session_state.language != "en"
            level_values = ["Low", "Medium", "High"]
            level_labels = {
                "Low": "ਘੱਟ" if is_pa_ohms_control else "Low",
                "Medium": "ਦਰਮਿਆਨਾ" if is_pa_ohms_control else "Medium",
                "High": "ਵੱਧ" if is_pa_ohms_control else "High",
            }
            class9_voltage_level = st.selectbox(
                "ਵੋਲਟੇਜ ਦਾ ਪੱਧਰ" if is_pa_ohms_control else "Voltage level",
                level_values,
                index=1,
                format_func=lambda x: level_labels[x],
                key=f"class9_voltage_level_{st.session_state.language}",
            )
            class9_resistance_level = st.selectbox(
                "ਰੋਧ ਦਾ ਪੱਧਰ" if is_pa_ohms_control else "Resistance level",
                level_values,
                index=1,
                format_func=lambda x: level_labels[x],
                key=f"class9_resistance_level_{st.session_state.language}",
            )
        if kind == "conductors":
            material_options = {
                "en": ["Copper", "Aluminium", "Iron", "Rubber", "Plastic", "Wood"],
                "pa": ["ਤਾਂਬਾ", "ਐਲੂਮੀਨੀਅਮ", "ਲੋਹਾ", "ਰਬੜ", "ਪਲਾਸਟਿਕ", "ਲੱਕੜ"]
            }
            material = st.selectbox(tr("material"), material_options[st.session_state.language], key=f"mat_{selected_class}_{exp_index}")
        static_charge_active = True
        static_target = "paper"
        if selected_class == 9 and exp_index == 4 and kind == "charge":
            is_pa_static_control = st.session_state.language != "en"
            static_charge_active = st.checkbox(
                "ਵਾਲਾਂ/ਉੱਨ ਨਾਲ ਗੁਬਾਰਾ ਰਗੜੋ" if is_pa_static_control else "Rub balloon on hair or wool",
                value=True,
                key=f"class9_static_rub_{st.session_state.language}",
            )
            static_target_options = ["paper", "water"]
            static_target_labels = {
                "paper": "ਕਾਗਜ਼ ਦੇ ਛੋਟੇ ਟੁਕੜੇ" if is_pa_static_control else "Tiny paper pieces",
                "water": "ਪਾਣੀ ਦੀ ਪਤਲੀ ਧਾਰ" if is_pa_static_control else "Thin stream of water",
            }
            static_target = st.selectbox(
                "ਜਾਂਚਣ ਲਈ ਚੀਜ਼" if is_pa_static_control else "Choose what to attract",
                static_target_options,
                format_func=lambda x: static_target_labels[x],
                key=f"class9_static_target_{st.session_state.language}",
            )
        charge_pair_mode = "unlike"
        if selected_class == 9 and exp_index == 0 and kind == "charge":
            is_pa_charge_control = st.session_state.language != "en"
            charge_options = ["like_positive", "like_negative", "unlike"]
            charge_labels = {
                "like_positive": "ਧਨਾਤਮਕ + ਧਨਾਤਮਕ" if is_pa_charge_control else "Positive + Positive",
                "like_negative": "ਰਿਣਾਤਮਕ + ਰਿਣਾਤਮਕ" if is_pa_charge_control else "Negative + Negative",
                "unlike": "ਧਨਾਤਮਕ + ਰਿਣਾਤਮਕ" if is_pa_charge_control else "Positive + Negative",
            }
            charge_pair_mode = st.selectbox(
                "ਚਾਰਜਾਂ ਦੀ ਜੋੜੀ ਚੁਣੋ" if is_pa_charge_control else "Choose charge pair",
                charge_options,
                format_func=lambda x: charge_labels[x],
                key=f"class9_charge_pair_{st.session_state.language}",
            )
        if kind == "liquids":
            liquids = ["water", "salt", "sugar", "lemon"]
            liquid = st.selectbox(tr("liquid"), liquids, format_func=lambda x: tr(x), key=f"liq_{selected_class}_{exp_index}")
        electrolysis_solution = "copper"
        if kind == "electrolysis":
            is_pa_electrolysis = st.session_state.language != "en"
            solution_options = ["copper", "lemon", "distilled"]
            solution_labels = {
                "copper": "ਕਾਪਰ ਸਲਫੇਟ ਘੋਲ" if is_pa_electrolysis else "Copper sulphate solution",
                "lemon": "ਨਿੰਬੂ ਵਾਲਾ ਪਾਣੀ" if is_pa_electrolysis else "Lemon water",
                "distilled": "ਡਿਸਟਿਲਡ ਪਾਣੀ" if is_pa_electrolysis else "Distilled water",
            }
            electrolysis_solution = st.selectbox(
                "ਘੋਲ ਚੁਣੋ" if is_pa_electrolysis else "Choose a solution",
                solution_options,
                format_func=lambda x: solution_labels[x],
                key=f"electrolysis_solution_{st.session_state.language}",
            )
        if kind == "ohms" and not (selected_class == 9 and exp_index == 1):
            prediction = st.selectbox(tr("predict_q"), [tr("select_prediction"), tr("double"), tr("same"), tr("half")], key=f"pred_{selected_class}_{exp_index}")
            if prediction != tr("select_prediction"):
                st.success(tr("correct") if prediction == tr("half") else tr("incorrect"))
    current = voltage / resistance if closed else 0.0
    power = voltage * current if closed else 0.0
    # Safe conceptual simulation: excessive current melts the virtual fuse link.
    fuse_blown = kind == "fuse" and fuse_current_condition == "high"
    if kind == "fuse":
        current = 3.0 if fuse_blown else 1.0
        power = 0.0 if fuse_blown else 12.0
    with right:
        st.markdown("### " + tr("result"))
        if selected_class == 10 and exp_index == 0 and kind == "ohms":
            # Class 10 Experiment 1: quantitative verification of Ohm's law.
            is_pa_ohms10 = st.session_state.language != "en"
            measured_current = voltage / resistance if closed else 0.0
            ohms_wire = "#16a34a" if closed else "#94a3b8"
            ohms_bulb = "#fde047" if closed else "#e2e8f0"
            ohms_glow = "filter:drop-shadow(0 0 10px #facc15);" if closed else ""
            ohms_status = ("ਸਵਿੱਚ ਬੰਦ — ਕਰੰਟ ਵਹਿੰਦਾ ਹੈ" if is_pa_ohms10 else "SWITCH ON — CURRENT FLOWS") if closed else ("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ — ਕਰੰਟ ਸਿਫ਼ਰ" if is_pa_ohms10 else "SWITCH OFF — CURRENT IS ZERO")
            ohms_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 460 300" width="100%" role="img" aria-label="Ohm's law circuit showing battery, ammeter in series, resistor and voltmeter in parallel">
  <g fill="none" stroke="{ohms_wire}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M58 68 H132 M184 68 H244 M304 68 H390 V220 H58 V145 M58 68 V105"/>
    <path d="M244 68 V125 M304 68 V125 M244 125 H304"/>
  </g>
  <g stroke="#334155" stroke-width="3"><line x1="40" y1="105" x2="76" y2="105"/><line x1="47" y1="123" x2="69" y2="123"/></g>
  <text x="58" y="162" fill="currentColor" font-size="12" text-anchor="middle">{"ਸੈੱਲ" if is_pa_ohms10 else "CELL"}</text>
  <circle cx="158" cy="68" r="26" fill="#dbeafe" stroke="#2563eb" stroke-width="3"/>
  <text x="158" y="74" fill="#1d4ed8" font-size="18" font-weight="bold" text-anchor="middle">A</text>
  <text x="158" y="32" fill="currentColor" font-size="12" text-anchor="middle">{"ਐਮੀਟਰ" if is_pa_ohms10 else "AMMETER (SERIES)"}</text>
  <rect x="304" y="50" width="86" height="36" rx="7" fill="#fed7aa" stroke="#c2410c" stroke-width="2.5"/>
  <path d="M313 68 l8 -9 l8 18 l8 -18 l8 18 l8 -18 l8 18 l8 -9" fill="none" stroke="#9a3412" stroke-width="2.5"/>
  <text x="347" y="39" fill="currentColor" font-size="12" text-anchor="middle">{"ਰੋਧਕ" if is_pa_ohms10 else "RESISTOR"}</text>
  <circle cx="274" cy="125" r="23" fill="#dcfce7" stroke="#15803d" stroke-width="3"/>
  <text x="274" y="131" fill="#166534" font-size="17" font-weight="bold" text-anchor="middle">V</text>
  <text x="274" y="160" fill="currentColor" font-size="11" text-anchor="middle">{"ਵੋਲਟਮੀਟਰ (ਸਮਾਂਤਰ)" if is_pa_ohms10 else "VOLTMETER (PARALLEL)"}</text>
  <g fill="{ohms_wire}"><path d="M105 220 l-10 -6 v12 Z"/><path d="M215 220 l-10 -6 v12 Z"/></g>
  <circle cx="390" cy="176" r="22" fill="{ohms_bulb}" stroke="#475569" stroke-width="3" style="{ohms_glow}"/>
  <path d="M379 165 l22 22 M401 165 l-22 22" stroke="#475569" stroke-width="3"/>
  <text x="390" y="210" fill="currentColor" font-size="11" text-anchor="middle">{"ਬਲਬ" if is_pa_ohms10 else "BULB"}</text>
  <rect x="70" y="245" width="320" height="35" rx="9" fill="#e2e8f0" stroke="#94a3b8"/>
  <text x="230" y="267" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">{ohms_status}</text>
</svg></div>"""
            st.markdown("#### " + ("ਓਮ ਦੇ ਨਿਯਮ ਦੀ ਜਾਂਚ ਲਈ ਸਰਕਟ" if is_pa_ohms10 else "Circuit to verify Ohm's law"))
            st.markdown(ohms_svg, unsafe_allow_html=True)
            m1, m2, m3 = st.columns(3)
            m1.metric("ਵੋਲਟੇਜ (V)" if is_pa_ohms10 else "Voltage (V)", f"{voltage} V")
            m2.metric("ਕਰੰਟ (I)" if is_pa_ohms10 else "Current (I)", f"{measured_current:.2f} A")
            m3.metric("ਰੋਧ (R)" if is_pa_ohms10 else "Resistance (R)", f"{resistance} Ω")
            st.markdown("**" + ("ਗਣਨਾ" if is_pa_ohms10 else "Calculation") + "**")
            st.latex(r"I = \frac{V}{R} = \frac{" + str(voltage) + "}{" + str(resistance) + "} = " + f"{measured_current:.2f}" + r"\text{ A}")
            st.markdown("**" + ("ਸਥਿਰ ਰੋਧ ਲਈ ਅਵਲੋਕਨ ਸਾਰਣੀ" if is_pa_ohms10 else "Observation table at fixed resistance") + "**")
            table_rows = []
            for test_v in [0, 6, 12, 18, 24]:
                test_i = test_v / resistance if closed else 0.0
                ratio = f"{test_v / test_i:.2f} Ω" if test_i > 0 else "—"
                table_rows.append({
                    ("ਵੋਲਟੇਜ V (V)" if is_pa_ohms10 else "Voltage V (V)"): test_v,
                    ("ਕਰੰਟ I (A)" if is_pa_ohms10 else "Current I (A)"): f"{test_i:.2f}",
                    ("V/I (Ω)" if is_pa_ohms10 else "V/I (Ω)"): ratio,
                })
            st.dataframe(table_rows, hide_index=True, use_container_width=True)
            if closed:
                st.success("V/I ਲਗਭਗ ਸਥਿਰ ਰਹਿੰਦਾ ਹੈ ਅਤੇ ਚੁਣੇ ਰੋਧ ਦੇ ਬਰਾਬਰ ਹੈ — ਇਹ ਓਮ ਦੇ ਨਿਯਮ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ।" if is_pa_ohms10 else f"V/I remains constant at {resistance} Ω for this ideal fixed resistor, so the observations verify Ohm's law.")
            else:
                st.info("ਸਵਿੱਚ ਖੁੱਲ੍ਹਣ ਤੇ ਕਰੰਟ ਸਿਫ਼ਰ ਹੁੰਦਾ ਹੈ; ਨਿਯਮ ਦੀ ਜਾਂਚ ਲਈ ਸਵਿੱਚ ਚਾਲੂ ਕਰੋ।" if is_pa_ohms10 else "With the switch open, current is zero; close the switch to test Ohm's law.")
            st.caption("ਆਦਰਸ਼ ਸਿਮੂਲੇਸ਼ਨ: ਸਾਰਣੀ ਗਣਿਤਕ ਮਾਡਲ ਤੋਂ ਬਣਦੀ ਹੈ, ਅਸਲੀ ਪ੍ਰਯੋਗਸ਼ਾਲਾ ਮਾਪ ਨਹੀਂ।" if is_pa_ohms10 else "Ideal simulation: the table is calculated from the model, not measured laboratory data. In a real experiment, record ammeter and voltmeter readings.")
        elif kind == "magnet" and selected_class == 6 and exp_index == 4:
            # Two-panel interactive visual: material gallery and magnet test outcome.
            is_pa = st.session_state.language != "en"
            magnetic_items = [
                ("Iron nail", "ਲੋਹੇ ਦੀ ਕਿੱਲ", "iron", True),
                ("Steel paper clip", "ਸਟੀਲ ਦੀ ਪੇਪਰ ਕਲਿੱਪ", "clip", True),
                ("Aluminium foil", "ਐਲੂਮੀਨੀਅਮ ਫੋਇਲ", "foil", False),
                ("Copper wire", "ਤਾਂਬੇ ਦੀ ਤਾਰ", "copper", False),
                ("Wood", "ਲੱਕੜ", "wood", False),
                ("Plastic", "ਪਲਾਸਟਿਕ", "plastic", False),
            ]
            magnet_name = "ਚੁੰਬਕ" if is_pa else "BAR MAGNET"
            title_one = "1. ਪਦਾਰਥ ਚੁਣੋ" if is_pa else "1. Select a material"
            title_two = "2. ਨਤੀਜਾ ਵੇਖੋ" if is_pa else "2. See the result"
            gallery = []
            for en_name_i, pa_name_i, shape_i, is_magnetic in magnetic_items:
                name_i = pa_name_i if is_pa else en_name_i
                if shape_i == "iron":
                    drawing = '<path d="M0 0 L15 -8 L105 -8 L118 0 L105 8 L15 8 Z" fill="#94a3b8" stroke="#475569" stroke-width="2"/>'
                elif shape_i == "clip":
                    drawing = '<path d="M10 0 C10 -24 48 -24 48 0 L48 12 C48 27 25 27 25 12 L25 -2 C25 -10 38 -10 38 -2" fill="none" stroke="#64748b" stroke-width="5"/>'
                elif shape_i == "foil":
                    drawing = '<path d="M0 0 L20 -15 L48 -5 L73 -19 L105 -4 L92 17 L55 8 L28 18 Z" fill="#cbd5e1" stroke="#64748b" stroke-width="2"/>'
                elif shape_i == "copper":
                    drawing = '<g fill="none" stroke="#b87333" stroke-width="6"><ellipse cx="35" cy="0" rx="30" ry="17"/><ellipse cx="48" cy="0" rx="30" ry="17"/><ellipse cx="61" cy="0" rx="30" ry="17"/></g>'
                elif shape_i == "wood":
                    drawing = '<path d="M0 -12 L90 -12 L105 0 L15 0 Z" fill="#d6a56b" stroke="#9a6b37" stroke-width="2"/><path d="M15 0 L105 0 L105 15 L15 15 Z" fill="#c58b4f" stroke="#9a6b37" stroke-width="2"/>'
                else:
                    drawing = '<path d="M15 -15 H75 Q90 -15 90 0 V10 Q90 20 75 20 H15 Q0 20 0 10 V0 Q0 -15 15 -15Z" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>'
                gallery.append('<g transform="translate(0,0)">' + drawing + '</g><text x="60" y="45" text-anchor="middle" font-size="11" fill="currentColor">' + name_i + '</text>')
            gallery_svg = (
                '<div style="border:1px solid #93c5fd;border-radius:14px;padding:10px;background:rgba(59,130,246,.04)">'
                '<div style="font-weight:700;margin-bottom:8px">' + title_one + '</div>'
                '<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;text-align:center">'
                + ''.join('<div style="border:1px solid rgba(120,140,160,.3);border-radius:10px;padding:8px;min-height:92px"><svg viewBox="0 -28 120 82" width="100%" height="65">' + item + '</svg></div>' for item in gallery)
                + '</div><div style="text-align:center;margin-top:8px"><svg viewBox="0 0 220 58" width="75%"><rect x="20" y="8" width="90" height="34" rx="5" fill="#dc2626"/><rect x="110" y="8" width="90" height="34" rx="5" fill="#2563eb"/><text x="65" y="31" fill="white" font-size="17" font-weight="bold" text-anchor="middle">N</text><text x="155" y="31" fill="white" font-size="17" font-weight="bold" text-anchor="middle">S</text></svg><div style="font-weight:600">' + magnet_name + '</div></div></div>'
            )
            st.markdown(gallery_svg, unsafe_allow_html=True)
            st.caption("All six materials are shown above. Select one below to test it." if not is_pa else "ਉੱਪਰ ਸਾਰੇ ਛੇ ਪਦਾਰਥ ਦਿਖਾਏ ਹਨ। ਜਾਂਚ ਲਈ ਹੇਠਾਂ ਇੱਕ ਚੁਣੋ।")
            magnetic_options = {
                "en": ["Iron nail", "Steel paper clip", "Aluminium foil", "Copper wire", "Wood", "Plastic"],
                "pa": ["ਲੋਹੇ ਦੀ ਕਿੱਲ", "ਸਟੀਲ ਦੀ ਪੇਪਰ ਕਲਿੱਪ", "ਐਲੂਮੀਨੀਅਮ ਫੋਇਲ", "ਤਾਂਬੇ ਦੀ ਤਾਰ", "ਲੱਕੜ", "ਪਲਾਸਟਿਕ"]
            }
            material = st.selectbox(tr("material"), magnetic_options[st.session_state.language], key=f"magmat_{selected_class}_{exp_index}")
            selected = next((item for item in magnetic_items if material in item[:2]), magnetic_items[0])
            en_name, pa_name, shape, attracted = selected
            display_name = pa_name if is_pa else en_name
            st.markdown("#### " + title_two)
            if attracted:
                result_label = "ਖਿੱਚਿਆ ਜਾਂਦਾ ਹੈ — ਚੁੰਬਕ ਨਾਲ ਸੰਪਰਕ" if is_pa else "ATTRACTED — touches the magnet"
                result_color = "#16a34a"
                object_x = 166
                connection = '<path d="M145 88 H166" stroke="#16a34a" stroke-width="5"/>'
                result_text = ("ਇਹ ਪਦਾਰਥ ਚੁੰਬਕ ਵੱਲ ਖਿੱਚਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਉਸ ਨਾਲ ਲੱਗ ਜਾਂਦਾ ਹੈ।" if is_pa else "This material is attracted and moves into contact with the magnet.")
            else:
                result_label = "ਨਹੀਂ ਖਿੱਚਿਆ ਜਾਂਦਾ — ਦੂਰੀ ਰਹਿੰਦੀ ਹੈ" if is_pa else "NOT ATTRACTED — stays apart"
                result_color = "#dc2626"
                object_x = 245
                connection = '<path d="M145 88 H235" stroke="#64748b" stroke-width="3" stroke-dasharray="7 6"/>'
                result_text = ("ਆਮ ਕਲਾਸਰੂਮ ਚੁੰਬਕ ਇਸ ਪਦਾਰਥ ਨੂੰ ਨਹੀਂ ਖਿੱਚਦਾ; ਇਸ ਲਈ ਵਿਚਕਾਰ ਖਾਲੀ ਥਾਂ ਰਹਿੰਦੀ ਹੈ।" if is_pa else "An ordinary classroom magnet does not attract this material, so a gap remains.")
            if shape == "iron":
                object_drawing = '<path d="M0 0 L12 -7 L82 -7 L94 0 L82 7 L12 7 Z" fill="#94a3b8" stroke="#475569" stroke-width="2"/>'
            elif shape == "clip":
                object_drawing = '<path d="M5 0 C5 -20 35 -20 35 0 L35 8 C35 20 17 20 17 8 L17 -2 C17 -8 27 -8 27 -2" fill="none" stroke="#64748b" stroke-width="5"/>'
            elif shape == "foil":
                object_drawing = '<path d="M0 0 L20 -13 L43 -4 L65 -16 L88 -2 L77 15 L44 7 L23 16 Z" fill="#cbd5e1" stroke="#64748b" stroke-width="2"/>'
            elif shape == "copper":
                object_drawing = '<g fill="none" stroke="#b87333" stroke-width="5"><ellipse cx="25" cy="0" rx="22" ry="13"/><ellipse cx="39" cy="0" rx="22" ry="13"/></g>'
            elif shape == "wood":
                object_drawing = '<rect x="0" y="-10" width="80" height="20" rx="3" fill="#d6a56b" stroke="#9a6b37" stroke-width="2"/>'
            else:
                object_drawing = '<rect x="0" y="-14" width="62" height="28" rx="8" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>'
            result_svg = (
                '<div style="border:1px solid ' + result_color + ';border-radius:14px;padding:10px;background:rgba(128,128,128,.035)">'
                '<svg viewBox="0 0 380 155" width="100%" role="img" aria-label="Selected material and magnet attraction result">'
                '<rect x="15" y="62" width="65" height="48" rx="4" fill="#dc2626"/><rect x="80" y="62" width="65" height="48" rx="4" fill="#2563eb"/>'
                '<text x="47" y="91" font-size="18" fill="white" font-weight="bold" text-anchor="middle">N</text><text x="112" y="91" font-size="18" fill="white" font-weight="bold" text-anchor="middle">S</text>'
                + connection + '<g transform="translate(' + str(object_x) + ',88)">' + object_drawing + '</g>'
                '<text x="190" y="132" font-size="12" fill="currentColor" text-anchor="middle">' + display_name + '</text>'
                '</svg><div style="color:' + result_color + ';font-weight:700;text-align:center">' + result_label + '</div>'
                '<div style="text-align:center;margin-top:6px">' + result_text + '</div></div>'
            )
            st.markdown(result_svg, unsafe_allow_html=True)
            st.info("Iron and steel are attracted by an ordinary classroom magnet; aluminium, copper, wood and plastic are not." if not is_pa else "ਲੋਹਾ ਅਤੇ ਸਟੀਲ ਆਮ ਚੁੰਬਕ ਵੱਲ ਖਿੱਚੇ ਜਾਂਦੇ ਹਨ; ਐਲੂਮੀਨੀਅਮ, ਤਾਂਬਾ, ਲੱਕੜ ਅਤੇ ਪਲਾਸਟਿਕ ਨਹੀਂ ਖਿੱਚੇ ਜਾਂਦੇ।")
            st.write("💡 " + note)
        elif kind == "circuit" and selected_class == 6 and exp_index == 1:
            # Three fixed comparison circuits: correct connection, same-terminal
            # connection, and a wire broken in the middle.
            green = "#16a34a"
            amber = "#d97706"
            muted = "#94a3b8"

            def draw_bulb_circuit(number, y, heading, state, mode):
                wire = green if state else amber
                fill = "#fde047" if state else "#e2e8f0"
                glow = "filter: drop-shadow(0 0 9px #facc15);" if state else ""
                if mode == "correct":
                    wires = (
                        '<path d="M60 ' + str(y+18) + ' H285 L300 ' + str(y+42) + '"/>'
                        '<path d="M320 ' + str(y+100) + ' V' + str(y+112) + ' H60 V' + str(y+52) + '"/>'
                    )
                    extra = '<text x="210" y="' + str(y+18) + '" font-size="11" fill="currentColor" text-anchor="middle">Wire 1</text><text x="210" y="' + str(y+117) + '" font-size="11" fill="currentColor" text-anchor="middle">Wire 2</text>'
                elif mode == "same_terminal":
                    wires = (
                        '<path d="M60 ' + str(y+18) + ' H285 L300 ' + str(y+42) + '"/>'
                        '<path d="M320 ' + str(y+100) + ' V' + str(y+112) + ' H285 L300 ' + str(y+62) + '"/>'
                    )
                    extra = '<text x="210" y="' + str(y+18) + '" font-size="11" fill="currentColor" text-anchor="middle">Both wires meet the same metal shell</text>'
                else:
                    wires = (
                        '<path d="M60 ' + str(y+18) + ' H175"/>'
                        '<path d="M205 ' + str(y+18) + ' H285 L300 ' + str(y+42) + '"/>'
                        '<path d="M320 ' + str(y+100) + ' V' + str(y+112) + ' H60 V' + str(y+52) + '"/>'
                    )
                    extra = '<path d="M178 ' + str(y+18) + ' l8 14 M194 ' + str(y+18) + ' l-8 14" stroke="' + amber + '" stroke-width="3"/><text x="190" y="' + str(y+45) + '" font-size="10" fill="currentColor" text-anchor="middle">Gap</text>'
                battery = (
                    '<g stroke="#334155" stroke-width="3"><line x1="42" y1="' + str(y+18) + '" x2="58" y2="' + str(y+18) + '"/><line x1="36" y1="' + str(y+35) + '" x2="64" y2="' + str(y+35) + '"/><line x1="42" y1="' + str(y+52) + '" x2="58" y2="' + str(y+52) + '"/></g>'
                    '<text x="50" y="' + str(y+70) + '" font-size="10" fill="currentColor" text-anchor="middle">Cell</text>'
                )
                bulb = (
                    '<g stroke="#334155" stroke-width="2.5"><circle cx="320" cy="' + str(y+60) + '" r="21" fill="' + fill + '" style="' + glow + '"/><path d="M308 ' + str(y+48) + ' l8 8 -5 6 9 6 8 -10" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="M306 ' + str(y+81) + ' v7 h28 v-7 M310 ' + str(y+88) + ' v6 h20 v-6" fill="' + muted + '"/><circle cx="320" cy="' + str(y+100) + '" r="4" fill="#475569"/></g>'
                )
                label = "BULB ON" if state else "BULB OFF"
                label_pa = "ਬਲਬ ਜਗਦਾ ਹੈ" if state else "ਬਲਬ ਨਹੀਂ ਜਗਦਾ"
                return (
                    '<g><text x="10" y="' + str(y-3) + '" font-size="13" font-weight="bold" fill="currentColor">' + number + '. ' + heading + '</text>'
                    '<g fill="none" stroke="' + wire + '" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">' + wires + '</g>'
                    + battery + bulb + extra
                    + '<text x="375" y="' + str(y+58) + '" font-size="11" font-weight="bold" fill="' + (green if state else amber) + '" text-anchor="middle">' + label + '</text>'
                    + '<text x="375" y="' + str(y+73) + '" font-size="10" fill="currentColor" text-anchor="middle">' + label_pa + '</text></g>'
                )

            is_pa = st.session_state.language != "en"
            headings = (
                ["Correct connections", "Both wires on one terminal", "Wire broken in the middle"]
                if not is_pa else
                ["ਸਹੀ ਜੋੜ", "ਦੋਵੇਂ ਤਾਰਾਂ ਇੱਕੋ ਟਰਮੀਨਲ ਨਾਲ", "ਵਿਚਕਾਰੋਂ ਟੁੱਟੀ ਤਾਰ"]
            )
            circuit_rows = (
                draw_bulb_circuit("1", 42, headings[0], True, "correct") +
                draw_bulb_circuit("2", 190, headings[1], False, "same_terminal") +
                draw_bulb_circuit("3", 338, headings[2], False, "broken")
            )
            bulb_svg = (
                '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">'
                '<svg viewBox="0 0 440 475" width="100%" role="img" aria-label="Three bulb circuits: correct connection glows; two wires on one terminal and a broken wire do not glow">'
                + circuit_rows +
                '</svg></div>'
            )
            st.markdown("#### " + tr("visual_circuit"), unsafe_allow_html=True)
            st.markdown(bulb_svg, unsafe_allow_html=True)
            st.info(
                "Circuit 1: each wire connects to a different bulb terminal, making a complete path, so the bulb glows. Circuit 2: both wires touch the same metal terminal; the other terminal is not connected, so the bulb stays off. Circuit 3: the wire has a gap, so the path is broken and the bulb stays off."
                if not is_pa else
                "ਸਰਕਟ 1: ਦੋਵੇਂ ਤਾਰਾਂ ਬਲਬ ਦੇ ਵੱਖ-ਵੱਖ ਟਰਮੀਨਲਾਂ ਨਾਲ ਜੁੜਦੀਆਂ ਹਨ, ਇਸ ਲਈ ਪੂਰਾ ਰਸਤਾ ਬਣਦਾ ਹੈ ਅਤੇ ਬਲਬ ਜਗਦਾ ਹੈ। ਸਰਕਟ 2: ਦੋਵੇਂ ਤਾਰਾਂ ਇੱਕੋ ਧਾਤੂ ਟਰਮੀਨਲ ਨਾਲ ਜੁੜੀਆਂ ਹਨ; ਦੂਜਾ ਟਰਮੀਨਲ ਨਹੀਂ ਜੁੜਿਆ, ਇਸ ਲਈ ਬਲਬ ਨਹੀਂ ਜਗਦਾ। ਸਰਕਟ 3: ਤਾਰ ਵਿਚਕਾਰੋਂ ਟੁੱਟੀ ਹੈ, ਇਸ ਲਈ ਰਸਤਾ ਅਧੂਰਾ ਹੈ ਅਤੇ ਬਲਬ ਨਹੀਂ ਜਗਦਾ।"
            )
            st.write("💡 " + note)
        elif kind == "circuit" and selected_class == 6 and exp_index == 3:
            # Class 6 Experiment 4: interactive open/closed switch comparison.
            bulb_on = closed
            wire_color = "#16a34a" if closed else "#d97706"
            bulb_fill = "#fde047" if bulb_on else "#e2e8f0"
            bulb_glow = "filter: drop-shadow(0 0 10px #facc15);" if bulb_on else ""
            switch_arm = (
                '<line x1="158" y1="50" x2="216" y2="50" stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round"/>'
                if closed else
                '<line x1="158" y1="50" x2="205" y2="29" stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round"/>'
            )
            circuit_svg = (
                '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">'
                '<svg viewBox="0 0 420 230" width="100%" role="img" aria-label="Interactive open and closed circuit with a cell, switch and bulb">'
                '<g fill="none" stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M70 50 H158"/>' + switch_arm +
                '<path d="M216 50 H320 V77"/><path d="M320 123 V165 H70 V110"/>'
                '<path d="M70 50 V77 M70 103 V110"/>'
                '</g>'
                '<g stroke="#334155" stroke-width="3"><line x1="50" y1="80" x2="90" y2="80"/><line x1="58" y1="100" x2="82" y2="100"/></g>'
                '<g stroke="#334155" stroke-width="3" fill="none"><circle cx="320" cy="100" r="23" fill="' + bulb_fill + '" style="' + bulb_glow + '"/><path d="M307 87 L315 95 L309 102 L319 108 L326 99 L333 108" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M309 124 V132 H331 V124 M312 132 V138 H328 V132" stroke="#64748b" stroke-width="2.5"/></g>'
                '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="70" y="129">' + tr("battery") + '</text><text x="187" y="17">' + tr("switch_label") + '</text><text x="320" y="194">' + tr("bulb") + '</text></g>'
                '<g fill="#334155"><circle cx="158" cy="50" r="4"/><circle cx="216" cy="50" r="4"/></g>'
                '<g fill="currentColor" font-size="13" font-weight="bold" text-anchor="middle"><text x="210" y="218">' + (("CLOSED: complete path" if closed else "OPEN: broken path") if st.session_state.language == "en" else ("ਬੰਦ: ਪੂਰਾ ਰਸਤਾ" if closed else "ਖੁੱਲ੍ਹਾ: ਟੁੱਟਿਆ ਰਸਤਾ")) + '</text></g>'
                '</svg></div>'
            )
            st.markdown("#### " + tr("visual_circuit"), unsafe_allow_html=True)
            st.markdown(circuit_svg, unsafe_allow_html=True)
            st.metric(tr("circuit"), tr("bulb_on") if bulb_on else tr("bulb_off"))
            st.info(
                "Close the switch to complete the conducting path: current can flow and the bulb glows. Open the switch to create a gap: the path is broken and the bulb goes off."
                if st.session_state.language == "en" else
                "ਸਰਕਟ ਦਾ ਰਸਤਾ ਪੂਰਾ ਕਰਨ ਲਈ ਸਵਿੱਚ ਬੰਦ ਕਰੋ: ਕਰੰਟ ਲੰਘ ਸਕਦਾ ਹੈ ਅਤੇ ਬਲਬ ਜਗਦਾ ਹੈ। ਸਵਿੱਚ ਖੋਲ੍ਹਣ ਨਾਲ ਰਸਤੇ ਵਿੱਚ ਖਾਲੀ ਥਾਂ ਬਣਦੀ ਹੈ: ਸਰਕਟ ਟੁੱਟ ਜਾਂਦਾ ਹੈ ਅਤੇ ਬਲਬ ਬੁੱਝ ਜਾਂਦਾ ਹੈ।"
            )
            st.write("💡 " + note)
        elif kind == "circuit" and selected_class == 7 and exp_index == 0:
            # Class 7 Experiment 1: component gallery, selection dropdown, then
            # a large symbol/function result and a complete sample circuit.
            is_pa = st.session_state.language != "en"
            component_data = [
                ("Cell", "ਸੈੱਲ", "cell", "A cell supplies electrical energy to the circuit.", "ਸੈੱਲ ਸਰਕਟ ਨੂੰ ਬਿਜਲੀ ਊਰਜਾ ਦਿੰਦਾ ਹੈ।"),
                ("Bulb", "ਬਲਬ", "bulb", "A bulb converts electrical energy into light (and heat).", "ਬਲਬ ਬਿਜਲੀ ਊਰਜਾ ਨੂੰ ਰੌਸ਼ਨੀ (ਅਤੇ ਤਾਪ) ਵਿੱਚ ਬਦਲਦਾ ਹੈ।"),
                ("Open switch", "ਖੁੱਲ੍ਹਾ ਸਵਿੱਚ", "open", "An open switch breaks the circuit, so current cannot flow.", "ਖੁੱਲ੍ਹਾ ਸਵਿੱਚ ਸਰਕਟ ਤੋੜਦਾ ਹੈ, ਇਸ ਲਈ ਕਰੰਟ ਨਹੀਂ ਵਹਿੰਦਾ।"),
                ("Closed switch", "ਬੰਦ ਸਵਿੱਚ", "closed", "A closed switch completes the circuit path.", "ਬੰਦ ਸਵਿੱਚ ਸਰਕਟ ਦਾ ਰਸਤਾ ਪੂਰਾ ਕਰਦਾ ਹੈ।"),
                ("Connecting wire", "ਜੋੜਨ ਵਾਲੀ ਤਾਰ", "wire", "A connecting wire joins components and provides a conducting path.", "ਜੋੜਨ ਵਾਲੀ ਤਾਰ ਭਾਗਾਂ ਨੂੰ ਜੋੜਦੀ ਅਤੇ ਚਾਲਕ ਰਸਤਾ ਦਿੰਦੀ ਹੈ।"),
            ]
            def component_symbol(shape):
                if shape == "cell":
                    return '<path d="M12 40 H55 M55 20 V60 M72 30 V50 M72 40 H112" stroke="#334155" stroke-width="4" fill="none"/>'
                if shape == "bulb":
                    return '<path d="M8 40 H35 M85 40 H112" stroke="#334155" stroke-width="4"/><circle cx="60" cy="40" r="24" fill="#fef3c7" stroke="#334155" stroke-width="3"/><path d="M46 26 L74 54 M74 26 L46 54 M50 65 H70 M52 71 H68" stroke="#334155" stroke-width="3" fill="none"/>'
                if shape == "open":
                    return '<path d="M8 45 H42 M78 45 H112 M42 45 L72 20" stroke="#334155" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="42" cy="45" r="4" fill="#334155"/><circle cx="78" cy="45" r="4" fill="#334155"/>'
                if shape == "closed":
                    return '<path d="M8 45 H42 M42 45 H78 M78 45 H112" stroke="#334155" stroke-width="4" fill="none" stroke-linecap="round"/><circle cx="42" cy="45" r="4" fill="#334155"/><circle cx="78" cy="45" r="4" fill="#334155"/>'
                return '<path d="M8 45 H112" stroke="#16a34a" stroke-width="5" fill="none" stroke-linecap="round"/>'
            gallery_title = "1. Component gallery — ਸਰਕਟ ਦੇ ਭਾਗ" if is_pa else "1. Component gallery — circuit components"
            st.markdown("#### " + gallery_title)
            gallery_cards = []
            for en, pa, shape, en_desc, pa_desc in component_data:
                label = pa if is_pa else en
                gallery_cards.append('<div style="border:1px solid rgba(120,140,160,.35);border-radius:12px;padding:8px;text-align:center;min-width:0"><svg viewBox="0 0 120 96" width="100%" role="img" aria-label="' + label + '">' + component_symbol(shape) + '</svg><div style="font-weight:600;font-size:13px">' + label + '</div></div>')
            st.markdown('<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(125px,1fr));gap:8px">' + ''.join(gallery_cards) + '</div>', unsafe_allow_html=True)
            st.caption("Study the symbols, then choose one below." if not is_pa else "ਚਿੰਨ੍ਹਾਂ ਨੂੰ ਵੇਖੋ ਅਤੇ ਫਿਰ ਹੇਠਾਂ ਇੱਕ ਚੁਣੋ।")
            choices = [x[1] for x in component_data] if is_pa else [x[0] for x in component_data]
            selected_component = st.selectbox("2. ਭਾਗ ਚੁਣੋ / Select a component", choices, key="class7_exp1_component")
            chosen = next(x for x in component_data if selected_component in x[:2])
            en, pa, shape, en_desc, pa_desc = chosen
            selected_label = pa if is_pa else en
            desc = pa_desc if is_pa else en_desc
            symbol_title = "3. ਚਿੰਨ੍ਹ ਅਤੇ ਕੰਮ" if is_pa else "3. Symbol and function"
            st.markdown("#### " + symbol_title)
            symbol_svg = '<div style="border:1px solid #60a5fa;border-radius:14px;padding:12px;background:rgba(59,130,246,.05);text-align:center"><div style="font-weight:700;font-size:18px;margin-bottom:8px">' + selected_label + '</div><svg viewBox="0 0 120 100" width="220" style="max-width:100%" role="img" aria-label="Selected circuit symbol">' + component_symbol(shape) + '</svg><div style="font-size:15px;margin-top:8px">' + desc + '</div></div>'
            st.markdown(symbol_svg, unsafe_allow_html=True)
            st.markdown("#### " + ("ਸਧਾਰਨ ਸਰਕਟ ਚਿੱਤਰ" if is_pa else "Example circuit diagram"))
            switch_caption = "ਸਵਿੱਚ ਬੰਦ ਹੈ — ਸਰਕਟ ਪੂਰਾ" if is_pa else "Switch closed — complete circuit"
            circuit_html = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:14px;padding:8px"><svg viewBox="0 0 360 180" width="100%" role="img" aria-label="Circuit diagram with cell, closed switch and bulb"><g fill="none" stroke="#16a34a" stroke-width="4" stroke-linecap="round"><path d="M55 45 H120 M160 45 H275 V70 M275 112 V145 H55 V105 M55 45 V70"/><path d="M120 45 H160"/></g><g stroke="#334155" stroke-width="3"><path d="M42 72 V103 M55 80 V95"/><circle cx="275" cy="91" r="21" fill="#fef08a"/><path d="M264 80 L286 102 M286 80 L264 102" fill="none"/><path d="M265 114 V122 H285 V114" fill="none"/></g><g fill="currentColor" font-size="12" text-anchor="middle"><text x="49" y="128">{'ਸੈੱਲ' if is_pa else 'Cell'}</text><text x="140" y="28">{'ਬੰਦ ਸਵਿੱਚ' if is_pa else 'Closed switch'}</text><text x="275" y="165">{'ਬਲਬ' if is_pa else 'Bulb'}</text></g></svg><div style="text-align:center;color:#16a34a;font-weight:700">{switch_caption}</div></div>"""
            st.markdown(circuit_html, unsafe_allow_html=True)
            st.info("Real circuit diagrams use standard symbols instead of pictures of components. This virtual diagram is for learning; never connect components to household mains electricity." if not is_pa else "ਅਸਲ ਸਰਕਟ ਚਿੱਤਰਾਂ ਵਿੱਚ ਭਾਗਾਂ ਦੀਆਂ ਤਸਵੀਰਾਂ ਦੀ ਥਾਂ ਮਿਆਰੀ ਚਿੰਨ੍ਹ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਇਹ ਵਰਚੁਅਲ ਚਿੱਤਰ ਸਿੱਖਣ ਲਈ ਹੈ; ਘਰੇਲੂ ਮੇਨ ਬਿਜਲੀ ਨਾਲ ਭਾਗ ਨਾ ਜੋੜੋ।")

            # Interactive symbol-recognition challenge for Class 7.
            st.markdown("#### " + ("4. ਚਿੰਨ੍ਹ ਪਛਾਣੋ — ਗਿਆਨ ਦੀ ਜਾਂਚ" if is_pa else "4. Symbol challenge — test your understanding"))
            quiz_items = [
                ("Cell", "ਸੈੱਲ", "cell"),
                ("Bulb", "ਬਲਬ", "bulb"),
                ("Open switch", "ਖੁੱਲ੍ਹਾ ਸਵਿੱਚ", "open"),
                ("Closed switch", "ਬੰਦ ਸਵਿੱਚ", "closed"),
                ("Connecting wire", "ਜੋੜਨ ਵਾਲੀ ਤਾਰ", "wire"),
            ]
            if "class7_exp1_quiz_index" not in st.session_state:
                st.session_state["class7_exp1_quiz_index"] = 0
            quiz_index = st.session_state["class7_exp1_quiz_index"] % len(quiz_items)
            quiz_target = quiz_items[quiz_index]
            st.caption("Look at the symbol first, then choose your answer below." if not is_pa else "ਪਹਿਲਾਂ ਚਿੰਨ੍ਹ ਵੇਖੋ, ਫਿਰ ਹੇਠਾਂ ਜਵਾਬ ਚੁਣੋ।")
            st.markdown(
                '<div style="border:1px solid #60a5fa;border-radius:12px;padding:16px;text-align:center;background:rgba(59,130,246,.04)"><svg viewBox="0 0 120 100" width="190" style="max-width:100%" role="img" aria-label="Circuit symbol to identify">'
                + component_symbol(quiz_target[2]) + '</svg></div>',
                unsafe_allow_html=True,
            )
            answer_options = (["ਜਵਾਬ ਚੁਣੋ…"] + [x[1] for x in quiz_items]) if is_pa else (["Choose an answer…"] + [x[0] for x in quiz_items])
            quiz_answer = st.selectbox(
                "ਤੁਹਾਡਾ ਜਵਾਬ / Your answer",
                answer_options,
                index=0,
                key=f"class7_exp1_quiz_answer_{quiz_index}",
            )
            correct_answer = quiz_target[1] if is_pa else quiz_target[0]
            placeholder = "ਜਵਾਬ ਚੁਣੋ…" if is_pa else "Choose an answer…"
            if quiz_answer != placeholder:
                if quiz_answer == correct_answer:
                    st.success("ਬਿਲਕੁਲ ਸਹੀ! ਤੁਸੀਂ ਚਿੰਨ੍ਹ ਪਛਾਣ ਲਿਆ।" if is_pa else "Correct! You identified the circuit symbol.")
                    if st.button("ਅਗਲਾ ਚਿੰਨ੍ਹ / Next symbol", key=f"class7_exp1_next_{quiz_index}"):
                        st.session_state["class7_exp1_quiz_index"] = (quiz_index + 1) % len(quiz_items)
                        st.rerun()
                else:
                    st.warning("ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।" if is_pa else "Not quite. Try again.")
            st.write("💡 " + note)
        elif kind == "circuit":
            # Fixed, illustrative low-voltage cell: no numerical electrical controls
            # are exposed for Classes 6–9.
            bulb_on = closed
            wire_color = "#16a34a" if closed else "#d97706"
            bulb_fill = "#fde047" if bulb_on else "#e2e8f0"
            bulb_glow = "filter: drop-shadow(0 0 10px #facc15);" if bulb_on else ""
            switch_arm = '<line x1="158" y1="54" x2="216" y2="54" stroke="#16a34a" stroke-width="5" stroke-linecap="round"/>' if closed else '<line x1="158" y1="54" x2="210" y2="32" stroke="#d97706" stroke-width="5" stroke-linecap="round"/>'
            circuit_svg = (
                '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">'
                '<svg viewBox="0 0 420 220" width="100%" role="img" aria-label="Simple circuit with a clearly shown switch, cell, connecting wires and filament bulb">'
                '<g fill="none" stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M70 54 H158"/>' + switch_arm +
                '<path d="M216 54 H320 V78"/><path d="M320 122 V166 H70 V116"/><path d="M70 54 V78"/>'
                '</g>'
                '<g stroke="#334155" stroke-width="3" fill="none"><line x1="51" y1="80" x2="89" y2="80"/><line x1="58" y1="98" x2="82" y2="98"/></g>'
                '<g stroke="#334155" stroke-width="3" fill="none"><circle cx="320" cy="100" r="23" fill="' + bulb_fill + '" style="' + bulb_glow + '"/><path d="M307 87 L315 95 L309 102 L319 108 L326 99 L333 108" stroke="#334155" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M309 124 V132 H331 V124 M312 132 V138 H328 V132" stroke="#64748b" stroke-width="2.5"/></g>'
                '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="70" y="137">' + tr("battery") + '</text><text x="187" y="20">' + tr("switch_label") + '</text><text x="320" y="194">' + tr("bulb") + '</text></g>'
                '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="205" y="205">' + (tr("complete_path") if closed else tr("broken_path")) + '</text></g>'
                '<g fill="#334155"><circle cx="158" cy="54" r="4"/><circle cx="216" cy="54" r="4"/></g>'
                '</svg></div>'
            )
            st.markdown("#### " + tr("visual_circuit"), unsafe_allow_html=True)
            st.markdown(circuit_svg, unsafe_allow_html=True)
            st.metric(tr("circuit"), tr("bulb_on") if bulb_on else tr("bulb_off"))
            st.write("💡 " + note)
        elif heating_experiment:
            is_pa = st.session_state.language != "en"
            levels = (["ਘੱਟ", "ਦਰਮਿਆਨਾ", "ਵੱਧ"] if is_pa else ["Low", "Medium", "High"])
            current_level_index = levels.index(heat_current_level)
            resistance_level_index = levels.index(heat_resistance_level)
            relative_heat_score = (current_level_index + 1) ** 2 * (resistance_level_index + 1)
            heat_band = "Low" if relative_heat_score <= 4 else ("Moderate" if relative_heat_score <= 12 else "High")
            heat_band_pa = {"Low": "ਘੱਟ", "Moderate": "ਦਰਮਿਆਨਾ", "High": "ਵੱਧ"}[heat_band]
            heat_label = heat_band_pa if is_pa else heat_band
            heat_color = "#38bdf8" if heat_band == "Low" else ("#f59e0b" if heat_band == "Moderate" else "#ef4444")
            glow = "0 0 18px " + heat_color if closed else "none"
            heat_title = "ਤਾਪੀ ਪ੍ਰਭਾਵ ਦਾ ਵਰਚੁਅਲ ਮਾਡਲ" if is_pa else "Virtual heating-effect model"
            resistor_fill = heat_color if closed else "#cbd5e1"
            heat_opacity = "1" if closed else "0.18"
            resistor_label = "ਰੋਧਕ" if is_pa else "Resistor"
            switch_state_caption = (("ਸਵਿੱਚ ਬੰਦ: ਤਾਪ ਪੈਦਾ ਹੁੰਦਾ ਹੈ" if is_pa else "Switch ON: heat is produced") if closed else ("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ: ਕਰੰਟ ਨਹੀਂ ਵਹਿੰਦਾ" if is_pa else "Switch OFF: no current flows"))
            st.markdown("#### " + heat_title)
            heat_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;text-align:center">
<svg viewBox="0 0 440 220" width="100%" role="img" aria-label="Virtual resistor heating as current and resistance change">
<path d="M30 90 H105 M335 90 H410" stroke="#64748b" stroke-width="6" stroke-linecap="round"/>
<rect x="105" y="62" width="230" height="56" rx="12" fill="{resistor_fill}" stroke="#334155" stroke-width="3" style="filter:drop-shadow({glow if closed else 'none'})"/>
<path d="M125 90 l18 -15 l18 30 l18 -30 l18 30 l18 -30 l18 30 l18 -30 l18 15" fill="none" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"/>
<g fill="{heat_color}" stroke="{heat_color}" stroke-width="3" stroke-linecap="round" opacity="{heat_opacity}"><path d="M155 48 Q145 35 155 22" fill="none"/><path d="M220 45 Q210 32 220 18" fill="none"/><path d="M285 48 Q275 35 285 22" fill="none"/></g>
<g fill="currentColor" font-size="14" text-anchor="middle"><text x="220" y="151">{resistor_label}</text><text x="220" y="184">{switch_state_caption}</text></g>
</svg></div>"""
            st.markdown(heat_svg, unsafe_allow_html=True)
            st.metric("ਤਾਪ ਦਾ ਪੱਧਰ" if is_pa else "Relative heating level", heat_label if closed else ("ਨਹੀਂ" if is_pa else "None — switch open"))
            st.info(
                ("ਇਸ ਗੁਣਾਤਮਕ ਮਾਡਲ ਵਿੱਚ ਕਰੰਟ ਜਾਂ ਰੋਧ ਦਾ ਪੱਧਰ ਵਧਾਉਣ ਨਾਲ ਰੋਧਕ ਵਿੱਚ ਤਾਪ ਵਧਦਾ ਦਿਖਾਇਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਅਸਲੀ ਮਾਪ ਨਹੀਂ ਹੈ।" if is_pa else
                 "In this qualitative model, increasing the current or resistance level shows greater heating in the resistor. This is illustrative, not a real measurement.")
            )
            st.write("💡 " + note)
        elif kind == "ohms" and selected_class == 9 and exp_index == 1:
            # Class 9 Experiment 2: qualitative Ohm's law exploration with no numerical values.
            is_pa_ohms = st.session_state.language != "en"
            relative_current_index = ["Low", "Medium", "High"].index(class9_voltage_level) - ["Low", "Medium", "High"].index(class9_resistance_level) + 1
            current_band = "Low" if relative_current_index <= 0 else ("High" if relative_current_index >= 2 else "Medium")
            current_colors = {"Low": "#64748b", "Medium": "#d97706", "High": "#16a34a"}
            current_color = current_colors[current_band] if closed else "#94a3b8"
            bulb_fill = "#e2e8f0" if not closed else {"Low": "#fde68a", "Medium": "#facc15", "High": "#fbbf24"}[current_band]
            bulb_glow = "filter:drop-shadow(0 0 12px #facc15);" if closed and current_band == "High" else ""
            wire_color = "#16a34a" if closed else "#94a3b8"
            if not closed:
                qualitative_result = ("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੈ — ਕਰੰਟ ਨਹੀਂ ਵਹਿੰਦਾ।" if is_pa_ohms else "Switch open — no current flows.")
            elif class9_voltage_level == "High" and class9_resistance_level == "Low":
                qualitative_result = ("ਵੋਲਟੇਜ ਵੱਧ ਅਤੇ ਰੋਧ ਘੱਟ ਹੋਣ ਕਰਕੇ ਕਰੰਟ ਵੱਧ ਹੁੰਦਾ ਹੈ।" if is_pa_ohms else "Higher voltage and lower resistance give greater current.")
            elif class9_voltage_level == "Low" and class9_resistance_level == "High":
                qualitative_result = ("ਵੋਲਟੇਜ ਘੱਟ ਅਤੇ ਰੋਧ ਵੱਧ ਹੋਣ ਕਰਕੇ ਕਰੰਟ ਘੱਟ ਹੁੰਦਾ ਹੈ।" if is_pa_ohms else "Lower voltage and higher resistance give lower current.")
            elif class9_voltage_level == class9_resistance_level:
                qualitative_result = ("ਇਸ ਗੁਣਾਤਮਕ ਮਾਡਲ ਵਿੱਚ ਵੋਲਟੇਜ ਅਤੇ ਰੋਧ ਦੇ ਪੱਧਰ ਸੰਤੁਲਿਤ ਹਨ।" if is_pa_ohms else "In this qualitative model, voltage and resistance levels are balanced.")
            elif class9_voltage_level == "High" or class9_resistance_level == "Low":
                qualitative_result = ("ਕਰੰਟ ਵਧਣ ਦੀ ਪ੍ਰਵਿਰਤੀ ਦਿਖਾਈ ਗਈ ਹੈ।" if is_pa_ohms else "The model shows a tendency toward greater current.")
            else:
                qualitative_result = ("ਕਰੰਟ ਘਟਣ ਦੀ ਪ੍ਰਵਿਰਤੀ ਦਿਖਾਈ ਗਈ ਹੈ।" if is_pa_ohms else "The model shows a tendency toward lower current.")
            if closed:
                current_band_label = {"Low": "ਘੱਟ" if is_pa_ohms else "LOW", "Medium": "ਦਰਮਿਆਨਾ" if is_pa_ohms else "MEDIUM", "High": "ਵੱਧ" if is_pa_ohms else "HIGH"}[current_band]
                qualitative_current_label = ("ਕਰੰਟ ਦਾ ਗੁਣਾਤਮਕ ਪੱਧਰ: " if is_pa_ohms else "QUALITATIVE CURRENT: ") + current_band_label
            else:
                qualitative_current_label = "ਕੋਈ ਕਰੰਟ ਨਹੀਂ" if is_pa_ohms else "NO CURRENT"
            ohms_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 440 260" width="100%" role="img" aria-label="Qualitative Ohm's law circuit with cell, resistor, switch, bulb and current flow arrows">
  <g fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M70 58 H150"/><path d="M235 58 H340 V103"/><path d="M340 153 V210 H70 V133"/><path d="M70 58 V103"/>
  </g>
  <g stroke="#334155" stroke-width="3"><line x1="50" y1="103" x2="90" y2="103"/><line x1="58" y1="123" x2="82" y2="123"/></g>
  <text x="70" y="153" fill="currentColor" font-size="12" text-anchor="middle">{"ਸੈੱਲ" if is_pa_ohms else "CELL"}</text>
  <rect x="150" y="43" width="85" height="30" rx="7" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <path d="M160 58 l8 -9 l8 18 l8 -18 l8 18 l8 -18 l8 18 l8 -9" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
  <text x="192" y="30" fill="currentColor" font-size="12" text-anchor="middle">{"ਰੋਧਕ" if is_pa_ohms else "RESISTOR"}</text>
  <circle cx="340" cy="128" r="25" fill="{bulb_fill}" stroke="#475569" stroke-width="3" style="{bulb_glow}"/>
  <path d="M328 120 l8 8 l-6 8 l12 4 l7 -10" fill="none" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
  <path d="M330 155 V162 H350 V155" fill="none" stroke="#475569" stroke-width="4"/>
  <text x="340" y="184" fill="currentColor" font-size="12" text-anchor="middle">{"ਬਲਬ" if is_pa_ohms else "BULB"}</text>
  <g fill="{current_color}"><path d="M110 58 l-10 -6 v12 Z"/><path d="M292 58 l-10 -6 v12 Z"/><path d="M292 210 l-10 -6 v12 Z"/></g>
  <rect x="100" y="222" width="240" height="27" rx="8" fill="#e2e8f0" stroke="#94a3b8"/>
   <text x="220" y="240" fill="#334155" font-size="12" font-weight="700" text-anchor="middle">{qualitative_current_label}</text>
</svg></div>"""
            st.markdown("#### " + ("ਵੋਲਟੇਜ, ਕਰੰਟ ਅਤੇ ਰੋਧ ਦਾ ਮਾਡਲ" if is_pa_ohms else "Voltage, current and resistance model"))
            st.markdown(ohms_svg, unsafe_allow_html=True)
            # Additional qualitative visual: compare selected levels without exposing numbers.
            level_width = {"Low": 70, "Medium": 135, "High": 200}
            voltage_width = level_width[class9_voltage_level]
            resistance_width = level_width[class9_resistance_level]
            voltage_caption = {"Low": "LOW" if not is_pa_ohms else "ਘੱਟ", "Medium": "MEDIUM" if not is_pa_ohms else "ਦਰਮਿਆਨਾ", "High": "HIGH" if not is_pa_ohms else "ਵੱਧ"}[class9_voltage_level]
            resistance_caption = {"Low": "LOW" if not is_pa_ohms else "ਘੱਟ", "Medium": "MEDIUM" if not is_pa_ohms else "ਦਰਮਿਆਨਾ", "High": "HIGH" if not is_pa_ohms else "ਵੱਧ"}[class9_resistance_level]
            current_caption = ({"Low": "LOW" if not is_pa_ohms else "ਘੱਟ", "Medium": "MEDIUM" if not is_pa_ohms else "ਦਰਮਿਆਨਾ", "High": "HIGH" if not is_pa_ohms else "ਵੱਧ"}[current_band] if closed else ("OFF" if not is_pa_ohms else "ਬੰਦ"))
            comparison_title = "COMPARE THE LEVELS" if not is_pa_ohms else "ਪੱਧਰਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ"
            voltage_title = "VOLTAGE" if not is_pa_ohms else "ਵੋਲਟੇਜ"
            resistance_title = "RESISTANCE" if not is_pa_ohms else "ਰੋਧ"
            current_title = "CURRENT" if not is_pa_ohms else "ਕਰੰਟ"
            comparison_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;margin-top:10px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 440 205" width="100%" role="img" aria-label="Qualitative comparison bars for voltage, resistance and current, with no numerical readings">
<text x="220" y="22" fill="currentColor" font-size="14" font-weight="700" text-anchor="middle">{comparison_title}</text>
<text x="18" y="52" fill="currentColor" font-size="12" font-weight="700">{voltage_title}</text><rect x="130" y="37" width="220" height="20" rx="8" fill="#e2e8f0"/><rect x="130" y="37" width="{voltage_width}" height="20" rx="8" fill="#0ea5e9"/><text x="370" y="52" fill="#0369a1" font-size="12" font-weight="700">{voltage_caption}</text>
<text x="18" y="93" fill="currentColor" font-size="12" font-weight="700">{resistance_title}</text><rect x="130" y="78" width="220" height="20" rx="8" fill="#e2e8f0"/><rect x="130" y="78" width="{resistance_width}" height="20" rx="8" fill="#f59e0b"/><text x="370" y="93" fill="#b45309" font-size="12" font-weight="700">{resistance_caption}</text>
<text x="18" y="134" fill="currentColor" font-size="12" font-weight="700">{current_title}</text><rect x="130" y="119" width="220" height="20" rx="8" fill="#e2e8f0"/><rect x="130" y="119" width="{level_width[current_band] if closed else 0}" height="20" rx="8" fill="{current_color}"/><text x="370" y="134" fill="currentColor" font-size="12" font-weight="700">{current_caption}</text>
<text x="220" y="174" fill="currentColor" font-size="11" text-anchor="middle">{"ਸੰਕੇਤਕ ਪੱਧਰ — ਅਸਲੀ ਮਾਪ ਨਹੀਂ" if is_pa_ohms else "Illustrative levels — not measured values"}</text>
<text x="220" y="192" fill="currentColor" font-size="11" text-anchor="middle">{"ਵੱਧ ਵੋਲਟੇਜ ਕਰੰਟ ਵਧਾਉਂਦਾ; ਵੱਧ ਰੋਧ ਕਰੰਟ ਘਟਾਉਂਦਾ" if is_pa_ohms else "Higher voltage tends to raise current; higher resistance tends to lower it"}</text>
</svg></div>"""
            st.markdown(comparison_svg, unsafe_allow_html=True)
            if closed:
                st.success(qualitative_result)
            else:
                st.info(qualitative_result)
            st.write("💡 " + note)
            st.caption("Qualitative visual only — no numerical values, units, calculated readings or graph." if not is_pa_ohms else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮੁੱਲ, ਇਕਾਈਆਂ, ਗਣਨਾ ਜਾਂ ਗ੍ਰਾਫ ਨਹੀਂ।")
        elif kind == "series_parallel" and selected_class == 9 and exp_index == 2:
            # Class 9 Experiment 3: visual, qualitative comparison of series and parallel circuits.
            is_pa_series = st.session_state.language != "en"
            series_switch = st.checkbox(
                "ਲੜੀਵਾਰ ਸਰਕਟ ਦਾ ਮੁੱਖ ਸਵਿੱਚ" if is_pa_series else "Series circuit main switch",
                value=True, key="c9_exp3_series_switch"
            )
            st.markdown("**" + ("ਸਮਾਂਤਰ ਸ਼ਾਖਾਵਾਂ ਦੇ ਵੱਖਰੇ ਸਵਿੱਚ" if is_pa_series else "Independent parallel-branch switches") + "**")
            pcol1, pcol2 = st.columns(2)
            with pcol1:
                parallel_switch_1 = st.checkbox(
                    "ਸ਼ਾਖਾ 1" if is_pa_series else "Branch 1",
                    value=True, key="c9_exp3_parallel_switch_1"
                )
            with pcol2:
                parallel_switch_2 = st.checkbox(
                    "ਸ਼ਾਖਾ 2" if is_pa_series else "Branch 2",
                    value=True, key="c9_exp3_parallel_switch_2"
                )

            series_wire = "#16a34a" if series_switch else "#94a3b8"
            series_bulb = "#fde047" if series_switch else "#e2e8f0"
            series_glow = "filter:drop-shadow(0 0 8px #facc15);" if series_switch else ""
            p1_wire = "#16a34a" if parallel_switch_1 else "#94a3b8"
            p2_wire = "#16a34a" if parallel_switch_2 else "#94a3b8"
            p1_bulb = "#fde047" if parallel_switch_1 else "#e2e8f0"
            p2_bulb = "#fde047" if parallel_switch_2 else "#e2e8f0"
            p1_glow = "filter:drop-shadow(0 0 8px #facc15);" if parallel_switch_1 else ""
            p2_glow = "filter:drop-shadow(0 0 8px #facc15);" if parallel_switch_2 else ""
            series_status = (
                ("ਸਰਕਟ ਪੂਰਾ — ਦੋਵੇਂ ਬਲਬ ਜਗਦੇ ਹਨ" if is_pa_series else "Complete path — both bulbs glow")
                if series_switch else
                ("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ — ਦੋਵੇਂ ਬਲਬ ਬੰਦ" if is_pa_series else "Open switch — both bulbs are off")
            )
            if is_pa_series:
                parallel_status = f"ਸ਼ਾਖਾ 1: {'ਚਾਲੂ' if parallel_switch_1 else 'ਬੰਦ'} | ਸ਼ਾਖਾ 2: {'ਚਾਲੂ' if parallel_switch_2 else 'ਬੰਦ'}"
            else:
                parallel_status = f"Branch 1: {'ON' if parallel_switch_1 else 'OFF'} | Branch 2: {'ON' if parallel_switch_2 else 'OFF'}"

            series_title = "ਲੜੀਵਾਰ ਜੋੜ" if is_pa_series else "SERIES CONNECTION"
            parallel_title = "ਸਮਾਂਤਰ ਜੋੜ" if is_pa_series else "PARALLEL CONNECTION"
            series_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:14px;padding:8px;background:rgba(128,128,128,.035)">
            <svg viewBox="0 0 340 235" width="100%" role="img" aria-label="Series circuit: one main switch controls both bulbs">
              <g fill="none" stroke="{series_wire}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
                <path d="M48 58 H92 M136 58 H204 M248 58 H292 V177 H195 M145 177 H48 V119 M48 58 V82"/>
                <path d="M145 177 L{195 if series_switch else 170} {177 if series_switch else 151}" stroke="#64748b" stroke-width="3"/>
              </g>
              <g stroke="#334155" stroke-width="3"><line x1="31" y1="82" x2="65" y2="82"/><line x1="38" y1="101" x2="58" y2="101"/></g>
              <circle cx="114" cy="58" r="22" fill="{series_bulb}" stroke="#475569" stroke-width="3" style="{series_glow}"/>
              <path d="M104 48 l20 20 M124 48 l-20 20" stroke="#475569" stroke-width="3"/>
              <circle cx="226" cy="58" r="22" fill="{series_bulb}" stroke="#475569" stroke-width="3" style="{series_glow}"/>
              <path d="M216 48 l20 20 M236 48 l-20 20" stroke="#475569" stroke-width="3"/>
              <text x="48" y="139" fill="currentColor" font-size="11" text-anchor="middle">{"ਸੈੱਲ" if is_pa_series else "CELL"}</text>
              <text x="180" y="158" fill="currentColor" font-size="10" text-anchor="middle">{"ਮੁੱਖ ਸਵਿੱਚ" if is_pa_series else "MAIN SWITCH"}</text>
              <text x="170" y="211" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">{"ਇੱਕ ਰਸਤਾ • ਦੋਵੇਂ ਬਲਬ ਇਕੱਠੇ" if is_pa_series else "ONE PATH • BOTH BULBS TOGETHER"}</text>
            </svg></div>"""

            parallel_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:14px;padding:8px;background:rgba(128,128,128,.035)">
            <svg viewBox="0 0 340 235" width="100%" role="img" aria-label="Parallel circuit: each bulb branch has its own switch">
              <g fill="none" stroke="#64748b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
                <path d="M48 58 H292 V177 H48 V119 M48 58 V82"/>
              </g>
              <path d="M112 58 V76 M112 94 V119 M112 157 V177" fill="none" stroke="{p1_wire}" stroke-width="4" stroke-linecap="round"/>
              <path d="M228 58 V76 M228 94 V119 M228 157 V177" fill="none" stroke="{p2_wire}" stroke-width="4" stroke-linecap="round"/>
              <g stroke="#475569" stroke-width="3" stroke-linecap="round">
                <circle cx="112" cy="76" r="2.5" fill="#475569"/><circle cx="112" cy="94" r="2.5" fill="#475569"/>
                <line x1="112" y1="76" x2="112" y2="{94 if parallel_switch_1 else 66}"/>
                <circle cx="228" cy="76" r="2.5" fill="#475569"/><circle cx="228" cy="94" r="2.5" fill="#475569"/>
                <line x1="228" y1="76" x2="228" y2="{94 if parallel_switch_2 else 66}"/>
              </g>
              <circle cx="112" cy="138" r="19" fill="{p1_bulb}" stroke="#475569" stroke-width="3" style="{p1_glow}"/>
              <path d="M103 129 l18 18 M121 129 l-18 18" stroke="#475569" stroke-width="3"/>
              <circle cx="228" cy="138" r="19" fill="{p2_bulb}" stroke="#475569" stroke-width="3" style="{p2_glow}"/>
              <path d="M219 129 l18 18 M237 129 l-18 18" stroke="#475569" stroke-width="3"/>
              <g stroke="#334155" stroke-width="3"><line x1="31" y1="82" x2="65" y2="82"/><line x1="38" y1="101" x2="58" y2="101"/></g>
              <text x="48" y="139" fill="currentColor" font-size="11" text-anchor="middle">{"ਸੈੱਲ" if is_pa_series else "CELL"}</text>
              <text x="112" y="201" fill="currentColor" font-size="10" text-anchor="middle">{"ਸਵਿੱਚ 1" if is_pa_series else "SWITCH 1"}</text>
              <text x="228" y="201" fill="currentColor" font-size="10" text-anchor="middle">{"ਸਵਿੱਚ 2" if is_pa_series else "SWITCH 2"}</text>
              <text x="170" y="222" fill="currentColor" font-size="11" font-weight="700" text-anchor="middle">{"ਵੱਖਰੀਆਂ ਸ਼ਾਖਾਵਾਂ" if is_pa_series else "INDEPENDENT BRANCHES"}</text>
            </svg></div>"""

            st.markdown("#### " + ("ਲੜੀਵਾਰ ਅਤੇ ਸਮਾਂਤਰ ਸਰਕਟਾਂ ਦੀ ਤੁਲਨਾ" if is_pa_series else "Compare Series and Parallel Circuits"))
            col_series, col_parallel = st.columns(2)
            with col_series:
                st.markdown("**" + series_title + "**")
                st.markdown(series_svg, unsafe_allow_html=True)
                st.caption("ਇੱਕ ਸਵਿੱਚ ਖੋਲ੍ਹਣ ਨਾਲ ਦੋਵੇਂ ਬਲਬ ਬੰਦ ਹੋ ਜਾਂਦੇ ਹਨ।" if is_pa_series else "Opening the main switch turns both bulbs off.")
                st.info(series_status)
            with col_parallel:
                st.markdown("**" + parallel_title + "**")
                st.markdown(parallel_svg, unsafe_allow_html=True)
                st.caption("ਇੱਕ ਸ਼ਾਖਾ ਬੰਦ ਹੋਵੇ ਤਾਂ ਦੂਜੀ ਚੱਲ ਸਕਦੀ ਹੈ।" if is_pa_series else "One branch can be off while the other remains on.")
                st.info(parallel_status)
            st.write("💡 " + note)
            st.caption("Qualitative visuals only — no numerical readings, calculations, units or graphs." if not is_pa_series else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਰੀਡਿੰਗ, ਗਣਨਾ, ਇਕਾਈ ਜਾਂ ਗ੍ਰਾਫ ਨਹੀਂ।")
        elif kind == "power" and selected_class == 9 and exp_index == 3:
            # Class 9 Experiment 4: qualitative electrical power and energy transformations.
            is_pa_power = st.session_state.language != "en"
            device_label = {
                "bulb": "ਬਲਬ" if is_pa_power else "BULB",
                "fan": "ਪੱਖਾ" if is_pa_power else "FAN",
                "heater": "ਹੀਟਰ" if is_pa_power else "HEATER",
            }[class9_power_device]
            if class9_power_device == "bulb":
                device_art = f'<circle cx="310" cy="112" r="30" fill="{ "#fde047" if closed else "#e2e8f0" }" stroke="#475569" stroke-width="3"/><path d="M294 104 l10 10 l-7 9 l13 5 l13 -17 l7 10" fill="none" stroke="#475569" stroke-width="3" stroke-linecap="round"/><path d="M299 145 V154 H321 V145" fill="none" stroke="#64748b" stroke-width="4"/>'
                output_label = "ਰੋਸ਼ਨੀ ਅਤੇ ਕੁਝ ਤਾਪ" if is_pa_power else "Light and some heat"
                glow = '<g stroke="#f59e0b" stroke-width="3" stroke-linecap="round"><path d="M310 65 V55 M270 80 L262 72 M350 80 L358 72 M263 112 H252 M357 112 H368"/></g>' if closed else ""
            elif class9_power_device == "fan":
                device_art = f'<circle cx="310" cy="112" r="34" fill="#e0f2fe" stroke="#0369a1" stroke-width="3"/><circle cx="310" cy="112" r="7" fill="#0369a1"/><g fill="{ "#38bdf8" if closed else "#94a3b8" }"><path d="M310 105 C292 76 278 91 298 110 Z"/><path d="M317 112 C346 94 331 80 313 101 Z"/><path d="M310 119 C328 148 342 133 322 114 Z"/><path d="M303 112 C274 130 289 144 307 123 Z"/></g>'
                output_label = "ਗਤੀ / ਹਵਾ" if is_pa_power else "Motion / moving air"
                glow = '<path d="M350 88 q15 8 0 16 M356 108 q15 8 0 16" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-linecap="round"/>' if closed else ""
            else:
                device_art = f'<rect x="280" y="78" width="60" height="70" rx="9" fill="#e2e8f0" stroke="#475569" stroke-width="3"/><path d="M292 91 q8 -8 16 0 t16 0 M292 105 q8 -8 16 0 t16 0 M292 119 q8 -8 16 0 t16 0" fill="none" stroke="{ "#ea580c" if closed else "#94a3b8" }" stroke-width="4" stroke-linecap="round"/>'
                output_label = "ਤਾਪ" if is_pa_power else "Heat"
                glow = '<g stroke="#f97316" stroke-width="3" stroke-linecap="round"><path d="M292 67 q-6 -7 0 -14 M310 67 q-6 -7 0 -14 M328 67 q-6 -7 0 -14"/></g>' if closed else ""
            wire_color = "#16a34a" if closed else "#94a3b8"
            switch_art = '<path d="M126 62 L155 62" stroke="#16a34a" stroke-width="4" stroke-linecap="round"/>' if closed else '<path d="M126 62 L151 47" stroke="#ea580c" stroke-width="4" stroke-linecap="round"/>'
            power_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">
            <svg viewBox="0 0 420 220" width="100%" role="img" aria-label="Qualitative electrical power and energy transformation visual">
              <g fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M60 62 H126"/><path d="M155 62 H310 V78"/><path d="M310 148 V184 H60 V110"/>
              </g>
              <g stroke="#475569" stroke-width="3" stroke-linecap="round"><line x1="48" y1="78" x2="72" y2="78"/><line x1="53" y1="91" x2="67" y2="91"/><line x1="60" y1="78" x2="60" y2="110"/></g>
              {switch_art}
              {device_art}{glow}
              <g fill="currentColor" font-size="12" text-anchor="middle"><text x="60" y="132">{ "ਸੈੱਲ" if is_pa_power else "CELL" }</text><text x="140" y="35">{ "ਸਵਿੱਚ" if is_pa_power else "SWITCH" }</text><text x="310" y="174">{device_label}</text></g>
              <rect x="82" y="190" width="256" height="23" rx="8" fill="#dbeafe" stroke="#93c5fd"/>
              <text x="210" y="206" fill="#1e40af" font-size="12" font-weight="700" text-anchor="middle">{output_label}</text>
            </svg></div>"""
            st.markdown("#### " + ("ਬਿਜਲੀ ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ ਦੇ ਰੂਪਾਂਤਰ" if is_pa_power else "Electrical Power and Energy Transformations"))
            st.markdown(power_svg, unsafe_allow_html=True)
            if closed:
                st.success(("ਸਵਿੱਚ ਬੰਦ ਹੈ: ਉਪਕਰਣ ਬਿਜਲੀ ਊਰਜਾ ਨੂੰ ਲਾਭਦਾਇਕ ਰੂਪ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।" if is_pa_power else "Switch closed: the device converts electrical energy into a useful form."))
            else:
                st.info(("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੈ: ਸਰਕਟ ਟੁੱਟਿਆ ਹੈ ਅਤੇ ਉਪਕਰਣ ਕੰਮ ਨਹੀਂ ਕਰਦਾ।" if is_pa_power else "Switch open: the circuit is broken and the device is off."))
            st.caption(("ਇਹ ਗੁਣਾਤਮਕ ਮਾਡਲ ਹੈ—ਕੋਈ ਅੰਕ, ਗਣਨਾ, ਇਕਾਈ ਜਾਂ ਗ੍ਰਾਫ ਨਹੀਂ।" if is_pa_power else "Qualitative model only — no numerical readings, calculations, units or graphs."))
        elif selected_class == 10 and exp_index == 1 and kind == "series_parallel":
            # Class 10 Experiment 2: compare equivalent resistance and current in series/parallel.
            is_pa_rnet = st.session_state.language != "en"
            r_each = resistance
            r_series = 2 * r_each
            r_parallel = r_each / 2
            i_series = voltage / r_series if closed else 0.0
            i_parallel_total = voltage / r_parallel if closed else 0.0
            i_branch = voltage / r_each if closed else 0.0
            wire = "#16a34a" if closed else "#94a3b8"
            bulb_fill = "#fde047" if closed else "#e2e8f0"
            bulb_glow = "filter:drop-shadow(0 0 8px #facc15);" if closed else ""
            net_title = "ਲੜੀਵਾਰ ਅਤੇ ਸਮਾਂਤਰ ਰੋਧ ਦੀ ਤੁਲਨਾ" if is_pa_rnet else "Compare Series and Parallel Resistance"
            net_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 460 430" width="100%" role="img" aria-label="Side-by-side series and parallel circuits with two equal resistors">
  <text x="230" y="22" fill="currentColor" font-size="15" font-weight="bold" text-anchor="middle">{net_title}</text>
  <text x="115" y="53" fill="currentColor" font-size="13" font-weight="bold" text-anchor="middle">{"ਲੜੀਵਾਰ ਸਰਕਟ" if is_pa_rnet else "SERIES CIRCUIT"}</text>
  <g fill="none" stroke="{wire}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M40 95 H74 M112 95 H140 M178 95 H205 V185 H40 V135 M40 95 V108"/>
    <path d="M74 95 l7 -10 l8 20 l8 -20 l8 20 l7 -10"/>
    <path d="M140 95 l7 -10 l8 20 l8 -20 l8 20 l7 -10"/>
  </g>
  <g fill="currentColor" font-size="11" text-anchor="middle"><text x="40" y="155">{"ਸੈੱਲ" if is_pa_rnet else "CELL"}</text><text x="93" y="75">R₁ = {r_each} Ω</text><text x="159" y="75">R₂ = {r_each} Ω</text></g>
  <circle cx="205" cy="140" r="16" fill="{bulb_fill}" stroke="#475569" stroke-width="2" style="{bulb_glow}"/><path d="M197 132 l16 16 m0 -16 l-16 16" stroke="#475569" stroke-width="2"/>
  <text x="115" y="210" fill="currentColor" font-size="12" text-anchor="middle">{"Rₛ = 2R = " if is_pa_rnet else "Rₛ = 2R = "}{r_series} Ω</text>
  <text x="345" y="53" fill="currentColor" font-size="13" font-weight="bold" text-anchor="middle">{"ਸਮਾਂਤਰ ਸਰਕਟ" if is_pa_rnet else "PARALLEL CIRCUIT"}</text>
  <g fill="none" stroke="{wire}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
    <path d="M260 95 H286 M324 95 H365 M260 95 V185 H365 V95 M260 95 V108"/>
    <path d="M286 95 l7 -10 l8 20 l8 -20 l8 20 l7 -10"/>
    <path d="M260 140 H286 M324 140 H365"/>
    <path d="M286 140 l7 -10 l8 20 l8 -20 l8 20 l7 -10"/>
  </g>
  <g fill="currentColor" font-size="11" text-anchor="middle"><text x="260" y="155">{"ਸੈੱਲ" if is_pa_rnet else "CELL"}</text><text x="305" y="75">R₁ = {r_each} Ω</text><text x="305" y="166">R₂ = {r_each} Ω</text></g>
  <text x="345" y="210" fill="currentColor" font-size="12" text-anchor="middle">{"Rₚ = R/2 = " if is_pa_rnet else "Rₚ = R/2 = "}{r_parallel:g} Ω</text>
  <line x1="20" y1="232" x2="440" y2="232" stroke="#94a3b8" stroke-dasharray="5 5"/>
  <rect x="24" y="250" width="412" height="68" rx="10" fill="#dbeafe" stroke="#93c5fd"/>
  <text x="230" y="275" fill="#1e40af" font-size="13" font-weight="bold" text-anchor="middle">{"ਲੜੀਵਾਰ: ਘੱਟ ਕਰੰਟ" if is_pa_rnet else "SERIES: LOWER TOTAL CURRENT"}</text>
  <text x="230" y="298" fill="#1e40af" font-size="12" text-anchor="middle">Iₛ = V / Rₛ = {i_series:.3f} A</text>
  <rect x="24" y="330" width="412" height="68" rx="10" fill="#dcfce7" stroke="#86efac"/>
  <text x="230" y="355" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">{"ਸਮਾਂਤਰ: ਵੱਧ ਕੁੱਲ ਕਰੰਟ" if is_pa_rnet else "PARALLEL: HIGHER TOTAL CURRENT"}</text>
  <text x="230" y="378" fill="#166534" font-size="12" text-anchor="middle">Iₚ = V / Rₚ = {i_parallel_total:.3f} A</text>
</svg></div>"""
            st.markdown("#### " + ("ਦੋ ਸਰਕਟਾਂ ਦਾ ਦ੍ਰਿਸ਼ ਮਾਡਲ" if is_pa_rnet else "Visual comparison of the two circuits"))
            st.markdown(net_svg, unsafe_allow_html=True)
            st.markdown("**" + ("ਮੌਜੂਦਾ ਸੈਟਿੰਗ ਲਈ ਗਣਨਾ" if is_pa_rnet else "Calculations for the selected settings") + "**")
            st.latex(r"R_s = R_1 + R_2 = " + str(r_each) + r" + " + str(r_each) + r" = " + str(r_series) + r"\,\Omega")
            st.latex(r"R_p = \frac{R_1R_2}{R_1+R_2} = \frac{" + str(r_each) + r"\times" + str(r_each) + "}{" + str(r_each) + "+" + str(r_each) + r"} = " + f"{r_parallel:g}" + r"\,\Omega")
            c1, c2, c3 = st.columns(3)
            c1.metric("ਵੋਲਟੇਜ (V)" if is_pa_rnet else "Voltage (V)", f"{voltage} V")
            c2.metric("ਲੜੀਵਾਰ Rₛ" if is_pa_rnet else "Series Rₛ", f"{r_series} Ω")
            c3.metric("ਸਮਾਂਤਰ Rₚ" if is_pa_rnet else "Parallel Rₚ", f"{r_parallel:g} Ω")
            c4, c5, c6 = st.columns(3)
            c4.metric("ਲੜੀਵਾਰ ਕਰੰਟ" if is_pa_rnet else "Series current", f"{i_series:.3f} A")
            c5.metric("ਸਮਾਂਤਰ ਕੁੱਲ ਕਰੰਟ" if is_pa_rnet else "Parallel total current", f"{i_parallel_total:.3f} A")
            c6.metric("ਸਮਾਂਤਰ ਹਰ ਸ਼ਾਖਾ" if is_pa_rnet else "Each parallel branch", f"{i_branch:.3f} A")
            obs = []
            for test_v in [6, 12, 18, 24]:
                si = test_v / r_series if closed else 0.0
                pi = test_v / r_parallel if closed else 0.0
                obs.append({
                    ("ਵੋਲਟੇਜ (V)" if is_pa_rnet else "Voltage (V)"): test_v,
                    ("ਲੜੀਵਾਰ ਕਰੰਟ (A)" if is_pa_rnet else "Series current (A)"): f"{si:.3f}",
                    ("ਸਮਾਂਤਰ ਕੁੱਲ ਕਰੰਟ (A)" if is_pa_rnet else "Parallel total current (A)"): f"{pi:.3f}",
                })
            st.markdown("**" + ("ਨਿਰੀਖਣ ਸਾਰਣੀ (ਦੋਵੇਂ ਰੋਧ ਬਰਾਬਰ)" if is_pa_rnet else "Observation table (two equal resistors)") + "**")
            st.dataframe(obs, hide_index=True, use_container_width=True)
            if closed:
                st.success("ਲੜੀਵਾਰ ਰੋਧ ਵੱਧ ਹੋਣ ਕਰਕੇ ਕਰੰਟ ਘੱਟ ਹੈ; ਸਮਾਂਤਰ ਸਮਤੁੱਲ ਰੋਧ ਘੱਟ ਹੋਣ ਕਰਕੇ ਕੁੱਲ ਕਰੰਟ ਵੱਧ ਹੈ।" if is_pa_rnet else "Series resistance is higher, so its current is lower. Parallel equivalent resistance is lower, so its total current is higher.")
            else:
                st.info("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੈ: ਦੋਵੇਂ ਸਰਕਟਾਂ ਵਿੱਚ ਕਰੰਟ ਸਿਫ਼ਰ ਹੈ।" if is_pa_rnet else "Switch is open: current is zero in both circuits.")
            st.caption("ਆਦਰਸ਼ ਸਿਮੂਲੇਸ਼ਨ—ਸਾਰਣੀ ਗਣਨਾ ਨਾਲ ਬਣਦੀ ਹੈ, ਅਸਲੀ ਲੈਬ ਮਾਪ ਨਹੀਂ। ਘਰੇਲੂ ਮੇਨ ਬਿਜਲੀ ਨਾਲ ਕਦੇ ਪ੍ਰਯੋਗ ਨਾ ਕਰੋ।" if is_pa_rnet else "Ideal simulation: table values are calculated, not real lab measurements. Never experiment with household mains electricity.")
        elif selected_class == 10 and exp_index == 2 and kind == "power":
            # Class 10 Experiment 3: quantitative electrical power and energy model.
            is_pa_power10 = st.session_state.language != "en"
            current_power10 = voltage / resistance if closed and resistance else 0.0
            power_w10 = voltage * current_power10
            hours_power10 = st.slider("ਸਮਾਂ (ਘੰਟੇ)" if is_pa_power10 else "Operating time (hours)", 0.5, 8.0, 2.0, 0.5, key="class10_power_hours")
            energy_wh10 = power_w10 * hours_power10
            energy_kwh10 = energy_wh10 / 1000.0
            circuit_color10 = "#16a34a" if closed and voltage > 0 else "#94a3b8"
            bulb_fill10 = "#fde047" if closed and voltage > 0 else "#e2e8f0"
            glow10 = '<g stroke="#f59e0b" stroke-width="3" stroke-linecap="round"><path d="M290 48 V37 M262 61 L254 53 M318 61 L326 53 M252 83 H241 M328 83 H339"/></g>' if closed and voltage > 0 else ""
            power_svg10 = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">
            <svg viewBox="0 0 420 210" width="100%" role="img" aria-label="Electrical power circuit with cell, switch, resistor and glowing bulb">
              <g fill="none" stroke="{circuit_color10}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M55 68 H105"/><path d="M140 68 H290 V51"/><path d="M290 116 V165 H55 V108"/>
              </g>
              <g stroke="#475569" stroke-width="3" stroke-linecap="round"><line x1="43" y1="76" x2="67" y2="76"/><line x1="48" y1="90" x2="62" y2="90"/></g>
              <path d="{ 'M105 68 L140 68' if closed else 'M105 68 L134 52' }" stroke="{circuit_color10}" stroke-width="4" stroke-linecap="round"/>
              <circle cx="290" cy="83" r="33" fill="{bulb_fill10}" stroke="#475569" stroke-width="3"/>
              <path d="M274 72 L284 82 L278 91 L291 98 L305 77 L313 86" fill="none" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
              <path d="M278 116 V126 H302 V116" fill="none" stroke="#64748b" stroke-width="4"/>
              {glow10}
              <rect x="156" y="145" width="118" height="30" rx="8" fill="#dbeafe" stroke="#93c5fd"/>
              <text x="215" y="164" fill="#1e40af" font-size="12" font-weight="700" text-anchor="middle">R = {resistance} Ω</text>
              <g fill="currentColor" font-size="12" text-anchor="middle"><text x="55" y="128">{ "ਸੈੱਲ" if is_pa_power10 else "CELL" }</text><text x="122" y="39">{ "ਸਵਿੱਚ" if is_pa_power10 else "SWITCH" }</text><text x="290" y="137">{ "ਬਲਬ" if is_pa_power10 else "BULB / LOAD" }</text></g>
              <text x="210" y="198" fill="currentColor" font-size="12" text-anchor="middle">V = {voltage} V · I = {current_power10:.2f} A · P = {power_w10:.2f} W</text>
            </svg></div>"""
            st.markdown("#### " + ("ਬਿਜਲੀ ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ" if is_pa_power10 else "Electrical Power and Energy"))
            st.markdown(power_svg10, unsafe_allow_html=True)
            st.markdown("**" + ("ਸੂਤਰ" if is_pa_power10 else "Formula") + ":** P = VI = V²/R  ·  E = Pt")
            c10a, c10b, c10c = st.columns(3)
            c10a.metric("I (A)", f"{current_power10:.2f}")
            c10b.metric("P (W)", f"{power_w10:.2f}")
            c10c.metric("E (kWh)", f"{energy_kwh10:.4f}")
            st.caption(("ਗਣਨਾ ਕੀਤਾ ਮਾਡਲ: E = P × ਸਮਾਂ। ਇਹ ਅਸਲੀ ਪ੍ਰਯੋਗ ਦੀ ਰੀਡਿੰਗ ਨਹੀਂ ਹੈ।" if is_pa_power10 else "Calculated simulation: E = power × time. These are modelled values, not real laboratory readings."))
            table_rows10 = []
            for v10 in (6, 12, 18, 24):
                i10 = v10 / resistance if closed else 0.0
                p10 = v10 * i10
                table_rows10.append({"V (V)": v10, "R (Ω)": resistance, "I (A)": round(i10, 2), "P (W)": round(p10, 2)})
            st.markdown("**" + ("ਵੋਲਟੇਜ ਬਦਲਣ ਨਾਲ ਰੀਡਿੰਗਾਂ" if is_pa_power10 else "Readings as voltage changes") + "**")
            st.dataframe(table_rows10, use_container_width=True, hide_index=True)
            if not closed:
                st.info("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੈ: ਕਰੰਟ, ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ ਸਿਫ਼ਰ ਹਨ।" if is_pa_power10 else "Switch open: current, power and energy are zero.")
            st.caption(("ਸਿਰਫ਼ ਆਦਰਸ਼ ਘੱਟ-ਵੋਲਟੇਜ ਸਿਮੂਲੇਸ਼ਨ; ਘਰੇਲੂ ਮੇਨ ਬਿਜਲੀ ਨਾਲ ਪ੍ਰਯੋਗ ਨਾ ਕਰੋ।" if is_pa_power10 else "Ideal low-voltage simulation only; never experiment with household mains electricity."))
        elif kind in ("ohms", "series_parallel", "power", "heating"):
            m1, m2 = st.columns(2)
            m1.metric(tr("current"), f"{current:.3f} A")
            m2.metric(tr("power"), f"{power:.3f} W")
            st.metric(tr("circuit"), tr("closed") if closed else tr("open_circuit"))
            if kind in ("ohms", "power", "heating"):
                volts = list(range(0, 25))
                df = pd.DataFrame({"Voltage (V)": volts, "Current (A)": [v / resistance for v in volts]})
                st.markdown("#### " + tr("graph"))
                st.caption(tr("graph_note"))
                st.line_chart(df.set_index("Voltage (V)"))
            if kind == "series_parallel":
                st.write(f"**Series (two {resistance} Ω resistors):** {2*resistance} Ω")
                st.write(f"**Parallel (two equal resistors):** {resistance/2:.2f} Ω")
        elif kind == "conductors":
            is_conductor = material in (["Copper", "Aluminium", "Iron"] if st.session_state.language == "en" else ["ਤਾਂਬਾ", "ਐਲੂਮੀਨੀਅਮ", "ਲੋਹਾ"])
            wire_color = "#16a34a" if is_conductor else "#d97706"
            bulb_fill = "#fde047" if is_conductor else "#e2e8f0"
            bulb_glow = "filter: drop-shadow(0 0 10px #facc15);" if is_conductor else ""
            material_label = material.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            svg = (
                '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">'
                '<svg viewBox="0 0 420 230" width="100%" role="img" aria-label="Virtual material testing circuit">'
                '<g fill="none" stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M65 48 H145"/><path d="M65 48 V76"/><path d="M65 94 V108"/><path d="M275 48 H320 V78"/><path d="M320 122 V170 H65 V108"/>'
                '</g>'
                '<g stroke="#334155" stroke-width="3" fill="none"><line x1="46" y1="76" x2="84" y2="76"/><line x1="53" y1="94" x2="77" y2="94"/></g>'
                '<g stroke="#334155" stroke-width="3"><circle cx="320" cy="100" r="23" fill="' + bulb_fill + '" style="' + bulb_glow + '"/><path d="M307 87 L315 95 L309 102 L319 108 L326 99 L333 108" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M309 124 V132 H331 V124 M312 132 V138 H328 V132" fill="none" stroke="#64748b" stroke-width="2.5"/></g>'
                '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="65" y="130">' + tr("battery") + '</text><text x="320" y="194">' + tr("bulb") + '</text></g>'
                '<g stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round"><path d="M145 48 H174"/><path d="M246 48 H275"/></g>'
                '<rect x="174" y="35" width="72" height="26" rx="5" fill="' + ("#bbf7d0" if is_conductor else "#fed7aa") + '" stroke="' + wire_color + '" stroke-width="2"/>'
                '<text x="210" y="51" font-size="10" font-weight="bold" fill="#1f2937" text-anchor="middle">' + material_label + '</text>'
                '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="210" y="20">' + ("TEST MATERIAL" if st.session_state.language == "en" else "ਪਦਾਰਥ ਦੀ ਜਾਂਚ") + '</text><text x="210" y="216">' + (("Path complete" if is_conductor else "Path incomplete") if st.session_state.language == "en" else ("ਰਸਤਾ ਪੂਰਾ" if is_conductor else "ਰਸਤਾ ਅਧੂਰਾ")) + '</text></g>'
                '</svg></div>'
            )
            st.markdown("#### " + tr("visual_circuit"), unsafe_allow_html=True)
            st.markdown(svg, unsafe_allow_html=True)
            st.metric(tr("conductivity"), tr("conductor") if is_conductor else tr("insulator"))
            st.metric(tr("circuit"), tr("bulb_on") if is_conductor else tr("bulb_off"))
            st.info(
                ("This material bridges the gap. Conductors such as metals allow current to pass and the bulb glows; insulators such as rubber, plastic and dry wood do not complete the path."
                 if st.session_state.language == "en" else
                 "ਇਹ ਪਦਾਰਥ ਸਰਕਟ ਦੇ ਖਾਲੀ ਹਿੱਸੇ ਨੂੰ ਜੋੜਦਾ ਹੈ। ਧਾਤਾਂ ਵਰਗੇ ਚਾਲਕ ਕਰੰਟ ਲੰਘਣ ਦਿੰਦੇ ਹਨ ਅਤੇ ਬਲਬ ਜਗਦਾ ਹੈ; ਰਬੜ, ਪਲਾਸਟਿਕ ਅਤੇ ਸੁੱਕੀ ਲੱਕੜ ਵਰਗੇ ਕੁਚਾਲਕ ਰਸਤਾ ਪੂਰਾ ਨਹੀਂ ਕਰਦੇ।")
            )
            st.write("💡 " + note)
        elif electromagnet_experiment:
            is_pa = st.session_state.language != "en"
            lifted = closed
            crane_title = "ਕਰੇਨ ਵਿੱਚ ਬਿਜਲੀ-ਚੁੰਬਕ" if is_pa else "Electromagnet used in a scrapyard crane"
            scrap_caption = "ਲੋਹੇ ਦਾ ਕਬਾੜ" if is_pa else "Iron scrap"
            magnet_caption = "ਬਿਜਲੀ-ਚੁੰਬਕ" if is_pa else "Electromagnet"
            on_caption = "ਸਵਿੱਚ ਬੰਦ: ਲੋਹਾ ਚੁੱਕਿਆ ਗਿਆ" if is_pa else "Switch ON: iron scrap is lifted"
            off_caption = "ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ: ਲੋਹਾ ਛੱਡ ਦਿੱਤਾ ਗਿਆ" if is_pa else "Switch OFF: iron scrap is released"
            state_caption = on_caption if closed else off_caption
            magnet_fill = "#dc2626" if closed else "#94a3b8"
            scrap_items = (
                '<g stroke="#475569" stroke-width="5" stroke-linecap="round" fill="none">'
                '<path d="M155 190 l18 -12 l12 17 l-14 13 Z"/>'
                '<path d="M205 192 l22 -14 l13 18 l-19 13 Z"/>'
                '<path d="M256 190 l19 -12 l13 18 l-16 14 Z"/>'
                '<path d="M300 194 l17 -11 l12 16 l-15 12 Z"/>'
                '</g>'
            ) if not closed else (
                '<g stroke="#475569" stroke-width="5" stroke-linecap="round" fill="none">'
                '<path d="M158 136 l18 -12 l12 17 l-14 13 Z"/>'
                '<path d="M202 141 l22 -14 l13 18 l-19 13 Z"/>'
                '<path d="M246 136 l19 -12 l13 18 l-16 14 Z"/>'
                '<path d="M288 141 l17 -11 l12 16 l-15 12 Z"/>'
                '</g>'
            )
            st.markdown("#### " + crane_title)
            crane_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 440 300" width="100%" role="img" aria-label="Scrapyard crane with a switch-controlled electromagnet lifting or releasing iron scrap">
<rect x="18" y="255" width="404" height="18" rx="5" fill="#94a3b8"/>
<rect x="45" y="56" width="24" height="199" rx="4" fill="#64748b"/>
<rect x="45" y="48" width="285" height="18" rx="4" fill="#f59e0b" stroke="#92400e" stroke-width="2"/>
<rect x="305" y="66" width="18" height="34" fill="#64748b"/>
<path d="M314 100 V142" stroke="#334155" stroke-width="4"/>
<rect x="278" y="139" width="72" height="31" rx="6" fill="{magnet_fill}" stroke="#7f1d1d" stroke-width="2"/>
<text x="314" y="159" fill="white" font-size="12" font-weight="bold" text-anchor="middle">E-MAGNET</text>
<text x="314" y="185" fill="currentColor" font-size="11" text-anchor="middle">{magnet_caption}</text>
{scrap_items}
<g fill="currentColor" font-size="12" text-anchor="middle"><text x="220" y="28">{"ਕਬਾੜਖਾਨੇ ਦੀ ਕਰੇਨ" if is_pa else "SCRAPYARD CRANE"}</text><text x="220" y="292">{scrap_caption}</text></g>
</svg></div>"""
            st.markdown(crane_svg, unsafe_allow_html=True)
            st.metric("ਕਰੇਨ ਦੀ ਸਥਿਤੀ" if is_pa else "Crane status", ("ਲੋਹਾ ਚੁੱਕਿਆ ਹੋਇਆ" if is_pa else "Iron scrap lifted") if lifted else ("ਲੋਹਾ ਛੱਡਿਆ ਹੋਇਆ" if is_pa else "Iron scrap released"))
            st.info(state_caption)
            st.markdown("**" + ("ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ?" if is_pa else "How it works") + "**")
            st.write(("ਸਵਿੱਚ ਬੰਦ ਕਰਨ ਨਾਲ ਕੋਇਲ ਵਿੱਚੋਂ ਕਰੰਟ ਲੰਘਦਾ ਹੈ ਅਤੇ ਲੋਹੇ ਦਾ ਕੋਰ ਚੁੰਬਕ ਬਣ ਜਾਂਦਾ ਹੈ। ਇਹ ਲੋਹੇ ਦੇ ਕਬਾੜ ਨੂੰ ਚੁੱਕ ਲੈਂਦਾ ਹੈ। ਸਵਿੱਚ ਖੋਲ੍ਹਣ ਨਾਲ ਕਰੰਟ ਰੁਕ ਜਾਂਦਾ ਹੈ ਅਤੇ ਕਬਾੜ ਹੇਠਾਂ ਡਿੱਗ ਜਾਂਦਾ ਹੈ।" if is_pa else "When the switch is closed, current flows through the coil and makes the iron core magnetic, so it lifts iron scrap. Opening the switch stops the current and releases the scrap."))
            st.caption("Illustrative classroom simulation — not a real crane or a measurement." if not is_pa else "ਇਹ ਸਿਰਫ਼ ਸਿੱਖਣ ਲਈ ਵਰਚੁਅਲ ਮਾਡਲ ਹੈ, ਅਸਲੀ ਕਰੇਨ ਜਾਂ ਮਾਪ ਨਹੀਂ।")
            st.write("💡 " + note)
        elif kind == "electromagnet":
            if selected_class == 8 and exp_index == 3:
                is_pa_em8 = st.session_state.language != "en"
                active_color = "#16a34a" if closed else "#94a3b8"
                magnet_fill = "#dc2626" if closed else "#94a3b8"
                clip_group = (
                    '<g stroke="#64748b" stroke-width="4" fill="none" stroke-linecap="round">'
                    '<path d="M130 180 v18 q0 14 13 14 q13 0 13 -14 v-12"/>'
                    '<path d="M165 180 v18 q0 14 13 14 q13 0 13 -14 v-12"/>'
                    '<path d="M200 180 v18 q0 14 13 14 q13 0 13 -14 v-12"/>'
                    '</g>'
                    if closed else
                    '<g stroke="#64748b" stroke-width="4" fill="none" stroke-linecap="round">'
                    '<path d="M130 222 v12 q0 10 13 10 q13 0 13 -10 v-8"/>'
                    '<path d="M165 222 v12 q0 10 13 10 q13 0 13 -10 v-8"/>'
                    '<path d="M200 222 v12 q0 10 13 10 q13 0 13 -10 v-8"/>'
                    '</g>'
                )
                field_lines = (
                    '<g fill="none" stroke="#3b82f6" stroke-width="2.5">'
                    '<path d="M125 115 C75 60 95 35 170 35 C245 35 265 60 225 115"/>'
                    '<path d="M125 135 C75 190 95 215 170 215 C245 215 265 190 225 135"/>'
                    '<path d="M138 118 C110 85 125 65 170 65 C215 65 230 85 212 118"/>'
                    '<path d="M138 132 C110 165 125 185 170 185 C215 185 230 165 212 132"/>'
                    '</g>'
                    '<g fill="#3b82f6"><path d="M120 66 l-2 10 9 -4 Z"/><path d="M230 184 l2 -10 -9 4 Z"/></g>'
                    if closed else
                    '<g fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 6" opacity=".4">'
                    '<path d="M125 115 C75 60 95 35 170 35 C245 35 265 60 225 115"/>'
                    '<path d="M125 135 C75 190 95 215 170 215 C245 215 265 190 225 135"/>'
                    '</g>'
                )
                status = (
                    ("ਸਵਿੱਚ ਬੰਦ — ਕਰੰਟ ਵਹਿੰਦਾ ਹੈ; ਕੋਇਲ ਚੁੰਬਕ ਬਣਦੀ ਹੈ" if closed else "ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ — ਕਰੰਟ ਰੁਕਿਆ; ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ ਘੱਟ/ਨਹੀਂ")
                    if is_pa_em8 else
                    ("SWITCH ON — CURRENT FLOWS; THE COIL BECOMES MAGNETIC" if closed else "SWITCH OPEN — CURRENT STOPS; THE MAGNETIC EFFECT DISAPPEARS")
                )
                em_svg = f"""
<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035);">
<svg viewBox="0 0 440 300" width="100%" role="img" aria-label="Two examples of electricity producing magnetism: an electromagnet lifting paper clips and magnetic field around a current-carrying wire">
  <g stroke-linecap="round" stroke-linejoin="round">
    <rect x="18" y="18" width="196" height="264" rx="12" fill="rgba(128,128,128,.04)" stroke="rgba(120,140,160,.45)"/>
    <rect x="226" y="18" width="196" height="264" rx="12" fill="rgba(128,128,128,.04)" stroke="rgba(120,140,160,.45)"/>
    <text x="116" y="39" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">{'ਕੋਇਲ ਵਾਲਾ ਚੁੰਬਕ' if is_pa_em8 else 'COIL ELECTROMAGNET'}</text>
    <path d="M116 55 V80" stroke="#dc2626" stroke-width="4"/>
    <path d="M116 55 H160 V70" stroke="#dc2626" stroke-width="4" fill="none"/>
    <rect x="143" y="64" width="33" height="18" rx="4" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
    <path d="M159 70 l-8 7 h12 l-8 7" fill="none" stroke="#475569" stroke-width="2"/>
    <rect x="95" y="82" width="42" height="98" rx="6" fill="#64748b" stroke="#334155" stroke-width="2"/>
    <g fill="none" stroke="#f59e0b" stroke-width="5">
      <path d="M91 91 C145 91 145 100 91 100 C145 100 145 109 91 109 C145 109 145 118 91 118 C145 118 145 127 91 127 C145 127 145 136 91 136 C145 136 145 145 91 145 C145 145 145 154 91 154 C145 154 145 163 91 163"/>
    </g>
    <path d="M116 180 V195" stroke="{active_color}" stroke-width="5"/>
    <rect x="70" y="195" width="92" height="12" rx="5" fill="{magnet_fill}" stroke="#7f1d1d" stroke-width="2"/>
    {clip_group}
    <text x="116" y="265" fill="currentColor" font-size="11" text-anchor="middle">{'ਲੋਹੇ ਦੀਆਂ ਕਲਿੱਪਾਂ' if is_pa_em8 else 'IRON PAPER CLIPS'}</text>
    <text x="324" y="39" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">{'ਕਰੰਟ ਵਾਲੀ ਤਾਰ' if is_pa_em8 else 'CURRENT-CARRYING WIRE'}</text>
    {field_lines}
    <path d="M324 65 V231" stroke="{active_color}" stroke-width="7"/>
    <path d="M324 70 l-7 12 h14 Z" fill="{active_color}"/>
    <circle cx="275" cy="143" r="25" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
    <g transform="rotate({25 if closed else 0} 275 143)">
      <path d="M275 121 L268 145 L275 139 L282 145 Z" fill="#dc2626"/>
      <path d="M275 165 L268 141 L275 147 L282 141 Z" fill="#334155"/>
    </g>
    <text x="324" y="254" fill="currentColor" font-size="11" text-anchor="middle">{'ਚੁੰਬਕੀ ਖੇਤਰ' if is_pa_em8 else 'MAGNETIC FIELD'}</text>
  </g>
</svg>
</div>
"""
                st.markdown("#### " + ("ਬਿਜਲੀ ਤੋਂ ਚੁੰਬਕਤਾ ਦੇ ਉਦਾਹਰਨ" if is_pa_em8 else "Examples of electricity producing magnetism"))
                st.markdown(em_svg, unsafe_allow_html=True)
                if closed:
                    st.success(status)
                else:
                    st.info(status)
                st.markdown("**" + ("ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ?" if is_pa_em8 else "How it works") + "**")
                st.write(
                    ("ਕੋਇਲ ਵਿੱਚੋਂ ਕਰੰਟ ਲੰਘਣ ਨਾਲ ਉਸ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਚੁੰਬਕੀ ਖੇਤਰ ਬਣਦਾ ਹੈ। ਲੋਹੇ ਦਾ ਕੋਰ ਇਸ ਪ੍ਰਭਾਵ ਨੂੰ ਮਜ਼ਬੂਤ ਕਰਦਾ ਹੈ ਅਤੇ ਇਲੈਕਟ੍ਰੋਮੈਗਨੈਟ ਕਲਿੱਪਾਂ ਨੂੰ ਖਿੱਚ ਸਕਦਾ ਹੈ। ਸਿੱਧੀ ਕਰੰਟ ਵਾਲੀ ਤਾਰ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਵੀ ਚੁੰਬਕੀ ਖੇਤਰ ਬਣਦਾ ਹੈ।"
                    if is_pa_em8 else
                    "Current through a coil creates a magnetic field. An iron core strengthens the effect, allowing the electromagnet to attract clips. A straight current-carrying wire also creates a magnetic field around it.")
                )
                st.caption("Qualitative visual model only — no numerical readings." if not is_pa_em8 else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ ਮਾਡਲ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮਾਪ ਨਹੀਂ।")
                st.write("💡 " + note)
            else:
                strength = turns * current_control
                st.metric(tr("magnetic"), f"{strength:.1f} relative units")
                st.write(f"{tr('turns')}: {turns} · {tr('current_control')}: {current_control:.1f} A")
        elif selected_class == 10 and exp_index == 3 and kind == "magnetic_field":
            # Class 10 Experiment 4: quantitative model of magnetic field around a straight wire.
            is_pa_wire10 = st.session_state.language != "en"
            wire_current10 = voltage / resistance if closed and resistance else 0.0
            # Relative visual index is proportional to current; it is not a measured field strength.
            field_index10 = wire_current10 * 10.0
            ring_color10 = "#2563eb" if closed and wire_current10 > 0 else "#94a3b8"
            ring_opacity10 = min(1.0, 0.25 + field_index10 / 10.0)
            ring_svg10 = ""
            for radius10 in (32, 50, 68, 86):
                ring_svg10 += f'<circle cx="230" cy="116" r="{radius10}" fill="none" stroke="{ring_color10}" stroke-width="2.5" opacity="{ring_opacity10:.2f}" stroke-dasharray="5 4"/>'
            direction_art10 = (
                '<circle cx="230" cy="116" r="13" fill="#dcfce7" stroke="#15803d" stroke-width="2"/><circle cx="230" cy="116" r="4" fill="#15803d"/>'
                if closed else
                '<circle cx="230" cy="116" r="13" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/><path d="M221 107 L239 125 M239 107 L221 125" stroke="#64748b" stroke-width="2"/>'
            )
            compass_angle10 = 28 if closed and wire_current10 > 0 else 0
            compass10 = f'<g transform="rotate({compass_angle10} 95 116)"><path d="M95 85 L87 119 L95 112 L103 119 Z" fill="#dc2626"/><path d="M95 147 L87 113 L95 120 L103 113 Z" fill="#334155"/></g>'
            wire_svg10 = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">
            <svg viewBox="0 0 460 235" width="100%" role="img" aria-label="Numerical magnetic field simulation around a straight wire with circular field lines and compass">
              {ring_svg10}
              <path d="M230 24 V207" stroke="{ '#16a34a' if closed and wire_current10 > 0 else '#94a3b8' }" stroke-width="7" stroke-linecap="round"/>
              {direction_art10}
              <circle cx="95" cy="116" r="38" fill="#f8fafc" stroke="#64748b" stroke-width="3"/>
              {compass10}
              <circle cx="95" cy="116" r="4" fill="#0f172a"/>
              <g fill="currentColor" font-size="12" text-anchor="middle"><text x="230" y="15">{ "ਕਰੰਟ ਵਾਲੀ ਤਾਰ" if is_pa_wire10 else "CURRENT-CARRYING WIRE" }</text><text x="95" y="169">{ "ਕੰਪਾਸ" if is_pa_wire10 else "COMPASS" }</text><text x="230" y="229">{ "ਗੋਲ ਚੁੰਬਕੀ ਖੇਤਰ ਰੇਖਾਵਾਂ" if is_pa_wire10 else "CIRCULAR MAGNETIC FIELD LINES" }</text></g>
              <text x="230" y="202" fill="currentColor" font-size="12" text-anchor="middle">I = {wire_current10:.2f} A</text>
            </svg></div>"""
            st.markdown("#### " + ("ਸਿੱਧੀ ਤਾਰ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਚੁੰਬਕੀ ਖੇਤਰ" if is_pa_wire10 else "Magnetic Field Around a Straight Wire"))
            st.markdown(wire_svg10, unsafe_allow_html=True)
            st.markdown("**" + ("ਸੰਬੰਧਿਤ ਸੂਤਰ" if is_pa_wire10 else "Relevant relationship") + ":** I = V/R  ·  For a long straight wire, B ∝ I/r")
            wire_a10, wire_b10, wire_c10 = st.columns(3)
            wire_a10.metric("V (V)", f"{voltage}")
            wire_b10.metric("I (A)", f"{wire_current10:.2f}")
            wire_c10.metric("Relative field index", f"{field_index10:.2f}")
            st.caption(("Relative field index ਸਿਰਫ਼ ਦ੍ਰਿਸ਼ ਤੁਲਨਾ ਲਈ ਹੈ, ਟੈਸਲਾ ਵਿੱਚ ਅਸਲ ਮਾਪ ਨਹੀਂ।" if is_pa_wire10 else "The relative field index is for visual comparison only; it is not a measured field in tesla."))
            st.markdown("**" + ("ਵੱਖ-ਵੱਖ ਵੋਲਟੇਜਾਂ ਲਈ ਗਣਨਾ" if is_pa_wire10 else "Calculated observations at different voltages") + "**")
            wire_rows10 = []
            for v_wire10 in (6, 12, 18, 24):
                i_wire10 = v_wire10 / resistance if closed else 0.0
                wire_rows10.append({"V (V)": v_wire10, "R (Ω)": resistance, "I = V/R (A)": round(i_wire10, 2), "Relative index": round(i_wire10 * 10.0, 2)})
            st.dataframe(wire_rows10, use_container_width=True, hide_index=True)
            if not closed:
                st.info("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੈ: ਕਰੰਟ ਨਹੀਂ ਵਗਦਾ, ਇਸ ਲਈ ਕਰੰਟ ਕਾਰਨ ਚੁੰਬਕੀ ਖੇਤਰ ਨਹੀਂ ਬਣਦਾ।" if is_pa_wire10 else "Switch open: no current flows, so there is no current-induced magnetic field.")
            st.caption(("ਆਦਰਸ਼ ਵਰਚੁਅਲ ਸਿਮੂਲੇਸ਼ਨ; ਅਸਲ ਮੈਦਾਨੀ ਤਾਕਤ ਤਾਰ ਤੋਂ ਦੂਰੀ ਅਤੇ ਹੋਰ ਹਾਲਾਤਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ।" if is_pa_wire10 else "Ideal virtual simulation; actual field strength also depends on distance from the wire and other conditions."))
        elif kind == "magnetic_field":
            if selected_class == 7 and exp_index == 4:
                is_pa_field = st.session_state.language != "en"
                field_color = "#2563eb" if closed else "#94a3b8"
                needle_angle = "25" if closed else "0"
                current_label = (
                    ("ਕਰੰਟ ਚਾਲੂ ਹੈ — ਚੁੰਬਕੀ ਖੇਤਰ ਮੌਜੂਦ ਹੈ" if closed else "ਕਰੰਟ ਬੰਦ ਹੈ — ਤਾਰ ਦਾ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ ਨਹੀਂ")
                    if is_pa_field else
                    ("CURRENT ON — MAGNETIC FIELD PRESENT" if closed else "CURRENT OFF — NO CURRENT-INDUCED FIELD")
                )
                field_paths = (
                    '<g fill="none" stroke="' + field_color + '" stroke-width="2.5">'
                    '<ellipse cx="205" cy="120" rx="42" ry="62"/><ellipse cx="205" cy="120" rx="61" ry="84"/><ellipse cx="205" cy="120" rx="81" ry="108"/>'
                    '</g>'
                    '<g fill="' + field_color + '"><path d="M244 85 l-9 -2 l5 8 Z"/><path d="M164 155 l9 2 l-5 -8 Z"/><path d="M258 120 l-8 -5 l0 10 Z"/></g>'
                    if closed else
                    '<g fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 6" opacity=".4"><ellipse cx="205" cy="120" rx="42" ry="62"/><ellipse cx="205" cy="120" rx="61" ry="84"/></g>'
                )
                compass_needle = (
                    '<g transform="rotate(' + needle_angle + ' 112 120)"><path d="M112 94 L105 122 L112 116 L119 122 Z" fill="#dc2626"/><path d="M112 146 L105 118 L112 124 L119 118 Z" fill="#334155"/></g>'
                    if closed else
                    '<g><path d="M112 94 L105 122 L112 116 L119 122 Z" fill="#dc2626"/><path d="M112 146 L105 118 L112 124 L119 118 Z" fill="#334155"/></g>'
                )
                field_svg = (
                    '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">'
                    '<svg viewBox="0 0 420 250" width="100%" role="img" aria-label="Magnetic effect of current shown with a current-carrying wire, circular magnetic field lines and a compass needle">'
                    + field_paths +
                    '<path d="M205 28 V211" stroke="' + ("#16a34a" if closed else "#94a3b8") + '" stroke-width="7" stroke-linecap="round"/>'
                    + ('<path d="M196 48 L205 30 L214 48" fill="none" stroke="#16a34a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>' if closed else '') +
                    '<circle cx="112" cy="120" r="39" fill="#f8fafc" stroke="#64748b" stroke-width="3"/>'
                    + compass_needle +
                    '<circle cx="112" cy="120" r="4" fill="#0f172a"/>'
                    '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="205" y="18">' + ("ਕਰੰਟ ਵਾਲੀ ਤਾਰ" if is_pa_field else "CURRENT-CARRYING WIRE") + '</text><text x="112" y="177">' + ("ਕੰਪਾਸ" if is_pa_field else "COMPASS") + '</text><text x="205" y="238">' + ("ਚੁੰਬਕੀ ਖੇਤਰ ਦੀਆਂ ਰੇਖਾਵਾਂ" if is_pa_field else "MAGNETIC FIELD LINES") + '</text></g>'
                    '</svg></div>'
                )
                st.markdown("#### " + ("ਕਰੰਟ ਦਾ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ" if is_pa_field else "Magnetic effect of electric current"))
                st.markdown(field_svg, unsafe_allow_html=True)
                if closed:
                    st.success(current_label)
                else:
                    st.info(current_label)
                st.write("💡 " + note)
                st.caption("ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਵਰਚੁਅਲ ਮਾਡਲ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮਾਪ ਨਹੀਂ।" if is_pa_field else "Qualitative virtual model only — no numerical measurements.")
            else:
                st.write(note)
        elif kind == "liquids":
            # Class 8 Experiment 1: qualitative circuit with beaker, two electrodes,
            # connecting wires, a cell and a bulb. No numeric values are displayed.
            is_pa_liquid = st.session_state.language != "en"
            conducts = liquid in ("salt", "lemon")
            bulb_glow = "filter: drop-shadow(0 0 13px #facc15);" if conducts else ""
            bulb_fill = "#fde047" if conducts else "#e2e8f0"
            wire_color = "#16a34a" if conducts else "#64748b"
            liquid_color = {"water": "#bae6fd", "salt": "#7dd3fc", "sugar": "#bfdbfe", "lemon": "#fde68a"}[liquid]
            liquid_label = {
                "water": ("Distilled water" if not is_pa_liquid else "ਡਿਸਟਿਲਡ ਪਾਣੀ"),
                "salt": ("Salt solution" if not is_pa_liquid else "ਨਮਕ ਦਾ ਘੋਲ"),
                "sugar": ("Sugar solution" if not is_pa_liquid else "ਚੀਨੀ ਦਾ ਘੋਲ"),
                "lemon": ("Lemon juice" if not is_pa_liquid else "ਨਿੰਬੂ ਦਾ ਰਸ"),
            }[liquid]
            state_text = (
                ("ਬਲਬ ਜਗ ਰਿਹਾ ਹੈ — ਘੋਲ ਵਿੱਚ ਮੌਜੂਦ ਆਇਨ ਕਰੰਟ ਲੰਘਾਉਂਦੇ ਹਨ।" if is_pa_liquid else "Bulb glows — mobile ions in the solution allow current to pass.")
                if conducts else
                ("ਬਲਬ ਨਹੀਂ ਜਗਦਾ — ਇਸ ਮਾਡਲ ਵਿੱਚ ਕਰੰਟ ਬਹੁਤ ਘੱਟ ਹੈ।" if is_pa_liquid else "Bulb stays off — in this model, current is too small to light it.")
            )
            liquid_svg = f"""
<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 460 300" width="100%" role="img" aria-label="Virtual circuit with cell, wires, glowing or unlit bulb, and electrodes dipped into a beaker of selected liquid">
  <defs><linearGradient id="beakerGlass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#bae6fd" stop-opacity=".35"/><stop offset=".5" stop-color="#e0f2fe" stop-opacity=".12"/><stop offset="1" stop-color="#7dd3fc" stop-opacity=".35"/></linearGradient></defs>
  <path d="M65 205 V55 H175" fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M285 55 H395 V205" fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="128" y="35" width="54" height="40" rx="7" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <line x1="143" y1="55" x2="154" y2="55" stroke="#1e3a8a" stroke-width="3"/>
  <line x1="148.5" y1="49" x2="148.5" y2="61" stroke="#1e3a8a" stroke-width="3"/>
  <line x1="160" y1="55" x2="171" y2="55" stroke="#1e3a8a" stroke-width="3"/>
  <text x="155" y="25" fill="currentColor" font-size="12" text-anchor="middle">{'ਸੈੱਲ' if is_pa_liquid else 'CELL'}</text>
  <path d="M175 55 H207" fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round"/>
  <path d="M253 55 H285" fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round"/>
  <circle cx="230" cy="55" r="24" fill="{bulb_fill}" stroke="#475569" stroke-width="3" style="{bulb_glow}"/>
  <path d="M218 53 l7 -7 l10 16 l7 -7" fill="none" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
  <path d="M220 77 V84 H240 V77" fill="none" stroke="#475569" stroke-width="4" stroke-linecap="round"/>
  <text x="230" y="111" fill="currentColor" font-size="12" text-anchor="middle">{'ਬਲਬ' if is_pa_liquid else 'BULB'}</text>
  <path d="M65 205 V224 H145" fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round"/>
  <path d="M315 224 H395 V205" fill="none" stroke="{wire_color}" stroke-width="5" stroke-linecap="round"/>
  <path d="M145 224 H315" fill="none" stroke="{wire_color}" stroke-width="4" stroke-dasharray="6 6" opacity=".55"/>
  <path d="M145 145 L145 238 Q145 255 162 255 H298 Q315 255 315 238 V145" fill="url(#beakerGlass)" stroke="#0284c7" stroke-width="3"/>
  <path d="M149 185 Q175 179 200 185 T250 185 T311 185 V238 Q311 251 297 251 H163 Q149 251 149 238 Z" fill="{liquid_color}" opacity=".9"/>
  <path d="M145 185 Q175 179 200 185 T250 185 T315 185" fill="none" stroke="#0284c7" stroke-width="2"/>
  <path d="M185 123 V216" stroke="#475569" stroke-width="7" stroke-linecap="round"/>
  <path d="M275 123 V216" stroke="#475569" stroke-width="7" stroke-linecap="round"/>
  <circle cx="185" cy="216" r="5" fill="#94a3b8"/><circle cx="275" cy="216" r="5" fill="#94a3b8"/>
  <text x="230" y="279" fill="currentColor" font-size="13" text-anchor="middle" font-weight="600">{liquid_label}</text>
  <text x="65" y="245" fill="currentColor" font-size="11" text-anchor="middle">{'ਤਾਰ' if is_pa_liquid else 'WIRE'}</text>
</svg></div>"""
            st.markdown("#### " + ("ਤਰਲ ਦੀ ਚਾਲਕਤਾ ਵਾਲਾ ਸਰਕਟ" if is_pa_liquid else "Liquid conductivity circuit"))
            st.markdown(liquid_svg, unsafe_allow_html=True)
            if conducts:
                st.success(state_text)
            else:
                st.info(state_text)
            st.write("💡 " + note)
            st.caption("Qualitative virtual model only — no numerical measurements." if not is_pa_liquid else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਵਰਚੁਅਲ ਮਾਡਲ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮਾਪ ਨਹੀਂ।")
        elif kind == "electrolysis":
            is_pa_electrolysis = st.session_state.language != "en"
            active_solution = electrolysis_solution
            has_effect = active_solution != "distilled"
            strong_effect = active_solution == "copper"
            liquid_fill = "#60a5fa" if strong_effect else ("#fef3c7" if active_solution == "lemon" else "#dbeafe")
            liquid_stroke = "#2563eb" if strong_effect else "#d97706"
            bubble_svg = (
                '<g fill="none" stroke="#e0f2fe" stroke-width="3">'
                '<circle cx="175" cy="155" r="5"/><circle cx="190" cy="132" r="4"/><circle cx="180" cy="115" r="3"/>'
                '<circle cx="258" cy="150" r="5"/><circle cx="245" cy="128" r="4"/><circle cx="255" cy="108" r="3"/>'
                '</g>'
                if has_effect else ""
            )
            deposit_svg = (
                '<path d="M244 91 L244 177 Q244 183 250 183 L264 183 Q270 183 270 177 L270 91 Z" fill="#b87333" opacity=".95"/>'
                if strong_effect else ""
            )
            effect_label = (
                ("ਕੈਥੋਡ ਉੱਤੇ ਤਾਂਬੇ ਦੀ ਪਰਤ ਅਤੇ ਬੁਲਬੁਲੇ" if is_pa_electrolysis else "Copper coating at cathode and bubbles")
                if strong_effect else
                (("ਹਲਕਾ ਰਸਾਇਣਕ ਪ੍ਰਭਾਵ" if is_pa_electrolysis else "Weak visible effect") if active_solution == "lemon" else
                 ("ਸਪਸ਼ਟ ਪ੍ਰਭਾਵ ਨਹੀਂ" if is_pa_electrolysis else "No clear visible effect"))
            )
            electrolysis_svg = f"""
<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035);">
<svg viewBox="0 0 440 300" width="100%" role="img" aria-label="Qualitative electrolysis beaker with two electrodes connected to a cell">
  <g stroke-linecap="round" stroke-linejoin="round">
    <path d="M105 85 V224 Q105 245 128 245 H312 Q335 245 335 224 V85" fill="none" stroke="#64748b" stroke-width="5"/>
    <path d="M110 145 H330 V224 Q330 240 310 240 H130 Q110 240 110 224 Z" fill="{liquid_fill}" opacity=".8"/>
    <path d="M110 145 H330" stroke="{liquid_stroke}" stroke-width="3" stroke-dasharray="7 5"/>
    <path d="M170 55 V190" stroke="#475569" stroke-width="12"/>
    <path d="M255 55 V190" stroke="#475569" stroke-width="12"/>
    <path d="M170 55 V30 H255 V55" fill="none" stroke="#dc2626" stroke-width="4"/>
    <path d="M212 30 V18" stroke="#dc2626" stroke-width="4"/>
    <rect x="190" y="8" width="44" height="28" rx="5" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
    <text x="212" y="27" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">CELL</text>
    {bubble_svg}
    {deposit_svg}
  </g>
  <g fill="currentColor" font-size="13" font-weight="600" text-anchor="middle">
    <text x="170" y="205">{'ਐਨੋਡ (+)' if is_pa_electrolysis else 'ANODE (+)'}</text>
    <text x="255" y="205">{'ਕੈਥੋਡ (−)' if is_pa_electrolysis else 'CATHODE (−)'}</text>
    <text x="220" y="275">{'ਘੋਲ' if is_pa_electrolysis else 'SOLUTION'}</text>
  </g>
</svg>
</div>
"""
            st.markdown("#### " + ("ਇਲੈਕਟ੍ਰੋਲਾਈਸਿਸ ਦਾ ਵਰਚੁਅਲ ਮਾਡਲ" if is_pa_electrolysis else "Virtual electrolysis model"))
            st.markdown(electrolysis_svg, unsafe_allow_html=True)
            if strong_effect:
                st.success(effect_label)
            elif has_effect:
                st.info(effect_label)
            else:
                st.warning(effect_label)
            st.write("💡 " + note)
            st.caption("Qualitative illustration only — effects depend on solution and electrode material; no numerical readings." if not is_pa_electrolysis else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਚਿੱਤਰ — ਪ੍ਰਭਾਵ ਘੋਲ ਅਤੇ ਇਲੈਕਟ੍ਰੋਡ ਦੇ ਪਦਾਰਥ ਉੱਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ; ਕੋਈ ਸੰਖਿਆਤਮਕ ਮਾਪ ਨਹੀਂ।")
        elif kind == "electroplating":
            is_pa_plate = st.session_state.language != "en"
            plate_options = ["copper", "silver", "nickel"]
            plate_labels = {
                "copper": "ਤਾਂਬੇ ਦੀ ਪਰਤ" if is_pa_plate else "Copper coating",
                "silver": "ਚਾਂਦੀ ਦੀ ਪਰਤ" if is_pa_plate else "Silver coating",
                "nickel": "ਨਿੱਕਲ ਦੀ ਪਰਤ" if is_pa_plate else "Nickel coating",
            }
            coating_metal = st.selectbox(
                "ਕਿਹੜੀ ਧਾਤ ਦੀ ਪਰਤ?" if is_pa_plate else "Choose coating metal",
                plate_options,
                format_func=lambda x: plate_labels[x],
                key=f"electroplate_metal_{st.session_state.language}",
            )
            coating_colors = {"copper": "#c87941", "silver": "#dbe4ee", "nickel": "#94a3b8"}
            coating_color = coating_colors[coating_metal]
            metal_name = plate_labels[coating_metal]
            # Illustrative cross-section: a base object receives a thin deposited metal layer.
            plating_svg = f"""
<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035);">
<svg viewBox="0 0 440 310" width="100%" role="img" aria-label="Electroplating illustration showing a metal coating depositing onto an object in an electrolyte bath">
  <defs>
    <linearGradient id="bath" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#bfdbfe" stop-opacity=".8"/>
      <stop offset="100%" stop-color="#60a5fa" stop-opacity=".45"/>
    </linearGradient>
    <linearGradient id="baseMetal" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#64748b"/>
      <stop offset="100%" stop-color="#334155"/>
    </linearGradient>
  </defs>
  <g stroke-linecap="round" stroke-linejoin="round">
    <path d="M62 95 V238 Q62 258 84 258 H356 Q378 258 378 238 V95" fill="none" stroke="#64748b" stroke-width="5"/>
    <path d="M67 130 H373 V237 Q373 253 354 253 H86 Q67 253 67 237 Z" fill="url(#bath)"/>
    <path d="M67 130 H373" stroke="#2563eb" stroke-width="3" stroke-dasharray="7 5"/>
    <path d="M132 54 V191" stroke="#c87941" stroke-width="13"/>
    <path d="M132 54 V28 H309 V54" fill="none" stroke="#dc2626" stroke-width="4"/>
    <path d="M309 54 V191" stroke="#64748b" stroke-width="13"/>
    <rect x="185" y="15" width="70" height="27" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="2"/>
    <text x="220" y="33" fill="#0f172a" font-size="12" font-weight="700" text-anchor="middle">CELL</text>
    <path d="M132 28 H185 M255 28 H309" stroke="#dc2626" stroke-width="4"/>
    <text x="132" y="48" fill="currentColor" font-size="12" text-anchor="middle">{'ਐਨੋਡ (+)' if is_pa_plate else 'ANODE (+)'}</text>
    <text x="309" y="48" fill="currentColor" font-size="12" text-anchor="middle">{'ਕੈਥੋਡ (−)' if is_pa_plate else 'CATHODE (−)'}</text>
    <g fill="{coating_color}" stroke="#475569" stroke-width="2">
      <path d="M196 179 L196 211 Q196 225 210 225 H270 Q284 225 284 211 V179 Q284 169 274 169 H206 Q196 169 196 179 Z"/>
    </g>
    <g fill="url(#baseMetal)" stroke="#1e293b" stroke-width="2">
      <path d="M204 184 L204 207 Q204 216 214 216 H266 Q276 216 276 207 V184 Q276 177 268 177 H212 Q204 177 204 184 Z"/>
    </g>
    <g fill="{coating_color}" stroke="{coating_color}" stroke-width="2">
      <circle cx="184" cy="160" r="4"/><circle cx="195" cy="150" r="3"/><circle cx="285" cy="155" r="4"/>
      <circle cx="294" cy="167" r="3"/><circle cx="175" cy="176" r="3"/><circle cx="304" cy="182" r="3"/>
    </g>
    <path d="M174 174 Q190 188 196 191 M306 174 Q291 188 284 191" fill="none" stroke="{coating_color}" stroke-width="3" stroke-dasharray="4 4"/>
    <path d="M284 196 L333 183" stroke="currentColor" stroke-width="1.5" fill="none"/>
    <text x="335" y="180" fill="currentColor" font-size="11">{'ਪਰਤ' if is_pa_plate else 'Coating'}</text>
    <path d="M220 235 V270" stroke="currentColor" stroke-width="1.5"/>
    <text x="220" y="286" fill="currentColor" font-size="12" text-anchor="middle">{'ਮੂਲ ਧਾਤ ਦੀ ਵਸਤੂ' if is_pa_plate else 'Base metal object'}</text>
    <text x="220" y="302" fill="currentColor" font-size="11" text-anchor="middle">{'ਉੱਤੇ ਜਮਦੀ ਹੈ: ' if is_pa_plate else 'Deposited layer: '}{metal_name}</text>
  </g>
</svg>
</div>
"""
            st.markdown("#### " + ("ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਦਾ ਵਰਚੁਅਲ ਮਾਡਲ" if is_pa_plate else "Virtual electroplating model"))
            st.markdown(plating_svg, unsafe_allow_html=True)
            st.success(
                ("ਚੁਣੀ ਧਾਤ ਦੀ ਪਤਲੀ ਪਰਤ ਵਸਤੂ ਉੱਤੇ ਜਮਦੀ ਦਿਖਾਈ ਗਈ ਹੈ।" if is_pa_plate else "A thin layer of the selected metal is shown depositing onto the object.")
            )
            st.write("💡 " + note)
            st.caption(
                "Qualitative illustration only — actual plating depends on the electrolyte, electrode materials and current; no numerical readings."
                if not is_pa_plate else
                "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਚਿੱਤਰ — ਅਸਲ ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਘੋਲ, ਇਲੈਕਟ੍ਰੋਡ ਦੇ ਪਦਾਰਥ ਅਤੇ ਕਰੰਟ ਉੱਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ; ਕੋਈ ਸੰਖਿਆਤਮਕ ਮਾਪ ਨਹੀਂ।"
            )
        elif kind == "cell" and selected_class == 8 and exp_index == 4:  # LIVE-DEPLOY-VERIFY-2026-10-21
            # Class 8 Experiment 5: qualitative cell animation with no numerical readings.
            is_pa_cell = st.session_state.language != "en"
            active = closed
            wire_color = "#16a34a" if active else "#94a3b8"
            bulb_fill = "#fde047" if active else "#e2e8f0"
            bulb_glow = "filter: drop-shadow(0 0 12px #facc15);" if active else ""
            current_arrows = (
                '<g fill="#16a34a"><path d="M120 52 l-10 -6 l0 12 Z"/><path d="M330 52 l10 -6 l0 12 Z"/><path d="M330 222 l10 -6 l0 12 Z"/></g>'
                if active else ""
            )
            switch_link = (
                '<path d="M198 52 H242" stroke="#16a34a" stroke-width="5" stroke-linecap="round"/>'
                if active else
                '<path d="M198 52 L236 32" stroke="#dc2626" stroke-width="5" stroke-linecap="round"/>'
            )
            status = (
                ("ਸਵਿੱਚ ਬੰਦ — ਕਰੰਟ ਵਹਿੰਦਾ ਹੈ ਅਤੇ ਬਲਬ ਜਗਦਾ ਹੈ" if active else "ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ — ਕਰੰਟ ਰੁਕਦਾ ਹੈ ਅਤੇ ਬਲਬ ਬੁੱਝਦਾ ਹੈ")
                if is_pa_cell else
                ("SWITCH CLOSED — CURRENT FLOWS AND BULB GLOWS" if active else "SWITCH OPEN — CURRENT STOPS AND BULB IS OFF")
            )
            cell_svg = (
                '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035);">'
                '<svg viewBox="0 0 440 285" width="100%" role="img" aria-label="Qualitative cell circuit showing chemical energy converted into electrical energy, with a switch and bulb">'
                '<g fill="none" stroke="' + wire_color + '" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M100 52 V116"/><path d="M100 135 V222"/><path d="M100 52 H175"/><path d="M242 52 H340 V108"/><path d="M340 155 V222 H100"/>'
                '</g>'
                + current_arrows +
                '<g stroke="#334155" stroke-width="3"><line x1="78" y1="116" x2="122" y2="116"/><line x1="87" y1="135" x2="113" y2="135"/></g>'
                '<text x="100" y="170" fill="currentColor" font-size="12" text-anchor="middle">' + ("ਸੈੱਲ" if is_pa_cell else "CELL") + '</text>'
                '<circle cx="340" cy="132" r="23" fill="' + bulb_fill + '" stroke="#475569" stroke-width="3" style="' + bulb_glow + '"/>'
                '<path d="M328 130 l8 -8 l9 17 l8 -8" fill="none" stroke="#475569" stroke-width="3" stroke-linecap="round"/>'
                '<path d="M330 157 V164 H350 V157" fill="none" stroke="#475569" stroke-width="4"/>'
                '<text x="340" y="187" fill="currentColor" font-size="12" text-anchor="middle">' + ("ਬਲਬ" if is_pa_cell else "BULB") + '</text>'
                '<circle cx="190" cy="52" r="5" fill="#475569"/><circle cx="242" cy="52" r="5" fill="#475569"/>'
                + switch_link +
                '<text x="216" y="20" fill="currentColor" font-size="12" text-anchor="middle">' + ("ਸਵਿੱਚ" if is_pa_cell else "SWITCH") + '</text>'
                '<rect x="137" y="238" width="166" height="34" rx="9" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>'
                '<text x="220" y="259" fill="#1e3a8a" font-size="12" font-weight="700" text-anchor="middle">' + ("ਰਸਾਇਣਕ ਊਰਜਾ → ਬਿਜਲੀ ਊਰਜਾ" if is_pa_cell else "CHEMICAL ENERGY → ELECTRICAL ENERGY") + '</text>'
                '</svg></div>'
            )
            st.markdown("#### " + ("ਸੈੱਲ ਦਾ ਵਰਚੁਅਲ ਸਰਕਟ" if is_pa_cell else "Virtual cell circuit"))
            st.markdown(cell_svg, unsafe_allow_html=True)
            if active:
                st.success(status)
            else:
                st.info(status)
            st.write("💡 " + note)
            st.caption(
                "Qualitative visual model only — a cell converts chemical energy into electrical energy; no numerical readings."
                if not is_pa_cell else
                "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ ਮਾਡਲ — ਸੈੱਲ ਰਸਾਇਣਕ ਊਰਜਾ ਨੂੰ ਬਿਜਲੀ ਊਰਜਾ ਵਿੱਚ ਬਦਲਦਾ ਹੈ; ਕੋਈ ਸੰਖਿਆਤਮਕ ਮਾਪ ਨਹੀਂ।"
            )
        elif kind == "cell":
            st.metric(tr("voltage"), f"{voltage} V")
            st.write(note)
        elif kind == "charge" and selected_class == 9 and exp_index == 4:
            # Class 9 Experiment 5: static electricity with interactive rubbing and target selection.
            is_pa_static = st.session_state.language != "en"
            balloon_color = "#e879f9" if static_charge_active else "#cbd5e1"
            attraction_color = "#0ea5e9" if static_charge_active else "#94a3b8"
            if static_target == "paper":
                target_visual = (
                    '<g fill="#fef3c7" stroke="#b45309" stroke-width="1.5">'
                    '<path d="M265 147 l18 -7 8 16 -17 6 Z"/><path d="M298 160 l17 -4 5 15 -19 4 Z"/>'
                    '<path d="M278 179 l15 -8 9 13 -16 8 Z"/><path d="M314 190 l13 -5 6 12 -15 5 Z"/></g>'
                    if static_charge_active else
                    '<g fill="#fde047" stroke="#92400e" stroke-width="2.5">'
                    '<path d="M260 151 l22 -9 10 19 -20 8 Z"/>'
                    '<path d="M294 166 l21 -6 7 18 -22 6 Z"/>'
                    '<path d="M270 190 l20 -10 11 17 -21 10 Z"/>'
                    '<path d="M311 198 l17 -7 8 15 -18 7 Z"/>'
                    '<path d="M287 213 l16 -6 7 12 -17 7 Z"/></g>'
                )
                target_label = "ਕਾਗਜ਼ ਦੇ ਟੁਕੜੇ" if is_pa_static else "Paper pieces"
            else:
                target_visual = (
                    '<path d="M302 112 C310 132 314 145 324 164 C333 183 335 198 341 210" fill="none" stroke="#38bdf8" stroke-width="8" stroke-linecap="round"/>'
                    '<path d="M302 112 C310 132 314 145 324 164 C333 183 335 198 341 210" fill="none" stroke="#e0f2fe" stroke-width="2" stroke-linecap="round"/>'
                    if static_charge_active else
                    '<path d="M330 112 V210" fill="none" stroke="#38bdf8" stroke-width="8" stroke-linecap="round"/>'
                )
                target_label = "ਪਾਣੀ ਦੀ ਧਾਰ" if is_pa_static else "Water stream"
            attraction_arrows = (
                '<path d="M245 142 Q260 151 269 163 M260 151 l9 12 -14 -1" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                if static_charge_active and static_target == "paper" else
                '<path d="M244 155 Q270 157 298 158 M286 151 l12 7 -12 5" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                if static_charge_active else ""
            )
            static_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 440 280" width="100%" role="img" aria-label="Interactive static electricity demonstration with a rubbed balloon attracting paper pieces or bending a thin stream of water">
  <defs><radialGradient id="staticBalloonGlow"><stop offset="0%" stop-color="#fff" stop-opacity=".45"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>
  <path d="M28 236 H412" stroke="#94a3b8" stroke-width="2" opacity=".6"/>
  <g stroke="#a16207" stroke-width="3" stroke-linecap="round"><path d="M77 55 q-14 22 0 39"/><path d="M96 47 q-14 22 0 39"/><path d="M115 55 q-14 22 0 39"/></g>
  <text x="94" y="32" fill="currentColor" font-size="12" text-anchor="middle">{("ਵਾਲ / ਉੱਨ" if is_pa_static else "Hair / wool")}</text>
  <ellipse cx="205" cy="116" rx="47" ry="59" fill="{balloon_color}" stroke="#fff" stroke-width="3"/>
  <ellipse cx="205" cy="116" rx="44" ry="56" fill="url(#staticBalloonGlow)"/>
  <path d="M198 174 l7 10 7 -10 Z" fill="{balloon_color}" stroke="#fff" stroke-width="1.5"/>
  <path d="M205 184 Q217 203 207 224" fill="none" stroke="#64748b" stroke-width="2"/>
  <text x="205" y="119" font-size="14" font-weight="700" fill="#4a044e" text-anchor="middle">{("ਚਾਰਜਡ ਗੁਬਾਰਾ" if static_charge_active else "ਬਿਨਾਂ ਰਗੜਿਆ ਗੁਬਾਰਾ") if is_pa_static else ("Charged balloon" if static_charge_active else "Unrubbed balloon")}</text>
  {attraction_arrows}
  {target_visual}
  <text x="328" y="86" fill="currentColor" font-size="12" text-anchor="middle">{target_label}</text>
  <text x="220" y="263" fill="{attraction_color}" font-size="13" font-weight="700" text-anchor="middle">{("ਖਿੱਚ ਦਿਖਾਈ ਦੇ ਰਹੀ ਹੈ" if static_charge_active else "ਰਗੜੋ ਤਾਂ ਪ੍ਰਭਾਵ ਵੇਖੋ") if is_pa_static else ("Electrostatic attraction shown" if static_charge_active else "Rub the balloon to observe the effect")}</text>
</svg></div>"""
            st.markdown("#### " + ("ਸਥਿਰ ਬਿਜਲੀ ਦਾ ਇੰਟਰਐਕਟਿਵ ਮਾਡਲ" if is_pa_static else "Interactive static electricity model"))
            st.markdown(static_svg, unsafe_allow_html=True)
            if static_charge_active:
                st.success("ਚਾਰਜ ਕੀਤਾ ਗੁਬਾਰਾ ਹਲਕੇ ਕਾਗਜ਼ ਨੂੰ ਖਿੱਚ ਸਕਦਾ ਹੈ। ਪਾਣੀ ਦੀ ਪਤਲੀ ਧਾਰ ਵੀ ਮੁੜ ਸਕਦੀ ਹੈ।" if is_pa_static else "A charged balloon can attract light paper. A thin stream of water can also bend.")
            else:
                st.info("ਗੁਬਾਰੇ ਨੂੰ ਵਾਲਾਂ ਜਾਂ ਉੱਨ ਨਾਲ ਰਗੜ ਕੇ ਮੁੜ ਵੇਖੋ।" if is_pa_static else "Rub the balloon on hair or wool and observe again.")
            st.caption("ਗੁਣਾਤਮਕ ਮਾਡਲ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮੁੱਲ ਜਾਂ ਮਾਪ ਨਹੀਂ।" if is_pa_static else "Qualitative model only — no numerical values or measurements.")
            st.write("💡 " + note)
        elif kind == "charge" and selected_class == 9 and exp_index == 0:
            # Class 9 Experiment 1: qualitative electric-charge interaction visual; no numerical values.
            is_pa_charge = st.session_state.language != "en"
            like_charges = charge_pair_mode != "unlike"
            left_charge = "-" if charge_pair_mode == "like_negative" else "+"
            right_charge = "-" if charge_pair_mode == "like_negative" else ("-" if charge_pair_mode == "unlike" else "+")
            particle_color_left = "#2563eb" if left_charge == "-" else "#dc2626"
            particle_color_right = "#2563eb" if right_charge == "-" else "#dc2626"
            interaction_color = "#d97706" if like_charges else "#16a34a"
            left_motion = '<path d="M145 130 L105 130 M116 119 L105 130 L116 141" fill="none" stroke="#d97706" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' if like_charges else '<path d="M145 130 L180 130 M169 119 L180 130 L169 141" fill="none" stroke="#16a34a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
            right_motion = '<path d="M295 130 L335 130 M324 119 L335 130 L324 141" fill="none" stroke="#d97706" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>' if like_charges else '<path d="M295 130 L260 130 M271 119 L260 130 L271 141" fill="none" stroke="#16a34a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
            interaction_title = (
                ("ਇੱਕੋ ਕਿਸਮ ਦੇ ਚਾਰਜ ਇੱਕ-ਦੂਜੇ ਨੂੰ ਦੂਰ ਧੱਕਦੇ ਹਨ" if is_pa_charge else "Like charges repel each other")
                if like_charges else
                ("ਵੱਖਰੀ ਕਿਸਮ ਦੇ ਚਾਰਜ ਇੱਕ-ਦੂਜੇ ਨੂੰ ਖਿੱਚਦੇ ਹਨ" if is_pa_charge else "Unlike charges attract each other")
            )
            charge_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035)">
<svg viewBox="0 0 440 245" width="100%" role="img" aria-label="Electric charge interaction showing like charges repelling and unlike charges attracting">
  <defs><radialGradient id="chargeGlow"><stop offset="0%" stop-color="#ffffff" stop-opacity=".45"/><stop offset="100%" stop-color="#ffffff" stop-opacity="0"/></radialGradient></defs>
  <path d="M32 205 H408" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 7" opacity=".55"/>
  {left_motion}{right_motion}
  <circle cx="145" cy="130" r="43" fill="{particle_color_left}" stroke="#ffffff" stroke-width="3"/>
  <circle cx="145" cy="130" r="42" fill="url(#chargeGlow)"/>
  <circle cx="295" cy="130" r="43" fill="{particle_color_right}" stroke="#ffffff" stroke-width="3"/>
  <circle cx="295" cy="130" r="42" fill="url(#chargeGlow)"/>
  <text x="145" y="143" font-size="42" font-weight="bold" fill="white" text-anchor="middle">{left_charge}</text>
  <text x="295" y="143" font-size="42" font-weight="bold" fill="white" text-anchor="middle">{right_charge}</text>
  <text x="145" y="75" font-size="13" fill="currentColor" text-anchor="middle">{"ਚਾਰਜ" if is_pa_charge else "CHARGE"}</text>
  <text x="295" y="75" font-size="13" fill="currentColor" text-anchor="middle">{"ਚਾਰਜ" if is_pa_charge else "CHARGE"}</text>
  <text x="220" y="32" font-size="15" font-weight="700" fill="{interaction_color}" text-anchor="middle">{("ਵਿਕਰਸ਼ਣ" if is_pa_charge else "REPULSION") if like_charges else ("ਆਕਰਸ਼ਣ" if is_pa_charge else "ATTRACTION")}</text>
  <text x="220" y="231" font-size="12" fill="currentColor" text-anchor="middle">{("ਦਿਸ਼ਾਵਾਂ ਦਿਖਾਉਂਦੀਆਂ ਹਨ ਕਿ ਚਾਰਜ ਕਿਵੇਂ ਹਿਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਨ" if is_pa_charge else "Arrows show the direction the charges tend to move")}</text>
</svg></div>"""
            st.markdown("#### " + ("ਬਿਜਲਈ ਚਾਰਜਾਂ ਦਾ ਪਰਸਪਰ ਪ੍ਰਭਾਵ" if is_pa_charge else "Interaction between electric charges"))
            st.markdown(charge_svg, unsafe_allow_html=True)
            if like_charges:
                st.warning(interaction_title)
            else:
                st.success(interaction_title)
            st.markdown("**" + ("ਯਾਦ ਰੱਖੋ" if is_pa_charge else "Remember") + "**")
            st.write(("ਇੱਕੋ ਕਿਸਮ ਦੇ ਚਾਰਜ ਵਿਕਰਸ਼ਣ ਕਰਦੇ ਹਨ; ਵੱਖਰੀ ਕਿਸਮ ਦੇ ਚਾਰਜ ਆਕਰਸ਼ਣ ਕਰਦੇ ਹਨ।" if is_pa_charge else "Like charges repel; unlike charges attract."))
            st.caption("Qualitative visual model only — no numerical values or measurements." if not is_pa_charge else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ ਮਾਡਲ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮੁੱਲ ਜਾਂ ਮਾਪ ਨਹੀਂ।")
            st.write("💡 " + note)
        elif kind == "charge":
            st.write(note)
        elif kind == "fuse":
            is_pa_fuse = st.session_state.language != "en"
            fuse_rating = 2.0
            circuit_current = 0.0 if fuse_blown else current
            st.markdown("#### " + ("ਫਿਊਜ਼ ਵਾਲਾ ਸਰਕਟ" if is_pa_fuse else "Circuit with a fuse"))
            fuse_wire = "#dc2626" if fuse_blown else "#16a34a"
            bulb_fill = "#e2e8f0" if fuse_blown else "#fde047"
            bulb_glow = "" if fuse_blown else "filter: drop-shadow(0 0 10px #facc15);"
            fuse_link = (
                '<path d="M174 50 H195 M215 50 H235" stroke="#dc2626" stroke-width="4" fill="none" stroke-linecap="round"/>'
                '<path d="M196 43 L202 50 L198 57 M208 43 L214 50 L210 57" stroke="#dc2626" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
                if fuse_blown else
                '<rect x="174" y="39" width="61" height="22" rx="5" fill="#bbf7d0" stroke="#15803d" stroke-width="2"/><line x1="182" y1="50" x2="227" y2="50" stroke="#15803d" stroke-width="3"/>'
            )
            fuse_status = ("ਫਿਊਜ਼ ਪਿਘਲ ਗਿਆ — ਸਰਕਟ ਟੁੱਟ ਗਿਆ" if fuse_blown else "ਫਿਊਜ਼ ਸਹੀ ਹੈ — ਕਰੰਟ ਵਹਿ ਰਿਹਾ ਹੈ") if is_pa_fuse else ("FUSE BLOWN — CIRCUIT BROKEN" if fuse_blown else "FUSE INTACT — CURRENT FLOWS")
            circuit_svg = (
                '<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">'
                '<svg viewBox="0 0 420 220" width="100%" role="img" aria-label="Virtual low-voltage circuit with a fuse that opens under excessive current">'
                '<g fill="none" stroke="' + fuse_wire + '" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M70 50 H174"/><path d="M235 50 H320 V78"/>' +
                '<path d="M320 122 V166 H70 V116"/><path d="M70 50 V78"/>'
                '</g>'
                '<g stroke="#334155" stroke-width="3" fill="none"><line x1="51" y1="80" x2="89" y2="80"/><line x1="58" y1="98" x2="82" y2="98"/></g>'
                + fuse_link +
                '<g stroke="#334155" stroke-width="3" fill="none"><circle cx="320" cy="100" r="23" fill="' + bulb_fill + '" style="' + bulb_glow + '"/><path d="M307 87 L315 95 L309 102 L319 108 L326 99 L333 108" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M309 124 V132 H331 V124 M312 132 V138 H328 V132" stroke="#64748b" stroke-width="2.5"/></g>'
                '<g fill="currentColor" font-size="12" text-anchor="middle"><text x="70" y="137">' + tr("battery") + '</text><text x="205" y="25">' + ("ਫਿਊਜ਼" if is_pa_fuse else "FUSE") + '</text><text x="320" y="194">' + tr("bulb") + '</text></g>'
                '<g fill="currentColor" font-size="12" font-weight="bold" text-anchor="middle"><text x="210" y="211">' + fuse_status + '</text></g>'
                '</svg></div>'
            )
            st.markdown(circuit_svg, unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            c1.metric("ਆਉਣ ਵਾਲਾ ਕਰੰਟ" if is_pa_fuse else "Incoming current", f"{current:.1f} A")
            c2.metric("ਫਿਊਜ਼ ਦੀ ਹੱਦ" if is_pa_fuse else "Fuse rating", f"{fuse_rating:.1f} A")
            c3.metric("ਫਿਊਜ਼ ਤੋਂ ਬਾਅਦ" if is_pa_fuse else "Current after fuse", f"{circuit_current:.1f} A")
            if fuse_blown:
                st.error("ਵੱਧ ਕਰੰਟ ਫਿਊਜ਼ ਦੀ ਹੱਦ ਤੋਂ ਵੱਧ ਹੈ। ਫਿਊਜ਼ ਦਾ ਲਿੰਕ ਟੁੱਟਦਾ ਹੈ, ਸਰਕਟ ਖੁੱਲ੍ਹ ਜਾਂਦਾ ਹੈ ਅਤੇ ਬਲਬ ਬੁੱਝ ਜਾਂਦਾ ਹੈ।" if is_pa_fuse else "The current exceeds the fuse rating. The fuse link breaks, opening the circuit and turning the bulb off.")
            else:
                st.success("ਕਰੰਟ ਫਿਊਜ਼ ਦੀ ਹੱਦ ਤੋਂ ਘੱਟ ਹੈ, ਇਸ ਲਈ ਫਿਊਜ਼ ਸਹੀ ਰਹਿੰਦਾ ਹੈ ਅਤੇ ਬਲਬ ਜਗਦਾ ਹੈ।" if is_pa_fuse else "Current is below the fuse rating, so the fuse stays intact and the bulb glows.")
            st.caption("ਸਿਰਫ਼ ਵਰਚੁਅਲ ਸਿਮੂਲੇਸ਼ਨ — ਅਸਲੀ ਫਿਊਜ਼ ਜਾਂ ਸ਼ਾਰਟ ਸਰਕਟ ਦੀ ਜਾਂਚ ਨਾ ਕਰੋ।" if is_pa_fuse else "Virtual simulation only — do not test a real fuse or create a real short circuit.")
        elif selected_class == 10 and exp_index == 4 and kind == "motor":
            # Class 10 Experiment 5: motor principle, with illustrative electrical/mechanical calculations.
            is_pa_motor10 = st.session_state.language != "en"
            motor_current10 = voltage / resistance if closed and resistance else 0.0
            motor_input10 = voltage * motor_current10
            motor_hours10 = st.slider("ਸਮਾਂ (ਘੰਟੇ)" if is_pa_motor10 else "Operating time (hours)", 0.5, 8.0, 1.0, 0.5, key="class10_motor_hours")
            motor_eff10 = st.slider("ਮਾਡਲ ਦੀ ਕੁਸ਼ਲਤਾ (%)" if is_pa_motor10 else "Assumed model efficiency (%)", 10, 90, 70, 5, key="class10_motor_efficiency")
            motor_output10 = motor_input10 * motor_eff10 / 100.0
            motor_energy10 = motor_input10 * motor_hours10 / 1000.0
            spin10 = closed and voltage > 0
            rotor_angle10 = 35 if spin10 else 0
            motor_color10 = "#16a34a" if spin10 else "#94a3b8"
            rotor_art10 = f'<g transform="rotate({rotor_angle10} 230 108)"><rect x="216" y="67" width="28" height="82" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="3"/><path d="M230 74 V142 M220 108 H240" stroke="#b45309" stroke-width="3"/><circle cx="230" cy="108" r="7" fill="#92400e"/></g>'
            spin_marks10 = '<path d="M195 61 A47 47 0 0 1 267 62 M262 53 L268 62 L257 64" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' if spin10 else ""
            motor_svg10 = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:10px;background:rgba(128,128,128,.035);">
            <svg viewBox="0 0 460 240" width="100%" role="img" aria-label="Simple DC motor showing north and south magnets, a rotating coil, axle and battery circuit">
              <rect x="48" y="65" width="52" height="90" rx="8" fill="#fecaca" stroke="#b91c1c" stroke-width="2"/><text x="74" y="113" fill="#991b1b" font-size="22" font-weight="700" text-anchor="middle">N</text>
              <rect x="360" y="65" width="52" height="90" rx="8" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/><text x="386" y="113" fill="#1e40af" font-size="22" font-weight="700" text-anchor="middle">S</text>
              <g stroke="#64748b" stroke-width="2" stroke-dasharray="5 5"><path d="M105 83 H355 M105 108 H355 M105 133 H355"/></g>
              {rotor_art10}{spin_marks10}
              <path d="M230 149 V178 H105 V201 H355 V178 H230" fill="none" stroke="{motor_color10}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
              <rect x="192" y="188" width="76" height="29" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/><text x="230" y="207" fill="#1e40af" font-size="12" font-weight="700" text-anchor="middle">{voltage} V cell</text>
              <g fill="currentColor" font-size="12" text-anchor="middle"><text x="74" y="53">{ "ਉੱਤਰੀ ਧਰੁਵ" if is_pa_motor10 else "NORTH POLE" }</text><text x="386" y="53">{ "ਦੱਖਣੀ ਧਰੁਵ" if is_pa_motor10 else "SOUTH POLE" }</text><text x="230" y="29">{ "ਕੋਇਲ / ਰੋਟਰ" if is_pa_motor10 else "COIL / ROTOR" }</text><text x="230" y="234">{ "ਕਰੰਟ ਚਾਲੂ: ਘੁੰਮਣ ਦਾ ਸਿਧਾਂਤ" if is_pa_motor10 and spin10 else "ਕਰੰਟ ਬੰਦ: ਰੋਟਰ ਰੁਕਿਆ" if is_pa_motor10 else "Current on: rotation principle" if spin10 else "Current off: rotor stopped" }</text></g>
            </svg></div>"""
            st.markdown("#### " + ("ਸਧਾਰਨ DC ਮੋਟਰ ਦਾ ਸਿਧਾਂਤ" if is_pa_motor10 else "Principle of a Simple DC Motor"))
            st.markdown(motor_svg10, unsafe_allow_html=True)
            st.markdown("**" + ("ਗਣਨਾ ਦੇ ਸੂਤਰ" if is_pa_motor10 else "Calculation formulas") + ":** I = V/R · P(input) = VI · P(output) = efficiency × P(input) · E = P(input) × time")
            motor_a10, motor_b10, motor_c10 = st.columns(3)
            motor_a10.metric("Current (A)", f"{motor_current10:.2f}")
            motor_b10.metric("Input power (W)", f"{motor_input10:.2f}")
            motor_c10.metric("Estimated output (W)", f"{motor_output10:.2f}")
            st.metric("Electrical energy (kWh)", f"{motor_energy10:.4f}")
            st.caption(("ਕੁਸ਼ਲਤਾ ਅਨੁਮਾਨਿਤ ਸੈਟਿੰਗ ਹੈ; ਇਹ ਅਸਲੀ ਮੋਟਰ ਦੀ ਮਾਪੀ ਹੋਈ ਕੁਸ਼ਲਤਾ ਨਹੀਂ।" if is_pa_motor10 else "Efficiency is an assumed setting; it is not a measured efficiency of a real motor."))
            st.markdown("**" + ("ਵੋਲਟੇਜ ਅਨੁਸਾਰ ਗਣਨਾ ਕੀਤੀਆਂ ਰੀਡਿੰਗਾਂ" if is_pa_motor10 else "Calculated observations at different voltages") + "**")
            motor_rows10 = []
            for vm10 in (6, 12, 18, 24):
                im10 = vm10 / resistance if closed else 0.0
                pin10 = vm10 * im10
                pout10 = pin10 * motor_eff10 / 100.0
                motor_rows10.append({"V (V)": vm10, "R (Ω)": resistance, "I (A)": round(im10, 2), "Input P (W)": round(pin10, 2), "Estimated output P (W)": round(pout10, 2)})
            st.dataframe(motor_rows10, use_container_width=True, hide_index=True)
            if not closed:
                st.info("ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੈ: ਕਰੰਟ ਨਹੀਂ ਵਗਦਾ ਅਤੇ ਮੋਟਰ ਰੁਕੀ ਰਹਿੰਦੀ ਹੈ।" if is_pa_motor10 else "Switch open: no current flows and the motor remains stopped.")
            st.caption(("ਆਦਰਸ਼ ਵਰਚੁਅਲ ਮਾਡਲ; ਅਸਲ ਮੋਟਰ ਦੀ ਗਤੀ ਲੋਡ, ਬਣਤਰ ਅਤੇ ਹੋਰ ਕਾਰਕਾਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦੀ ਹੈ। ਘਰੇਲੂ ਮੇਨ ਬਿਜਲੀ ਨਾਲ ਪ੍ਰਯੋਗ ਨਾ ਕਰੋ।" if is_pa_motor10 else "Ideal virtual model; real motor speed depends on load, design and other factors. Never experiment with household mains electricity."))
        elif kind == "motor":
            st.metric("Motor model", "Rotating" if closed and voltage > 0 else "Stopped")
            st.write(note)
        elif kind == "magnet":
            st.write("Iron and steel are usually attracted by a magnet; wood, plastic and rubber are not.")
            st.write(note)
        else:
            st.write(note)
    # Bilingual interactive knowledge check for Classes 7-10 and Class 7 Experiments 4-5.
    if (selected_class == 7 and exp_index in (3, 4)) or selected_class in (8, 9, 10):
        is_pa_check = st.session_state.language != "en"
        st.markdown("---")
        st.subheader("🧠 " + ("ਸਮਝ ਦੀ ਜਾਂਚ ਕਰੋ" if is_pa_check else "Explore & Check Your Understanding"))
        checks = {
            "fuse": ("What is the main job of a fuse?", "Break the circuit when excessive current flows", ["Make the bulb brighter", "Always increase current", "Break the circuit when excessive current flows"], "ਫਿਊਜ਼ ਦਾ ਮੁੱਖ ਕੰਮ ਕੀ ਹੈ?", "ਵੱਧ ਕਰੰਟ ਹੋਣ ਤੇ ਸਰਕਟ ਤੋੜਨਾ", ["ਬਲਬ ਦੀ ਰੌਸ਼ਨੀ ਵਧਾਉਣਾ", "ਕਰੰਟ ਨੂੰ ਹਮੇਸ਼ਾ ਵਧਾਉਣਾ", "ਵੱਧ ਕਰੰਟ ਹੋਣ ਤੇ ਸਰਕਟ ਤੋੜਨਾ"]),
            "magnetic_field": ("What is produced around a wire carrying current?", "A magnetic field", ["A magnetic field", "No effect", "Sound only"], "ਤਾਰ ਵਿੱਚ ਕਰੰਟ ਹੋਣ ਤੇ ਕੀ ਬਣਦਾ ਹੈ?", "ਚੁੰਬਕੀ ਖੇਤਰ", ["ਚੁੰਬਕੀ ਖੇਤਰ", "ਕੋਈ ਪ੍ਰਭਾਵ ਨਹੀਂ", "ਸਿਰਫ਼ ਧੁਨੀ"]),
            "liquids": ("Which liquid usually conducts better?", "Salt water", ["Pure sugar solution", "Salt water", "Oil"], "ਕਿਹੜਾ ਤਰਲ ਆਮ ਤੌਰ ਤੇ ਵਧੀਆ ਚਾਲਕ ਹੈ?", "ਲੂਣ ਵਾਲਾ ਪਾਣੀ", ["ਚੀਨੀ ਦਾ ਘੋਲ", "ਲੂਣ ਵਾਲਾ ਪਾਣੀ", "ਤੇਲ"]),
            "electrolysis": ("What can current cause in a suitable solution?", "A chemical change", ["A chemical change", "Gravity disappears", "Mass always doubles"], "ਢੁਕਵੇਂ ਘੋਲ ਵਿੱਚ ਕਰੰਟ ਨਾਲ ਕੀ ਹੋ ਸਕਦਾ ਹੈ?", "ਰਸਾਇਣਕ ਤਬਦੀਲੀ", ["ਰਸਾਇਣਕ ਤਬਦੀਲੀ", "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਖਤਮ", "ਭਾਰ ਹਮੇਸ਼ਾ ਦੁੱਗਣਾ"]),
            "electroplating": ("What does electroplating do?", "Deposits a thin metal coating", ["Deposits a thin metal coating", "Turns metal into wood", "Stops electricity"], "ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਕੀ ਕਰਦੀ ਹੈ?", "ਧਾਤ ਦੀ ਪਤਲੀ ਪਰਤ ਚੜ੍ਹਾਉਂਦੀ ਹੈ", ["ਧਾਤ ਦੀ ਪਤਲੀ ਪਰਤ ਚੜ੍ਹਾਉਂਦੀ ਹੈ", "ਧਾਤ ਨੂੰ ਲੱਕੜ ਬਣਾਉਂਦੀ ਹੈ", "ਬਿਜਲੀ ਰੋਕਦੀ ਹੈ"]),
            "cell": ("Which energy does a cell convert to electrical energy?", "Chemical energy", ["Sound energy", "Chemical energy", "Wind energy"], "ਸੈੱਲ ਕਿਹੜੀ ਊਰਜਾ ਨੂੰ ਬਿਜਲੀ ਊਰਜਾ ਵਿੱਚ ਬਦਲਦਾ ਹੈ?", "ਰਸਾਇਣਕ ਊਰਜਾ", ["ਧੁਨੀ ਊਰਜਾ", "ਰਸਾਇਣਕ ਊਰਜਾ", "ਪਵਨ ਊਰਜਾ"]),
            "charge": ("How do like charges behave?", "Repel each other", ["Repel each other", "Always attract", "Disappear"], "ਇੱਕੋ ਕਿਸਮ ਦੇ ਚਾਰਜ ਕਿਵੇਂ ਵਰਤਦੇ ਹਨ?", "ਇੱਕ-ਦੂਜੇ ਨੂੰ ਦੂਰ ਧੱਕਦੇ ਹਨ", ["ਇੱਕ-ਦੂਜੇ ਨੂੰ ਦੂਰ ਧੱਕਦੇ ਹਨ", "ਹਮੇਸ਼ਾ ਖਿੱਚਦੇ ਹਨ", "ਗਾਇਬ ਹੋ ਜਾਂਦੇ ਹਨ"]),
            "ohms": ("For a fixed resistor, which is Ohm's law?", "V = I × R", ["V = I × R", "V = I + R", "V = I ÷ R"], "ਸਥਿਰ ਰੋਧ ਲਈ ਓਮ ਦਾ ਨਿਯਮ ਕਿਹੜਾ ਹੈ?", "V = I × R", ["V = I × R", "V = I + R", "V = I ÷ R"]),
            "series_parallel": ("How many main paths are in a series circuit?", "One", ["One", "Two or more", "None"], "ਲੜੀਵਾਰ ਸਰਕਟ ਵਿੱਚ ਕਿੰਨੇ ਮੁੱਖ ਰਸਤੇ ਹੁੰਦੇ ਹਨ?", "ਇੱਕ", ["ਇੱਕ", "ਦੋ ਜਾਂ ਵੱਧ", "ਕੋਈ ਨਹੀਂ"]),
            "power": ("Which formula gives electrical power?", "P = V × I", ["P = V × I", "P = V + I", "P = V ÷ I"], "ਬਿਜਲੀ ਸ਼ਕਤੀ ਦਾ ਸੂਤਰ ਕਿਹੜਾ ਹੈ?", "P = V × I", ["P = V × I", "P = V + I", "P = V ÷ I"]),
            "motor": ("What does an electric motor do?", "Converts electrical energy into motion", ["Converts electrical energy into motion", "Always stops motion", "Produces only light"], "ਇਲੈਕਟ੍ਰਿਕ ਮੋਟਰ ਕੀ ਕਰਦੀ ਹੈ?", "ਬਿਜਲੀ ਊਰਜਾ ਨੂੰ ਗਤੀ ਵਿੱਚ ਬਦਲਦੀ ਹੈ", ["ਬਿਜਲੀ ਊਰਜਾ ਨੂੰ ਗਤੀ ਵਿੱਚ ਬਦਲਦੀ ਹੈ", "ਗਤੀ ਹਮੇਸ਼ਾ ਰੋਕਦੀ ਹੈ", "ਸਿਰਫ਼ ਰੋਸ਼ਨੀ ਬਣਾਉਂਦੀ ਹੈ"]),
            "heating": ("Electrical energy in a resistor can change into what?", "Heat", ["Heat", "Gravity", "Weight"], "ਰੋਧਕ ਵਿੱਚ ਬਿਜਲੀ ਊਰਜਾ ਕਿਸ ਵਿੱਚ ਬਦਲ ਸਕਦੀ ਹੈ?", "ਤਾਪ", ["ਤਾਪ", "ਗੁਰੁਤਵਾਕਰਸ਼ਣ", "ਭਾਰ"]),
            "electromagnet": ("How can a crane electromagnet release scrap?", "By switching off the current", ["By switching off the current", "Adding more wires", "Changing its colour"], "ਕਰੇਨ ਦਾ ਬਿਜਲੀ-ਚੁੰਬਕ ਕਬਾੜ ਕਿਵੇਂ ਛੱਡਦਾ ਹੈ?", "ਕਰੰਟ ਬੰਦ ਕਰਨ ਨਾਲ", ["ਕਰੰਟ ਬੰਦ ਕਰਨ ਨਾਲ", "ਹੋਰ ਤਾਰ ਜੋੜ ਕੇ", "ਰੰਗ ਬਦਲਣ ਨਾਲ"]),
            "circuit": ("When does a bulb light?", "When the circuit is complete", ["When the circuit is complete", "When a wire is broken", "When the switch is open"], "ਬਲਬ ਕਦੋਂ ਜਗਦਾ ਹੈ?", "ਜਦੋਂ ਸਰਕਟ ਪੂਰਾ ਹੋਵੇ", ["ਜਦੋਂ ਸਰਕਟ ਪੂਰਾ ਹੋਵੇ", "ਜਦੋਂ ਤਾਰ ਟੁੱਟੀ ਹੋਵੇ", "ਜਦੋਂ ਸਵਿੱਚ ਖੁੱਲ੍ਹਾ ਹੋਵੇ"])
        }
        if kind == "charge" and selected_class == 9 and exp_index == 4:
            item = ("What can a charged balloon do?", "Attract light objects", ["Attract light objects", "Create a continuous electric current", "Make gravity disappear"], "ਚਾਰਜ ਕੀਤਾ ਗੁਬਾਰਾ ਕੀ ਕਰ ਸਕਦਾ ਹੈ?", "ਹਲਕੀਆਂ ਚੀਜ਼ਾਂ ਨੂੰ ਖਿੱਚ ਸਕਦਾ ਹੈ", ["ਹਲਕੀਆਂ ਚੀਜ਼ਾਂ ਨੂੰ ਖਿੱਚ ਸਕਦਾ ਹੈ", "ਲਗਾਤਾਰ ਬਿਜਲੀ ਕਰੰਟ ਬਣਾਉਂਦਾ ਹੈ", "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਖਤਮ ਕਰਦਾ ਹੈ"])
        elif kind == "power" and selected_class == 9 and exp_index == 3:
            item = ("What does electrical power describe?", "How quickly electrical energy is transferred", ["How quickly electrical energy is transferred", "The colour of a wire", "The length of a switch"], "ਬਿਜਲੀ ਸ਼ਕਤੀ ਕੀ ਦਰਸਾਉਂਦੀ ਹੈ?", "ਬਿਜਲੀ ਊਰਜਾ ਦੇ ਤਬਾਦਲੇ ਦੀ ਦਰ", ["ਬਿਜਲੀ ਊਰਜਾ ਦੇ ਤਬਾਦਲੇ ਦੀ ਦਰ", "ਤਾਰ ਦਾ ਰੰਗ", "ਸਵਿੱਚ ਦੀ ਲੰਬਾਈ"])
        else:
            item = checks.get(kind, checks["circuit"])
        prompt = item[3] if is_pa_check else item[0]
        correct = item[4] if is_pa_check else item[1]
        choices = item[5] if is_pa_check else item[2]
        answer = st.radio(prompt, choices, key=f"lab_check_{selected_class}_{exp_index}_{st.session_state.language}")
        if st.button("ਜਵਾਬ ਜਾਂਚੋ" if is_pa_check else "Check answer", key=f"lab_check_button_{selected_class}_{exp_index}_{st.session_state.language}"):
            if answer == correct:
                st.success("ਬਿਲਕੁਲ ਠੀਕ! 👏" if is_pa_check else "Correct! Great scientific thinking. 👏")
            else:
                st.info(("ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰੋ। ਸੰਕੇਤ: " if is_pa_check else "Try again. Hint: ") + correct)
    st.markdown("---")
    st.markdown(f"**{tr('conclusion')}:** {note}")
    with st.expander(tr("note")):
        st.write(note)
        st.write(tr("safe"))
    st.caption(tr("safe"))

PHYSICS_EXPERIMENTS = {
  6: [
    ("Measure Distance and Time","ਦੂਰੀ ਅਤੇ ਸਮਾਂ ਮਾਪੋ","Explore how distance and time describe motion.","ਗਤੀ ਨੂੰ ਦੂਰੀ ਅਤੇ ਸਮੇਂ ਨਾਲ ਸਮਝੋ।","motion","A moving object covers distance over time.","ਚੱਲਦੀ ਵਸਤੂ ਸਮੇਂ ਦੌਰਾਨ ਦੂਰੀ ਤੈਅ ਕਰਦੀ ਹੈ।"),
    ("Compare Fast and Slow Motion","ਤੇਜ਼ ਅਤੇ ਹੌਲੀ ਗਤੀ ਦੀ ਤੁਲਨਾ","Change distance and time to compare average speed.","ਦੂਰੀ ਅਤੇ ਸਮਾਂ ਬਦਲ ਕੇ ਔਸਤ ਚਾਲ ਦੀ ਤੁਲਨਾ ਕਰੋ।","speed","Average speed = distance ÷ time.","ਔਸਤ ਚਾਲ = ਦੂਰੀ ÷ ਸਮਾਂ।"),
    ("Explore Pushes and Pulls","ਧੱਕੇ ਅਤੇ ਖਿੱਚ ਦੀ ਖੋਜ","Change the applied force and observe a cart model.","ਲਗਾਏ ਬਲ ਨੂੰ ਬਦਲ ਕੇ ਗੱਡੀ ਦਾ ਮਾਡਲ ਵੇਖੋ।","force","A force can change an object's motion or direction.","ਬਲ ਵਸਤੂ ਦੀ ਗਤੀ ਜਾਂ ਦਿਸ਼ਾ ਬਦਲ ਸਕਦਾ ਹੈ।"),
    ("Light and Shadows","ਰੋਸ਼ਨੀ ਅਤੇ ਪਰਛਾਵੇਂ","Move a light source and object to explore shadows.","ਪਰਛਾਵਾਂ ਸਮਝਣ ਲਈ ਰੋਸ਼ਨੀ ਅਤੇ ਵਸਤੂ ਹਿਲਾਓ।","shadow","Opaque objects block light and form shadows.","ਅਪਾਰਦਰਸ਼ੀ ਵਸਤੂਆਂ ਰੋਸ਼ਨੀ ਰੋਕ ਕੇ ਪਰਛਾਵਾਂ ਬਣਾਉਂਦੀਆਂ ਹਨ।"),
    ("Magnets Attract or Repel","ਚੁੰਬਕ ਖਿੱਚਦੇ ਜਾਂ ਧੱਕਦੇ ਹਨ","Choose pole orientation and observe the interaction.","ਧਰੁਵਾਂ ਦੀ ਦਿਸ਼ਾ ਚੁਣ ਕੇ ਪ੍ਰਭਾਵ ਵੇਖੋ।","magnet","Like poles repel; unlike poles attract.","ਇੱਕੋ ਧਰੁਵ ਦੂਰ ਧੱਕਦੇ ਅਤੇ ਵੱਖਰੇ ਧਰੁਵ ਖਿੱਚਦੇ ਹਨ।")
  ],
  7: [
    ("Motion on a Distance-Time Track","ਦੂਰੀ-ਸਮਾਂ ਪਟੜੀ ਉੱਤੇ ਗਤੀ","Compare the motion of a model object over time.","ਸਮੇਂ ਨਾਲ ਮਾਡਲ ਵਸਤੂ ਦੀ ਗਤੀ ਦੀ ਤੁਲਨਾ ਕਰੋ।","motion","A distance-time record helps describe motion.","ਦੂਰੀ-ਸਮਾਂ ਰਿਕਾਰਡ ਗਤੀ ਦਾ ਵਰਣਨ ਕਰਦਾ ਹੈ।"),
    ("Friction on Different Surfaces","ਵੱਖਰੀਆਂ ਸਤਹਾਂ ਉੱਤੇ ਘਰਸ਼ਣ","Compare how surfaces affect a sliding block.","ਸਤਹਾਂ ਦਾ ਫਿਸਲਦੇ ਬਲਾਕ ਉੱਤੇ ਪ੍ਰਭਾਵ ਵੇਖੋ।","friction","Rougher surfaces often produce more friction.","ਖੁਰਦਰੀਆਂ ਸਤਹਾਂ ਉੱਤੇ ਆਮ ਤੌਰ ਤੇ ਘਰਸ਼ਣ ਵੱਧ ਹੁੰਦਾ ਹੈ।"),
    ("Air and Water Pressure","ਹਵਾ ਅਤੇ ਪਾਣੀ ਦਾ ਦਬਾਅ","Explore how depth changes the pressure model.","ਡੂੰਘਾਈ ਨਾਲ ਦਬਾਅ ਦੇ ਮਾਡਲ ਵਿੱਚ ਤਬਦੀਲੀ ਵੇਖੋ।","pressure","Liquid pressure generally increases with depth.","ਤਰਲ ਦਾ ਦਬਾਅ ਆਮ ਤੌਰ ਤੇ ਡੂੰਘਾਈ ਨਾਲ ਵਧਦਾ ਹੈ।"),
    ("Reflection of Light","ਰੋਸ਼ਨੀ ਦਾ ਪਰਾਵਰਤਨ","Change the incoming ray angle on a mirror.","ਸ਼ੀਸ਼ੇ ਉੱਤੇ ਆਉਣ ਵਾਲੀ ਕਿਰਨ ਦਾ ਕੋਣ ਬਦਲੋ।","reflection","Angle of incidence equals angle of reflection for a plane mirror.","ਸਮਤਲ ਸ਼ੀਸ਼ੇ ਵਿੱਚ ਆਗਮਨ ਕੋਣ ਪਰਾਵਰਤਨ ਕੋਣ ਦੇ ਬਰਾਬਰ ਹੁੰਦਾ ਹੈ।"),
    ("Sound Vibrations","ਧੁਨੀ ਦੀਆਂ ਕੰਪਨਾਂ","Change vibration frequency in a string model.","ਤਾਰ ਦੇ ਮਾਡਲ ਵਿੱਚ ਕੰਪਨ ਦੀ ਆਵ੍ਰਿਤੀ ਬਦਲੋ।","sound","Sound is produced by vibrating sources.","ਧੁਨੀ ਕੰਪਨ ਕਰਦੇ ਸਰੋਤਾਂ ਤੋਂ ਪੈਦਾ ਹੁੰਦੀ ਹੈ।")
  ],
  8: [
    ("Pressure and Contact Area","ਦਬਾਅ ਅਤੇ ਸੰਪਰਕ ਖੇਤਰਫਲ","Explore everyday examples showing that a larger contact area reduces pressure, while a smaller contact area increases pressure.","ਰੋਜ਼ਾਨਾ ਦੀਆਂ ਉਦਾਹਰਨਾਂ ਰਾਹੀਂ ਵੇਖੋ ਕਿ ਵੱਡਾ ਸੰਪਰਕ ਖੇਤਰਫਲ ਦਬਾਅ ਘਟਾਉਂਦਾ ਹੈ ਅਤੇ ਛੋਟਾ ਖੇਤਰਫਲ ਦਬਾਅ ਵਧਾਉਂਦਾ ਹੈ।","pressure_area","For the same force, spreading it over a larger area produces less pressure; concentrating it on a smaller area produces more pressure.","ਇੱਕੋ ਬਲ ਵੱਡੇ ਖੇਤਰਫਲ ਉੱਤੇ ਫੈਲਣ ਨਾਲ ਦਬਾਅ ਘਟਦਾ ਹੈ; ਛੋਟੇ ਖੇਤਰਫਲ ਉੱਤੇ ਲੱਗਣ ਨਾਲ ਦਬਾਅ ਵਧਦਾ ਹੈ।"),
    ("Balanced and Unbalanced Forces","ਸੰਤੁਲਿਤ ਅਤੇ ਅਸੰਤੁਲਿਤ ਬਲ","Observe two people pushing a table in the same direction, in opposite directions, and with unequal opposing pushes.","ਦੋ ਵਿਅਕਤੀਆਂ ਨੂੰ ਮੇਜ਼ ਇੱਕੋ ਦਿਸ਼ਾ ਵਿੱਚ, ਉਲਟ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਅਤੇ ਅਸਮਾਨ ਬਲ ਨਾਲ ਧੱਕਦੇ ਵੇਖੋ।","balanced","Balanced forces do not change an object’s motion; an unbalanced force can start, stop, speed up, slow down or change its direction.","ਸੰਤੁਲਿਤ ਬਲ ਵਸਤੂ ਦੀ ਗਤੀ ਨਹੀਂ ਬਦਲਦੇ; ਅਸੰਤੁਲਿਤ ਬਲ ਵਸਤੂ ਨੂੰ ਚਲਾ, ਰੋਕ ਜਾਂ ਉਸ ਦੀ ਚਾਲ ਜਾਂ ਦਿਸ਼ਾ ਬਦਲ ਸਕਦਾ ਹੈ।"),
    ("Conduction of Heat","ਤਾਪ ਦਾ ਚਾਲਨ","Compare heat transfer through different materials.","ਵੱਖਰੇ ਪਦਾਰਥਾਂ ਵਿੱਚੋਂ ਤਾਪ ਦੇ ਤਬਾਦਲੇ ਦੀ ਤੁਲਨਾ ਕਰੋ।","heat","Materials conduct heat at different rates.","ਪਦਾਰਥ ਤਾਪ ਨੂੰ ਵੱਖ-ਵੱਖ ਦਰਾਂ ਨਾਲ ਚਲਾਉਂਦੇ ਹਨ।"),
    ("Reflection in a Plane Mirror","ਸਮਤਲ ਸ਼ੀਸ਼ੇ ਵਿੱਚ ਪਰਾਵਰਤਨ","Trace incident and reflected rays.","ਆਉਣ ਵਾਲੀਆਂ ਅਤੇ ਪਰਾਵਰਤਿਤ ਕਿਰਨਾਂ ਦਾ ਪਤਾ ਲਗਾਓ।","reflection","The incident and reflected rays lie in the same plane.","ਆਗਮਨ ਅਤੇ ਪਰਾਵਰਤਿਤ ਕਿਰਨਾਂ ਇੱਕੋ ਸਮਤਲ ਵਿੱਚ ਹੁੰਦੀਆਂ ਹਨ।"),
    ("Simple Sound Wave","ਸਧਾਰਨ ਧੁਨੀ ਤਰੰਗ","Change frequency and amplitude in a wave display.","ਤਰੰਗ ਵਿੱਚ ਆਵ੍ਰਿਤੀ ਅਤੇ ਐਂਪਲੀਟਿਊਡ ਬਦਲੋ।","wave","Frequency relates to pitch; amplitude relates to loudness.","ਆਵ੍ਰਿਤੀ ਸੁਰ ਦੀ ਉਚਾਈ ਅਤੇ ਐਂਪਲੀਟਿਊਡ ਉੱਚੀ ਆਵਾਜ਼ ਨਾਲ ਜੁੜੀ ਹੈ।")
  ],
  9: [
    ("Speed and Acceleration","ਚਾਲ ਅਤੇ ਤਵਰਣ","Explore changes in velocity over a time interval.","ਸਮੇਂ ਨਾਲ ਵੇਗ ਵਿੱਚ ਤਬਦੀਲੀ ਦੀ ਖੋਜ ਕਰੋ।","acceleration","Acceleration is change in velocity divided by time.","ਤਵਰਣ = ਵੇਗ ਵਿੱਚ ਤਬਦੀਲੀ ÷ ਸਮਾਂ।"),
    ("Newton's Second Law","ਨਿਊਟਨ ਦਾ ਦੂਜਾ ਨਿਯਮ","Change force and mass to explore acceleration.","ਤਵਰਣ ਸਮਝਣ ਲਈ ਬਲ ਅਤੇ ਪੁੰਜ ਬਦਲੋ।","newton","For a constant mass, F = ma.","ਸਥਿਰ ਪੁੰਜ ਲਈ F = ma।"),
    ("Work and Mechanical Energy","ਕੰਮ ਅਤੇ ਮਕੈਨੀਕੀ ਊਰਜਾ","Explore work done by a force over a distance.","ਦੂਰੀ ਉੱਤੇ ਬਲ ਦੁਆਰਾ ਕੀਤੇ ਕੰਮ ਨੂੰ ਸਮਝੋ।","work","For force along motion, work = force × distance.","ਗਤੀ ਦੀ ਦਿਸ਼ਾ ਵਿੱਚ ਬਲ ਹੋਵੇ ਤਾਂ ਕੰਮ = ਬਲ × ਦੂਰੀ।"),
    ("Refraction Through a Glass Block","ਕੱਚ ਦੇ ਬਲਾਕ ਵਿੱਚ ਅਪਵਰਤਨ","Observe a ray change direction at a boundary.","ਸੀਮਾ ਉੱਤੇ ਕਿਰਨ ਦੀ ਦਿਸ਼ਾ ਬਦਲਦੀ ਵੇਖੋ।","refraction","Light changes direction when it enters a different optical medium at an angle.","ਕੋਣ ਨਾਲ ਵੱਖਰੇ ਮਾਧਿਅਮ ਵਿੱਚ ਜਾਣ ਸਮੇਂ ਰੋਸ਼ਨੀ ਦੀ ਦਿਸ਼ਾ ਬਦਲ ਸਕਦੀ ਹੈ।"),
    ("Gravitational Potential Energy","ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ","Change mass and height in an energy model.","ਊਰਜਾ ਮਾਡਲ ਵਿੱਚ ਪੁੰਜ ਅਤੇ ਉਚਾਈ ਬਦਲੋ।","potential","Near Earth's surface, gravitational potential energy change ≈ mgh.","ਧਰਤੀ ਦੀ ਸਤਹ ਨੇੜੇ ਸਥਿਤਿਜ ਊਰਜਾ ਵਿੱਚ ਤਬਦੀਲੀ ਲਗਭਗ mgh ਹੈ।")
  ],
  10: [
    ("Verify Laws of Reflection","ਪਰਾਵਰਤਨ ਦੇ ਨਿਯਮ ਦੀ ਜਾਂਚ","Change the incident angle and compare the reflected angle.","ਆਗਮਨ ਕੋਣ ਬਦਲ ਕੇ ਪਰਾਵਰਤਨ ਕੋਣ ਦੀ ਤੁਲਨਾ ਕਰੋ।","reflection","For an ideal plane mirror, i = r.","ਆਦਰਸ਼ ਸਮਤਲ ਸ਼ੀਸ਼ੇ ਲਈ i = r।"),
    ("Refraction and Refractive Index","ਅਪਵਰਤਨ ਅਤੇ ਅਪਵਰਤਨ ਅੰਕ","Explore how optical medium affects ray bending.","ਪ੍ਰਕਾਸ਼ੀ ਮਾਧਿਅਮ ਦਾ ਕਿਰਨ ਦੇ ਮੁੜਨ ਉੱਤੇ ਪ੍ਰਭਾਵ ਵੇਖੋ।","refraction","Snell's law relates refractive indices and ray angles.","ਸਨੇਲ ਦਾ ਨਿਯਮ ਅਪਵਰਤਨ ਅੰਕਾਂ ਅਤੇ ਕਿਰਨਾਂ ਦੇ ਕੋਣਾਂ ਦਾ ਸਬੰਧ ਦੱਸਦਾ ਹੈ।"),
    ("Convex Lens and Image Formation","ਉੱਤਲ ਲੈਂਸ ਅਤੇ ਪ੍ਰਤਿਬਿੰਬ","Change object distance to explore image position.","ਪ੍ਰਤਿਬਿੰਬ ਦੀ ਸਥਿਤੀ ਸਮਝਣ ਲਈ ਵਸਤੂ ਦੀ ਦੂਰੀ ਬਦਲੋ।","lens","Image characteristics depend on object distance and focal length.","ਪ੍ਰਤਿਬਿੰਬ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਸਤੂ ਦੀ ਦੂਰੀ ਅਤੇ ਫੋਕਸ ਦੂਰੀ ਉੱਤੇ ਨਿਰਭਰ ਹਨ।"),
    ("Work, Power and Energy","ਕੰਮ, ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ","Calculate work and average power in a simple model.","ਸਧਾਰਨ ਮਾਡਲ ਵਿੱਚ ਕੰਮ ਅਤੇ ਔਸਤ ਸ਼ਕਤੀ ਦੀ ਗਣਨਾ ਕਰੋ।","work","Work = force × distance; average power = work ÷ time.","ਕੰਮ = ਬਲ × ਦੂਰੀ; ਔਸਤ ਸ਼ਕਤੀ = ਕੰਮ ÷ ਸਮਾਂ।"),
    ("Wave Frequency and Sound","ਤਰੰਗ ਆਵ੍ਰਿਤੀ ਅਤੇ ਧੁਨੀ","Change frequency and amplitude to compare wave properties.","ਤਰੰਗ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਦੀ ਤੁਲਨਾ ਲਈ ਆਵ੍ਰਿਤੀ ਅਤੇ ਐਂਪਲੀਟਿਊਡ ਬਦਲੋ।","wave","Frequency is measured in hertz; amplitude is a wave displacement measure.","ਆਵ੍ਰਿਤੀ ਹਰਟਜ਼ ਵਿੱਚ ਮਾਪੀ ਜਾਂਦੀ ਹੈ; ਐਂਪਲੀਟਿਊਡ ਵਿਸਥਾਪਨ ਦਾ ਮਾਪ ਹੈ।")
  ]
}

def physics_lab():
    if st.button(tr("back"), key="physics_back"):
        go("home")
        st.rerun()
    is_pa = st.session_state.language != "en"
    st.title("🚀 " + ("ਭੌਤਿਕ ਵਿਗਿਆਨ ਲੈਬ" if is_pa else "Physics Lab"))
    st.caption("25 interactive experiments · Classes 6–10 · Virtual learning models")
    classes = [6, 7, 8, 9, 10]
    pc = st.selectbox("ਜਮਾਤ ਚੁਣੋ" if is_pa else "Select class", classes,
        index=classes.index(st.session_state.get("physics_class", 6)),
        format_func=lambda x: f"{x}ਵੀਂ ਜਮਾਤ" if is_pa else f"Class {x}", key="physics_class")
    exp_list = PHYSICS_EXPERIMENTS[pc]
    ei = st.selectbox("ਪ੍ਰਯੋਗ ਚੁਣੋ" if is_pa else "Select experiment", list(range(5)),
        format_func=lambda i: f"EXPERIMENT {i+1} · {exp_list[i][1 if is_pa else 0]}", key=f"physics_exp_{pc}")
    en_title, pa_title, en_aim, pa_aim, kind, en_note, pa_note = exp_list[ei]
    title = pa_title if is_pa else en_title
    aim = pa_aim if is_pa else en_aim
    note = pa_note if is_pa else en_note
    st.markdown("---")
    st.header(f"EXPERIMENT {ei+1} · CLASS {pc}")
    st.subheader(title)
    st.markdown(f"**{'ਉਦੇਸ਼' if is_pa else 'Aim'}:** {aim}")
    st.markdown("### " + ("ਇੰਟਰਐਕਟਿਵ ਕੰਟਰੋਲ" if is_pa else "Interactive controls"))
    kind_labels = {
      "motion":("Distance (m)","Time (s)","ਦੂਰੀ (m)","ਸਮਾਂ (s)"),
      "speed":("Distance (m)","Time (s)","ਦੂਰੀ (m)","ਸਮਾਂ (s)"),
      "force":("Applied force (N)","Mass (kg)","ਲਗਾਇਆ ਬਲ (N)","ਪੁੰਜ (kg)"),
      "shadow":("Light distance (cm)","Object size (cm)","ਰੋਸ਼ਨੀ ਦੀ ਦੂਰੀ (cm)","ਵਸਤੂ ਦਾ ਆਕਾਰ (cm)"),
      "magnet":("Pole arrangement","Strength (illustrative)","ਧਰੁਵਾਂ ਦੀ ਬਣਤਰ","ਤਾਕਤ (ਸਮਝਾਉਣ ਲਈ)"),
      "friction":("Surface roughness","Block mass (kg)","ਸਤਹ ਦੀ ਖੁਰਦਰਾਪਣ","ਬਲਾਕ ਦਾ ਪੁੰਜ (kg)"),
      "pressure":("Depth (m)","Liquid density (kg/m³)","ਡੂੰਘਾਈ (m)","ਤਰਲ ਘਣਤਾ (kg/m³)"),
      "reflection":("Incident angle (°)","Mirror setting","ਆਗਮਨ ਕੋਣ (°)","ਸ਼ੀਸ਼ੇ ਦੀ ਸਥਿਤੀ"),
      "sound":("Frequency (Hz)","Amplitude (relative)","ਆਵ੍ਰਿਤੀ (Hz)","ਐਂਪਲੀਟਿਊਡ (ਸਾਪੇਖ)"),
      "pressure_area":("Force (N)","Contact area (cm²)","ਬਲ (N)","ਸੰਪਰਕ ਖੇਤਰਫਲ (cm²)"),
      "balanced":("Rightward force (N)","Leftward force (N)","ਸੱਜੇ ਪਾਸੇ ਬਲ (N)","ਖੱਬੇ ਪਾਸੇ ਬਲ (N)"),
      "heat":("Heating level (relative)","Material","ਤਾਪ ਪੱਧਰ (ਸਾਪੇਖ)","ਪਦਾਰਥ"),
      "wave":("Frequency (Hz)","Amplitude (relative)","ਆਵ੍ਰਿਤੀ (Hz)","ਐਂਪਲੀਟਿਊਡ (ਸਾਪੇਖ)"),
      "acceleration":("Final velocity (m/s)","Time (s)","ਅੰਤਿਮ ਵੇਗ (m/s)","ਸਮਾਂ (s)"),
      "newton":("Force (N)","Mass (kg)","ਬਲ (N)","ਪੁੰਜ (kg)"),
      "work":("Force (N)","Distance (m)","ਬਲ (N)","ਦੂਰੀ (m)"),
      "refraction":("Incident angle (°)","Refractive index","ਆਗਮਨ ਕੋਣ (°)","ਅਪਵਰਤਨ ਅੰਕ"),
      "potential":("Mass (kg)","Height (m)","ਪੁੰਜ (kg)","ਉਚਾਈ (m)"),
      "lens":("Object distance (cm)","Focal length (cm)","ਵਸਤੂ ਦੀ ਦੂਰੀ (cm)","ਫੋਕਸ ਦੂਰੀ (cm)")
    }
    labels = kind_labels.get(kind, ("Control A","Control B","કੰਟਰੋਲ A","ਕੰਟਰੋਲ B"))
    slow_fast_experiment = pc == 6 and ei == 1 and kind == "speed"
    force_examples_experiment = pc == 6 and ei == 2 and kind == "force"
    shadow_examples_experiment = pc == 6 and ei == 3 and kind == "shadow"
    magnet_poles_experiment = pc == 6 and ei == 4 and kind == "magnet"
    friction_types_experiment = pc == 7 and ei == 1 and kind == "friction"
    liquid_pressure_examples_experiment = pc == 7 and ei == 2 and kind == "pressure"
    reflection_angle_experiment = pc == 7 and ei == 3 and kind == "reflection"
    class8_reflection_experiment = pc == 8 and ei == 3 and kind == "reflection"
    current_magnetic_field_experiment = pc == 7 and ei == 4 and kind == "magnetic_field"
    pressure_area_examples_experiment = pc == 8 and ei == 0 and kind == "pressure_area"
    balanced_forces_examples_experiment = pc == 8 and ei == 1 and kind == "balanced"
    heat_conduction_examples_experiment = pc == 8 and ei == 2 and kind == "heat"
    class8_sound_wave_examples_experiment = pc == 8 and ei == 4 and kind == "wave"
    class9_speed_acceleration_experiment = pc == 9 and ei == 0 and kind == "acceleration"
    class9_newton_experiment = pc == 9 and ei == 1 and kind == "newton"
    class9_work_energy_experiment = pc == 9 and ei == 2 and kind == "work"
    class9_refraction_experiment = pc == 9 and ei == 3 and kind == "refraction"
    class9_gravity_experiment = pc == 9 and ei == 4 and kind == "potential"
    class10_reflection_experiment = pc == 10 and ei == 0 and kind == "reflection"
    class10_refraction_experiment = pc == 10 and ei == 1 and kind == "refraction"
    class10_convex_lens_experiment = pc == 10 and ei == 2 and kind == "lens"
    class10_work_power_energy_experiment = pc == 10 and ei == 3 and kind == "work"
    class10_wave_sound_experiment = pc == 10 and ei == 4 and kind == "wave"
    # Class 8 sound uses a qualitative dropdown, not numeric frequency/amplitude sliders.
    if class8_sound_wave_examples_experiment:
        sound_examples = ["Soft, low-pitched sound", "Loud, low-pitched sound", "Soft, high-pitched sound", "Loud, high-pitched sound"]
        sound_examples_pa = ["ਹੌਲੀ, ਨੀਵੀਂ ਸੁਰ ਵਾਲੀ ਧੁਨੀ", "ਉੱਚੀ ਆਵਾਜ਼, ਨੀਵੀਂ ਸੁਰ", "ਹੌਲੀ, ਉੱਚੀ ਸੁਰ ਵਾਲੀ ਧੁਨੀ", "ਉੱਚੀ ਆਵਾਜ਼, ਉੱਚੀ ਸੁਰ"]
        a = st.selectbox("Choose a sound to compare" if not is_pa else "ਤੁਲਨਾ ਲਈ ਧੁਨੀ ਚੁਣੋ", sound_examples, format_func=lambda x: sound_examples_pa[sound_examples.index(x)] if is_pa else x, key="physics_class8_sound_example")
        b = a
    elif balanced_forces_examples_experiment:
        balanced_force_examples = ["Both people push the table to the right", "People push equally in opposite directions", "People push in opposite directions, one harder"]
        balanced_force_examples_pa = ["ਦੋਵੇਂ ਵਿਅਕਤੀ ਮੇਜ਼ ਨੂੰ ਸੱਜੇ ਧੱਕਦੇ ਹਨ", "ਦੋਵੇਂ ਬਰਾਬਰ ਬਲ ਨਾਲ ਉਲਟ ਧੱਕਦੇ ਹਨ", "ਉਲਟ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਧੱਕਾ, ਇੱਕ ਵੱਧ ਤਾਕਤ ਨਾਲ"]
        a = st.selectbox("Choose how the people push the table" if not is_pa else "ਚੁਣੋ ਕਿ ਵਿਅਕਤੀ ਮੇਜ਼ ਨੂੰ ਕਿਵੇਂ ਧੱਕਦੇ ਹਨ", balanced_force_examples, format_func=lambda x: balanced_force_examples_pa[balanced_force_examples.index(x)] if is_pa else x, key="physics_class8_balanced_force_example")
        b = a
    elif balanced_forces_examples_experiment:
        same_direction = a == "Both people push the table to the right"
        equal_opposite = a == "People push equally in opposite directions"
        person_left = '<circle cx="58" cy="72" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M58 85 V119 M58 94 L82 103 L96 103 M58 119 L45 143 M58 119 L72 143" stroke="#2563eb" stroke-width="7" stroke-linecap="round" fill="none"/>'
        person_right = '<circle cx="402" cy="72" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M402 85 V119 M402 94 L378 103 L364 103 M402 119 L389 143 M402 119 L416 143" stroke="#16a34a" stroke-width="7" stroke-linecap="round" fill="none"/>'
        if same_direction:
            left_arrow = '<path d="M155 105 H95 M105 95 L93 105 L105 115" stroke="#0ea5e9" stroke-width="5" fill="none"/>'
            right_arrow = '<path d="M305 105 H365 M355 95 L367 105 L355 115" stroke="#f59e0b" stroke-width="5" fill="none"/>'
            motion_text = "TABLE MOVES RIGHT →" if not is_pa else "ਮੇਜ਼ ਸੱਜੇ ਵੱਲ ਚੱਲਦੀ ਹੈ →"
            status_text = "UNBALANCED · BOTH PUSH RIGHT" if not is_pa else "ਅਸੰਤੁਲਿਤ · ਦੋਵੇਂ ਸੱਜੇ ਧੱਕਦੇ ਹਨ"
        elif equal_opposite:
            left_arrow = '<path d="M165 105 H105 M115 95 L103 105 L115 115" stroke="#0ea5e9" stroke-width="5" fill="none"/>'
            right_arrow = '<path d="M295 105 H355 M345 95 L357 105 L345 115" stroke="#f59e0b" stroke-width="5" fill="none"/>'
            motion_text = "TABLE STAYS STILL" if not is_pa else "ਮੇਜ਼ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ"
            status_text = "BALANCED · EQUAL OPPOSING FORCES" if not is_pa else "ਸੰਤੁਲਿਤ · ਬਰਾਬਰ ਉਲਟ ਬਲ"
        else:
            left_arrow = '<path d="M165 105 H75 M85 95 L73 105 L85 115" stroke="#0ea5e9" stroke-width="7" fill="none"/>'
            right_arrow = '<path d="M295 105 H335 M325 95 L337 105 L325 115" stroke="#f59e0b" stroke-width="3" fill="none"/>'
            motion_text = "TABLE MOVES LEFT ←" if not is_pa else "ਮੇਜ਼ ਖੱਬੇ ਵੱਲ ਚੱਲਦੀ ਹੈ ←"
            status_text = "UNBALANCED · LEFT PUSH STRONGER" if not is_pa else "ਅਸੰਤੁਲਿਤ · ਖੱਬੇ ਪਾਸੇ ਦਾ ਧੱਕਾ ਵੱਧ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#334155">{("TWO PEOPLE PUSHING A TABLE" if not is_pa else "ਦੋ ਵਿਅਕਤੀ ਮੇਜ਼ ਨੂੰ ਧੱਕਦੇ ਹੋਏ")}</text>{person_left}{person_right}<rect x="155" y="84" width="150" height="43" rx="5" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M175 127 V151 M285 127 V151" stroke="#854d0e" stroke-width="6"/>{left_arrow}{right_arrow}<text x="230" y="174" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">{status_text}</text><text x="230" y="198" text-anchor="middle" font-size="14" font-weight="700" fill="#0f766e">{motion_text}</text>'
    elif balanced_forces_examples_experiment:
        if a == "Both people push the table to the right":
            result = ("Both people push in the same direction, so their effects add together. The forces are unbalanced and the table moves to the right." if not is_pa else "ਦੋਵੇਂ ਵਿਅਕਤੀ ਇੱਕੋ ਦਿਸ਼ਾ ਵਿੱਚ ਧੱਕਦੇ ਹਨ, ਇਸ ਲਈ ਉਨ੍ਹਾਂ ਦੇ ਬਲ ਇਕੱਠੇ ਹੋ ਜਾਂਦੇ ਹਨ। ਬਲ ਅਸੰਤੁਲਿਤ ਹਨ ਅਤੇ ਮੇਜ਼ ਸੱਜੇ ਵੱਲ ਚੱਲਦੀ ਹੈ।")
        elif a == "People push equally in opposite directions":
            result = ("The two pushes are equal and opposite. They balance each other, so the table’s motion does not change; if it was at rest, it stays at rest." if not is_pa else "ਦੋਵੇਂ ਧੱਕੇ ਬਰਾਬਰ ਅਤੇ ਉਲਟ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਹਨ। ਇਹ ਇੱਕ-ਦੂਜੇ ਨੂੰ ਸੰਤੁਲਿਤ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਮੇਜ਼ ਦੀ ਗਤੀ ਨਹੀਂ ਬਦਲਦੀ; ਜੇ ਇਹ ਪਹਿਲਾਂ ਸਥਿਰ ਸੀ ਤਾਂ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ।")
        else:
            result = ("The pushes are opposite but unequal. The stronger push to the left makes the forces unbalanced, so the table accelerates left." if not is_pa else "ਧੱਕੇ ਉਲਟ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਹਨ ਪਰ ਬਰਾਬਰ ਨਹੀਂ। ਖੱਬੇ ਪਾਸੇ ਦਾ ਵੱਧ ਬਲ ਅਸੰਤੁਲਨ ਪੈਦਾ ਕਰਦਾ ਹੈ, ਇਸ ਲਈ ਮੇਜ਼ ਖੱਬੇ ਵੱਲ ਤੇਜ਼ ਹੁੰਦੀ ਹੈ।")
    elif heat_conduction_examples_experiment:
        heat_materials = ["Metal rod (iron / steel)", "Copper spoon", "Wooden stick", "Plastic ruler"]
        heat_materials_pa = ["ਧਾਤ ਦੀ ਛੜ (ਲੋਹਾ / ਸਟੀਲ)", "ਤਾਂਬੇ ਦਾ ਚਮਚਾ", "ਲੱਕੜੀ ਦੀ ਛੜੀ", "ਪਲਾਸਟਿਕ ਦਾ ਪੈਮਾਨਾ"]
        a = st.selectbox("Choose a material to heat" if not is_pa else "ਗਰਮ ਕਰਨ ਲਈ ਪਦਾਰਥ ਚੁਣੋ", heat_materials, format_func=lambda x: heat_materials_pa[heat_materials.index(x)] if is_pa else x, key="physics_class8_heat_material")
        b = a
    elif pressure_area_examples_experiment:
        pressure_area_examples = ["Snowshoes vs high heels", "Sharp knife vs blunt knife", "Broad tractor tyres vs narrow tyres", "Wide building foundation"]
        pressure_area_examples_pa = ["ਬਰਫ਼ ਵਾਲੇ ਜੁੱਤੇ ਬਨਾਮ ਉੱਚੀ ਅੱਡੀ", "ਤੇਜ਼ ਛੁਰੀ ਬਨਾਮ ਮੋਟੀ ਧਾਰ ਵਾਲੀ ਛੁਰੀ", "ਚੌੜੇ ਟਰੈਕਟਰ ਟਾਇਰ ਬਨਾਮ ਤੰਗ ਟਾਇਰ", "ਚੌੜੀ ਇਮਾਰਤੀ ਨੀਂਹ"]
        a = st.selectbox("Choose a surface-area example" if not is_pa else "ਸਤਹੀ ਖੇਤਰਫਲ ਦੀ ਉਦਾਹਰਨ ਚੁਣੋ", pressure_area_examples, format_func=lambda x: pressure_area_examples_pa[pressure_area_examples.index(x)] if is_pa else x, key="physics_class8_pressure_area_example")
        b = a
    elif current_magnetic_field_experiment:
        current_states = ["Switch ON — current flows", "Switch OFF — no current"]
        current_states_pa = ["ਸਵਿੱਚ ਚਾਲੂ — ਕਰੰਟ ਵਗਦਾ ਹੈ", "ਸਵਿੱਚ ਬੰਦ — ਕਰੰਟ ਨਹੀਂ ਵਗਦਾ"]
        a = st.selectbox("Operate the circuit switch" if not is_pa else "ਸਰਕਟ ਦਾ ਸਵਿੱਚ ਚਲਾਓ", current_states, format_func=lambda x: current_states_pa[current_states.index(x)] if is_pa else x, key="physics_class7_magnetic_current_switch")
        b = a
    elif reflection_angle_experiment or class8_reflection_experiment:
        reflection_angles = [10, 20, 30, 40, 50, 60, 70, 80]
        select_key = "physics_class7_reflection_angle" if reflection_angle_experiment else "physics_class8_reflection_angle"
        a = st.selectbox("Select angle of incidence" if not is_pa else "ਆਗਮਨ ਕੋਣ ਚੁਣੋ", reflection_angles, index=2, format_func=lambda x: f"{x}°", key=select_key)
        b = a
    elif liquid_pressure_examples_experiment:
        pressure_examples = ["Water jets from holes at different depths", "Water pressing against a dam wall", "Water flowing from an overhead tank"]
        pressure_examples_pa = ["ਵੱਖ-ਵੱਖ ਡੂੰਘਾਈਆਂ ਵਾਲੇ ਛੇਕਾਂ ਵਿੱਚੋਂ ਪਾਣੀ ਦੀਆਂ ਧਾਰਾਂ", "ਬੰਨ੍ਹ ਦੀ ਕੰਧ ਉੱਤੇ ਪਾਣੀ ਦਾ ਦਬਾਅ", "ਉੱਚੀ ਟੈਂਕੀ ਵਿੱਚੋਂ ਪਾਣੀ ਦਾ ਵਹਾਅ"]
        a = st.selectbox("Choose a liquid-pressure example" if not is_pa else "ਤਰਲ ਦਬਾਅ ਦੀ ਉਦਾਹਰਨ ਚੁਣੋ", pressure_examples, format_func=lambda x: pressure_examples_pa[pressure_examples.index(x)] if is_pa else x, key="physics_class7_liquid_pressure_example")
        b = a
    elif friction_types_experiment:
        friction_examples = ["Sliding friction — block on different surfaces", "Rolling friction — wheel on a road", "Fluid friction — cyclist or boat through a fluid"]
        friction_examples_pa = ["ਸਰਕਣ ਘਰਸ਼ਣ — ਵੱਖਰੀਆਂ ਸਤਹਾਂ ਉੱਤੇ ਬਲਾਕ", "ਲੁੜਕਣ ਘਰਸ਼ਣ — ਸੜਕ ਉੱਤੇ ਪਹੀਆ", "ਤਰਲ ਘਰਸ਼ਣ — ਹਵਾ ਜਾਂ ਪਾਣੀ ਵਿੱਚ ਸਾਈਕਲ ਸਵਾਰ / ਕਿਸ਼ਤੀ"]
        a = st.selectbox("Choose a type of friction" if not is_pa else "ਘਰਸ਼ਣ ਦੀ ਕਿਸਮ ਚੁਣੋ", friction_examples, format_func=lambda x: friction_examples_pa[friction_examples.index(x)] if is_pa else x, key="physics_class7_friction_type")
        b = a
    elif magnet_poles_experiment:
        a = st.selectbox("Choose the poles facing each other" if not is_pa else "ਇੱਕ-ਦੂਜੇ ਵੱਲ ਮੂੰਹ ਕਰਦੇ ਧਰੁਵ ਚੁਣੋ", ["Like poles (N–N)", "Unlike poles (N–S)"], format_func=lambda x: (("ਇੱਕੋ ਜਿਹੇ ਧਰੁਵ (N–N)" if x.startswith("Like") else "ਵੱਖਰੇ ਧਰੁਵ (N–S)") if is_pa else x), key="physics_class6_magnet_poles")
        b = a
    elif shadow_examples_experiment:
        shadow_examples = ["Torch and hand", "Tree on a sunny day", "Opaque book blocking light", "Translucent curtain"]
        shadow_examples_pa = ["ਟਾਰਚ ਅਤੇ ਹੱਥ", "ਧੁੱਪ ਵਿੱਚ ਦਰੱਖਤ", "ਰੋਸ਼ਨੀ ਰੋਕਦੀ ਅਪਾਰਦਰਸ਼ੀ ਕਿਤਾਬ", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ ਪਰਦਾ"]
        a = st.selectbox(
            "Choose a light and shadow example" if not is_pa else "ਰੋਸ਼ਨੀ ਅਤੇ ਪਰਛਾਵੇਂ ਦੀ ਉਦਾਹਰਨ ਚੁਣੋ",
            shadow_examples,
            format_func=lambda x: shadow_examples_pa[shadow_examples.index(x)] if is_pa else x,
            key="physics_class6_shadow_example"
        )
        b = a
    elif force_examples_experiment:
        examples = ["Push a shopping cart", "Kick a football", "Pull a wagon", "Open a drawer"]
        punjabi_examples = ["ਖਰੀਦਦਾਰੀ ਵਾਲੀ ਗੱਡੀ ਨੂੰ ਧੱਕਾ", "ਫੁੱਟਬਾਲ ਨੂੰ ਲੱਤ ਮਾਰਨਾ", "ਗੱਡੇ ਨੂੰ ਖਿੱਚਣਾ", "ਦਰਾਜ਼ ਖੋਲ੍ਹਣਾ"]
        a = st.selectbox("Choose a force example" if not is_pa else "ਬਲ ਦੀ ਉਦਾਹਰਨ ਚੁਣੋ", examples, format_func=lambda x: (punjabi_examples[examples.index(x)] if is_pa else x), key="physics_class6_force_example")
        b = a
    elif slow_fast_experiment:
        a = st.selectbox(
            "Choose an example" if not is_pa else "ਉਦਾਹਰਨ ਚੁਣੋ",
            ["Slow motion", "Fast motion"],
            format_func=lambda x: (("ਹੌਲੀ ਗਤੀ" if x == "Slow motion" else "ਤੇਜ਼ ਗਤੀ") if is_pa else x),
            key="physics_class6_slow_fast_choice"
        )
        b = a
    elif class10_wave_sound_experiment:
        wave_sound_cases = ["Low pitch — long wavelength", "High pitch — short wavelength", "Soft sound — small amplitude", "Loud sound — large amplitude"]
        wave_sound_cases_pa = ["ਨੀਵੀਂ ਸੁਰ — ਲੰਮੀ ਤਰੰਗ-ਲੰਬਾਈ", "ਉੱਚੀ ਸੁਰ — ਛੋਟੀ ਤਰੰਗ-ਲੰਬਾਈ", "ਹੌਲੀ ਧੁਨੀ — ਛੋਟੀ ਐਂਪਲੀਟਿਊਡ", "ਉੱਚੀ ਧੁਨੀ — ਵੱਡੀ ਐਂਪਲੀਟਿਊਡ"]
        a = st.selectbox("Choose a wave property to explore" if not is_pa else "ਤਰੰਗ ਦੀ ਵਿਸ਼ੇਸ਼ਤਾ ਚੁਣੋ", wave_sound_cases, format_func=lambda x: wave_sound_cases_pa[wave_sound_cases.index(x)] if is_pa else x, key="physics_class10_wave_sound_case_" + st.session_state.language)
        b = a
    elif class10_work_power_energy_experiment:
        work_power_cases = ["Pushing a box and it moves", "Lifting a load", "Holding a box still", "Doing the same task quickly", "Doing the same task slowly"]
        work_power_cases_pa = ["ਡੱਬੇ ਨੂੰ ਧੱਕਣਾ ਅਤੇ ਇਸ ਦਾ ਚੱਲਣਾ", "ਭਾਰ ਨੂੰ ਉੱਪਰ ਚੁੱਕਣਾ", "ਡੱਬੇ ਨੂੰ ਸਥਿਰ ਫੜਨਾ", "ਉਹੀ ਕੰਮ ਜਲਦੀ ਕਰਨਾ", "ਉਹੀ ਕੰਮ ਹੌਲੀ ਕਰਨਾ"]
        a = st.selectbox("Choose a work and power situation" if not is_pa else "ਕੰਮ ਅਤੇ ਸ਼ਕਤੀ ਦੀ ਸਥਿਤੀ ਚੁਣੋ", work_power_cases, format_func=lambda x: work_power_cases_pa[work_power_cases.index(x)] if is_pa else x, key="physics_class10_work_power_case_" + st.session_state.language)
        b = a
    elif class10_convex_lens_experiment:
        lens_cases = ["Object beyond 2F", "Object at 2F", "Object between F and 2F", "Object at F", "Object between lens and F"]
        lens_cases_pa = ["ਵਸਤੂ 2F ਤੋਂ ਪਰੇ", "ਵਸਤੂ 2F ਉੱਤੇ", "ਵਸਤੂ F ਅਤੇ 2F ਵਿਚਕਾਰ", "ਵਸਤੂ F ਉੱਤੇ", "ਲੈਂਸ ਅਤੇ F ਵਿਚਕਾਰ ਵਸਤੂ"]
        a = st.selectbox("Choose object position" if not is_pa else "ਵਸਤੂ ਦੀ ਸਥਿਤੀ ਚੁਣੋ", lens_cases, format_func=lambda x: lens_cases_pa[lens_cases.index(x)] if is_pa else x, key="physics_class10_lens_case_" + st.session_state.language)
        b = a
    elif class10_refraction_experiment:
        refraction_scenarios = ["Air into glass", "Glass into air", "Light straight along the normal"]
        refraction_scenarios_pa = ["ਹਵਾ ਤੋਂ ਕੱਚ ਵਿੱਚ", "ਕੱਚ ਤੋਂ ਹਵਾ ਵਿੱਚ", "ਲੰਬ ਦੇ ਨਾਲ ਸਿੱਧੀ ਰੋਸ਼ਨੀ"]
        a = st.selectbox("Choose the light path" if not is_pa else "ਰੋਸ਼ਨੀ ਦਾ ਰਸਤਾ ਚੁਣੋ", refraction_scenarios, format_func=lambda x: refraction_scenarios_pa[refraction_scenarios.index(x)] if is_pa else x, key="physics_class10_refraction_path_" + st.session_state.language)
        b = a
    elif class10_reflection_experiment:
        reflection_scenarios = ["Shallow incident ray", "Medium incident ray", "Steep incident ray"]
        reflection_scenarios_pa = ["ਛੋਟੇ ਝੁਕਾਅ ਵਾਲੀ ਆਗਮਨ ਕਿਰਨ", "ਦਰਮਿਆਨੇ ਝੁਕਾਅ ਵਾਲੀ ਆਗਮਨ ਕਿਰਨ", "ਵੱਧ ਝੁਕਾਅ ਵਾਲੀ ਆਗਮਨ ਕਿਰਨ"]
        a = st.selectbox("Choose an incident ray" if not is_pa else "ਆਗਮਨ ਕਿਰਨ ਚੁਣੋ", reflection_scenarios, format_func=lambda x: reflection_scenarios_pa[reflection_scenarios.index(x)] if is_pa else x, key="physics_class10_reflection_scenario_" + st.session_state.language)
        b = a
    elif class9_gravity_experiment:
        gravity_scenarios = ["Ball at a high position", "Ball at a low position", "Ball falling"]
        gravity_scenarios_pa = ["ਉੱਚੀ ਥਾਂ ਉੱਤੇ ਗੇਂਦ", "ਨੀਵੀਂ ਥਾਂ ਉੱਤੇ ਗੇਂਦ", "ਡਿੱਗਦੀ ਹੋਈ ਗੇਂਦ"]
        a = st.selectbox("Choose a gravity situation" if not is_pa else "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਦੀ ਸਥਿਤੀ ਚੁਣੋ", gravity_scenarios, format_func=lambda x: gravity_scenarios_pa[gravity_scenarios.index(x)] if is_pa else x, key="physics_class9_gravity_situation_" + st.session_state.language)
        b = a
    elif class9_refraction_experiment:
        refraction_scenarios = ["Air to glass block", "Glass block to air"]
        refraction_scenarios_pa = ["ਹਵਾ ਤੋਂ ਕੱਚ ਦੇ ਬਲਾਕ ਵਿੱਚ", "ਕੱਚ ਦੇ ਬਲਾਕ ਤੋਂ ਹਵਾ ਵਿੱਚ"]
        a = st.selectbox("Choose the direction of light" if not is_pa else "ਰੋਸ਼ਨੀ ਦੀ ਦਿਸ਼ਾ ਚੁਣੋ", refraction_scenarios, format_func=lambda x: refraction_scenarios_pa[refraction_scenarios.index(x)] if is_pa else x, key="physics_class9_refraction_direction_" + st.session_state.language)
        b = a
    elif class9_work_energy_experiment:
        work_scenarios = ["Pushing a box forward", "Lifting a box upward", "Holding a box still"]
        work_scenarios_pa = ["ਅੱਗੇ ਵੱਲ ਡੱਬੇ ਨੂੰ ਧੱਕਣਾ", "ਡੱਬੇ ਨੂੰ ਉੱਪਰ ਚੁੱਕਣਾ", "ਡੱਬੇ ਨੂੰ ਸਥਿਰ ਫੜਨਾ"]
        a = st.selectbox("Choose a work-and-energy situation" if not is_pa else "ਕੰਮ ਅਤੇ ਊਰਜਾ ਦੀ ਸਥਿਤੀ ਚੁਣੋ", work_scenarios, format_func=lambda x: work_scenarios_pa[work_scenarios.index(x)] if is_pa else x, key="physics_class9_work_energy_scenario_" + st.session_state.language)
        b = a
    elif class9_newton_experiment:
        push_levels = ["Gentle push", "Strong push"]
        mass_levels = ["Light cart", "Loaded cart"]
        a = st.selectbox("Choose push strength" if not is_pa else "ਧੱਕੇ ਦੀ ਤਾਕਤ ਚੁਣੋ", push_levels, format_func=lambda x: ({"Gentle push":"ਹਲਕਾ ਧੱਕਾ","Strong push":"ਜ਼ੋਰਦਾਰ ਧੱਕਾ"}[x] if is_pa else x), key="physics_class9_newton_push_" + st.session_state.language)
        b = st.selectbox("Choose cart load" if not is_pa else "ਗੱਡੀ ਦਾ ਭਾਰ ਚੁਣੋ", mass_levels, format_func=lambda x: ({"Light cart":"ਹਲਕੀ ਗੱਡੀ","Loaded cart":"ਭਾਰ ਵਾਲੀ ਗੱਡੀ"}[x] if is_pa else x), key="physics_class9_newton_mass_" + st.session_state.language)
    elif class9_speed_acceleration_experiment:
        motion_examples = ["Starting from rest and speeding up", "Moving at steady speed", "Slowing down", "Changing direction"]
        motion_examples_pa = ["ਆਰਾਮ ਤੋਂ ਚੱਲ ਕੇ ਤੇਜ਼ ਹੋਣਾ", "ਇਕਸਾਰ ਚਾਲ ਨਾਲ ਚੱਲਣਾ", "ਹੌਲਾ ਹੋਣਾ", "ਦਿਸ਼ਾ ਬਦਲਣਾ"]
        a = st.selectbox("Choose a motion example" if not is_pa else "ਗਤੀ ਦੀ ਉਦਾਹਰਨ ਚੁਣੋ", motion_examples, format_func=lambda x: motion_examples_pa[motion_examples.index(x)] if is_pa else x, key="physics_class9_motion_example_" + st.session_state.language)
        b = a
    else:
        c1, c2 = st.columns(2)
        with c1:
            if kind == "magnet":
                a = st.selectbox(labels[0] if not is_pa else labels[2], ["Unlike poles","Like poles"], key=f"ph_a_{pc}_{ei}")
            elif kind == "heat":
                a = st.slider(labels[0] if not is_pa else labels[2], 1, 10, 5, key=f"ph_a_{pc}_{ei}")
            elif kind in ("motion","speed","force","pressure","pressure_area","balanced","friction","acceleration","newton","work","potential","lens"):
                a = st.slider(labels[0] if not is_pa else labels[2], 1, 100 if kind in ("motion","speed") else 30, 10, key=f"ph_a_{pc}_{ei}")
            elif kind in ("reflection","refraction"):
                a = st.slider(labels[0] if not is_pa else labels[2], 5, 80, 35, key=f"ph_a_{pc}_{ei}")
            elif kind in ("sound","wave"):
                a = st.slider(labels[0] if not is_pa else labels[2], 100, 2000, 500, 100, key=f"ph_a_{pc}_{ei}")
            elif kind == "shadow":
                a = st.slider(labels[0] if not is_pa else labels[2], 10, 100, 40, key=f"ph_a_{pc}_{ei}")
            else:
                a = st.slider(labels[0] if not is_pa else labels[2], 1, 20, 5, key=f"ph_a_{pc}_{ei}")
        with c2:
            if kind == "magnet":
                b = st.slider(labels[1] if not is_pa else labels[3], 1, 10, 5, key=f"ph_b_{pc}_{ei}")
            elif kind == "heat":
                b = st.selectbox(labels[1] if not is_pa else labels[3], ["Copper","Aluminium","Glass","Wood"], key=f"ph_b_{pc}_{ei}")
            elif kind in ("motion","speed","force","pressure","pressure_area","balanced","friction","acceleration","newton","work","potential","lens"):
                b = st.slider(labels[1] if not is_pa else labels[3], 1, 50, 5, key=f"ph_b_{pc}_{ei}")
            elif kind in ("reflection","refraction"):
                b = st.slider(labels[1] if not is_pa else labels[3], 1, 2, 1, key=f"ph_b_{pc}_{ei}") if kind == "reflection" else st.slider(labels[1] if not is_pa else labels[3], 1.0, 2.0, 1.5, 0.1, key=f"ph_b_{pc}_{ei}")
            else:
                b = st.slider(labels[1] if not is_pa else labels[3], 1, 10, 5, key=f"ph_b_{pc}_{ei}")
    if kind in ("sound","wave") and not class10_wave_sound_experiment:
        c = st.slider("Amplitude (relative)" if not is_pa else "ਐਂਪਲੀਟਿਊਡ (ਸਾਪੇਖ)", 1, 10, 5, key=f"ph_c_{pc}_{ei}")
    elif kind in ("reflection","refraction"):
        c = 0
    else:
        c = b
    # Produce a distinct, responsive schematic for the selected phenomenon.
    # Class 10 lens case is an independent if branch, not an elif without a parent.
    visual = ""
    if class10_wave_sound_experiment:
        wave_heading = "WAVE FREQUENCY AND SOUND" if not is_pa else "ਤਰੰਗ ਆਵ੍ਰਿਤੀ ਅਤੇ ਧੁਨੀ"
        if a.startswith("Low pitch"):
            cycles, amp = 3, 20
            property_label = "LOW PITCH · LONG WAVELENGTH" if not is_pa else "ਨੀਵੀਂ ਸੁਰ · ਲੰਮੀ ਤਰੰਗ-ਲੰਬਾਈ"
            compressions = [65, 150, 235, 320, 405]
        elif a.startswith("High pitch"):
            cycles, amp = 8, 20
            property_label = "HIGH PITCH · SHORT WAVELENGTH" if not is_pa else "ਉੱਚੀ ਸੁਰ · ਛੋਟੀ ਤਰੰਗ-ਲੰਬਾਈ"
            compressions = [55, 95, 135, 175, 215, 255, 295, 335, 375, 415]
        elif a.startswith("Soft sound"):
            cycles, amp = 5, 8
            property_label = "SOFT SOUND · SMALL AMPLITUDE" if not is_pa else "ਹੌਲੀ ਧੁਨੀ · ਛੋਟੀ ਐਂਪਲੀਟਿਊਡ"
            compressions = [65, 115, 165, 215, 265, 315, 365, 415]
        else:
            cycles, amp = 5, 29
            property_label = "LOUD SOUND · LARGE AMPLITUDE" if not is_pa else "ਉੱਚੀ ਧੁਨੀ · ਵੱਡੀ ਐਂਪਲੀਟਿਊਡ"
            compressions = [65, 115, 165, 215, 265, 315, 365, 415]
        wave_points = " ".join(f"{x},{105-amp*__import__('math').sin((x-25)*cycles*2*3.14159/390):.1f}" for x in range(25, 436, 3))
        compression_marks = "".join(f'<path d="M{x} 151 V188 M{x+5} 151 V188 M{x+10} 151 V188" stroke="#0ea5e9" stroke-width="2.5" stroke-linecap="round"/>' for x in compressions)
        wave_caption = "TRANSVERSE WAVE: FREQUENCY / AMPLITUDE" if not is_pa else "ਅਨੁਪ੍ਰਸਥ ਤਰੰਗ: ਆਵ੍ਰਿਤੀ / ਐਂਪਲੀਟਿਊਡ"
        sound_caption = "SOUND IN AIR: COMPRESSIONS AND RAREFACTIONS" if not is_pa else "ਹਵਾ ਵਿੱਚ ਧੁਨੀ: ਸੰਘਣਨ ਅਤੇ ਵਿਰਲਨ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="29" text-anchor="middle" font-size="13" font-weight="700" fill="#334155">{wave_heading}</text><text x="28" y="49" font-size="10" font-weight="700" fill="#0369a1">{wave_caption}</text><path d="M25 82 H435" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/><polyline points="{wave_points}" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-linejoin="round"/><text x="28" y="132" font-size="10" font-weight="700" fill="#0369a1">{sound_caption}</text><path d="M25 170 H435" stroke="#94a3b8" stroke-width="1.5"/>{compression_marks}<text x="230" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">{property_label}</text>'
    elif class10_work_power_energy_experiment:
        work_heading = "WORK, POWER AND ENERGY" if not is_pa else "ਕੰਮ, ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ"
        person = '<circle cx="65" cy="105" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M65 118 V153 M65 128 L88 143 L105 143 M65 153 L51 176 M65 153 L80 176" stroke="#2563eb" stroke-width="7" stroke-linecap="round" fill="none"/>'
        box_shape = '<rect x="108" y="121" width="58" height="43" rx="4" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M116 129 L158 156 M158 129 L116 156" stroke="#a16207" stroke-width="2"/>'
        if a == "Pushing a box and it moves":
            action = '<path d="M90 142 H106 M99 134 L108 142 L99 150" stroke="#16a34a" stroke-width="4" fill="none"/>'
            scene = "FORCE + DISPLACEMENT = WORK" if not is_pa else "ਬਲ + ਵਿਸਥਾਪਨ = ਕੰਮ"
            extra = '<path d="M180 176 H330 M320 166 L332 176 L320 186" stroke="#16a34a" stroke-width="4" fill="none"/><rect x="250" y="127" width="58" height="43" rx="4" fill="#c08457" stroke="#854d0e" stroke-width="3"/>'
        elif a == "Lifting a load":
            action = '<path d="M139 118 V73 M129 84 L139 71 L149 84" stroke="#16a34a" stroke-width="4" fill="none"/>'
            scene = "WORK DONE AGAINST GRAVITY" if not is_pa else "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਦੇ ਵਿਰੁੱਧ ਕੰਮ"
            extra = '<path d="M115 83 H163 V117 H115 Z" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M139 67 V52" stroke="#64748b" stroke-width="3"/>'
        elif a == "Holding a box still":
            action = '<path d="M102 141 H111 M105 134 L112 141 L105 148" stroke="#64748b" stroke-width="3" fill="none"/>'
            scene = "NO DISPLACEMENT · NO WORK ON THE BOX" if not is_pa else "ਵਿਸਥਾਪਨ ਨਹੀਂ · ਡੱਬੇ ਉੱਤੇ ਕੰਮ ਨਹੀਂ"
            extra = '<path d="M180 120 V165 M170 130 L180 118 L190 130 M170 155 L180 167 L190 155" stroke="#7c3aed" stroke-width="3" fill="none"/>'
        elif a == "Doing the same task quickly":
            action = '<path d="M92 142 H106 M99 134 L108 142 L99 150" stroke="#16a34a" stroke-width="4" fill="none"/>'
            scene = "SAME WORK IN LESS TIME · GREATER POWER" if not is_pa else "ਉਹੀ ਕੰਮ ਘੱਟ ਸਮੇਂ ਵਿੱਚ · ਵੱਧ ਸ਼ਕਤੀ"
            extra = '<circle cx="285" cy="140" r="27" fill="#dcfce7" stroke="#16a34a" stroke-width="3"/><path d="M285 140 L285 120 M285 140 L301 149" stroke="#15803d" stroke-width="3" fill="none"/><path d="M325 140 H365 M355 130 L367 140 L355 150" stroke="#16a34a" stroke-width="4" fill="none"/>'
        else:
            action = '<path d="M92 142 H106 M99 134 L108 142 L99 150" stroke="#f59e0b" stroke-width="3" fill="none"/>'
            scene = "SAME WORK IN MORE TIME · LOWER POWER" if not is_pa else "ਉਹੀ ਕੰਮ ਵੱਧ ਸਮੇਂ ਵਿੱਚ · ਘੱਟ ਸ਼ਕਤੀ"
            extra = '<circle cx="285" cy="140" r="27" fill="#fef3c7" stroke="#d97706" stroke-width="3"/><path d="M285 140 L285 120 M285 140 L301 149" stroke="#b45309" stroke-width="3" fill="none"/><path d="M325 140 H365 M355 130 L367 140 L355 150" stroke="#d97706" stroke-width="4" fill="none"/>'
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{work_heading}</text><path d="M30 180 H420" stroke="#94a3b8" stroke-width="3"/>{person}{box_shape}{action}{extra}<text x="230" y="204" text-anchor="middle" font-size="10" font-weight="700" fill="#0f766e">{scene}</text>'
    elif class10_convex_lens_experiment:
        lens_heading = "CONVEX LENS: IMAGE FORMATION" if not is_pa else "ਉੱਤਲ ਲੈਂਸ: ਪ੍ਰਤਿਬਿੰਬ ਬਣਨਾ"
        axis = '<path d="M28 142 H432" stroke="#64748b" stroke-width="2"/><path d="M424 136 L434 142 L424 148" stroke="#64748b" stroke-width="2" fill="none"/>'
        lens_shape = '<path d="M230 43 Q195 142 230 225 Q265 142 230 43" fill="#bae6fd" fill-opacity=".75" stroke="#0284c7" stroke-width="3"/>'
        markers = '<path d="M160 75 V205 M300 75 V205 M90 92 V192 M370 92 V192" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 4"/><text x="160" y="68" text-anchor="middle" font-size="11" fill="#475569">F</text><text x="300" y="68" text-anchor="middle" font-size="11" fill="#475569">F</text><text x="90" y="85" text-anchor="middle" font-size="11" fill="#475569">2F</text><text x="370" y="85" text-anchor="middle" font-size="11" fill="#475569">2F</text>'
        if a == "Object beyond 2F":
            obj_x, img_x, image_y = 60, 340, 192
            image_label = "REAL · INVERTED · SMALLER" if not is_pa else "ਅਸਲੀ · ਉਲਟਾ · ਛੋਟਾ"
            rays = '<path d="M60 92 L230 92 L340 112" stroke="#f59e0b" stroke-width="2.5" fill="none"/><path d="M60 92 L230 192 L340 112" stroke="#0ea5e9" stroke-width="2.5" fill="none"/>'
        elif a == "Object at 2F":
            obj_x, img_x, image_y = 90, 370, 192
            image_label = "REAL · INVERTED · SAME SIZE" if not is_pa else "ਅਸਲੀ · ਉਲਟਾ · ਬਰਾਬਰ ਆਕਾਰ"
            rays = '<path d="M90 92 L230 92 L370 92" stroke="#f59e0b" stroke-width="2.5" fill="none"/><path d="M90 92 L230 192 L370 192" stroke="#0ea5e9" stroke-width="2.5" fill="none"/>'
        elif a == "Object between F and 2F":
            obj_x, img_x, image_y = 125, 405, 219
            image_label = "REAL · INVERTED · LARGER" if not is_pa else "ਅਸਲੀ · ਉਲਟਾ · ਵੱਡਾ"
            rays = '<path d="M125 92 L230 92 L405 65" stroke="#f59e0b" stroke-width="2.5" fill="none"/><path d="M125 92 L230 192 L405 65" stroke="#0ea5e9" stroke-width="2.5" fill="none"/>'
        elif a == "Object at F":
            obj_x, img_x, image_y = 160, 410, 192
            image_label = "IMAGE AT INFINITY · RAYS PARALLEL" if not is_pa else "ਪ੍ਰਤਿਬਿੰਬ ਅਨੰਤ ਉੱਤੇ · ਕਿਰਨਾਂ ਸਮਾਂਤਰ"
            rays = '<path d="M160 92 L230 92 L410 92" stroke="#f59e0b" stroke-width="2.5" fill="none"/><path d="M160 92 L230 192 L410 192" stroke="#0ea5e9" stroke-width="2.5" fill="none"/>'
        else:
            obj_x, img_x, image_y = 195, 125, 65
            image_label = "VIRTUAL · UPRIGHT · MAGNIFIED" if not is_pa else "ਆਭਾਸੀ · ਸਿੱਧਾ · ਵੱਡਾ"
            rays = '<path d="M195 92 L230 92 L405 65" stroke="#f59e0b" stroke-width="2.5" fill="none"/><path d="M195 92 L230 192 L405 192" stroke="#0ea5e9" stroke-width="2.5" fill="none" stroke-dasharray="5 4"/><path d="M230 92 L125 65 M230 192 L125 65" stroke="#7c3aed" stroke-width="2" fill="none" stroke-dasharray="5 4"/>'
        object_arrow = f'<path d="M{obj_x} 142 V92 M{obj_x-7} 102 L{obj_x} 90 L{obj_x+7} 102" stroke="#16a34a" stroke-width="4" fill="none"/>'
        if a == "Object at F":
            image_arrow = '<path d="M370 92 H420 M410 84 L422 92 L410 100" stroke="#7c3aed" stroke-width="3" fill="none"/>'
        else:
            tip_y = image_y
            tail_y = image_y + 28 if image_y < 142 else image_y - 28
            image_arrow = f'<path d="M{img_x} {tail_y} V{tip_y} M{img_x-7} {tip_y+8 if tip_y < tail_y else tip_y-8} L{img_x} {tip_y} L{img_x+7} {tip_y+8 if tip_y < tail_y else tip_y-8}" stroke="#dc2626" stroke-width="4" fill="none"/>'
        object_tag = "OBJECT" if not is_pa else "ਵਸਤੂ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#334155">{lens_heading}</text>{axis}{markers}{lens_shape}{rays}{object_arrow}{image_arrow}<text x="{obj_x}" y="165" text-anchor="middle" font-size="10" font-weight="700" fill="#15803d">{object_tag}</text><text x="230" y="211" text-anchor="middle" font-size="10" font-weight="700" fill="#0f766e">{image_label}</text>'
    elif class9_speed_acceleration_experiment:
        if a == "Starting from rest and speeding up":
            motion_arrows = '<path d="M145 112 H195 M185 102 L197 112 L185 122 M220 112 H270 M260 102 L272 112 L260 122" stroke="#16a34a" stroke-width="4" fill="none"/>'
            scene_label = "SPEEDING UP · SPACING GROWS" if not is_pa else "ਤੇਜ਼ ਹੋਣਾ · ਦੂਰੀ ਵਧਦੀ ਹੈ"
            positions = '<circle cx="65" cy="145" r="5" fill="#0ea5e9"/><circle cx="100" cy="145" r="5" fill="#0ea5e9"/><circle cx="155" cy="145" r="5" fill="#0ea5e9"/><circle cx="235" cy="145" r="5" fill="#0ea5e9"/>'
        elif a == "Moving at steady speed":
            motion_arrows = '<path d="M145 112 H185 M175 102 L187 112 L175 122 M220 112 H260 M250 102 L262 112 L250 122" stroke="#0ea5e9" stroke-width="4" fill="none"/>'
            scene_label = "STEADY SPEED · EQUAL SPACING" if not is_pa else "ਇਕਸਾਰ ਚਾਲ · ਬਰਾਬਰ ਦੂਰੀ"
            positions = '<circle cx="65" cy="145" r="5" fill="#0ea5e9"/><circle cx="115" cy="145" r="5" fill="#0ea5e9"/><circle cx="165" cy="145" r="5" fill="#0ea5e9"/><circle cx="215" cy="145" r="5" fill="#0ea5e9"/>'
        elif a == "Slowing down":
            motion_arrows = '<path d="M145 112 H165 M155 102 L167 112 L155 122 M220 112 H240 M230 102 L242 112 L230 122" stroke="#f59e0b" stroke-width="4" fill="none"/>'
            scene_label = "SLOWING DOWN · SPACING SHRINKS" if not is_pa else "ਹੌਲਾ ਹੋਣਾ · ਦੂਰੀ ਘਟਦੀ ਹੈ"
            positions = '<circle cx="65" cy="145" r="5" fill="#0ea5e9"/><circle cx="145" cy="145" r="5" fill="#0ea5e9"/><circle cx="185" cy="145" r="5" fill="#0ea5e9"/><circle cx="210" cy="145" r="5" fill="#0ea5e9"/>'
        else:
            motion_arrows = '<path d="M145 112 H185 M175 102 L187 112 L175 122" stroke="#7c3aed" stroke-width="4" fill="none"/><path d="M210 126 L230 146 M220 146 H232 V134" stroke="#7c3aed" stroke-width="4" fill="none"/>'
            scene_label = "DIRECTION CHANGES · VELOCITY CHANGES" if not is_pa else "ਦਿਸ਼ਾ ਬਦਲਦੀ ਹੈ · ਵੇਗ ਬਦਲਦਾ ਹੈ"
            positions = '<circle cx="65" cy="145" r="5" fill="#0ea5e9"/><circle cx="115" cy="145" r="5" fill="#0ea5e9"/><circle cx="165" cy="145" r="5" fill="#0ea5e9"/><circle cx="215" cy="145" r="5" fill="#7c3aed"/>'
        heading = "MOTION AND ACCELERATION" if not is_pa else "ਗਤੀ ਅਤੇ ਤਵਰਣ"
        road_label = "Vehicle positions (illustrative)" if not is_pa else "ਵਾਹਨ ਦੀਆਂ ਸਥਿਤੀਆਂ (ਸਮਝਾਉਣ ਲਈ)"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="32" text-anchor="middle" fill="#334155" font-size="14" font-weight="700">{heading}</text><path d="M30 150 H420" stroke="#64748b" stroke-width="3" stroke-dasharray="10 7"/>{positions}<rect x="92" y="75" width="78" height="35" rx="8" fill="#60a5fa" stroke="#1d4ed8" stroke-width="2"/><rect x="104" y="81" width="22" height="12" rx="2" fill="#dbeafe"/><rect x="132" y="81" width="22" height="12" rx="2" fill="#dbeafe"/><circle cx="108" cy="112" r="8" fill="#334155"/><circle cx="154" cy="112" r="8" fill="#334155"/>{motion_arrows}<text x="230" y="177" text-anchor="middle" fill="#334155" font-size="12">{road_label}</text><text x="230" y="201" text-anchor="middle" fill="#0f766e" font-size="13" font-weight="700">{scene_label}</text>'
    elif class10_refraction_experiment:
        if a == "Air into glass":
            path_label = "AIR → GLASS: BENDS TOWARD NORMAL" if not is_pa else "ਹਵਾ → ਕੱਚ: ਲੰਬ ਵੱਲ ਮੁੜਦੀ ਹੈ"
            ray_paths = '<path d="M55 55 L220 115 L255 178" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M241 173 L256 180 L254 162" stroke="#f59e0b" stroke-width="3" fill="none"/>'
            media_labels = '<text x="65" y="83" font-size="12" fill="#075985">AIR</text><text x="75" y="177" font-size="12" fill="#075985">GLASS</text>'
        elif a == "Glass into air":
            path_label = "GLASS → AIR: BENDS AWAY FROM NORMAL" if not is_pa else "ਕੱਚ → ਹਵਾ: ਲੰਬ ਤੋਂ ਦੂਰ ਮੁੜਦੀ ਹੈ"
            ray_paths = '<path d="M55 178 L220 115 L365 45" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M346 47 L366 44 L357 62" stroke="#f59e0b" stroke-width="3" fill="none"/>'
            media_labels = '<text x="65" y="83" font-size="12" fill="#075985">AIR</text><text x="75" y="177" font-size="12" fill="#075985">GLASS</text>'
        else:
            path_label = "ALONG THE NORMAL: NO CHANGE IN DIRECTION" if not is_pa else "ਲੰਬ ਦੇ ਨਾਲ: ਦਿਸ਼ਾ ਨਹੀਂ ਬਦਲਦੀ"
            ray_paths = '<path d="M220 42 V188" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M211 173 L220 190 L229 173" stroke="#f59e0b" stroke-width="3" fill="none"/>'
            media_labels = '<text x="65" y="83" font-size="12" fill="#075985">AIR</text><text x="75" y="177" font-size="12" fill="#075985">GLASS</text>'
        refraction_heading = "REFRACTION OF LIGHT" if not is_pa else "ਰੋਸ਼ਨੀ ਦਾ ਅਪਵਰਤਨ"
        normal_label = "NORMAL" if not is_pa else "ਲੰਬ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{refraction_heading}</text><rect x="38" y="110" width="394" height="82" rx="3" fill="#bae6fd" fill-opacity=".55" stroke="#0284c7" stroke-width="2"/><path d="M220 40 V200" stroke="#64748b" stroke-width="2" stroke-dasharray="6 5"/><text x="229" y="51" font-size="10" fill="#475569">{normal_label}</text>{media_labels}{ray_paths}<circle cx="220" cy="115" r="5" fill="#dc2626"/><text x="230" y="211" text-anchor="middle" font-size="10" font-weight="700" fill="#0f766e">{path_label}</text>'
    elif class10_reflection_experiment:
        if a == "Shallow incident ray":
            ray_start_x, ray_start_y = 65, 82
        elif a == "Medium incident ray":
            ray_start_x, ray_start_y = 65, 48
        else:
            ray_start_x, ray_start_y = 110, 38
        reflected_end_x = 440 - ray_start_x
        reflected_end_y = ray_start_y
        reflection_heading = "REFLECTION OF LIGHT — PLANE MIRROR" if not is_pa else "ਸਮਤਲ ਸ਼ੀਸ਼ੇ ਤੋਂ ਰੋਸ਼ਨੀ ਦਾ ਪਰਾਵਰਤਨ"
        incident_label = "INCIDENT RAY" if not is_pa else "ਆਗਮਨ ਕਿਰਨ"
        reflected_label = "REFLECTED RAY" if not is_pa else "ਪਰਾਵਰਤਿਤ ਕਿਰਨ"
        normal_label = "NORMAL" if not is_pa else "ਲੰਬ"
        law_label = "ANGLE OF INCIDENCE = ANGLE OF REFLECTION" if not is_pa else "ਆਗਮਨ ਕੋਣ = ਪਰਾਵਰਤਨ ਕੋਣ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#334155">{reflection_heading}</text><rect x="42" y="144" width="376" height="8" rx="3" fill="#94a3b8" stroke="#475569" stroke-width="1"/><path d="M220 43 V193" stroke="#64748b" stroke-width="2" stroke-dasharray="6 5"/><text x="229" y="53" font-size="10" fill="#475569">{normal_label}</text><path d="M{ray_start_x} {ray_start_y} L220 145" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M220 145 L{reflected_end_x} {reflected_end_y}" stroke="#0ea5e9" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M{ray_start_x+10} {ray_start_y+4} L{ray_start_x} {ray_start_y} L{ray_start_x+3} {ray_start_y+12}" stroke="#f59e0b" stroke-width="3" fill="none"/><path d="M{reflected_end_x-13} {reflected_end_y+2} L{reflected_end_x} {reflected_end_y} L{reflected_end_x-4} {reflected_end_y+13}" stroke="#0ea5e9" stroke-width="3" fill="none"/><path d="M190 116 A40 40 0 0 1 220 105" stroke="#f59e0b" stroke-width="2" fill="none"/><path d="M220 105 A40 40 0 0 1 250 116" stroke="#0ea5e9" stroke-width="2" fill="none"/><text x="78" y="65" font-size="10" font-weight="700" fill="#b45309">{incident_label}</text><text x="320" y="65" font-size="10" font-weight="700" fill="#0369a1">{reflected_label}</text><text x="230" y="202" text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">{law_label}</text>'
    elif class9_gravity_experiment:
        if a == "Ball at a high position":
            ball_y = 70
            ball_color = "#f97316"
            scene_label = "MORE GRAVITATIONAL POTENTIAL ENERGY" if not is_pa else "ਵੱਧ ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ"
            object_motion = '<path d="M118 87 V132 M108 121 L118 134 L128 121" stroke="#dc2626" stroke-width="3" fill="none" stroke-linecap="round"/>'
        elif a == "Ball at a low position":
            ball_y = 143
            ball_color = "#f97316"
            scene_label = "LESS GRAVITATIONAL POTENTIAL ENERGY" if not is_pa else "ਘੱਟ ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ"
            object_motion = '<path d="M118 158 V180 M108 170 L118 182 L128 170" stroke="#dc2626" stroke-width="3" fill="none" stroke-linecap="round"/>'
        else:
            ball_y = 92
            ball_color = "#f97316"
            scene_label = "GRAVITY PULLS THE BALL DOWNWARD" if not is_pa else "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਗੇਂਦ ਨੂੰ ਹੇਠਾਂ ਖਿੱਚਦਾ ਹੈ"
            object_motion = '<path d="M118 111 V163 M108 151 L118 165 L128 151" stroke="#dc2626" stroke-width="4" fill="none" stroke-linecap="round"/>'
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{("GRAVITY AND GRAVITATIONAL POTENTIAL ENERGY" if not is_pa else "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਅਤੇ ਸਥਿਤਿਜ ਊਰਜਾ")}</text><path d="M45 190 H420" stroke="#64748b" stroke-width="4"/><path d="M45 116 H168 V190" stroke="#94a3b8" stroke-width="3" fill="none"/><path d="M45 116 H168" stroke="#64748b" stroke-width="5"/><circle cx="118" cy="{ball_y}" r="17" fill="{ball_color}" stroke="#9a3412" stroke-width="3"/><path d="M112 {ball_y-5} Q118 {ball_y-14} 125 {ball_y-4}" stroke="#fed7aa" stroke-width="3" fill="none"/>{object_motion}<path d="M235 61 V140 M225 128 L235 142 L245 128" stroke="#7c3aed" stroke-width="4" fill="none" stroke-linecap="round"/><text x="270" y="82" font-size="12" font-weight="700" fill="#6d28d9">{("GRAVITY" if not is_pa else "ਗੁਰੁਤਵਾਕਰਸ਼ਣ")}</text><text x="280" y="101" font-size="11" fill="#334155">{("Pulls objects toward Earth" if not is_pa else "ਵਸਤੂਆਂ ਨੂੰ ਧਰਤੀ ਵੱਲ ਖਿੱਚਦਾ ਹੈ")}</text><text x="235" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">{scene_label}</text>'
    elif class9_refraction_experiment:
        if a == "Air to glass block":
            ray_label = "AIR → GLASS: BENDS TOWARD NORMAL" if not is_pa else "ਹਵਾ → ਕੱਚ: ਲੰਬ ਵੱਲ ਮੁੜਦੀ ਹੈ"
            incident_color = "#f59e0b"
            refracted_color = "#0ea5e9"
            refracted_path = '<path d="M65 58 L220 135 L272 175" stroke="#0ea5e9" stroke-width="4" fill="none" stroke-linecap="round"/>'
            arrow_head = '<path d="M258 171 L274 176 L269 160" stroke="#0ea5e9" stroke-width="4" fill="none"/>'
        else:
            ray_label = "GLASS → AIR: BENDS AWAY FROM NORMAL" if not is_pa else "ਕੱਚ → ਹਵਾ: ਲੰਬ ਤੋਂ ਦੂਰ ਮੁੜਦੀ ਹੈ"
            incident_color = "#f59e0b"
            refracted_color = "#0ea5e9"
            refracted_path = '<path d="M220 135 L360 65" stroke="#0ea5e9" stroke-width="4" fill="none" stroke-linecap="round"/>'
            arrow_head = '<path d="M342 67 L362 64 L352 82" stroke="#0ea5e9" stroke-width="4" fill="none"/>'
        incident_path = '<path d="M65 58 L220 135" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M207 126 L221 136 L216 119" stroke="#f59e0b" stroke-width="4" fill="none"/>' if a == "Air to glass block" else '<path d="M65 205 L220 135" stroke="#f59e0b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M205 143 L221 135 L203 131" stroke="#f59e0b" stroke-width="4" fill="none"/>'
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{("REFRACTION OF LIGHT THROUGH A GLASS BLOCK" if not is_pa else "ਕੱਚ ਦੇ ਬਲਾਕ ਵਿੱਚ ਰੋਸ਼ਨੀ ਦਾ ਅਪਵਰਤਨ")}</text><rect x="70" y="82" width="320" height="112" rx="4" fill="#bae6fd" fill-opacity=".55" stroke="#0284c7" stroke-width="2"/><text x="92" y="101" font-size="11" fill="#075985">{("GLASS BLOCK" if not is_pa else "ਕੱਚ ਦਾ ਬਲਾਕ")}</text><path d="M220 45 V207" stroke="#64748b" stroke-width="2" stroke-dasharray="6 5"/><text x="229" y="53" font-size="11" fill="#475569">{("NORMAL" if not is_pa else "ਲੰਬ")}</text>{incident_path}{refracted_path}{arrow_head}<circle cx="220" cy="135" r="5" fill="#dc2626"/><text x="62" y="47" font-size="11" font-weight="700" fill="#b45309">{("INCIDENT RAY" if not is_pa else "ਆਗਮਨ ਕਿਰਨ")}</text><text x="230" y="211" text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">{ray_label}</text>'
    elif class10_refraction_experiment:
        if a == "Air into glass":
            result = ("When light enters glass from air at an angle, it slows down and bends towards the normal." if not is_pa else "ਜਦੋਂ ਰੋਸ਼ਨੀ ਕੋਣ ਨਾਲ ਹਵਾ ਤੋਂ ਕੱਚ ਵਿੱਚ ਜਾਂਦੀ ਹੈ, ਇਸ ਦੀ ਗਤੀ ਘਟਦੀ ਹੈ ਅਤੇ ਕਿਰਨ ਲੰਬ ਵੱਲ ਮੁੜਦੀ ਹੈ।")
        elif a == "Glass into air":
            result = ("When light travels from glass into air at an angle, it speeds up and bends away from the normal." if not is_pa else "ਜਦੋਂ ਰੋਸ਼ਨੀ ਕੋਣ ਨਾਲ ਕੱਚ ਤੋਂ ਹਵਾ ਵਿੱਚ ਜਾਂਦੀ ਹੈ, ਇਸ ਦੀ ਗਤੀ ਵਧਦੀ ਹੈ ਅਤੇ ਕਿਰਨ ਲੰਬ ਤੋਂ ਦੂਰ ਮੁੜਦੀ ਹੈ।")
        else:
            result = ("A ray travelling along the normal enters the new medium without changing direction." if not is_pa else "ਲੰਬ ਦੇ ਨਾਲ ਆਉਣ ਵਾਲੀ ਕਿਰਨ ਨਵੇਂ ਮਾਧਿਅਮ ਵਿੱਚ ਦਿਸ਼ਾ ਬਦਲੇ ਬਿਨਾਂ ਜਾਂਦੀ ਹੈ।")
    elif class10_reflection_experiment:
        result = ("The incident ray strikes the plane mirror and reflects on the other side of the normal. The reflected ray makes the same angle with the normal as the incident ray. The mirror, incident ray, reflected ray and normal lie in the same plane." if not is_pa else "ਆਗਮਨ ਕਿਰਨ ਸਮਤਲ ਸ਼ੀਸ਼ੇ ਨਾਲ ਟਕਰਾ ਕੇ ਲੰਬ ਦੇ ਦੂਜੇ ਪਾਸੇ ਪਰਾਵਰਤਿਤ ਹੁੰਦੀ ਹੈ। ਪਰਾਵਰਤਨ ਕੋਣ, ਆਗਮਨ ਕੋਣ ਦੇ ਬਰਾਬਰ ਹੁੰਦਾ ਹੈ। ਸ਼ੀਸ਼ਾ, ਆਗਮਨ ਕਿਰਨ, ਪਰਾਵਰਤਿਤ ਕਿਰਨ ਅਤੇ ਲੰਬ ਇੱਕੋ ਸਮਤਲ ਵਿੱਚ ਹੁੰਦੇ ਹਨ।")
    elif class9_gravity_experiment:
        if a == "Ball at a high position":
            result = ("The ball is higher above the ground, so it has more gravitational potential energy. If released, gravity pulls it downward." if not is_pa else "ਗੇਂਦ ਜ਼ਮੀਨ ਤੋਂ ਵੱਧ ਉਚਾਈ ਉੱਤੇ ਹੈ, ਇਸ ਲਈ ਇਸ ਦੀ ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ ਵੱਧ ਹੈ। ਛੱਡਣ ਉੱਤੇ ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਇਸ ਨੂੰ ਹੇਠਾਂ ਖਿੱਚੇਗਾ।")
        elif a == "Ball at a low position":
            result = ("Near the ground, the ball has less gravitational potential energy than it would at a higher position." if not is_pa else "ਜ਼ਮੀਨ ਦੇ ਨੇੜੇ ਗੇਂਦ ਦੀ ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ ਉੱਚੀ ਥਾਂ ਨਾਲੋਂ ਘੱਟ ਹੁੰਦੀ ਹੈ।")
        else:
            result = ("Gravity pulls the ball downward. As it falls, gravitational potential energy is transferred mainly into kinetic energy." if not is_pa else "ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਗੇਂਦ ਨੂੰ ਹੇਠਾਂ ਖਿੱਚਦਾ ਹੈ। ਡਿੱਗਣ ਸਮੇਂ ਸਥਿਤਿਜ ਊਰਜਾ ਮੁੱਖ ਤੌਰ ਉੱਤੇ ਗਤੀ ਊਰਜਾ ਵਿੱਚ ਬਦਲਦੀ ਹੈ।")
    elif class9_refraction_experiment:
        if a == "Air to glass block":
            result = ("As light enters glass from air at an angle, it slows down and bends towards the normal. The ray changes direction at the boundary." if not is_pa else "ਜਦੋਂ ਰੋਸ਼ਨੀ ਕੋਣ ਨਾਲ ਹਵਾ ਤੋਂ ਕੱਚ ਵਿੱਚ ਜਾਂਦੀ ਹੈ, ਇਸ ਦੀ ਗਤੀ ਘਟਦੀ ਹੈ ਅਤੇ ਕਿਰਨ ਲੰਬ ਵੱਲ ਮੁੜਦੀ ਹੈ। ਸੀਮਾ ਉੱਤੇ ਦਿਸ਼ਾ ਬਦਲਦੀ ਹੈ।")
        else:
            result = ("As light leaves glass and enters air at an angle, it speeds up and bends away from the normal." if not is_pa else "ਜਦੋਂ ਰੋਸ਼ਨੀ ਕੋਣ ਨਾਲ ਕੱਚ ਤੋਂ ਹਵਾ ਵਿੱਚ ਜਾਂਦੀ ਹੈ, ਇਸ ਦੀ ਗਤੀ ਵਧਦੀ ਹੈ ਅਤੇ ਕਿਰਨ ਲੰਬ ਤੋਂ ਦੂਰ ਮੁੜਦੀ ਹੈ।")
    elif class9_work_energy_experiment:
        if a == "Pushing a box forward":
            action_label = "FORCE + FORWARD MOTION" if not is_pa else "ਬਲ + ਅੱਗੇ ਵੱਲ ਗਤੀ"
            energy_label = "WORK IS DONE ON THE BOX" if not is_pa else "ਡੱਬੇ ਉੱਤੇ ਕੰਮ ਹੁੰਦਾ ਹੈ"
            person = '<circle cx="80" cy="85" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M80 98 V137 M80 108 L111 120 L130 120 M80 137 L65 160 M80 137 L95 160" stroke="#2563eb" stroke-width="7" stroke-linecap="round" fill="none"/>'
            action = '<path d="M126 119 H178 M166 109 L180 119 L166 129" stroke="#16a34a" stroke-width="5" fill="none" stroke-linecap="round"/>'
            box = '<rect x="184" y="91" width="75" height="58" rx="5" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M194 101 L249 139 M249 101 L194 139" stroke="#a16207" stroke-width="2"/>'
            track = '<path d="M35 166 H420" stroke="#64748b" stroke-width="4"/><path d="M280 166 H370 M358 156 L372 166 L358 176" stroke="#0ea5e9" stroke-width="4" fill="none"/>'
        elif a == "Lifting a box upward":
            action_label = "UPWARD FORCE + UPWARD MOTION" if not is_pa else "ਉੱਪਰ ਵੱਲ ਬਲ + ਉੱਪਰ ਵੱਲ ਗਤੀ"
            energy_label = "ENERGY IS STORED AS HEIGHT INCREASES" if not is_pa else "ਉਚਾਈ ਵਧਣ ਨਾਲ ਸਥਿਤਿਜ ਊਰਜਾ ਵਧਦੀ ਹੈ"
            person = '<circle cx="80" cy="93" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M80 106 V145 M80 115 L104 102 L127 91 M80 145 L65 166 M80 145 L95 166" stroke="#2563eb" stroke-width="7" stroke-linecap="round" fill="none"/>'
            action = '<path d="M213 86 V48 M203 58 L213 46 L223 58" stroke="#16a34a" stroke-width="5" fill="none" stroke-linecap="round"/>'
            box = '<rect x="178" y="88" width="70" height="48" rx="5" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M188 98 L238 126 M238 98 L188 126" stroke="#a16207" stroke-width="2"/>'
            track = '<path d="M35 175 H420" stroke="#64748b" stroke-width="4"/><path d="M278 162 V100" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 5"/>'
        else:
            action_label = "NO MOVEMENT" if not is_pa else "ਕੋਈ ਗਤੀ ਨਹੀਂ"
            energy_label = "NO MECHANICAL WORK ON THE BOX WHILE IT STAYS STILL" if not is_pa else "ਡੱਬਾ ਸਥਿਰ ਰਹੇ ਤਾਂ ਉਸ ਉੱਤੇ ਮਕੈਨੀਕੀ ਕੰਮ ਨਹੀਂ ਹੁੰਦਾ"
            person = '<circle cx="80" cy="85" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M80 98 V137 M80 108 L108 121 L132 121 M80 137 L65 160 M80 137 L95 160" stroke="#2563eb" stroke-width="7" stroke-linecap="round" fill="none"/>'
            action = '<path d="M132 120 H170" stroke="#64748b" stroke-width="4" stroke-dasharray="5 5"/>'
            box = '<rect x="184" y="91" width="75" height="58" rx="5" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M194 101 L249 139 M249 101 L194 139" stroke="#a16207" stroke-width="2"/>'
            track = '<path d="M35 166 H420" stroke="#64748b" stroke-width="4"/>'
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{("WORK AND MECHANICAL ENERGY" if not is_pa else "ਕੰਮ ਅਤੇ ਮਕੈਨੀਕੀ ਊਰਜਾ")}</text>{person}{action}{box}{track}<text x="230" y="190" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">{action_label}</text><text x="230" y="207" text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">{energy_label}</text>'
    elif class9_newton_experiment:
        strong_push = a == "Strong push"
        loaded_cart = b == "Loaded cart"
        cart_x = 150 if loaded_cart else 175
        cart_color = "#c08457" if loaded_cart else "#60a5fa"
        arrow_len = 82 if strong_push else 42
        arrow_color = "#16a34a" if strong_push else "#0ea5e9"
        push_label = ("ਜ਼ੋਰਦਾਰ ਧੱਕਾ" if is_pa and strong_push else "ਹਲਕਾ ਧੱਕਾ" if is_pa else "STRONGER PUSH" if strong_push else "GENTLE PUSH")
        load_label = ("ਵੱਧ ਭਾਰ" if is_pa and loaded_cart else "ਘੱਟ ਭਾਰ" if is_pa else "MORE MASS" if loaded_cart else "LESS MASS")
        effect_label = ("ਵੱਧ ਤਵਰਣ" if is_pa and strong_push else "ਘੱਟ ਤਵਰਣ" if is_pa else "GREATER ACCELERATION" if strong_push else "SMALLER ACCELERATION")
        mass_block = f'<rect x="{cart_x+28}" y="82" width="44" height="27" rx="4" fill="#a16207" stroke="#713f12" stroke-width="2"/>' if loaded_cart else ""
        visual = f"""<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{("NEWTON'S SECOND LAW" if not is_pa else "ਨਿਊਟਨ ਦਾ ਦੂਜਾ ਨਿਯਮ")}</text><path d="M30 174 H425" stroke="#64748b" stroke-width="4"/><rect x="{cart_x}" y="111" width="100" height="48" rx="8" fill="{cart_color}" stroke="#475569" stroke-width="3"/><circle cx="{cart_x+22}" cy="166" r="10" fill="#334155"/><circle cx="{cart_x+78}" cy="166" r="10" fill="#334155"/>{mass_block}<path d="M{cart_x-8} 132 H{cart_x-arrow_len} M{cart_x-arrow_len+10} 122 L{cart_x-arrow_len} 132 L{cart_x-arrow_len+10} 142" stroke="{arrow_color}" stroke-width="{6 if strong_push else 4}" fill="none" stroke-linecap="round"/><text x="230" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">{push_label} · {load_label}</text><text x="230" y="202" text-anchor="middle" font-size="13" font-weight="700" fill="#0f766e">{effect_label}</text>"""
    elif current_magnetic_field_experiment:
        current_on = a.startswith("Switch ON")
        field_color = "#0ea5e9" if current_on else "#cbd5e1"
        field_lines = ('<ellipse cx="220" cy="112" rx="42" ry="30" fill="none" stroke="#0ea5e9" stroke-width="2.5"/><ellipse cx="220" cy="112" rx="68" ry="49" fill="none" stroke="#0ea5e9" stroke-width="2.5"/><ellipse cx="220" cy="112" rx="94" ry="68" fill="none" stroke="#0ea5e9" stroke-width="2.5"/>' if current_on else '<text x="220" y="80" text-anchor="middle" fill="#64748b" font-size="13">No current → no magnetic field from the wire</text>')
        needle = ('<path d="M95 93 L86 123 L95 116 L104 123 Z" fill="#dc2626"/><path d="M95 145 L86 115 L95 122 L104 115 Z" fill="#334155"/>' if current_on else '<path d="M95 88 L95 123 L88 115 Z" fill="#dc2626"/><path d="M95 145 L95 112 L102 120 Z" fill="#334155"/>')
        status_text = ("SWITCH ON · FIELD PRESENT" if current_on else "SWITCH OFF · FIELD DISAPPEARS") if not is_pa else ("ਸਵਿੱਚ ਚਾਲੂ · ਚੁੰਬਕੀ ਖੇਤਰ ਮੌਜੂਦ" if current_on else "ਸਵਿੱਚ ਬੰਦ · ਚੁੰਬਕੀ ਖੇਤਰ ਖਤਮ")
        visual = f'<rect x="12" y="12" width="436" height="206" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" fill="#334155" font-size="14" font-weight="700">MAGNETIC EFFECT OF CURRENT</text>{field_lines}<path d="M220 45 V178" stroke="#b45309" stroke-width="7"/><circle cx="220" cy="112" r="6" fill="#f59e0b" stroke="#92400e" stroke-width="2"/><text x="245" y="54" fill="#334155" font-size="12">Current-carrying wire</text><circle cx="95" cy="116" r="34" fill="#fff" stroke="#64748b" stroke-width="2"/>{needle}<text x="95" y="164" text-anchor="middle" fill="#334155" font-size="12">Compass</text><rect x="340" y="72" width="72" height="48" rx="6" fill="{('#bbf7d0' if current_on else '#e2e8f0')}" stroke="{('#15803d' if current_on else '#64748b')}" stroke-width="2"/><text x="376" y="91" text-anchor="middle" fill="#334155" font-size="11">Switch</text><text x="376" y="108" text-anchor="middle" fill="#334155" font-size="12" font-weight="700">{('ON' if current_on else 'OFF')}</text><path d="M340 96 H292 V45 H220" stroke="#64748b" stroke-width="3" fill="none"/><path d="M220 178 V190 H340 V120" stroke="#64748b" stroke-width="3" fill="none"/><text x="230" y="207" text-anchor="middle" fill="#334155" font-size="12">{status_text}</text>'
    elif reflection_angle_experiment or class8_reflection_experiment:
        ray_geometry = {10: (21, 118), 20: (41, 113), 30: (60, 104), 40: (77, 92), 50: (92, 77), 60: (104, 60), 70: (113, 41), 80: (118, 21)}
        dx, dy = ray_geometry[int(a)]
        angle_label = f"{int(a)}°"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="32" text-anchor="middle" fill="#334155" font-size="14" font-weight="700">LAW OF REFLECTION</text><path d="M35 180 H425" stroke="#64748b" stroke-width="5"/><text x="405" y="201" text-anchor="end" fill="#334155" font-size="12">Plane mirror</text><path d="M220 48 V180" stroke="#64748b" stroke-width="2" stroke-dasharray="6 5"/><text x="230" y="55" fill="#334155" font-size="12">Normal</text><path d="M{220-dx} {180-dy} L220 180" stroke="#f59e0b" stroke-width="4" fill="none"/><path d="M220 180 L{220+dx} {180-dy}" stroke="#0ea5e9" stroke-width="4" fill="none"/><path d="M{220-dx+10} {180-dy+8} L{220-dx} {180-dy} L{220-dx+12} {180-dy+1}" stroke="#f59e0b" stroke-width="3" fill="none"/><path d="M{220+dx-12} {180-dy+1} L{220+dx} {180-dy} L{220+dx-10} {180-dy+8}" stroke="#0ea5e9" stroke-width="3" fill="none"/><path d="M220 180 L{220-dx} {180-dy}" stroke="#f59e0b" stroke-width="4" fill="none"/><path d="M220 180 L{220+dx} {180-dy}" stroke="#0ea5e9" stroke-width="4" fill="none"/><circle cx="220" cy="180" r="5" fill="#e11d48"/><text x="75" y="65" fill="#b45309" font-size="13" font-weight="700">Incident ray</text><text x="310" y="65" fill="#0369a1" font-size="13" font-weight="700">Reflected ray</text><text x="{220-dx-18}" y="{180-dy+38}" fill="#b45309" font-size="14" font-weight="700">{angle_label}</text><text x="{220+dx+2}" y="{180-dy+38}" fill="#0369a1" font-size="14" font-weight="700">{angle_label}</text><text x="230" y="211" text-anchor="middle" fill="#334155" font-size="12">Angle of incidence = angle of reflection</text>'
    elif liquid_pressure_examples_experiment:
        if a.startswith("Water jets"):
            visual = '<rect x="18" y="18" width="424" height="194" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/><text x="230" y="38" text-anchor="middle" font-size="15" font-weight="700" fill="#334155">LIQUID PRESSURE INCREASES WITH DEPTH</text><path d="M90 50 V172 Q90 185 105 185 H280 Q295 185 295 172 V50" fill="#7dd3fc" fill-opacity=".65" stroke="#0369a1" stroke-width="3"/><path d="M93 68 H292 M93 102 H292 M93 136 H292" stroke="#0284c7" stroke-width="2" stroke-dasharray="5 4"/><circle cx="90" cy="75" r="5" fill="#0f172a"/><circle cx="90" cy="112" r="5" fill="#0f172a"/><circle cx="90" cy="150" r="5" fill="#0f172a"/><path d="M90 75 H137 M129 68 L139 75 L129 82" stroke="#0ea5e9" stroke-width="3" fill="none"/><path d="M90 112 H180 M172 105 L182 112 L172 119" stroke="#0ea5e9" stroke-width="3" fill="none"/><path d="M90 150 H230 M222 143 L232 150 L222 157" stroke="#dc2626" stroke-width="4" fill="none"/><text x="350" y="78" font-size="12" fill="#334155">Upper hole</text><text x="350" y="115" font-size="12" fill="#334155">Middle hole</text><text x="350" y="153" font-size="12" fill="#334155">Lower hole</text><text x="230" y="204" text-anchor="middle" font-size="12" fill="#334155">Deeper hole → stronger outward jet</text>'
        elif a.startswith("Water pressing"):
            visual = '<rect x="18" y="18" width="424" height="194" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/><text x="230" y="38" text-anchor="middle" font-size="15" font-weight="700" fill="#334155">WATER PRESSURE ON A DAM</text><path d="M35 58 H260 V178 H35 Z" fill="#7dd3fc" fill-opacity=".7" stroke="#0284c7" stroke-width="2"/><path d="M35 58 H260" stroke="#0284c7" stroke-width="3"/><path d="M260 48 L310 178 L260 178 Z" fill="#94a3b8" stroke="#475569" stroke-width="3"/><path d="M90 75 H145 M137 67 L147 75 L137 83 M90 112 H175 M167 104 L177 112 L167 120 M90 150 H215 M207 142 L217 150 L207 158" stroke="#dc2626" stroke-width="4" fill="none"/><text x="115" y="52" text-anchor="middle" font-size="12" fill="#334155">Water</text><text x="345" y="100" text-anchor="middle" font-size="13" fill="#334155">Dam wall</text><text x="230" y="204" text-anchor="middle" font-size="12" fill="#334155">Wall is built thicker near the bottom</text>'
        else:
            visual = '<rect x="18" y="18" width="424" height="194" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/><text x="230" y="38" text-anchor="middle" font-size="15" font-weight="700" fill="#334155">OVERHEAD WATER TANK</text><rect x="105" y="48" width="150" height="100" rx="5" fill="#7dd3fc" fill-opacity=".65" stroke="#0369a1" stroke-width="3"/><path d="M105 75 H255 M105 102 H255 M105 129 H255" stroke="#0284c7" stroke-width="2" stroke-dasharray="5 4"/><path d="M255 130 H320 V178 H385" stroke="#64748b" stroke-width="10" fill="none"/><path d="M320 178 H385" stroke="#38bdf8" stroke-width="5"/><path d="M320 178 H385 M377 170 L387 178 L377 186" stroke="#0ea5e9" stroke-width="3" fill="none"/><path d="M180 148 V178 M172 170 L180 180 L188 170" stroke="#0ea5e9" stroke-width="3" fill="none"/><text x="180" y="93" text-anchor="middle" font-size="14" fill="#075985">Water</text><text x="325" y="153" text-anchor="middle" font-size="12" fill="#334155">Outlet pipe</text><text x="230" y="204" text-anchor="middle" font-size="12" fill="#334155">Water head helps push water through the pipe</text>'
    elif friction_types_experiment:
        if a.startswith("Sliding"):
            visual = '<rect x="18" y="18" width="424" height="194" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/><text x="230" y="40" text-anchor="middle" font-size="15" font-weight="700" fill="#334155">SLIDING FRICTION · SURFACE COMPARISON</text><rect x="35" y="75" width="175" height="88" rx="6" fill="#d6d3d1" stroke="#78716c" stroke-width="2"/><path d="M38 92 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8" stroke="#78716c" stroke-width="3" fill="none"/><rect x="250" y="75" width="175" height="88" rx="6" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/><path d="M252 92 H423 M252 112 H423 M252 132 H423 M252 152 H423" stroke="#60a5fa" stroke-width="2"/><rect x="83" y="53" width="72" height="35" rx="5" fill="#f59e0b" stroke="#92400e" stroke-width="2"/><rect x="300" y="53" width="72" height="35" rx="5" fill="#f59e0b" stroke="#92400e" stroke-width="2"/><path d="M80 47 H45 M53 39 L43 47 L53 55 M158 47 H193 M185 39 L195 47 L185 55" stroke="#dc2626" stroke-width="3" fill="none"/><path d="M300 47 H275 M283 39 L273 47 L283 55 M372 47 H405 M397 39 L407 47 L397 55" stroke="#0ea5e9" stroke-width="3" fill="none"/><text x="122" y="185" text-anchor="middle" font-size="13" fill="#334155">Rough carpet / rough wood</text><text x="337" y="185" text-anchor="middle" font-size="13" fill="#1e40af">Smooth tile / polished surface</text><text x="230" y="204" text-anchor="middle" font-size="12" fill="#334155">Rougher surface usually resists sliding more</text>'
        elif a.startswith("Rolling"):
            visual = '<rect x="18" y="18" width="424" height="194" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/><text x="230" y="40" text-anchor="middle" font-size="15" font-weight="700" fill="#334155">ROLLING FRICTION</text><rect x="35" y="130" width="175" height="38" fill="#d6d3d1" stroke="#78716c" stroke-width="2"/><path d="M38 139 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8 l12 -8 l12 8" stroke="#78716c" stroke-width="2" fill="none"/><rect x="250" y="130" width="175" height="38" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/><path d="M252 140 H423 M252 151 H423 M252 162 H423" stroke="#60a5fa" stroke-width="2"/><circle cx="120" cy="112" r="27" fill="#475569" stroke="#0f172a" stroke-width="3"/><circle cx="120" cy="112" r="8" fill="#f8fafc"/><path d="M150 105 H190 M182 97 L192 105 L182 113" stroke="#dc2626" stroke-width="4" fill="none"/><circle cx="337" cy="112" r="27" fill="#475569" stroke="#0f172a" stroke-width="3"/><circle cx="337" cy="112" r="8" fill="#f8fafc"/><path d="M365 105 H405 M397 97 L407 105 L397 113" stroke="#0ea5e9" stroke-width="4" fill="none"/><text x="120" y="190" text-anchor="middle" font-size="13" fill="#334155">Rough road</text><text x="337" y="190" text-anchor="middle" font-size="13" fill="#1e40af">Smooth road</text>'
        else:
            visual = '<rect x="18" y="18" width="424" height="194" rx="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/><text x="230" y="40" text-anchor="middle" font-size="15" font-weight="700" fill="#334155">FLUID FRICTION · AIR / WATER RESISTANCE</text><path d="M35 85 Q55 65 75 85 T115 85 T155 85 T195 85 T235 85 T275 85 T315 85 T355 85 T395 85 T430 85 M35 105 Q55 85 75 105 T115 105 T155 105 T195 105 T235 105 T275 105 T315 105 T355 105 T395 105 T430 105" stroke="#38bdf8" stroke-width="3" fill="none"/><path d="M35 155 Q55 135 75 155 T115 155 T155 155 T195 155 T235 155 T275 155 T315 155 T355 155 T395 155 T430 155" stroke="#38bdf8" stroke-width="3" fill="none"/><path d="M115 76 L155 76 L176 88 L155 100 L115 100 L95 88 Z" fill="#f59e0b" stroke="#92400e" stroke-width="2"/><circle cx="130" cy="72" r="10" fill="#2563eb"/><path d="M145 77 L164 63 L180 70" stroke="#2563eb" stroke-width="5" fill="none"/><path d="M195 88 H245 M237 80 L247 88 L237 96" stroke="#dc2626" stroke-width="4" fill="none"/><path d="M280 137 Q320 115 360 137 L345 160 L295 160 Z" fill="#f59e0b" stroke="#92400e" stroke-width="2"/><path d="M300 135 L320 115 L340 135" stroke="#92400e" stroke-width="3" fill="none"/><path d="M365 145 H410 M402 137 L412 145 L402 153" stroke="#dc2626" stroke-width="4" fill="none"/><text x="140" y="122" text-anchor="middle" font-size="13" fill="#334155">Cyclist in air</text><text x="330" y="184" text-anchor="middle" font-size="13" fill="#334155">Boat in water</text>'
    elif magnet_poles_experiment:
        like_poles = a.startswith("Like")
        left_x = 42 if like_poles else 70
        right_x = 285 if like_poles else 230
        gap_label = ("REPEL · MOVE APART" if like_poles else "ATTRACT · TOUCH") if not is_pa else ("ਵਿਕਰਸ਼ਣ · ਦੂਰ ਹਟਦੇ ਹਨ" if like_poles else "ਖਿੱਚ · ਇਕੱਠੇ ਜੁੜਦੇ ਹਨ")
        left_bar = f'<rect x="{left_x}" y="85" width="80" height="54" rx="5" fill="#2563eb" stroke="#1e3a8a" stroke-width="2"/><rect x="{left_x+80}" y="85" width="80" height="54" rx="5" fill="#ef4444" stroke="#991b1b" stroke-width="2"/><text x="{left_x+40}" y="118" text-anchor="middle" font-size="21" font-weight="700" fill="white">S</text><text x="{left_x+120}" y="118" text-anchor="middle" font-size="21" font-weight="700" fill="white">N</text>'
        right_left_pole = "N" if like_poles else "S"
        right_right_pole = "S" if like_poles else "N"
        right_left_color = "#ef4444" if like_poles else "#2563eb"
        right_right_color = "#2563eb" if like_poles else "#ef4444"
        right_bar = f'<rect x="{right_x}" y="85" width="80" height="54" rx="5" fill="{right_left_color}" stroke="#1e3a8a" stroke-width="2"/><rect x="{right_x+80}" y="85" width="80" height="54" rx="5" fill="{right_right_color}" stroke="#991b1b" stroke-width="2"/><text x="{right_x+40}" y="118" text-anchor="middle" font-size="21" font-weight="700" fill="white">{right_left_pole}</text><text x="{right_x+120}" y="118" text-anchor="middle" font-size="21" font-weight="700" fill="white">{right_right_pole}</text>'
        if like_poles:
            movement = '<path d="M205 93 H175 M183 85 L173 93 L183 101 M255 93 H285 M277 85 L287 93 L277 101" stroke="#f59e0b" stroke-width="4" fill="none"/><text x="230" y="68" text-anchor="middle" font-size="14" font-weight="700" fill="currentColor">N ↔ N</text>'
        else:
            movement = '<path d="M185 65 H215 M207 57 L217 65 L207 73 M275 65 H245 M253 57 L243 65 L253 73" stroke="#0ea5e9" stroke-width="4" fill="none"/><text x="230" y="48" text-anchor="middle" font-size="14" font-weight="700" fill="currentColor">N ↔ S</text>'
        visual = left_bar + right_bar + movement + f'<path d="M20 160 H440" stroke="#94a3b8" stroke-width="3"/><text x="230" y="195" text-anchor="middle" font-size="16" font-weight="700" fill="currentColor">{gap_label}</text><text x="{left_x+80}" y="153" text-anchor="middle" font-size="12" fill="currentColor">Magnet 1</text><text x="{right_x+80}" y="153" text-anchor="middle" font-size="12" fill="currentColor">Magnet 2</text>'
    elif force_examples_experiment:
        selected_push = a in ("Push a shopping cart", "Kick a football")
        action_label = ("PUSH" if selected_push else "PULL") if not is_pa else ("ਧੱਕਾ" if selected_push else "ਖਿੱਚ")
        if a == "Push a shopping cart":
            visual = '<circle cx="135" cy="146" r="17" fill="#334155"/><circle cx="190" cy="146" r="17" fill="#334155"/><rect x="115" y="88" width="105" height="45" rx="6" fill="#60a5fa" stroke="#1d4ed8" stroke-width="3"/><path d="M115 92 L95 65 L82 65" stroke="#334155" stroke-width="5" fill="none"/><path d="M55 120 H95 M87 111 L97 120 L87 129" stroke="#f59e0b" stroke-width="4" fill="none"/><text x="170" y="45" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">PUSH →</text><text x="170" y="190" text-anchor="middle" fill="currentColor" font-size="14">Shopping cart</text>'
        elif a == "Kick a football":
            visual = '<circle cx="230" cy="112" r="35" fill="#f8fafc" stroke="#334155" stroke-width="3"/><path d="M230 91 L245 102 L239 120 L220 120 L214 102 Z M230 91 L230 77 M245 102 L260 95 M239 120 L250 135 M220 120 L210 135 M214 102 L200 95" stroke="#334155" stroke-width="3" fill="none"/><path d="M70 165 L100 135 L118 155 L135 165 L150 165" stroke="#2563eb" stroke-width="8" stroke-linecap="round" fill="none"/><path d="M145 110 H188 M180 102 L190 110 L180 118" stroke="#f59e0b" stroke-width="4" fill="none"/><text x="230" y="45" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">PUSH →</text><text x="230" y="190" text-anchor="middle" fill="currentColor" font-size="14">Kicking a football</text>'
        elif a == "Pull a wagon":
            visual = '<circle cx="160" cy="151" r="14" fill="#334155"/><circle cx="225" cy="151" r="14" fill="#334155"/><path d="M140 98 H240 L225 137 H155 Z" fill="#fb923c" stroke="#c2410c" stroke-width="3"/><path d="M140 105 L95 68 L75 68" stroke="#334155" stroke-width="5" fill="none"/><path d="M55 65 H90 M82 57 L92 65 L82 73" stroke="#0ea5e9" stroke-width="4" fill="none"/><text x="215" y="45" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">PULL ←</text><text x="200" y="190" text-anchor="middle" fill="currentColor" font-size="14">Pulling a wagon</text>'
        else:
            visual = '<rect x="165" y="60" width="130" height="100" rx="5" fill="#c08457" stroke="#854d0e" stroke-width="4"/><rect x="180" y="75" width="100" height="70" fill="#f5d0a9" stroke="#854d0e" stroke-width="3"/><circle cx="230" cy="110" r="5" fill="#854d0e"/><path d="M85 110 H145 M137 102 L147 110 L137 118" stroke="#0ea5e9" stroke-width="4" fill="none"/><text x="230" y="35" text-anchor="middle" fill="currentColor" font-size="18" font-weight="700">PULL ←</text><text x="230" y="190" text-anchor="middle" fill="currentColor" font-size="14">Opening a drawer</text>'
    elif shadow_examples_experiment:
        if a == "Torch and hand":
            visual = '<circle cx="70" cy="112" r="27" fill="#fde68a" stroke="#d97706" stroke-width="3"/><path d="M92 112 H140 M130 104 L142 112 L130 120" stroke="#f59e0b" stroke-width="4" fill="none"/><path d="M172 150 L172 110 Q172 95 184 95 Q194 95 194 110 L194 84 Q194 72 204 72 Q214 72 214 84 L214 102 Q224 90 232 101 L232 130 L220 158 Z" fill="#f8c9a5" stroke="#9a3412" stroke-width="3"/><path d="M245 65 L245 175 L425 175 L425 65 Z" fill="#334155" fill-opacity=".12"/><path d="M245 65 L245 175 L300 175 L300 65 Z" fill="#334155" fill-opacity=".3"/><text x="70" y="160" text-anchor="middle" fill="currentColor" font-size="13">Torch</text><text x="198" y="195" text-anchor="middle" fill="currentColor" font-size="13">Hand</text><text x="335" y="195" text-anchor="middle" fill="currentColor" font-size="13">Shadow</text>'
        elif a == "Tree on a sunny day":
            visual = '<circle cx="75" cy="58" r="27" fill="#fde047" stroke="#ca8a04" stroke-width="3"/><path d="M103 70 L175 100" stroke="#f59e0b" stroke-width="4"/><path d="M175 100 L240 125" stroke="#f59e0b" stroke-width="4"/><path d="M210 178 L210 105" stroke="#854d0e" stroke-width="15"/><circle cx="210" cy="80" r="39" fill="#65a30d" stroke="#3f6212" stroke-width="3"/><path d="M255 175 L425 175 L390 160 L320 160 Z" fill="#334155" fill-opacity=".45"/><path d="M20 180 H440" stroke="#64748b" stroke-width="3"/><text x="75" y="105" text-anchor="middle" fill="currentColor" font-size="13">Sunlight</text><text x="330" y="198" text-anchor="middle" fill="currentColor" font-size="13">Tree shadow</text>'
        elif a == "Opaque book blocking light":
            visual = '<circle cx="65" cy="105" r="25" fill="#fde68a" stroke="#d97706" stroke-width="3"/><path d="M92 92 L160 70 M92 105 H160 M92 118 L160 140" stroke="#f59e0b" stroke-width="3"/><rect x="160" y="65" width="55" height="95" rx="4" fill="#2563eb" stroke="#1e3a8a" stroke-width="3"/><path d="M220 65 L220 160 L420 160 L420 65 Z" fill="#334155" fill-opacity=".16"/><path d="M220 65 L220 160 L290 160 L290 65 Z" fill="#334155" fill-opacity=".38"/><path d="M20 180 H440" stroke="#64748b" stroke-width="3"/><text x="65" y="150" text-anchor="middle" fill="currentColor" font-size="13">Light</text><text x="187" y="178" text-anchor="middle" fill="currentColor" font-size="13">Book</text><text x="330" y="185" text-anchor="middle" fill="currentColor" font-size="13">Dark shadow</text>'
        else:
            visual = '<circle cx="65" cy="105" r="25" fill="#fde68a" stroke="#d97706" stroke-width="3"/><path d="M92 92 L155 70 M92 105 H155 M92 118 L155 140" stroke="#f59e0b" stroke-width="3"/><rect x="155" y="50" width="25" height="115" fill="#7dd3fc" fill-opacity=".45" stroke="#0284c7" stroke-width="3"/><path d="M184 92 L255 82 M184 105 H255 M184 118 L255 128" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 5"/><rect x="255" y="55" width="155" height="105" fill="#334155" fill-opacity=".12"/><path d="M20 180 H440" stroke="#64748b" stroke-width="3"/><text x="65" y="150" text-anchor="middle" fill="currentColor" font-size="13">Light</text><text x="168" y="185" text-anchor="middle" fill="currentColor" font-size="13">Curtain</text><text x="330" y="185" text-anchor="middle" fill="currentColor" font-size="13">Faint shadow</text>'
    elif slow_fast_experiment:
        if a == "Slow motion":
            slow_style = 'stroke-width="5" stroke="#0ea5e9"'
            fast_style = 'stroke-width="3" stroke="#94a3b8"'
            slow_label = "SELECTED · SLOW" if not is_pa else "ਚੁਣਿਆ · ਹੌਲੀ"
            fast_label = "FAST EXAMPLES" if not is_pa else "ਤੇਜ਼ ਉਦਾਹਰਨਾਂ"
        else:
            slow_style = 'stroke-width="3" stroke="#94a3b8"'
            fast_style = 'stroke-width="5" stroke="#f59e0b"'
            slow_label = "SLOW EXAMPLES" if not is_pa else "ਹੌਲੀਆਂ ਉਦਾਹਰਨਾਂ"
            fast_label = "SELECTED · FAST" if not is_pa else "ਚੁਣਿਆ · ਤੇਜ਼"
        visual = f'<rect x="12" y="12" width="210" height="206" rx="14" fill="#e0f2fe" fill-opacity=".35" {slow_style}/><rect x="238" y="12" width="210" height="206" rx="14" fill="#fef3c7" fill-opacity=".35" {fast_style}/><text x="117" y="36" text-anchor="middle" fill="currentColor" font-size="14" font-weight="700">{slow_label}</text><text x="343" y="36" text-anchor="middle" fill="currentColor" font-size="14" font-weight="700">{fast_label}</text><path d="M44 106 Q25 83 42 73 Q58 69 66 89 L82 96 L72 108 L54 107 Z" fill="#84cc16" stroke="#3f6212" stroke-width="3"/><circle cx="43" cy="78" r="3" fill="#3f6212"/><path d="M49 108 L43 124 M69 108 L76 124" stroke="#3f6212" stroke-width="4"/><circle cx="117" cy="111" r="8" fill="#2563eb"/><path d="M117 120 L112 139 M117 124 L133 129 M112 139 L103 151 M112 139 L126 151" stroke="#2563eb" stroke-width="5" stroke-linecap="round"/><path d="M28 163 H194" stroke="#64748b" stroke-width="3" stroke-dasharray="5 5"/><circle cx="286" cy="132" r="13" fill="#334155"/><circle cx="384" cy="132" r="13" fill="#334155"/><path d="M270 126 L285 93 L354 93 L385 126 Z" fill="#ef4444" stroke="#991b1b" stroke-width="3"/><rect x="300" y="99" width="25" height="17" rx="3" fill="#bfdbfe"/><rect x="330" y="99" width="19" height="17" rx="3" fill="#bfdbfe"/><path d="M265 78 H305 M297 70 L307 78 L297 86 M330 67 H370 M362 59 L372 67 L362 75" stroke="#f59e0b" stroke-width="3" fill="none"/><path d="M264 163 H423" stroke="#64748b" stroke-width="3" stroke-dasharray="5 5"/><text x="117" y="184" text-anchor="middle" fill="currentColor" font-size="12">{("Tortoise and walking person" if not is_pa else "ਕੱਛੂਆ ਅਤੇ ਪੈਦਲ ਵਿਅਕਤੀ")}</text><text x="343" y="184" text-anchor="middle" fill="currentColor" font-size="12">{("Racing car / fast train" if not is_pa else "ਰੇਸਿੰਗ ਕਾਰ / ਤੇਜ਼ ਰੇਲ")}</text><text x="117" y="203" text-anchor="middle" fill="currentColor" font-size="11">{("Less distance in same time" if not is_pa else "ਇੱਕੋ ਸਮੇਂ ਵਿੱਚ ਘੱਟ ਦੂਰੀ")}</text><text x="343" y="203" text-anchor="middle" fill="currentColor" font-size="11">{("More distance in same time" if not is_pa else "ਇੱਕੋ ਸਮੇਂ ਵਿੱਚ ਵੱਧ ਦੂਰੀ")}</text>'
    elif pressure_area_examples_experiment:
        if a == "Snowshoes vs high heels":
            example_label = "SNOWSHOES vs HIGH HEELS" if not is_pa else "ਬਰਫ਼ ਵਾਲੇ ਜੁੱਤੇ ਬਨਾਮ ਉੱਚੀ ਅੱਡੀ"
            left_label, right_label = ("WIDE SNOWSHOES", "NARROW HEELS") if not is_pa else ("ਚੌੜੇ ਜੁੱਤੇ", "ਤੰਗ ਅੱਡੀ")
            left_shape = '<path d="M85 78 Q75 95 88 140 L165 140 Q177 95 163 78 Z" fill="#bae6fd" stroke="#0369a1" stroke-width="3"/>'
            right_shape = '<path d="M322 78 L337 78 L334 126 L345 126 L345 140 L310 140 L310 126 L321 126 Z" fill="#fda4af" stroke="#be123c" stroke-width="3"/>'
        elif a == "Sharp knife vs blunt knife":
            example_label = "SHARP vs BLUNT KNIFE" if not is_pa else "ਤੇਜ਼ ਬਨਾਮ ਮੋਟੀ ਧਾਰ"
            left_label, right_label = ("SHARP EDGE · SMALL AREA", "BLUNT EDGE · LARGER AREA") if not is_pa else ("ਤੇਜ਼ ਧਾਰ · ਛੋਟਾ ਖੇਤਰ", "ਮੋਟੀ ਧਾਰ · ਵੱਡਾ ਖੇਤਰ")
            left_shape = '<path d="M85 86 L165 86 L125 142 Z" fill="#cbd5e1" stroke="#475569" stroke-width="3"/><path d="M125 142 V148" stroke="#be123c" stroke-width="5"/>'
            right_shape = '<path d="M302 86 L382 86 L350 136 L334 136 Z" fill="#cbd5e1" stroke="#475569" stroke-width="3"/><path d="M334 136 H350" stroke="#be123c" stroke-width="8"/>'
        elif a == "Broad tractor tyres vs narrow tyres":
            example_label = "BROAD vs NARROW TYRES" if not is_pa else "ਚੌੜੇ ਬਨਾਮ ਤੰਗ ਟਾਇਰ"
            left_label, right_label = ("BROAD TYRE · LARGER AREA", "NARROW TYRE · SMALLER AREA") if not is_pa else ("ਚੌੜਾ ਟਾਇਰ · ਵੱਡਾ ਖੇਤਰ", "ਤੰਗ ਟਾਇਰ · ਛੋਟਾ ਖੇਤਰ")
            left_shape = '<rect x="91" y="72" width="68" height="76" rx="13" fill="#334155" stroke="#0f172a" stroke-width="3"/><path d="M100 82 L150 138 M150 82 L100 138" stroke="#94a3b8" stroke-width="4"/>'
            right_shape = '<rect x="325" y="72" width="28" height="76" rx="8" fill="#334155" stroke="#0f172a" stroke-width="3"/><path d="M328 82 L350 138 M350 82 L328 138" stroke="#94a3b8" stroke-width="3"/>'
        else:
            example_label = "WIDE vs NARROW FOUNDATION" if not is_pa else "ਚੌੜੀ ਬਨਾਮ ਤੰਗ ਨੀਂਹ"
            left_label, right_label = ("WIDE FOUNDATION", "NARROW FOUNDATION") if not is_pa else ("ਚੌੜੀ ਨੀਂਹ", "ਤੰਗ ਨੀਂਹ")
            left_shape = '<rect x="82" y="65" width="90" height="66" fill="#d6d3d1" stroke="#78716c" stroke-width="3"/><rect x="65" y="131" width="124" height="18" fill="#a8a29e" stroke="#57534e" stroke-width="3"/>'
            right_shape = '<rect x="307" y="65" width="90" height="66" fill="#d6d3d1" stroke="#78716c" stroke-width="3"/><rect x="338" y="131" width="28" height="18" fill="#a8a29e" stroke="#57534e" stroke-width="3"/>'
        low_label = "LOWER PRESSURE" if not is_pa else "ਘੱਟ ਦਬਾਅ"
        high_label = "HIGHER PRESSURE" if not is_pa else "ਵੱਧ ਦਬਾਅ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="32" text-anchor="middle" font-size="14" font-weight="700" fill="#334155">{example_label}</text><path d="M25 158 H435" stroke="#64748b" stroke-width="3"/>{left_shape}{right_shape}<path d="M125 42 V64 M117 56 L125 66 L133 56 M125 45 V62 M117 52 L125 62 L133 52" stroke="#0ea5e9" stroke-width="3" fill="none"/><path d="M337 42 V64 M329 56 L337 66 L345 56 M337 45 V62 M329 52 L337 62 L345 52" stroke="#f59e0b" stroke-width="3" fill="none"/><text x="125" y="177" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">{left_label}</text><text x="337" y="177" text-anchor="middle" font-size="11" font-weight="700" fill="#be123c">{right_label}</text><text x="125" y="198" text-anchor="middle" font-size="13" font-weight="700" fill="#0369a1">{low_label}</text><text x="337" y="198" text-anchor="middle" font-size="13" font-weight="700" fill="#be123c">{high_label}</text>'
    elif heat_conduction_examples_experiment:
        is_conductor = a in ("Metal rod (iron / steel)", "Copper spoon")
        material_label = ({"Metal rod (iron / steel)": "METAL ROD", "Copper spoon": "COPPER SPOON", "Wooden stick": "WOOD", "Plastic ruler": "PLASTIC"}[a])
        transfer_label = ("HEAT TRAVELS ALONG METAL" if is_conductor else "HEAT DOES NOT TRAVEL EASILY") if not is_pa else ("ਧਾਤ ਵਿੱਚ ਤਾਪ ਅੱਗੇ ਵੱਲ ਜਾਂਦਾ ਹੈ" if is_conductor else "ਤਾਪ ਆਸਾਨੀ ਨਾਲ ਅੱਗੇ ਨਹੀਂ ਜਾਂਦਾ")
        rod_color = "#fb923c" if is_conductor else "#94a3b8"
        heat_marks = '<path d="M180 95 L198 83 M220 95 L238 83 M260 95 L278 83 M300 95 L318 83" stroke="#f97316" stroke-width="4" stroke-linecap="round"/>' if is_conductor else '<path d="M180 95 L192 91 M220 95 L232 91" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>'
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#fff7ed" stroke="#fdba74" stroke-width="2"/><text x="230" y="31" text-anchor="middle" font-size="14" font-weight="700" fill="#7c2d12">{material_label}</text><path d="M55 150 H405" stroke="#64748b" stroke-width="4"/><rect x="120" y="88" width="250" height="24" rx="8" fill="{rod_color}" stroke="#475569" stroke-width="2"/><path d="M68 148 C48 128 75 117 62 99 C92 111 98 129 82 148 Z" fill="#ef4444"/><path d="M82 148 C68 130 95 121 91 105 C116 128 111 138 101 148 Z" fill="#f59e0b"/><path d="M100 148 C91 132 113 124 112 113 C132 133 124 141 119 148 Z" fill="#facc15"/>{heat_marks}<text x="83" y="174" text-anchor="middle" font-size="12" font-weight="700" fill="#9a3412">{("HEAT SOURCE" if not is_pa else "ਤਾਪ ਸਰੋਤ")}</text><text x="245" y="72" text-anchor="middle" font-size="12" font-weight="700" fill="#9a3412">{("HOT END" if not is_pa else "ਗਰਮ ਸਿਰਾ")}</text><text x="350" y="137" text-anchor="middle" font-size="12" font-weight="700" fill="#334155">{("FAR END" if not is_pa else "ਦੂਰਲਾ ਸਿਰਾ")}</text><text x="230" y="198" text-anchor="middle" font-size="13" font-weight="700" fill="#7c2d12">{transfer_label}</text>'
    elif kind in ("reflection","refraction"):
        ang = int(a)
        visual = f'<path d="M40 180 L420 180" stroke="#64748b" stroke-width="5"/><path d="M220 180 L{220-int(ang*1.5)} {180-int(ang*1.5)}" stroke="#f59e0b" stroke-width="4"/><path d="M220 180 L{220+int(ang*1.5)} {180-int(ang*1.5)}" stroke="#0ea5e9" stroke-width="4"/><circle cx="220" cy="180" r="5" fill="#e11d48"/><text x="70" y="35" fill="currentColor" font-size="16">Incident ray</text><text x="270" y="35" fill="currentColor" font-size="16">Outgoing ray</text>'
    elif class8_sound_wave_examples_experiment:
        loud_sound = a.startswith("Loud")
        high_pitch = "high-pitched" in a
        amp = 36 if loud_sound else 13
        cycles = 9 if high_pitch else 3
        points = " ".join(f"{x},{112-amp*__import__('math').sin((x-22)*cycles*2*3.14159/400):.1f}" for x in range(22,439,4))
        pitch_label = ("HIGHER PITCH" if high_pitch else "LOWER PITCH") if not is_pa else ("ਉੱਚੀ ਸੁਰ" if high_pitch else "ਨੀਵੀਂ ਸੁਰ")
        loud_label = ("LOUDER SOUND · LARGER AMPLITUDE" if loud_sound else "SOFTER SOUND · SMALLER AMPLITUDE") if not is_pa else ("ਉੱਚੀ ਆਵਾਜ਼ · ਵੱਡੀ ਐਂਪਲੀਟਿਊਡ" if loud_sound else "ਹੌਲੀ ਆਵਾਜ਼ · ਛੋਟੀ ਐਂਪਲੀਟਿਊਡ")
        visual = f'<rect x="12" y="12" width="436" height="206" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="31" text-anchor="middle" fill="#334155" font-size="14" font-weight="700">{("SOUND WAVE COMPARISON" if not is_pa else "ਧੁਨੀ ਤਰੰਗ ਦੀ ਤੁਲਨਾ")}</text><path d="M25 112 H435" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 5"/><polyline points="{points}" fill="none" stroke="#0ea5e9" stroke-width="3.5" stroke-linejoin="round"/><text x="230" y="166" text-anchor="middle" fill="#0369a1" font-size="13" font-weight="700">{pitch_label}</text><text x="230" y="190" text-anchor="middle" fill="#334155" font-size="12" font-weight="700">{loud_label}</text><text x="230" y="209" text-anchor="middle" fill="#475569" font-size="11">{("More cycles = higher pitch; taller wave = louder sound" if not is_pa else "ਵੱਧ ਚੱਕਰ = ਉੱਚੀ ਸੁਰ; ਉੱਚੀ ਤਰੰਗ = ਉੱਚੀ ਆਵਾਜ਼")}</text>'
    elif kind in ("sound","wave"):
        pts = " ".join(f"{x},{105-int(c*5)*__import__('math').sin((x-20)*int(a)/300)}" for x in range(20,441,8))
        visual = f'<polyline points="{pts}" fill="none" stroke="#0ea5e9" stroke-width="3"/><path d="M20 105 H440" stroke="#94a3b8" stroke-dasharray="4 5"/><text x="20" y="30" fill="currentColor" font-size="15">Frequency: {a} Hz</text>'
    elif kind == "magnet":
        visual = f'<rect x="75" y="80" width="125" height="55" rx="8" fill="#fecaca" stroke="#b91c1c" stroke-width="2"/><rect x="260" y="80" width="125" height="55" rx="8" fill="#bfdbfe" stroke="#1d4ed8" stroke-width="2"/><text x="137" y="113" font-size="22" text-anchor="middle" fill="#991b1b">N</text><text x="322" y="113" font-size="22" text-anchor="middle" fill="#1e40af">{"S" if a=="Unlike poles" else "N"}</text><path d="M200 90 Q230 45 260 90 M200 125 Q230 170 260 125" stroke="#0ea5e9" fill="none" stroke-width="3"/>'
    elif balanced_forces_examples_experiment:
        same_direction = a == "Both people push the table to the right"
        equal_opposite = a == "People push equally in opposite directions"
        person_left = '<circle cx="58" cy="72" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M58 85 V119 M58 94 L82 103 L96 103 M58 119 L45 143 M58 119 L72 143" stroke="#2563eb" stroke-width="7" stroke-linecap="round" fill="none"/>'
        person_right = '<circle cx="402" cy="72" r="13" fill="#f1c27d" stroke="#92400e" stroke-width="2"/><path d="M402 85 V119 M402 94 L378 103 L364 103 M402 119 L389 143 M402 119 L416 143" stroke="#16a34a" stroke-width="7" stroke-linecap="round" fill="none"/>'
        if same_direction:
            left_arrow = '<path d="M155 105 H95 M105 95 L93 105 L105 115" stroke="#0ea5e9" stroke-width="5" fill="none"/>'
            right_arrow = '<path d="M305 105 H365 M355 95 L367 105 L355 115" stroke="#f59e0b" stroke-width="5" fill="none"/>'
            motion_text = "TABLE MOVES RIGHT →" if not is_pa else "ਮੇਜ਼ ਸੱਜੇ ਵੱਲ ਚੱਲਦੀ ਹੈ →"
            status_text = "UNBALANCED · BOTH PUSH RIGHT" if not is_pa else "ਅਸੰਤੁਲਿਤ · ਦੋਵੇਂ ਸੱਜੇ ਧੱਕਦੇ ਹਨ"
        elif equal_opposite:
            left_arrow = '<path d="M165 105 H105 M115 95 L103 105 L115 115" stroke="#0ea5e9" stroke-width="5" fill="none"/>'
            right_arrow = '<path d="M295 105 H355 M345 95 L357 105 L345 115" stroke="#f59e0b" stroke-width="5" fill="none"/>'
            motion_text = "TABLE STAYS STILL" if not is_pa else "ਮੇਜ਼ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ"
            status_text = "BALANCED · EQUAL OPPOSING FORCES" if not is_pa else "ਸੰਤੁਲਿਤ · ਬਰਾਬਰ ਉਲਟ ਬਲ"
        else:
            left_arrow = '<path d="M165 105 H75 M85 95 L73 105 L85 115" stroke="#0ea5e9" stroke-width="7" fill="none"/>'
            right_arrow = '<path d="M295 105 H335 M325 95 L337 105 L325 115" stroke="#f59e0b" stroke-width="3" fill="none"/>'
            motion_text = "TABLE MOVES LEFT ←" if not is_pa else "ਮੇਜ਼ ਖੱਬੇ ਵੱਲ ਚੱਲਦੀ ਹੈ ←"
            status_text = "UNBALANCED · LEFT PUSH STRONGER" if not is_pa else "ਅਸੰਤੁਲਿਤ · ਖੱਬੇ ਪਾਸੇ ਦਾ ਧੱਕਾ ਵੱਧ"
        visual = f'<rect x="12" y="12" width="436" height="206" rx="14" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/><text x="230" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#334155">{("TWO PEOPLE PUSHING A TABLE" if not is_pa else "ਦੋ ਵਿਅਕਤੀ ਮੇਜ਼ ਨੂੰ ਧੱਕਦੇ ਹੋਏ")}</text>{person_left}{person_right}<rect x="155" y="84" width="150" height="43" rx="5" fill="#c08457" stroke="#854d0e" stroke-width="3"/><path d="M175 127 V151 M285 127 V151" stroke="#854d0e" stroke-width="6"/>{left_arrow}{right_arrow}<text x="230" y="174" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">{status_text}</text><text x="230" y="198" text-anchor="middle" font-size="14" font-weight="700" fill="#0f766e">{motion_text}</text>'
    elif kind in ("force","friction","balanced","newton","motion","speed","acceleration"):
        pos = 70 + int(min(250, float(a)*5))
        visual = f'<path d="M35 185 H425" stroke="#64748b" stroke-width="4"/><rect x="{pos}" y="125" width="65" height="55" rx="8" fill="#bae6fd" stroke="#0284c7" stroke-width="3"/><circle cx="{pos+15}" cy="185" r="8" fill="#475569"/><circle cx="{pos+50}" cy="185" r="8" fill="#475569"/><path d="M{pos+32} 120 V65 M{pos+32} 65 l-10 14 M{pos+32} 65 l10 14" stroke="#f59e0b" stroke-width="4" fill="none"/><text x="35" y="35" fill="currentColor" font-size="16">Force / motion model</text>'
    elif kind in ("pressure","pressure_area"):
        visual = f'<rect x="100" y="55" width="260" height="135" fill="#bae6fd" fill-opacity=".55" stroke="#0284c7" stroke-width="2"/><path d="M100 90 H360 M100 125 H360 M100 160 H360" stroke="#0284c7" stroke-opacity=".5" stroke-width="2"/><path d="M230 75 V150 M220 140 L230 152 L240 140" stroke="#f59e0b" stroke-width="4" fill="none"/><text x="230" y="35" text-anchor="middle" fill="currentColor" font-size="15">Pressure model</text>'
    elif kind == "lens":
        visual = '<path d="M220 35 Q170 110 220 185 Q270 110 220 35" fill="#bae6fd" fill-opacity=".7" stroke="#0284c7" stroke-width="3"/><path d="M35 110 H405 M80 55 V165" stroke="#f59e0b" stroke-width="3"/><path d="M220 110 L360 70 M220 110 L360 150" stroke="#0ea5e9" stroke-width="3"/><text x="75" y="45" fill="currentColor" font-size="14">Object</text><text x="335" y="45" fill="currentColor" font-size="14">Image region</text>'
    elif kind in ("work","potential"):
        visual = f'<path d="M50 190 H410" stroke="#64748b" stroke-width="4"/><rect x="100" y="{150-int(min(100,float(b)*2))}" width="55" height="40" rx="5" fill="#bae6fd" stroke="#0284c7" stroke-width="3"/><path d="M130 45 V100 M120 90 L130 102 L140 90" stroke="#f59e0b" stroke-width="4" fill="none"/><text x="205" y="55" fill="currentColor" font-size="15">Work / energy</text>'
    else:
        visual = '<circle cx="130" cy="110" r="42" fill="#fde68a" stroke="#d97706" stroke-width="3"/><path d="M180 110 H280 M265 95 L282 110 L265 125" stroke="#0ea5e9" stroke-width="4" fill="none"/><rect x="300" y="75" width="75" height="70" rx="8" fill="#bae6fd" stroke="#0284c7" stroke-width="3"/><text x="130" y="116" text-anchor="middle" font-size="14" fill="#92400e">Input</text><text x="337" y="116" text-anchor="middle" font-size="14" fill="#075985">Effect</text>'
    st.markdown("### " + ("ਦ੍ਰਿਸ਼ ਮਾਡਲ" if is_pa else "Visual model"))
    st.markdown(f'<div style="border:1px solid rgba(120,140,160,.35);border-radius:16px;padding:12px;background:rgba(128,128,128,.035)"><svg viewBox="0 0 460 230" width="100%" role="img" aria-label="{title} interactive physics diagram">{visual}</svg></div>', unsafe_allow_html=True)
    result = ""
    if current_magnetic_field_experiment:
        result = ("When the switch is ON, current flows through the wire and a magnetic field is produced around it. When the switch is OFF, current stops and the magnetic effect from the current-carrying wire disappears." if not is_pa else "ਸਵਿੱਚ ਚਾਲੂ ਹੋਣ ਤੇ ਤਾਰ ਵਿੱਚੋਂ ਕਰੰਟ ਵਗਦਾ ਹੈ ਅਤੇ ਇਸ ਦੇ ਆਲੇ-ਦੁਆਲੇ ਚੁੰਬਕੀ ਖੇਤਰ ਬਣਦਾ ਹੈ। ਸਵਿੱਚ ਬੰਦ ਹੋਣ ਤੇ ਕਰੰਟ ਰੁਕ ਜਾਂਦਾ ਹੈ ਅਤੇ ਕਰੰਟ ਕਾਰਨ ਬਣਿਆ ਚੁੰਬਕੀ ਪ੍ਰਭਾਵ ਖਤਮ ਹੋ ਜਾਂਦਾ ਹੈ।")
    elif reflection_angle_experiment or class8_reflection_experiment:
        result = (f"Angle of incidence = {a}° and angle of reflection = {a}°. The reflected ray changes direction with the selected angle; both angles are measured from the normal." if not is_pa else f"ਆਗਮਨ ਕੋਣ = {a}° ਅਤੇ ਪਰਾਵਰਤਨ ਕੋਣ = {a}°। ਪਰਾਵਰਤਿਤ ਕਿਰਨ ਚੁਣੇ ਕੋਣ ਅਨੁਸਾਰ ਦਿਸ਼ਾ ਬਦਲਦੀ ਹੈ; ਦੋਵੇਂ ਕੋਣ ਲੰਬ ਤੋਂ ਮਾਪੇ ਜਾਂਦੇ ਹਨ।")
    elif liquid_pressure_examples_experiment:
        if a.startswith("Water jets"):
            result = ("Liquid pressure increases with depth, so water from a lower hole usually shoots farther than water from an upper hole." if not is_pa else "ਤਰਲ ਦਾ ਦਬਾਅ ਡੂੰਘਾਈ ਨਾਲ ਵਧਦਾ ਹੈ, ਇਸ ਲਈ ਹੇਠਲੇ ਛੇਕ ਵਿੱਚੋਂ ਪਾਣੀ ਦੀ ਧਾਰ ਆਮ ਤੌਰ ਤੇ ਉੱਪਰਲੇ ਛੇਕ ਨਾਲੋਂ ਦੂਰ ਜਾਂਦੀ ਹੈ।")
        elif a.startswith("Water pressing"):
            result = ("Water pressure is greater at greater depth. That is why dam walls are designed thicker and stronger near the bottom." if not is_pa else "ਵੱਧ ਡੂੰਘਾਈ ਉੱਤੇ ਪਾਣੀ ਦਾ ਦਬਾਅ ਵੱਧ ਹੁੰਦਾ ਹੈ। ਇਸੇ ਲਈ ਬੰਨ੍ਹ ਦੀ ਕੰਧ ਹੇਠਾਂ ਵੱਲ ਵਧੇਰੇ ਮੋਟੀ ਅਤੇ ਮਜ਼ਬੂਤ ਬਣਾਈ ਜਾਂਦੀ ਹੈ।")
        else:
            result = ("Water pressure at the outlet depends partly on the height of water above it. An overhead tank can push water through connected pipes." if not is_pa else "ਨਿਕਾਸ ਵਾਲੀ ਥਾਂ ਉੱਤੇ ਪਾਣੀ ਦਾ ਦਬਾਅ ਉਸ ਤੋਂ ਉੱਪਰਲੇ ਪਾਣੀ ਦੀ ਉਚਾਈ ਉੱਤੇ ਵੀ ਨਿਰਭਰ ਕਰਦਾ ਹੈ। ਉੱਚੀ ਟੈਂਕੀ ਪਾਈਪਾਂ ਵਿੱਚੋਂ ਪਾਣੀ ਧੱਕ ਸਕਦੀ ਹੈ।")
    elif friction_types_experiment:
        if a.startswith("Sliding"):
            result = ("Sliding friction acts when two surfaces slide against each other. A rough carpet usually opposes sliding more than a smooth tile." if not is_pa else "ਜਦੋਂ ਦੋ ਸਤਹਾਂ ਇੱਕ-ਦੂਜੇ ਉੱਤੇ ਸਰਕਦੀਆਂ ਹਨ ਤਾਂ ਸਰਕਣ ਘਰਸ਼ਣ ਲੱਗਦਾ ਹੈ। ਖੁਰਦਰਾ ਕਾਰਪੇਟ ਆਮ ਤੌਰ ਤੇ ਚਿਕਣੀ ਟਾਇਲ ਨਾਲੋਂ ਵੱਧ ਰੁਕਾਵਟ ਪੈਦਾ ਕਰਦਾ ਹੈ।")
        elif a.startswith("Rolling"):
            result = ("Rolling friction acts when a wheel or ball rolls over a surface. A rough road usually resists rolling more than a smooth road." if not is_pa else "ਜਦੋਂ ਪਹੀਆ ਜਾਂ ਗੇਂਦ ਸਤਹ ਉੱਤੇ ਲੁੜਕਦੀ ਹੈ ਤਾਂ ਲੁੜਕਣ ਘਰਸ਼ਣ ਹੁੰਦਾ ਹੈ। ਖੁਰਦਰੀ ਸੜਕ ਆਮ ਤੌਰ ਤੇ ਚਿਕਣੀ ਸੜਕ ਨਾਲੋਂ ਲੁੜਕਣ ਨੂੰ ਵੱਧ ਰੋਕਦੀ ਹੈ।")
        else:
            result = ("Fluid friction (drag) acts when an object moves through air or water. The fluid pushes against the moving cyclist or boat." if not is_pa else "ਜਦੋਂ ਕੋਈ ਵਸਤੂ ਹਵਾ ਜਾਂ ਪਾਣੀ ਵਿੱਚੋਂ ਲੰਘਦੀ ਹੈ ਤਾਂ ਤਰਲ ਘਰਸ਼ਣ ਜਾਂ ਡਰੈਗ ਲੱਗਦਾ ਹੈ। ਹਵਾ ਜਾਂ ਪਾਣੀ ਚੱਲਦੇ ਸਾਈਕਲ ਸਵਾਰ ਜਾਂ ਕਿਸ਼ਤੀ ਦੀ ਗਤੀ ਦਾ ਵਿਰੋਧ ਕਰਦਾ ਹੈ।")
    elif magnet_poles_experiment:
        if a.startswith("Like"):
            result = ("Like poles (N–N) repel, so both bar magnets move apart. Each magnet has both north and south poles." if not is_pa else "ਇੱਕੋ ਜਿਹੇ ਧਰੁਵ (N–N) ਇੱਕ-ਦੂਜੇ ਨੂੰ ਦੂਰ ਧੱਕਦੇ ਹਨ, ਇਸ ਲਈ ਦੋਵੇਂ ਬਾਰ ਚੁੰਬਕ ਦੂਰ ਹੁੰਦੇ ਹਨ। ਹਰ ਚੁੰਬਕ ਵਿੱਚ ਉੱਤਰੀ ਅਤੇ ਦੱਖਣੀ ਦੋਵੇਂ ਧਰੁਵ ਹੁੰਦੇ ਹਨ।")
        else:
            result = ("Unlike poles (N–S) attract, so the magnets move toward each other and touch in this simplified model. Each magnet has both N and S poles." if not is_pa else "ਵੱਖਰੇ ਧਰੁਵ (N–S) ਇੱਕ-ਦੂਜੇ ਨੂੰ ਖਿੱਚਦੇ ਹਨ, ਇਸ ਲਈ ਇਸ ਸਰਲ ਮਾਡਲ ਵਿੱਚ ਦੋਵੇਂ ਚੁੰਬਕ ਨੇੜੇ ਆ ਕੇ ਛੂਹਦੇ ਹਨ। ਹਰ ਚੁੰਬਕ ਵਿੱਚ N ਅਤੇ S ਦੋਵੇਂ ਧਰੁਵ ਹੁੰਦੇ ਹਨ।")
    elif force_examples_experiment:
        if a == "Push a shopping cart":
            result = ("Pushing the cart applies a force that can make it move or change its speed." if not is_pa else "ਗੱਡੀ ਨੂੰ ਧੱਕਣ ਨਾਲ ਲੱਗਿਆ ਬਲ ਇਸ ਨੂੰ ਚਲਾ ਸਕਦਾ ਹੈ ਜਾਂ ਇਸ ਦੀ ਚਾਲ ਬਦਲ ਸਕਦਾ ਹੈ।")
        elif a == "Kick a football":
            result = ("A kick is a push that can start the ball moving or change its direction." if not is_pa else "ਲੱਤ ਮਾਰਨਾ ਧੱਕਾ ਹੈ, ਜੋ ਗੇਂਦ ਨੂੰ ਚਲਾ ਸਕਦਾ ਹੈ ਜਾਂ ਇਸ ਦੀ ਦਿਸ਼ਾ ਬਦਲ ਸਕਦਾ ਹੈ।")
        elif a == "Pull a wagon":
            result = ("Pulling applies a force toward the person and can move the wagon." if not is_pa else "ਖਿੱਚਣ ਨਾਲ ਵਿਅਕਤੀ ਵੱਲ ਬਲ ਲੱਗਦਾ ਹੈ ਅਤੇ ਗੱਡਾ ਹਿੱਲ ਸਕਦਾ ਹੈ।")
        else:
            result = ("Pulling the handle applies a force that opens the drawer." if not is_pa else "ਹੈਂਡਲ ਖਿੱਚਣ ਨਾਲ ਬਲ ਲੱਗਦਾ ਹੈ ਅਤੇ ਦਰਾਜ਼ ਖੁੱਲ੍ਹਦੀ ਹੈ।")
    elif shadow_examples_experiment:
        shadow_results = {
            "Torch and hand": ("The hand blocks some torchlight, so a shadow forms behind it.", "ਹੱਥ ਟਾਰਚ ਦੀ ਰੋਸ਼ਨੀ ਰੋਕਦਾ ਹੈ, ਇਸ ਲਈ ਪਿੱਛੇ ਪਰਛਾਵਾਂ ਬਣਦਾ ਹੈ।"),
            "Tree on a sunny day": ("A tree blocks sunlight and casts a shadow on the ground.", "ਦਰੱਖਤ ਸੂਰਜ ਦੀ ਰੋਸ਼ਨੀ ਰੋਕਦਾ ਹੈ ਅਤੇ ਜ਼ਮੀਨ ਉੱਤੇ ਪਰਛਾਵਾਂ ਪੈਂਦਾ ਹੈ।"),
            "Opaque book blocking light": ("An opaque book blocks light and makes a distinct dark shadow.", "ਅਪਾਰਦਰਸ਼ੀ ਕਿਤਾਬ ਰੋਸ਼ਨੀ ਰੋਕਦੀ ਹੈ ਅਤੇ ਸਪਸ਼ਟ ਗੂੜ੍ਹਾ ਪਰਛਾਵਾਂ ਬਣਾਉਂਦੀ ਹੈ।"),
            "Translucent curtain": ("A translucent curtain lets some light through, so the shadow is usually softer and fainter.", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ ਪਰਦਾ ਕੁਝ ਰੋਸ਼ਨੀ ਲੰਘਣ ਦਿੰਦਾ ਹੈ, ਇਸ ਲਈ ਪਰਛਾਵਾਂ ਆਮ ਤੌਰ ਤੇ ਹਲਕਾ ਹੁੰਦਾ ਹੈ।")
        }
        result = shadow_results[a][1] if is_pa else shadow_results[a][0]
    elif slow_fast_experiment:
        if a == "Slow motion":
            result = ("Slow motion: a tortoise or a walking person usually covers less distance in the same time." if not is_pa else "ਹੌਲੀ ਗਤੀ: ਕੱਛੂਆ ਜਾਂ ਪੈਦਲ ਚੱਲਦਾ ਵਿਅਕਤੀ ਆਮ ਤੌਰ ਤੇ ਇੱਕੋ ਸਮੇਂ ਵਿੱਚ ਘੱਟ ਦੂਰੀ ਤੈਅ ਕਰਦਾ ਹੈ।")
        else:
            result = ("Fast motion: a racing car or a fast train usually covers more distance in the same time." if not is_pa else "ਤੇਜ਼ ਗਤੀ: ਰੇਸਿੰਗ ਕਾਰ ਜਾਂ ਤੇਜ਼ ਰੇਲ ਆਮ ਤੌਰ ਤੇ ਇੱਕੋ ਸਮੇਂ ਵਿੱਚ ਵੱਧ ਦੂਰੀ ਤੈਅ ਕਰਦੀ ਹੈ।")
    elif balanced_forces_examples_experiment:
        if a == "Both people push the table to the right":
            result = ("Both people push in the same direction, so their effects add together. The forces are unbalanced and the table moves to the right." if not is_pa else "ਦੋਵੇਂ ਵਿਅਕਤੀ ਇੱਕੋ ਦਿਸ਼ਾ ਵਿੱਚ ਧੱਕਦੇ ਹਨ, ਇਸ ਲਈ ਉਨ੍ਹਾਂ ਦੇ ਬਲ ਇਕੱਠੇ ਹੋ ਜਾਂਦੇ ਹਨ। ਬਲ ਅਸੰਤੁਲਿਤ ਹਨ ਅਤੇ ਮੇਜ਼ ਸੱਜੇ ਵੱਲ ਚੱਲਦੀ ਹੈ।")
        elif a == "People push equally in opposite directions":
            result = ("The two pushes are equal and opposite. They balance each other, so the table’s motion does not change; if it was at rest, it stays at rest." if not is_pa else "ਦੋਵੇਂ ਧੱਕੇ ਬਰਾਬਰ ਅਤੇ ਉਲਟ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਹਨ। ਇਹ ਇੱਕ-ਦੂਜੇ ਨੂੰ ਸੰਤੁਲਿਤ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਮੇਜ਼ ਦੀ ਗਤੀ ਨਹੀਂ ਬਦਲਦੀ; ਜੇ ਇਹ ਪਹਿਲਾਂ ਸਥਿਰ ਸੀ ਤਾਂ ਸਥਿਰ ਰਹਿੰਦੀ ਹੈ।")
        else:
            result = ("The pushes are opposite but unequal. The stronger push to the left makes the forces unbalanced, so the table accelerates left." if not is_pa else "ਧੱਕੇ ਉਲਟ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਹਨ ਪਰ ਬਰਾਬਰ ਨਹੀਂ। ਖੱਬੇ ਪਾਸੇ ਦਾ ਵੱਧ ਬਲ ਅਸੰਤੁਲਨ ਪੈਦਾ ਕਰਦਾ ਹੈ, ਇਸ ਲਈ ਮੇਜ਼ ਖੱਬੇ ਵੱਲ ਤੇਜ਼ ਹੁੰਦੀ ਹੈ।")
    elif class9_newton_experiment:
        strong_push = a == "Strong push"
        loaded_cart = b == "Loaded cart"
        if strong_push and not loaded_cart:
            result = ("A stronger net force produces greater acceleration when the mass is small. This is a qualitative model, with no numerical calculations." if not is_pa else "ਘੱਟ ਪੁੰਜ ਵਾਲੀ ਗੱਡੀ ਉੱਤੇ ਵੱਧ ਨਤੀਜਕ ਬਲ ਵੱਧ ਤਵਰਣ ਪੈਦਾ ਕਰਦਾ ਹੈ। ਇਹ ਗੁਣਾਤਮਕ ਮਾਡਲ ਹੈ, ਕੋਈ ਸੰਖਿਆਤਮਕ ਗਣਨਾ ਨਹੀਂ।")
        elif not strong_push and loaded_cart:
            result = ("A loaded cart accelerates less under a gentle push because its mass is greater." if not is_pa else "ਵੱਧ ਪੁੰਜ ਵਾਲੀ ਭਰੀ ਗੱਡੀ ਹਲਕੇ ਧੱਕੇ ਨਾਲ ਘੱਟ ਤਵਰਣ ਕਰਦੀ ਹੈ।")
        elif strong_push and loaded_cart:
            result = ("A stronger push helps the loaded cart accelerate more than a gentle push would, although its greater mass resists changes in motion." if not is_pa else "ਜ਼ੋਰਦਾਰ ਧੱਕਾ ਭਰੀ ਗੱਡੀ ਨੂੰ ਹਲਕੇ ਧੱਕੇ ਨਾਲੋਂ ਵੱਧ ਤਵਰਣ ਦਿੰਦਾ ਹੈ, ਪਰ ਵੱਧ ਪੁੰਜ ਗਤੀ ਵਿੱਚ ਤਬਦੀਲੀ ਦਾ ਵਿਰੋਧ ਕਰਦਾ ਹੈ।")
        else:
            result = ("A light cart responds more readily to a gentle push than a loaded cart would." if not is_pa else "ਹਲਕੀ ਗੱਡੀ ਹਲਕੇ ਧੱਕੇ ਨਾਲ ਵੀ ਭਾਰੀ ਗੱਡੀ ਨਾਲੋਂ ਆਸਾਨੀ ਨਾਲ ਗਤੀ ਬਦਲਦੀ ਹੈ।")
    elif class9_work_energy_experiment:
        if a == "Pushing a box forward":
            result = ("When a force moves the box in the direction of the push, mechanical work is done. Energy is transferred to the moving box." if not is_pa else "ਜਦੋਂ ਬਲ ਡੱਬੇ ਨੂੰ ਧੱਕੇ ਦੀ ਦਿਸ਼ਾ ਵਿੱਚ ਹਿਲਾਉਂਦਾ ਹੈ, ਤਾਂ ਮਕੈਨੀਕੀ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਊਰਜਾ ਚੱਲਦੇ ਡੱਬੇ ਨੂੰ ਮਿਲਦੀ ਹੈ।")
        elif a == "Lifting a box upward":
            result = ("Lifting the box does work against gravity. As its height increases, its gravitational potential energy increases." if not is_pa else "ਡੱਬੇ ਨੂੰ ਚੁੱਕਣ ਸਮੇਂ ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਦੇ ਵਿਰੁੱਧ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਉਚਾਈ ਵਧਣ ਨਾਲ ਇਸ ਦੀ ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ ਵਧਦੀ ਹੈ।")
        else:
            result = ("If the box does not move, no mechanical work is done on it by the holding force, even though effort is applied." if not is_pa else "ਜੇ ਡੱਬਾ ਹਿਲਦਾ ਨਹੀਂ, ਤਾਂ ਫੜਨ ਵਾਲੇ ਬਲ ਦੁਆਰਾ ਉਸ ਉੱਤੇ ਮਕੈਨੀਕੀ ਕੰਮ ਨਹੀਂ ਹੁੰਦਾ, ਭਾਵੇਂ ਜ਼ੋਰ ਲਾਇਆ ਜਾ ਰਿਹਾ ਹੋਵੇ।")
    elif class9_speed_acceleration_experiment:
        motion_results = {
            "Starting from rest and speeding up": ("The vehicle's speed increases. Its velocity changes with time, so it is accelerating.", "ਵਾਹਨ ਦੀ ਚਾਲ ਵਧਦੀ ਹੈ। ਸਮੇਂ ਨਾਲ ਇਸ ਦਾ ਵੇਗ ਬਦਲਦਾ ਹੈ, ਇਸ ਲਈ ਤਵਰਣ ਹੁੰਦਾ ਹੈ।"),
            "Moving at steady speed": ("If the vehicle keeps the same speed in a straight line, its velocity is constant and its acceleration is zero.", "ਜੇ ਵਾਹਨ ਸਿੱਧੀ ਰੇਖਾ ਵਿੱਚ ਇਕੋ ਚਾਲ ਨਾਲ ਚੱਲਦਾ ਹੈ ਤਾਂ ਵੇਗ ਸਥਿਰ ਹੈ ਅਤੇ ਤਵਰਣ ਸਿਫ਼ਰ ਹੈ।"),
            "Slowing down": ("The vehicle's speed decreases. This is negative acceleration (deceleration) relative to its direction of motion.", "ਵਾਹਨ ਦੀ ਚਾਲ ਘਟਦੀ ਹੈ। ਗਤੀ ਦੀ ਦਿਸ਼ਾ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਇਸ ਨੂੰ ਰਿਣਾਤਮਕ ਤਵਰਣ ਜਾਂ ਮੰਦਨ ਕਹਿੰਦੇ ਹਨ।"),
            "Changing direction": ("Velocity includes direction as well as speed. A change in direction means velocity changes, so acceleration occurs even if speed stays the same.", "ਵੇਗ ਵਿੱਚ ਚਾਲ ਦੇ ਨਾਲ ਦਿਸ਼ਾ ਵੀ ਸ਼ਾਮਲ ਹੁੰਦੀ ਹੈ। ਦਿਸ਼ਾ ਬਦਲਣ ਨਾਲ ਵੇਗ ਬਦਲਦਾ ਹੈ, ਇਸ ਲਈ ਇਕੋ ਚਾਲ ਹੋਣ ਤੇ ਵੀ ਤਵਰਣ ਹੋ ਸਕਦਾ ਹੈ।")
        }
        result = motion_results[a][1] if is_pa else motion_results[a][0]
    elif kind in ("motion","speed"):
        value = float(a) / max(1.0,float(b))
        result = f"Average speed = {value:.2f} m/s" if not is_pa else f"ਔਸਤ ਚਾਲ = {value:.2f} m/s"
    elif kind in ("force","newton"):
        result = f"Acceleration = {float(a)/max(1.0,float(b)):.2f} m/s² (F/m)" if not is_pa else f"ਤਵਰਣ = {float(a)/max(1.0,float(b)):.2f} m/s² (F/m)"
    elif kind == "acceleration" and not class9_speed_acceleration_experiment:
        result = f"Average acceleration from rest = {float(a)/max(1.0,float(b)):.2f} m/s²" if not is_pa else f"ਆਰਾਮ ਤੋਂ ਔਸਤ ਤਵਰਣ = {float(a)/max(1.0,float(b)):.2f} m/s²"
    elif kind == "work" and not class10_work_power_energy_experiment:
        result = f"Work = {float(a)*float(b):.2f} J; average power is work/time (set a time in a real measurement)." if not is_pa else f"ਕੰਮ = {float(a)*float(b):.2f} J"
    elif kind == "potential" and not class9_gravity_experiment:
        result = f"Gravitational potential energy ≈ {float(a)*9.8*float(b):.2f} J" if not is_pa else f"ਗੁਰੁਤਵਾਕਰਸ਼ੀ ਸਥਿਤਿਜ ਊਰਜਾ ≈ {float(a)*9.8*float(b):.2f} J"
    elif pressure_area_examples_experiment:
        if a == "Snowshoes vs high heels":
            result = ("Snowshoes spread a person's weight over a larger area, so pressure on snow is lower. A narrow heel concentrates the same body weight on a small area, creating higher pressure." if not is_pa else "ਬਰਫ਼ ਵਾਲੇ ਜੁੱਤੇ ਸਰੀਰ ਦਾ ਭਾਰ ਵੱਡੇ ਖੇਤਰਫਲ ਉੱਤੇ ਫੈਲਾਉਂਦੇ ਹਨ, ਇਸ ਲਈ ਬਰਫ਼ ਉੱਤੇ ਦਬਾਅ ਘੱਟ ਹੁੰਦਾ ਹੈ। ਤੰਗ ਅੱਡੀ ਉਹੀ ਭਾਰ ਛੋਟੇ ਖੇਤਰ ਉੱਤੇ ਪਾਉਂਦੀ ਹੈ, ਇਸ ਲਈ ਦਬਾਅ ਵੱਧ ਹੁੰਦਾ ਹੈ।")
        elif a == "Sharp knife vs blunt knife":
            result = ("A sharp edge touches a very small area and creates greater pressure for the same push, helping it cut. A blunt edge spreads the push over a larger area and creates less pressure." if not is_pa else "ਤੇਜ਼ ਧਾਰ ਬਹੁਤ ਛੋਟੇ ਖੇਤਰ ਨੂੰ ਛੂੰਹਦੀ ਹੈ ਅਤੇ ਇੱਕੋ ਧੱਕੇ ਨਾਲ ਵੱਧ ਦਬਾਅ ਬਣਾਉਂਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਕੱਟਣਾ ਸੌਖਾ ਹੁੰਦਾ ਹੈ। ਮੋਟੀ ਧਾਰ ਬਲ ਨੂੰ ਵੱਡੇ ਖੇਤਰ ਵਿੱਚ ਫੈਲਾਉਂਦੀ ਹੈ ਅਤੇ ਦਬਾਅ ਘੱਟ ਬਣਦਾ ਹੈ।")
        elif a == "Broad tractor tyres vs narrow tyres":
            result = ("Broad tyres spread the tractor's weight over a larger contact area and reduce pressure on soft soil. Narrow tyres concentrate the weight on a smaller area and produce greater pressure." if not is_pa else "ਚੌੜੇ ਟਾਇਰ ਟਰੈਕਟਰ ਦਾ ਭਾਰ ਵੱਡੇ ਸੰਪਰਕ ਖੇਤਰਫਲ ਉੱਤੇ ਫੈਲਾ ਕੇ ਨਰਮ ਮਿੱਟੀ ਉੱਤੇ ਦਬਾਅ ਘਟਾਉਂਦੇ ਹਨ। ਤੰਗ ਟਾਇਰ ਭਾਰ ਛੋਟੇ ਖੇਤਰ ਉੱਤੇ ਪਾ ਕੇ ਵੱਧ ਦਬਾਅ ਬਣਾਉਂਦੇ ਹਨ।")
        else:
            result = ("A wide building foundation spreads the building's weight over more ground and reduces pressure on the soil. A narrow foundation concentrates the load and increases pressure." if not is_pa else "ਚੌੜੀ ਇਮਾਰਤੀ ਨੀਂਹ ਇਮਾਰਤ ਦਾ ਭਾਰ ਵੱਧ ਜ਼ਮੀਨ ਉੱਤੇ ਫੈਲਾਉਂਦੀ ਹੈ ਅਤੇ ਮਿੱਟੀ ਉੱਤੇ ਦਬਾਅ ਘਟਾਉਂਦੀ ਹੈ। ਤੰਗ ਨੀਂਹ ਭਾਰ ਨੂੰ ਘੱਟ ਖੇਤਰ ਉੱਤੇ ਕੇਂਦਰਿਤ ਕਰਦੀ ਹੈ ਅਤੇ ਦਬਾਅ ਵਧਾਉਂਦੀ ਹੈ।")
    elif kind == "pressure_area" and not pressure_area_examples_experiment:
        result = f"Pressure = {float(a)/(float(b)/10000):.2f} Pa" if not is_pa else f"ਦਬਾਅ = {float(a)/(float(b)/10000):.2f} Pa"
    elif kind == "pressure" and not liquid_pressure_examples_experiment:
        result = f"Hydrostatic pressure (gauge) ≈ ρgh = {float(a)*float(b)*9.8:.2f} Pa" if not is_pa else f"ਤਰਲ ਦਬਾਅ ≈ ρgh = {float(a)*float(b)*9.8:.2f} Pa"
    elif kind == "reflection" and not reflection_angle_experiment:
        result = f"Angle of reflection = {a}° for an ideal plane mirror." if not is_pa else f"ਆਦਰਸ਼ ਸ਼ੀਸ਼ੇ ਲਈ ਪਰਾਵਰਤਨ ਕੋਣ = {a}°।"
    elif kind == "refraction":
        result = f"Illustrative refractive index = {b}; ray bending depends on both media and incident angle." if not is_pa else f"ਸਮਝਾਉਣ ਲਈ ਅਪਵਰਤਨ ਅੰਕ = {b}।"
    elif kind == "magnet" and not magnet_poles_experiment:
        result = "Attraction" if a == "Unlike poles" else "Repulsion"
        if is_pa: result = "ਖਿੱਚ" if a == "Unlike poles" else "ਵਿਕਰਸ਼ਣ"
    elif class8_sound_wave_examples_experiment:
        result = ("A louder sound is shown with a taller wave (greater amplitude), while a softer sound has a smaller wave. A high-pitched sound has more wave cycles in the same space than a low-pitched sound. This is a qualitative visual; no measurements are calculated." if not is_pa else "ਉੱਚੀ ਆਵਾਜ਼ ਨੂੰ ਵੱਡੀ ਐਂਪਲੀਟਿਊਡ ਵਾਲੀ ਤਰੰਗ ਅਤੇ ਹੌਲੀ ਆਵਾਜ਼ ਨੂੰ ਛੋਟੀ ਤਰੰਗ ਨਾਲ ਦਿਖਾਇਆ ਗਿਆ ਹੈ। ਉੱਚੀ ਸੁਰ ਵਿੱਚ ਇੱਕੋ ਥਾਂ ਅੰਦਰ ਨੀਵੀਂ ਸੁਰ ਨਾਲੋਂ ਵੱਧ ਤਰੰਗ-ਚੱਕਰ ਹੁੰਦੇ ਹਨ। ਇਹ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ ਹੈ; ਕੋਈ ਗਣਨਾ ਨਹੀਂ ਕੀਤੀ ਜਾਂਦੀ।")
    elif kind in ("sound","wave") and not class10_wave_sound_experiment:
        result = f"Frequency = {a} Hz; period ≈ {1/float(a):.4f} s; amplitude setting = {c}/10." if not is_pa else f"ਆਵ੍ਰਿਤੀ = {a} Hz; ਆਵਰਤ ਕਾਲ ≈ {1/float(a):.4f} s।"
    elif kind == "friction" and not friction_types_experiment:
        result = f"Illustrative friction tendency rises with roughness and normal force (mass setting {b} kg)." if not is_pa else f"ਖੁਰਦਰਾਪਣ ਅਤੇ ਲੰਬਕਾਰੀ ਬਲ ਵਧਣ ਨਾਲ ਘਰਸ਼ਣ ਦੀ ਰੁਝਾਨੀ ਮਾਤਰਾ ਵਧਦੀ ਹੈ।"
    elif kind == "balanced":
        net = float(a)-float(b)
        result = f"Net force = {net:.1f} N; " + ("balanced" if net == 0 else "rightward resultant" if net > 0 else "leftward resultant")
        if is_pa: result = f"ਕੁੱਲ ਬਲ = {net:.1f} N"
    elif heat_conduction_examples_experiment:
        is_conductor = a in ("Metal rod (iron / steel)", "Copper spoon")
        result = "Metals such as iron, steel and copper conduct heat relatively well. Heating one end transfers thermal energy along the material toward the cooler end. Wood and plastic are comparatively poor conductors, so heat travels through them much less readily. This is a qualitative illustration, not a timed measurement." if not is_pa else "ਲੋਹਾ, ਸਟੀਲ ਅਤੇ ਤਾਂਬਾ ਵਰਗੀਆਂ ਧਾਤਾਂ ਤਾਪ ਦੀਆਂ ਚੰਗੀਆਂ ਚਾਲਕ ਹਨ। ਇੱਕ ਸਿਰਾ ਗਰਮ ਕਰਨ ਨਾਲ ਤਾਪੀ ਊਰਜਾ ਠੰਢੇ ਸਿਰੇ ਵੱਲ ਪਹੁੰਚਦੀ ਹੈ। ਲੱਕੜ ਅਤੇ ਪਲਾਸਟਿਕ ਤਾਪ ਦੇ ਮਾੜੇ ਚਾਲਕ ਹਨ, ਇਸ ਲਈ ਇਨ੍ਹਾਂ ਵਿੱਚੋਂ ਤਾਪ ਘੱਟ ਆਸਾਨੀ ਨਾਲ ਲੰਘਦਾ ਹੈ। ਇਹ ਗੁਣਾਤਮਕ ਚਿੱਤਰ ਹੈ, ਸਮੇਂ ਨਾਲ ਮਾਪ ਨਹੀਂ।"
    elif kind == "heat":
        result = f"{b} is represented qualitatively; actual heat transfer depends on dimensions and conditions." if not is_pa else f"{b} ਦਾ ਤਾਪ ਚਾਲਨ ਗੁਣਾਤਮਕ ਤੌਰ ਤੇ ਦਿਖਾਇਆ ਗਿਆ ਹੈ।"
    elif kind == "shadow" and not shadow_examples_experiment:
        result = "A larger object or a closer light source can produce a larger shadow in this simplified setup." if not is_pa else "ਇਸ ਸਧਾਰਨ ਮਾਡਲ ਵਿੱਚ ਵੱਡੀ ਵਸਤੂ ਜਾਂ ਨੇੜੇ ਰੋਸ਼ਨੀ ਨਾਲ ਵੱਡਾ ਪਰਛਾਵਾਂ ਬਣ ਸਕਦਾ ਹੈ।"
    elif class10_wave_sound_experiment:
        wave_sound_results = {
            "Low pitch — long wavelength": ("A lower-frequency sound has a lower pitch and a longer wavelength in the same medium. The sound-wave model shows more widely spaced compressions.", "ਘੱਟ ਆਵ੍ਰਿਤੀ ਵਾਲੀ ਧੁਨੀ ਦੀ ਸੁਰ ਨੀਵੀਂ ਅਤੇ ਉਸੇ ਮਾਧਿਅਮ ਵਿੱਚ ਤਰੰਗ-ਲੰਬਾਈ ਲੰਮੀ ਹੁੰਦੀ ਹੈ। ਮਾਡਲ ਵਿੱਚ ਸੰਘਣਨ ਵਧੇਰੇ ਦੂਰ-ਦੂਰ ਦਿਖਾਏ ਗਏ ਹਨ।"),
            "High pitch — short wavelength": ("A higher-frequency sound has a higher pitch and a shorter wavelength in the same medium. The model shows compressions closer together.", "ਵੱਧ ਆਵ੍ਰਿਤੀ ਵਾਲੀ ਧੁਨੀ ਦੀ ਸੁਰ ਉੱਚੀ ਅਤੇ ਉਸੇ ਮਾਧਿਅਮ ਵਿੱਚ ਤਰੰਗ-ਲੰਬਾਈ ਛੋਟੀ ਹੁੰਦੀ ਹੈ। ਮਾਡਲ ਵਿੱਚ ਸੰਘਣਨ ਨੇੜੇ-ਨੇੜੇ ਦਿਖਾਏ ਗਏ ਹਨ।"),
            "Soft sound — small amplitude": ("A softer sound is represented with smaller wave amplitude. In this simplified model, the spacing is kept similar so that amplitude is the feature being compared.", "ਹੌਲੀ ਧੁਨੀ ਨੂੰ ਛੋਟੀ ਐਂਪਲੀਟਿਊਡ ਨਾਲ ਦਰਸਾਇਆ ਗਿਆ ਹੈ। ਇਸ ਸਰਲ ਮਾਡਲ ਵਿੱਚ ਦੂਰੀ ਲਗਭਗ ਇੱਕੋ ਰੱਖੀ ਗਈ ਹੈ ਤਾਂ ਜੋ ਐਂਪਲੀਟਿਊਡ ਦੀ ਤੁਲਨਾ ਹੋ ਸਕੇ।"),
            "Loud sound — large amplitude": ("A louder sound is represented with larger wave amplitude. Loudness relates mainly to amplitude, while pitch relates to frequency.", "ਉੱਚੀ ਆਵਾਜ਼ ਵਾਲੀ ਧੁਨੀ ਨੂੰ ਵੱਡੀ ਐਂਪਲੀਟਿਊਡ ਨਾਲ ਦਰਸਾਇਆ ਗਿਆ ਹੈ। ਉੱਚੀ ਆਵਾਜ਼ ਮੁੱਖ ਤੌਰ ਤੇ ਐਂਪਲੀਟਿਊਡ ਨਾਲ ਅਤੇ ਸੁਰ ਆਵ੍ਰਿਤੀ ਨਾਲ ਸੰਬੰਧਿਤ ਹੈ।")
        }
        result = wave_sound_results[a][1] if is_pa else wave_sound_results[a][0]
    elif class10_work_power_energy_experiment:
        work_power_results = {
            "Pushing a box and it moves": ("Work is done when a force causes displacement in its direction. The moving box shows force and displacement together.", "ਜਦੋਂ ਬਲ ਵਸਤੂ ਦਾ ਆਪਣੀ ਦਿਸ਼ਾ ਵਿੱਚ ਵਿਸਥਾਪਨ ਕਰਦਾ ਹੈ ਤਾਂ ਕੰਮ ਹੁੰਦਾ ਹੈ। ਚੱਲਦਾ ਡੱਬਾ ਬਲ ਅਤੇ ਵਿਸਥਾਪਨ ਦੋਵੇਂ ਦਿਖਾਉਂਦਾ ਹੈ।"),
            "Lifting a load": ("Lifting the load requires work against gravity, transferring energy to the raised object.", "ਭਾਰ ਨੂੰ ਉੱਪਰ ਚੁੱਕਣ ਲਈ ਗੁਰੁਤਵਾਕਰਸ਼ਣ ਦੇ ਵਿਰੁੱਧ ਕੰਮ ਕਰਨਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਵਸਤੂ ਦੀ ਊਰਜਾ ਵਧਦੀ ਹੈ।"),
            "Holding a box still": ("If the box does not move, there is no displacement; in the school-physics sense, no mechanical work is done on the box by the holding force.", "ਜੇ ਡੱਬਾ ਹਿਲਦਾ ਨਹੀਂ ਤਾਂ ਵਿਸਥਾਪਨ ਨਹੀਂ ਹੁੰਦਾ; ਸਕੂਲੀ ਭੌਤਿਕ ਵਿਗਿਆਨ ਅਨੁਸਾਰ ਫੜਨ ਵਾਲੇ ਬਲ ਦੁਆਰਾ ਡੱਬੇ ਉੱਤੇ ਮਕੈਨੀਕੀ ਕੰਮ ਨਹੀਂ ਹੁੰਦਾ।"),
            "Doing the same task quickly": ("Power describes how quickly work is done. Doing the same work in less time means greater power.", "ਸ਼ਕਤੀ ਦੱਸਦੀ ਹੈ ਕਿ ਕੰਮ ਕਿੰਨੀ ਜਲਦੀ ਹੁੰਦਾ ਹੈ। ਉਹੀ ਕੰਮ ਘੱਟ ਸਮੇਂ ਵਿੱਚ ਕਰਨ ਦਾ ਅਰਥ ਵੱਧ ਸ਼ਕਤੀ ਹੈ।"),
            "Doing the same task slowly": ("Power describes how quickly work is done. Doing the same work in more time means lower power.", "ਸ਼ਕਤੀ ਦੱਸਦੀ ਹੈ ਕਿ ਕੰਮ ਕਿੰਨੀ ਜਲਦੀ ਹੁੰਦਾ ਹੈ। ਉਹੀ ਕੰਮ ਵੱਧ ਸਮੇਂ ਵਿੱਚ ਕਰਨ ਦਾ ਅਰਥ ਘੱਟ ਸ਼ਕਤੀ ਹੈ।")
        }
        result = work_power_results[a][1] if is_pa else work_power_results[a][0]
    elif class10_convex_lens_experiment:
        lens_results = {
            "Object beyond 2F": ("The image forms between F and 2F on the opposite side of the convex lens. It is real, inverted and smaller.", "ਪ੍ਰਤਿਬਿੰਬ ਉੱਤਲ ਲੈਂਸ ਦੇ ਦੂਜੇ ਪਾਸੇ F ਅਤੇ 2F ਵਿਚਕਾਰ ਬਣਦਾ ਹੈ। ਇਹ ਅਸਲੀ, ਉਲਟਾ ਅਤੇ ਛੋਟਾ ਹੁੰਦਾ ਹੈ।"),
            "Object at 2F": ("The image forms at 2F on the opposite side. It is real, inverted and the same size as the object.", "ਪ੍ਰਤਿਬਿੰਬ ਦੂਜੇ ਪਾਸੇ 2F ਉੱਤੇ ਬਣਦਾ ਹੈ। ਇਹ ਅਸਲੀ, ਉਲਟਾ ਅਤੇ ਵਸਤੂ ਦੇ ਬਰਾਬਰ ਆਕਾਰ ਦਾ ਹੁੰਦਾ ਹੈ।"),
            "Object between F and 2F": ("The image forms beyond 2F on the opposite side. It is real, inverted and enlarged.", "ਪ੍ਰਤਿਬਿੰਬ ਦੂਜੇ ਪਾਸੇ 2F ਤੋਂ ਪਰੇ ਬਣਦਾ ਹੈ। ਇਹ ਅਸਲੀ, ਉਲਟਾ ਅਤੇ ਵੱਡਾ ਹੁੰਦਾ ਹੈ।"),
            "Object at F": ("The emerging rays are parallel; the image is considered to form at infinity.", "ਬਾਹਰ ਨਿਕਲਣ ਵਾਲੀਆਂ ਕਿਰਨਾਂ ਸਮਾਂਤਰ ਹੁੰਦੀਆਂ ਹਨ; ਪ੍ਰਤਿਬਿੰਬ ਅਨੰਤ ਉੱਤੇ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ।"),
            "Object between lens and F": ("The image is on the same side as the object. It is virtual, upright and enlarged.", "ਪ੍ਰਤਿਬਿੰਬ ਵਸਤੂ ਵਾਲੇ ਪਾਸੇ ਬਣਦਾ ਹੈ। ਇਹ ਆਭਾਸੀ, ਸਿੱਧਾ ਅਤੇ ਵੱਡਾ ਹੁੰਦਾ ਹੈ।")
        }
        result = lens_results[a][1] if is_pa else lens_results[a][0]
    elif kind == "lens":
        result = f"Object distance = {a} cm; focal length = {b} cm. Image behaviour changes around the focal length." if not is_pa else f"ਵਸਤੂ ਦੀ ਦੂਰੀ = {a} cm; ਫੋਕਸ ਦੂਰੀ = {b} cm।"
    st.markdown("### " + ("ਨਿਰੀਖਣ" if is_pa else "Observation"))
    st.success(result or note)
    st.markdown("**" + ("ਵਿਗਿਆਨਕ ਵਿਆਖਿਆ" if is_pa else "Scientific explanation") + ":** " + note)
    with st.expander("🧠 " + ("ਸੋਚੋ ਅਤੇ ਜਵਾਬ ਦਿਓ" if is_pa else "Think and answer")):
        q = "ਕੰਟਰੋਲ ਬਦਲਣ ਨਾਲ ਨਤੀਜਾ ਕਿਉਂ ਬਦਲਿਆ?" if is_pa else "Why did the result change when you changed a control?"
        st.write(q)
        response = st.text_input("ਤੁਹਾਡਾ ਜਵਾਬ" if is_pa else "Your explanation", key=f"physics_reflect_{pc}_{ei}")
        if st.button("ਜਵਾਬ ਦਿਖਾਓ" if is_pa else "Show learning point", key=f"physics_hint_{pc}_{ei}"):
            st.info(note)
    st.caption("Virtual model for learning. Results are simplified and are not substitutes for measured laboratory data." if not is_pa else "ਇਹ ਸਿੱਖਣ ਲਈ ਵਰਚੁਅਲ ਮਾਡਲ ਹੈ। ਨਤੀਜੇ ਸਰਲ ਕੀਤੇ ਗਏ ਹਨ, ਅਸਲ ਲੈਬ ਮਾਪ ਨਹੀਂ।")


CHEMISTRY_EXPERIMENTS = {
    6: [
        ("Sorting Materials by Their Properties", "ਗੁਣਾਂ ਅਨੁਸਾਰ ਪਦਾਰਥਾਂ ਦੀ ਛਾਂਟੀ", "Compare materials by appearance, flexibility, transparency and texture.", "ਦਿੱਖ, ਲਚਕ, ਪਾਰਦਰਸ਼ਤਾ ਅਤੇ ਬਣਤਰ ਅਨੁਸਾਰ ਪਦਾਰਥਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "materials", "Materials have different observable properties; classify them using evidence.", "ਪਦਾਰਥਾਂ ਦੇ ਦਿੱਖਣ ਵਾਲੇ ਗੁਣ ਵੱਖਰੇ ਹੁੰਦੇ ਹਨ; ਸਬੂਤ ਦੇ ਆਧਾਰ ਤੇ ਵਰਗੀਕਰਨ ਕਰੋ।"),
        ("Soluble and Insoluble Substances", "ਘੁਲਣਸ਼ੀਲ ਅਤੇ ਅਘੁਲਣਸ਼ੀਲ ਪਦਾਰਥ", "Observe which sample mixes uniformly with water.", "ਵੇਖੋ ਕਿ ਕਿਹੜਾ ਨਮੂਨਾ ਪਾਣੀ ਵਿੱਚ ਇਕਸਾਰ ਮਿਲਦਾ ਹੈ।", "solubility", "Some substances dissolve in water while others remain separate.", "ਕੁਝ ਪਦਾਰਥ ਪਾਣੀ ਵਿੱਚ ਘੁਲ ਜਾਂਦੇ ਹਨ ਅਤੇ ਕੁਝ ਵੱਖਰੇ ਰਹਿੰਦੇ ਹਨ।"),
        ("Separate Sand from Water", "ਪਾਣੀ ਵਿੱਚੋਂ ਰੇਤ ਵੱਖ ਕਰਨਾ", "Model settling and filtration to separate an insoluble solid.", "ਅਘੁਲਣਸ਼ੀਲ ਠੋਸ ਨੂੰ ਵੱਖ ਕਰਨ ਲਈ ਤਲਛਟ ਅਤੇ ਛਾਣਨ ਦਾ ਮਾਡਲ ਵੇਖੋ।", "filtration", "Settling and filtration separate insoluble particles from water.", "ਤਲਛਟ ਅਤੇ ਛਾਣਨ ਨਾਲ ਪਾਣੀ ਵਿੱਚੋਂ ਅਘੁਲਣਸ਼ੀਲ ਕਣ ਵੱਖ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।"),
        ("Explore Changes in Materials", "ਪਦਾਰਥਾਂ ਵਿੱਚ ਤਬਦੀਲੀਆਂ", "Compare a change of state with a change that forms a new substance.", "ਅਵਸਥਾ ਬਦਲਣ ਅਤੇ ਨਵਾਂ ਪਦਾਰਥ ਬਣਨ ਵਾਲੀ ਤਬਦੀਲੀ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "changes", "A physical change does not form a new substance; a chemical change does.", "ਭੌਤਿਕ ਤਬਦੀਲੀ ਵਿੱਚ ਨਵਾਂ ਪਦਾਰਥ ਨਹੀਂ ਬਣਦਾ; ਰਸਾਇਣਕ ਤਬਦੀਲੀ ਵਿੱਚ ਬਣ ਸਕਦਾ ਹੈ।"),
        ("Observe Transparent, Translucent and Opaque Materials", "ਪਾਰਦਰਸ਼ੀ, ਅਰਧ-ਪਾਰਦਰਸ਼ੀ ਅਤੇ ਅਪਾਰਦਰਸ਼ੀ ਪਦਾਰਥ", "Compare how light passes through different materials.", "ਵੱਖ-ਵੱਖ ਪਦਾਰਥਾਂ ਵਿੱਚੋਂ ਰੋਸ਼ਨੀ ਲੰਘਣ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "transparency", "Transparent materials transmit most light; opaque materials block it.", "ਪਾਰਦਰਸ਼ੀ ਪਦਾਰਥ ਵੱਧ ਰੋਸ਼ਨੀ ਲੰਘਾਉਂਦੇ ਹਨ; ਅਪਾਰਦਰਸ਼ੀ ਪਦਾਰਥ ਰੋਕਦੇ ਹਨ।")
    ],
    7: [
        ("Acidic and Basic Substances with Indicators", "ਸੂਚਕਾਂ ਨਾਲ ਤੇਜ਼ਾਬੀ ਅਤੇ ਖਾਰੀ ਪਦਾਰਥ", "Use a virtual indicator to compare familiar household samples.", "ਘਰੇਲੂ ਨਮੂਨਿਆਂ ਦੀ ਤੁਲਨਾ ਵਰਚੁਅਲ ਸੂਚਕ ਨਾਲ ਕਰੋ।", "indicators", "Indicators change colour in acidic or basic conditions; never taste lab samples.", "ਸੂਚਕ ਤੇਜ਼ਾਬੀ ਜਾਂ ਖਾਰੀ ਹਾਲਤ ਵਿੱਚ ਰੰਗ ਬਦਲਦੇ ਹਨ; ਲੈਬ ਨਮੂਨੇ ਕਦੇ ਨਾ ਚੱਖੋ।"),
        ("Reversible and Irreversible Changes", "ਉਲਟਣਯੋਗ ਅਤੇ ਅਣਉਲਟਣਯੋਗ ਤਬਦੀਲੀਆਂ", "Compare examples of reversible and irreversible changes.", "ਉਲਟਣਯੋਗ ਅਤੇ ਅਣਉਲਟਣਯੋਗ ਤਬਦੀਲੀਆਂ ਦੀਆਂ ਉਦਾਹਰਨਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "reversible", "Melting and freezing can be reversed; burning usually cannot be reversed easily.", "ਪਿਘਲਣਾ ਅਤੇ ਜੰਮਣਾ ਉਲਟ ਸਕਦੇ ਹਨ; ਸਾੜਨ ਨੂੰ ਆਮ ਤੌਰ ਤੇ ਆਸਾਨੀ ਨਾਲ ਉਲਟਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ।"),
        ("Physical and Chemical Changes", "ਭੌਤਿਕ ਅਤੇ ਰਸਾਇਣਕ ਤਬਦੀਲੀਆਂ", "Distinguish state or shape changes from chemical reactions.", "ਅਵਸਥਾ ਜਾਂ ਆਕਾਰ ਦੀ ਤਬਦੀਲੀ ਨੂੰ ਰਸਾਇਣਕ ਕਿਰਿਆ ਤੋਂ ਵੱਖ ਪਛਾਣੋ।", "physical_chemical", "Evidence such as gas, colour change or a new solid may indicate a chemical change.", "ਗੈਸ, ਰੰਗ ਬਦਲਣਾ ਜਾਂ ਨਵਾਂ ਠੋਸ ਬਣਨਾ ਰਸਾਇਣਕ ਤਬਦੀਲੀ ਦਾ ਸੰਕੇਤ ਹੋ ਸਕਦਾ ਹੈ।"),
        ("Rusting of Iron", "ਲੋਹੇ ਨੂੰ ਜੰਗ ਲੱਗਣਾ", "Explore why iron rusts in the presence of air and moisture.", "ਹਵਾ ਅਤੇ ਨਮੀ ਦੀ ਮੌਜੂਦਗੀ ਵਿੱਚ ਲੋਹੇ ਨੂੰ ਜੰਗ ਕਿਉਂ ਲੱਗਦੀ ਹੈ, ਸਮਝੋ।", "rusting", "Rusting needs iron, oxygen and moisture; protective coatings slow it.", "ਜੰਗ ਲਈ ਲੋਹਾ, ਆਕਸੀਜਨ ਅਤੇ ਨਮੀ ਲੋੜੀਂਦੇ ਹਨ; ਸੁਰੱਖਿਆ ਪਰਤ ਇਸ ਨੂੰ ਹੌਲੀ ਕਰਦੀ ਹੈ।"),
        ("Separation of Mixtures", "ਮਿਸ਼ਰਣਾਂ ਨੂੰ ਵੱਖ ਕਰਨਾ", "Choose a suitable method for a mixture's properties.", "ਮਿਸ਼ਰਣ ਦੇ ਗੁਣਾਂ ਅਨੁਸਾਰ ਢੁਕਵਾਂ ਵੱਖ ਕਰਨ ਦਾ ਤਰੀਕਾ ਚੁਣੋ।", "separation", "Filtration, evaporation and magnetic separation work for different mixtures.", "ਛਾਣਨ, ਵਾਸ਼ਪੀਕਰਨ ਅਤੇ ਚੁੰਬਕੀ ਵੱਖਰਾ ਕਰਨਾ ਵੱਖ-ਵੱਖ ਮਿਸ਼ਰਣਾਂ ਲਈ ਢੁਕਵੇਂ ਹਨ।")
    ],
    8: [
        ("Combustion and Conditions for Burning", "ਦਹਿਨ ਅਤੇ ਸੜਨ ਦੀਆਂ ਸ਼ਰਤਾਂ", "Explore the fire triangle using a safe visual model.", "ਸੁਰੱਖਿਅਤ ਚਿੱਤਰਕ ਮਾਡਲ ਨਾਲ ਅੱਗ ਦੇ ਤਿਕੋਣ ਨੂੰ ਸਮਝੋ।", "combustion", "Combustion needs fuel, oxygen and sufficient heat.", "ਦਹਿਨ ਲਈ ਇੰਧਨ, ਆਕਸੀਜਨ ਅਤੇ ਕਾਫ਼ੀ ਤਾਪ ਲੋੜੀਂਦੇ ਹਨ।"),
        ("Flame Zones", "ਲਾਟ ਦੇ ਖੇਤਰ", "Identify the zones of a candle flame in a diagram.", "ਮੋਮਬੱਤੀ ਦੀ ਲਾਟ ਦੇ ਖੇਤਰ ਚਿੱਤਰ ਵਿੱਚ ਪਛਾਣੋ।", "flame", "A flame has zones with different temperatures and combustion conditions.", "ਲਾਟ ਦੇ ਵੱਖ-ਵੱਖ ਖੇਤਰਾਂ ਵਿੱਚ ਤਾਪਮਾਨ ਅਤੇ ਦਹਿਨ ਦੀਆਂ ਹਾਲਤਾਂ ਵੱਖਰੀਆਂ ਹੁੰਦੀਆਂ ਹਨ।"),
        ("Metals and Non-metals", "ਧਾਤਾਂ ਅਤੇ ਅਧਾਤਾਂ", "Compare typical physical properties of metals and non-metals.", "ਧਾਤਾਂ ਅਤੇ ਅਧਾਤਾਂ ਦੇ ਆਮ ਭੌਤਿਕ ਗੁਣਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "metals", "Metals are often lustrous and good conductors; exceptions exist.", "ਧਾਤਾਂ ਆਮ ਤੌਰ ਤੇ ਚਮਕਦਾਰ ਅਤੇ ਚੰਗੀਆਂ ਚਾਲਕ ਹੁੰਦੀਆਂ ਹਨ; ਅਪਵਾਦ ਵੀ ਹਨ।"),
        ("Chemical Effects of Air and Water", "ਹਵਾ ਅਤੇ ਪਾਣੀ ਦੇ ਰਸਾਇਣਕ ਪ੍ਰਭਾਵ", "Model corrosion and protective methods.", "ਖੋਰ ਅਤੇ ਇਸ ਤੋਂ ਬਚਾਅ ਦੇ ਤਰੀਕਿਆਂ ਦਾ ਮਾਡਲ ਵੇਖੋ।", "corrosion", "Air and moisture can cause corrosion in susceptible materials.", "ਹਵਾ ਅਤੇ ਨਮੀ ਸੰਵੇਦਨਸ਼ੀਲ ਪਦਾਰਥਾਂ ਵਿੱਚ ਖੋਰ ਪੈਦਾ ਕਰ ਸਕਦੇ ਹਨ।"),
        ("Crystallisation", "ਕ੍ਰਿਸਟਲੀਕਰਨ", "Visualise crystals forming as a solution cools or solvent evaporates.", "ਘੋਲ ਠੰਢਾ ਹੋਣ ਜਾਂ ਘੋਲਕ ਉੱਡਣ ਨਾਲ ਕ੍ਰਿਸਟਲ ਬਣਨ ਦਾ ਚਿੱਤਰ ਵੇਖੋ।", "crystals", "Crystallisation can obtain purer solid crystals from a suitable solution.", "ਕ੍ਰਿਸਟਲੀਕਰਨ ਨਾਲ ਢੁਕਵੇਂ ਘੋਲ ਵਿੱਚੋਂ ਵਧੇਰੇ ਸ਼ੁੱਧ ਠੋਸ ਕ੍ਰਿਸਟਲ ਮਿਲ ਸਕਦੇ ਹਨ।")
    ],
    9: [
        ("Prepare and Observe a Mixture and a Compound", "ਮਿਸ਼ਰਣ ਅਤੇ ਯੋਗਿਕ ਦੀ ਤਿਆਰੀ ਤੇ ਨਿਰੀਖਣ", "Compare a physical mixture with a substance formed by chemical combination.", "ਭੌਤਿਕ ਮਿਸ਼ਰਣ ਅਤੇ ਰਸਾਇਣਕ ਮਿਲਾਪ ਨਾਲ ਬਣੇ ਪਦਾਰਥ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "mixture_compound", "Mixture components retain their identity and may be separated physically; compounds have a fixed composition.", "ਮਿਸ਼ਰਣ ਦੇ ਅੰਸ਼ ਆਪਣੀ ਪਛਾਣ ਰੱਖਦੇ ਹਨ ਅਤੇ ਭੌਤਿਕ ਤਰੀਕੇ ਨਾਲ ਵੱਖ ਹੋ ਸਕਦੇ ਹਨ; ਯੋਗਿਕ ਦੀ ਬਣਤਰ ਨਿਰਧਾਰਤ ਹੁੰਦੀ ਹੈ।"),
        ("Atoms, Molecules and Particle Models", "ਪਰਮਾਣੂ, ਅਣੂ ਅਤੇ ਕਣ ਮਾਡਲ", "Explore how atoms combine into molecules using particle diagrams.", "ਕਣ ਚਿੱਤਰਾਂ ਨਾਲ ਸਮਝੋ ਕਿ ਪਰਮਾਣੂ ਮਿਲ ਕੇ ਅਣੂ ਕਿਵੇਂ ਬਣਾਉਂਦੇ ਹਨ।", "particles", "Particle models help represent atoms and molecules; they are not to scale.", "ਕਣ ਮਾਡਲ ਪਰਮਾਣੂਆਂ ਅਤੇ ਅਣੂਆਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ; ਇਹ ਅਸਲ ਮਾਪ ਅਨੁਸਾਰ ਨਹੀਂ ਹਨ।"),
        ("Law of Conservation of Mass", "ਪੁੰਜ ਸੰਰੱਖਣ ਦਾ ਨਿਯਮ", "Compare particle counts before and after a model reaction.", "ਮਾਡਲ ਕਿਰਿਆ ਤੋਂ ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ ਕਣਾਂ ਦੀ ਗਿਣਤੀ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "conservation", "In a closed system, atoms are rearranged rather than created or destroyed in a chemical reaction.", "ਬੰਦ ਪ੍ਰਣਾਲੀ ਵਿੱਚ ਰਸਾਇਣਕ ਕਿਰਿਆ ਦੌਰਾਨ ਪਰਮਾਣੂ ਮੁੜ-ਵਿਉਂਤ ਹੁੰਦੇ ਹਨ, ਬਣਦੇ ਜਾਂ ਨਸ਼ਟ ਨਹੀਂ ਹੁੰਦੇ।"),
        ("Solutions, Suspensions and Colloids", "ਘੋਲ, ਨਿਲੰਬਨ ਅਤੇ ਕੋਲਾਇਡ", "Compare how particles behave in different kinds of mixtures.", "ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਮਿਸ਼ਰਣਾਂ ਵਿੱਚ ਕਣਾਂ ਦੇ ਵਰਤਾਅ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "mixture_types", "Solutions are uniform; suspensions can settle; colloids have intermediate dispersed particles.", "ਘੋਲ ਇਕਸਾਰ ਹੁੰਦੇ ਹਨ; ਨਿਲੰਬਨ ਦੇ ਕਣ ਬੈਠ ਸਕਦੇ ਹਨ; ਕੋਲਾਇਡ ਵਿੱਚ ਦਰਮਿਆਨੇ ਆਕਾਰ ਦੇ ਫੈਲੇ ਕਣ ਹੁੰਦੇ ਹਨ।"),
        ("Separation by Evaporation and Distillation", "ਵਾਸ਼ਪੀਕਰਨ ਅਤੇ ਆਸਵਨ ਨਾਲ ਵੱਖਰਾ ਕਰਨਾ", "Compare evaporation with condensation-based distillation.", "ਵਾਸ਼ਪੀਕਰਨ ਦੀ ਸੰਘਣਨ ਵਾਲੇ ਆਸਵਨ ਨਾਲ ਤੁਲਨਾ ਕਰੋ।", "distillation", "Evaporation leaves dissolved solids behind; distillation also collects condensed vapour.", "ਵਾਸ਼ਪੀਕਰਨ ਨਾਲ ਘੁਲਿਆ ਠੋਸ ਪਿੱਛੇ ਰਹਿੰਦਾ ਹੈ; ਆਸਵਨ ਵਿੱਚ ਭਾਫ਼ ਨੂੰ ਸੰਘਣਾ ਕਰਕੇ ਇਕੱਠਾ ਵੀ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।")
    ],
    10: [
        ("Test Acids and Bases with Indicators", "ਸੂਚਕਾਂ ਨਾਲ ਤੇਜ਼ਾਬ ਅਤੇ ਖਾਰ ਦੀ ਜਾਂਚ", "Compare indicator colours for acidic, neutral and basic samples.", "ਤੇਜ਼ਾਬੀ, ਉਦਾਸੀਨ ਅਤੇ ਖਾਰੀ ਨਮੂਨਿਆਂ ਦੇ ਸੂਚਕ ਰੰਗਾਂ ਦੀ ਤੁਲਨਾ ਕਰੋ।", "ph", "Indicator colours help classify a solution; pH values are included only as a chemistry concept.", "ਸੂਚਕਾਂ ਦੇ ਰੰਗ ਘੋਲ ਦੀ ਕਿਸਮ ਪਛਾਣਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ; pH ਮੁੱਲ ਰਸਾਇਣਕ ਧਾਰਨਾ ਵਜੋਂ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।"),
        ("Observe a Chemical Reaction", "ਰਸਾਇਣਕ ਕਿਰਿਆ ਦਾ ਨਿਰੀਖਣ", "Identify evidence such as gas formation, colour change or precipitate in a reaction model.", "ਕਿਰਿਆ ਦੇ ਮਾਡਲ ਵਿੱਚ ਗੈਸ ਬਣਨਾ, ਰੰਗ ਬਦਲਣਾ ਜਾਂ ਅਵਖੇਪ ਬਣਨਾ ਪਛਾਣੋ।", "reaction", "Chemical reactions rearrange particles and may release or absorb energy.", "ਰਸਾਇਣਕ ਕਿਰਿਆਵਾਂ ਕਣਾਂ ਦੀ ਮੁੜ-ਵਿਉਂਤ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਊਰਜਾ ਛੱਡ ਜਾਂ ਸੋਖ ਸਕਦੀਆਂ ਹਨ।"),
        ("Neutralisation", "ਉਦਾਸੀਨੀਕਰਨ", "Model an acid reacting with a base to form salt and water.", "ਤੇਜ਼ਾਬ ਅਤੇ ਖਾਰ ਦੀ ਕਿਰਿਆ ਨਾਲ ਲੂਣ ਅਤੇ ਪਾਣੀ ਬਣਨ ਦਾ ਮਾਡਲ ਵੇਖੋ।", "neutralisation", "Acid + base can form salt and water; the model is conceptual.", "ਤੇਜ਼ਾਬ ਅਤੇ ਖਾਰ ਦੀ ਕਿਰਿਆ ਨਾਲ ਲੂਣ ਅਤੇ ਪਾਣੀ ਬਣ ਸਕਦੇ ਹਨ; ਇਹ ਧਾਰਣਾਤਮਕ ਮਾਡਲ ਹੈ।"),
        ("Reactivity of Metals", "ਧਾਤਾਂ ਦੀ ਕਿਰਿਆਸ਼ੀਲਤਾ", "Compare how selected metals behave in a conceptual reactivity series.", "ਧਾਰਣਾਤਮਕ ਕਿਰਿਆਸ਼ੀਲਤਾ ਲੜੀ ਵਿੱਚ ਚੁਣੀਆਂ ਧਾਤਾਂ ਦਾ ਵਰਤਾਅ ਸਮਝੋ।", "reactivity", "More reactive metals can displace less reactive metals from suitable salt solutions.", "ਵੱਧ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤਾਂ ਢੁਕਵੇਂ ਲੂਣ ਦੇ ਘੋਲ ਵਿੱਚੋਂ ਘੱਟ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ ਨੂੰ ਹਟਾ ਸਕਦੀਆਂ ਹਨ।"),
        ("Electrolysis and Electroplating", "ਇਲੈਕਟ੍ਰੋਲਾਈਸਿਸ ਅਤੇ ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ", "Visualise electrodes, ion movement and a thin metal coating.", "ਇਲੈਕਟ੍ਰੋਡ, ਆਇਨਾਂ ਦੀ ਗਤੀ ਅਤੇ ਧਾਤ ਦੀ ਪਤਲੀ ਪਰਤ ਦਾ ਚਿੱਤਰ ਵੇਖੋ।", "electrochemistry", "Electric current can drive chemical change and deposit metal on a suitable object.", "ਬਿਜਲੀ ਕਰੰਟ ਰਸਾਇਣਕ ਤਬਦੀਲੀ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਢੁਕਵੀਂ ਵਸਤੂ ਉੱਤੇ ਧਾਤ ਜਮਾ ਸਕਦਾ ਹੈ।")
    ]
}

def chemistry_visual(kind, pa, choice=None):
    """Return a class-appropriate SVG illustration for a chemistry concept."""
    titles = {
        "materials": ("MATERIAL PROPERTY SORT", "ਗੁਣਾਂ ਅਨੁਸਾਰ ਛਾਂਟੀ"),
        "solubility": ("DISSOLVE OR STAY SEPARATE?", "ਘੁਲੇ ਜਾਂ ਵੱਖਰੇ ਰਹਿਣ?"),
        "filtration": ("SETTLING AND FILTRATION", "ਤਲਛਟ ਅਤੇ ਛਾਣਨ"),
        "changes": ("PHYSICAL OR CHEMICAL CHANGE", "ਭੌਤਿਕ ਜਾਂ ਰਸਾਇਣਕ ਤਬਦੀਲੀ"),
        "transparency": ("HOW LIGHT PASSES", "ਰੋਸ਼ਨੀ ਕਿਵੇਂ ਲੰਘਦੀ ਹੈ"),
        "indicators": ("INDICATOR COLOUR TEST", "ਸੂਚਕ ਰੰਗ ਜਾਂਚ"),
        "reversible": ("REVERSIBLE / IRREVERSIBLE", "ਉਲਟਣਯੋਗ / ਅਣਉਲਟਣਯੋਗ"),
        "physical_chemical": ("COMPARE THE CHANGES", "ਤਬਦੀਲੀਆਂ ਦੀ ਤੁਲਨਾ"),
        "rusting": ("IRON + AIR + MOISTURE", "ਲੋਹਾ + ਹਵਾ + ਨਮੀ"),
        "separation": ("SEPARATION METHODS", "ਵੱਖ ਕਰਨ ਦੇ ਤਰੀਕੇ"),
        "combustion": ("THE FIRE TRIANGLE", "ਅੱਗ ਦਾ ਤਿਕੋਣ"),
        "flame": ("CANDLE FLAME ZONES", "ਮੋਮਬੱਤੀ ਦੀ ਲਾਟ ਦੇ ਖੇਤਰ"),
        "metals": ("METALS AND NON-METALS", "ਧਾਤਾਂ ਅਤੇ ਅਧਾਤਾਂ"),
        "corrosion": ("PROTECT AGAINST CORROSION", "ਖੋਰ ਤੋਂ ਬਚਾਅ"),
        "crystals": ("CRYSTAL FORMATION", "ਕ੍ਰਿਸਟਲ ਬਣਨਾ"),
        "mixture_compound": ("MIXTURE VS COMPOUND", "ਮਿਸ਼ਰਣ ਬਨਾਮ ਯੋਗਿਕ"),
        "particles": ("ATOMS FORM MOLECULES", "ਪਰਮਾਣੂਆਂ ਤੋਂ ਅਣੂ"),
        "conservation": ("ATOMS ARE REARRANGED", "ਪਰਮਾਣੂ ਮੁੜ-ਵਿਉਂਤ ਹੁੰਦੇ ਹਨ"),
        "mixture_types": ("THREE MIXTURE TYPES", "ਮਿਸ਼ਰਣਾਂ ਦੀਆਂ ਤਿੰਨ ਕਿਸਮਾਂ"),
        "distillation": ("EVAPORATION AND DISTILLATION", "ਵਾਸ਼ਪੀਕਰਨ ਅਤੇ ਆਸਵਨ"),
        "ph": ("INDICATORS AND pH", "ਸੂਚਕ ਅਤੇ pH"),
        "reaction": ("SIGNS OF A REACTION", "ਕਿਰਿਆ ਦੇ ਸੰਕੇਤ"),
        "neutralisation": ("ACID + BASE", "ਤੇਜ਼ਾਬ + ਖਾਰ"),
        "reactivity": ("METAL DISPLACEMENT", "ਧਾਤ ਦਾ ਵਿਸਥਾਪਨ"),
        "electrochemistry": ("ELECTROLYSIS / COATING", "ਇਲੈਕਟ੍ਰੋਲਾਈਸਿਸ / ਪਰਤ")
    }
    title = titles.get(kind, ("CHEMISTRY MODEL", "ਰਸਾਇਣਕ ਮਾਡਲ"))[1 if pa else 0]
    # SVG is deliberately schematic and qualitative, not a measurement.
    common = {
        "materials": '<rect x="75" y="92" width="90" height="48" rx="8" fill="#b8c8d8"/><rect x="205" y="92" width="90" height="48" rx="8" fill="#f4d06f"/><rect x="335" y="92" width="90" height="48" rx="8" fill="#80c9b0"/><text x="120" y="166" text-anchor="middle" fill="currentColor">METAL</text><text x="250" y="166" text-anchor="middle" fill="currentColor">WOOD</text><text x="380" y="166" text-anchor="middle" fill="currentColor">PLASTIC</text>',
        "solubility": '<path d="M95 70 L115 70 L110 145 Q145 158 180 145 L175 70" fill="#bde7f4" stroke="#397b98" stroke-width="3"/><circle cx="135" cy="120" r="4" fill="#fff"/><circle cx="150" cy="105" r="4" fill="#fff"/><path d="M260 70 L280 70 L275 145 Q310 158 345 145 L340 70" fill="#d8e8f2" stroke="#397b98" stroke-width="3"/><circle cx="290" cy="137" r="5" fill="#9a6b45"/><circle cx="320" cy="137" r="5" fill="#9a6b45"/><circle cx="305" cy="132" r="5" fill="#9a6b45"/>',
        "filtration": '<path d="M110 62 L205 62 L168 110 L168 142" fill="#d5e7f0" stroke="#397b98" stroke-width="3"/><path d="M128 80 L190 80 L168 108 Z" fill="#c4a484"/><path d="M150 140 L150 158 L185 158 L185 140" fill="#c5e7f7" stroke="#397b98" stroke-width="3"/><path d="M280 62 L375 62 L338 110 L338 142" fill="#d5e7f0" stroke="#397b98" stroke-width="3"/><path d="M298 80 L360 80 L338 108 Z" fill="#f4f5f6"/>',
        "changes": '<circle cx="120" cy="112" r="32" fill="#d7eaf5" stroke="#4c8198" stroke-width="3"/><path d="M120 78 V146 M86 112 H154" stroke="#4c8198" stroke-width="2"/><path d="M230 112 H280" stroke="#4c8198" stroke-width="4"/><path d="M268 101 L280 112 L268 123" fill="none" stroke="#4c8198" stroke-width="4"/><path d="M325 130 Q350 95 375 130 Q350 153 325 130" fill="#ef9c4b" stroke="#b86a28" stroke-width="3"/>',
        "transparency": '<circle cx="85" cy="112" r="19" fill="#ffd76a"/><path d="M105 112 H185 M175 102 L185 112 L175 122" stroke="#e4a72e" stroke-width="4" fill="none"/><rect x="195" y="75" width="24" height="74" fill="#8ad8e8" fill-opacity=".55" stroke="#3988a0" stroke-width="2"/><path d="M225 112 H300" stroke="#e4a72e" stroke-width="4"/><rect x="310" y="75" width="24" height="74" fill="#8d96a1" stroke="#58616b" stroke-width="2"/><path d="M340 112 H365" stroke="#e4a72e" stroke-width="4" stroke-dasharray="5 7"/>',
        "indicators": '<path d="M80 75 L100 75 L96 138 Q125 151 154 138 L150 75" fill="#ef8ea8" stroke="#8e5369" stroke-width="3"/><path d="M210 75 L230 75 L226 138 Q255 151 284 138 L280 75" fill="#a6d9f3" stroke="#397b98" stroke-width="3"/><path d="M340 75 L360 75 L356 138 Q385 151 414 138 L410 75" fill="#9bcf9d" stroke="#4c8b55" stroke-width="3"/>',
        "reversible": '<path d="M90 95 H185 M175 85 L185 95 L175 105" stroke="#4c8198" stroke-width="4" fill="none"/><path d="M185 125 H90 M100 115 L90 125 L100 135" stroke="#4c8198" stroke-width="4" fill="none"/><path d="M300 95 H395" stroke="#b45d45" stroke-width="4"/><path d="M385 85 L395 95 L385 105" stroke="#b45d45" stroke-width="4" fill="none"/><path d="M325 115 L365 145 M365 115 L325 145" stroke="#b45d45" stroke-width="4"/>',
        "physical_chemical": '<circle cx="105" cy="105" r="23" fill="#8bc5df"/><circle cx="145" cy="105" r="23" fill="#efbd66"/><path d="M190 105 H240" stroke="#4c8198" stroke-width="4"/><path d="M228 94 L240 105 L228 116" stroke="#4c8198" stroke-width="4" fill="none"/><circle cx="300" cy="105" r="23" fill="#a6d7a8"/><circle cx="340" cy="105" r="23" fill="#a6d7a8"/><circle cx="320" cy="135" r="10" fill="#a6d7a8"/>',
        "rusting": '<rect x="95" y="70" width="18" height="95" rx="6" fill="#a4adb4"/><rect x="95" y="110" width="18" height="55" rx="6" fill="#b9683e"/><path d="M220 78 Q240 58 260 78 Q280 58 300 78" stroke="#65a7d3" stroke-width="4" fill="none"/><path d="M240 95 Q230 110 240 119 Q250 110 240 95" fill="#65a7d3"/><path d="M355 72 Q370 90 355 108 Q340 90 355 72" fill="#65a7d3"/>',
        "separation": '<circle cx="105" cy="110" r="26" fill="#b7dff0"/><circle cx="95" cy="105" r="5" fill="#b18b5e"/><circle cx="115" cy="117" r="5" fill="#b18b5e"/><path d="M155 110 H205" stroke="#4c8198" stroke-width="4"/><path d="M193 99 L205 110 L193 121" stroke="#4c8198" stroke-width="4" fill="none"/><path d="M240 70 L300 70 L280 110 L280 140" fill="#d7edf5" stroke="#4c8198" stroke-width="3"/><path d="M340 70 L400 70 L380 110 L380 140" fill="#d7edf5" stroke="#4c8198" stroke-width="3"/>',
        "combustion": '<path d="M145 140 L185 65 L225 140 Z" fill="#ffd66f" stroke="#b87a28" stroke-width="3"/><path d="M265 140 L305 65 L345 140 Z" fill="#f18b57" stroke="#b95332" stroke-width="3"/><text x="185" y="120" text-anchor="middle" fill="#6b4715">HEAT</text><text x="305" y="120" text-anchor="middle" fill="#6b2416">FUEL</text>',
        "flame": '<path d="M250 55 C205 100 225 115 250 145 C280 115 295 95 250 55Z" fill="#f6a34b" stroke="#bd5d29" stroke-width="3"/><path d="M250 95 C235 116 243 128 250 135 C263 119 263 110 250 95Z" fill="#ffe48b"/><rect x="225" y="145" width="50" height="14" rx="3" fill="#8e8f92"/><path d="M250 145 V134" stroke="#333" stroke-width="4"/>',
        "metals": '<rect x="95" y="82" width="100" height="55" rx="8" fill="#b9c4ce" stroke="#71808e" stroke-width="2"/><path d="M105 95 L180 95 M105 108 L180 108 M105 121 L180 121" stroke="#edf2f5" stroke-width="3"/><rect x="285" y="82" width="100" height="55" rx="8" fill="#7f8b94"/><circle cx="310" cy="100" r="4" fill="#d1d6da"/><circle cx="350" cy="120" r="4" fill="#d1d6da"/>',
        "corrosion": '<rect x="105" y="75" width="18" height="80" rx="5" fill="#a3aeb5"/><rect x="105" y="115" width="18" height="40" rx="5" fill="#b86b42"/><rect x="240" y="75" width="18" height="80" rx="5" fill="#d5c7a1"/><rect x="375" y="75" width="18" height="80" rx="5" fill="#a7b2ba"/><path d="M95 65 H135 M230 65 H270 M365 65 H405" stroke="#4c8198" stroke-width="4"/>',
        "crystals": '<path d="M120 140 L135 100 L150 140 L170 88 L190 140 Z" fill="#8dc9ed" stroke="#397b98" stroke-width="2"/><path d="M270 140 L290 85 L310 140 L330 100 L350 140 Z" fill="#b2def4" stroke="#397b98" stroke-width="2"/><path d="M90 145 H380" stroke="#4c8198" stroke-width="3"/>',
        "mixture_compound": '<circle cx="100" cy="95" r="15" fill="#69a8df"/><circle cx="140" cy="120" r="15" fill="#e5b45d"/><circle cx="180" cy="92" r="15" fill="#69a8df"/><path d="M260 95 L285 120 L310 95" stroke="#4c8198" stroke-width="4" fill="none"/><circle cx="260" cy="95" r="14" fill="#69a8df"/><circle cx="285" cy="120" r="14" fill="#e5b45d"/><circle cx="310" cy="95" r="14" fill="#69a8df"/>',
        "particles": '<circle cx="125" cy="95" r="17" fill="#69a8df"/><circle cx="180" cy="95" r="17" fill="#e5b45d"/><path d="M215 95 H270" stroke="#4c8198" stroke-width="4"/><path d="M258 84 L270 95 L258 106" stroke="#4c8198" stroke-width="4" fill="none"/><circle cx="300" cy="95" r="17" fill="#69a8df"/><circle cx="333" cy="116" r="17" fill="#e5b45d"/><circle cx="366" cy="95" r="17" fill="#69a8df"/>',
        "conservation": '<circle cx="95" cy="95" r="13" fill="#69a8df"/><circle cx="125" cy="120" r="13" fill="#e5b45d"/><circle cx="155" cy="95" r="13" fill="#69a8df"/><path d="M190 105 H245" stroke="#4c8198" stroke-width="4"/><path d="M233 94 L245 105 L233 116" stroke="#4c8198" stroke-width="4" fill="none"/><circle cx="290" cy="95" r="13" fill="#69a8df"/><circle cx="320" cy="120" r="13" fill="#e5b45d"/><circle cx="350" cy="95" r="13" fill="#69a8df"/>',
        "mixture_types": '<path d="M65 70 L80 70 L78 140 Q105 150 132 140 L130 70" fill="#8ac6e8" stroke="#397b98" stroke-width="3"/><path d="M190 70 L205 70 L203 140 Q230 150 257 140 L255 70" fill="#b7dff0" stroke="#397b98" stroke-width="3"/><circle cx="210" cy="128" r="4" fill="#a07852"/><circle cx="235" cy="128" r="4" fill="#a07852"/><path d="M315 70 L330 70 L328 140 Q355 150 382 140 L380 70" fill="#b7dff0" stroke="#397b98" stroke-width="3"/><circle cx="338" cy="100" r="5" fill="#fff"/><circle cx="360" cy="118" r="5" fill="#fff"/>',
        "distillation": '<path d="M85 70 L105 70 L100 120 Q130 150 160 120 L155 70" fill="#b8e0ef" stroke="#397b98" stroke-width="3"/><path d="M120 145 V160" stroke="#397b98" stroke-width="3"/><path d="M155 85 L215 85 L250 65 L285 65" stroke="#397b98" stroke-width="5" fill="none"/><path d="M215 75 L235 95 M235 75 L255 95" stroke="#8bc9e7" stroke-width="5"/><path d="M315 70 L335 70 L330 135 Q355 148 380 135 L375 70" fill="#b8e0ef" stroke="#397b98" stroke-width="3"/>',
        "ph": '<rect x="85" y="75" width="90" height="22" rx="5" fill="#e87f85"/><rect x="175" y="75" width="90" height="22" fill="#f1c75b"/><rect x="265" y="75" width="90" height="22" fill="#82c89a"/><path d="M110 120 L150 120 M200 120 L240 120 M290 120 L330 120" stroke="#4c8198" stroke-width="4"/>',
        "reaction": '<path d="M90 70 L110 70 L106 135 Q130 148 154 135 L150 70" fill="#b8e0ef" stroke="#397b98" stroke-width="3"/><circle cx="125" cy="115" r="6" fill="#fff"/><circle cx="135" cy="95" r="5" fill="#fff"/><path d="M185 105 H240" stroke="#4c8198" stroke-width="4"/><path d="M228 94 L240 105 L228 116" stroke="#4c8198" stroke-width="4" fill="none"/><path d="M285 70 L305 70 L301 135 Q325 148 349 135 L345 70" fill="#a5d4b0" stroke="#4c8b55" stroke-width="3"/><circle cx="313" cy="120" r="5" fill="#f7f2d7"/><circle cx="329" cy="100" r="5" fill="#f7f2d7"/>',
        "neutralisation": '<path d="M85 70 L105 70 L101 135 Q125 148 149 135 L145 70" fill="#e994a5" stroke="#9d596b" stroke-width="3"/><path d="M190 70 L210 70 L206 135 Q230 148 254 135 L250 70" fill="#85c4e4" stroke="#397b98" stroke-width="3"/><path d="M275 105 H310" stroke="#4c8198" stroke-width="4"/><path d="M298 94 L310 105 L298 116" stroke="#4c8198" stroke-width="4" fill="none"/><path d="M335 70 L355 70 L351 135 Q375 148 399 135 L395 70" fill="#b9d9a6" stroke="#608c4e" stroke-width="3"/>',
        "reactivity": '<rect x="95" y="75" width="65" height="70" rx="6" fill="#d5e5ee" stroke="#397b98" stroke-width="2"/><rect x="105" y="100" width="45" height="38" fill="#77b8d8"/><rect x="215" y="75" width="65" height="70" rx="6" fill="#d5e5ee" stroke="#397b98" stroke-width="2"/><rect x="225" y="100" width="45" height="38" fill="#77b8d8"/><path d="M165 110 H205" stroke="#4c8198" stroke-width="4"/><path d="M193 99 L205 110 L193 121" stroke="#4c8198" stroke-width="4" fill="none"/><rect x="325" y="75" width="65" height="70" rx="6" fill="#d5e5ee" stroke="#397b98" stroke-width="2"/><rect x="335" y="100" width="45" height="38" fill="#77b8d8"/><rect x="347" y="108" width="20" height="25" fill="#b7c1c9"/>',
        "electrochemistry": '<path d="M95 70 L115 70 L110 140 Q140 150 170 140 L165 70" fill="#b8e0ef" stroke="#397b98" stroke-width="3"/><rect x="118" y="70" width="9" height="45" fill="#c1c7ce"/><rect x="150" y="70" width="9" height="45" fill="#d7a85d"/><circle cx="130" cy="120" r="4" fill="#d7a85d"/><circle cx="145" cy="128" r="4" fill="#d7a85d"/><path d="M210 105 H260" stroke="#4c8198" stroke-width="4"/><path d="M248 94 L260 105 L248 116" stroke="#4c8198" stroke-width="4" fill="none"/><rect x="310" y="70" width="80" height="70" rx="8" fill="#b9c4ce" stroke="#71808e" stroke-width="2"/><rect x="310" y="70" width="80" height="12" rx="4" fill="#d9a84e"/>'
    }
    drawing = common.get(kind, common["reaction"])
    # Add a selected-sample label and visual cue for each Class 6 dropdown choice.
    if kind == "materials" and choice:
        groups = {
            "Metal spoon": ("METALS / CONDUCTORS", "ધાતਾਂ / ਚਾਲਕ", "#b8c8d8"),
            "Iron nail": ("METALS / CONDUCTORS", "ਧਾਤਾਂ / ਚਾਲਕ", "#b8c8d8"),
            "Wood": ("OPAQUE / RIGID", "ਅਪਾਰਦਰਸ਼ੀ / ਸਖ਼ਤ", "#c89b68"),
            "Plastic ruler": ("LIGHTWEIGHT INSULATORS", "ਹਲਕੇ ਕੁਚਾਲਕ", "#80c9b0"),
            "Rubber band": ("FLEXIBLE INSULATORS", "ਲਚਕੀਲੇ ਕੁਚਾਲਕ", "#80c9b0"),
            "Cotton cloth": ("SOFT / FLEXIBLE", "ਨਰਮ / ਲਚਕੀਲੇ", "#e7c6d7"),
            "Clear glass": ("TRANSPARENT", "ਪਾਰਦਰਸ਼ੀ", "#8ad8e8"),
            "Cardboard": ("OPAQUE", "ਅਪਾਰਦਰਸ਼ੀ", "#c89b68")
        }
        group = groups.get(choice, ("MATERIAL GROUP", "ਪਦਾਰਥ ਸਮੂਹ", "#b8c8d8"))
        drawing += f'<rect x="35" y="45" width="410" height="30" rx="8" fill="{group[2]}" opacity=".9"/><text x="240" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#243746">{choice.upper()} → {group[0]}</text><text x="240" y="185" text-anchor="middle" font-size="12" font-weight="bold" fill="currentColor">{group[1] if pa else group[0]}</text>'
    elif kind == "solubility" and choice:
        soluble = choice in ("Salt in water", "Sugar in water")
        oil = choice == "Oil and water"
        label = "SOLUBLE / ਘੁਲਣਸ਼ੀਲ" if soluble else ("SEPARATE LAYER / ਵੱਖਰੀ ਪਰਤ" if oil else "INSOLUBLE / ਅਘੁਲਣਸ਼ੀਲ")
        color = "#2e9d75" if soluble else ("#d49b2a" if oil else "#bd7950")
        dots = ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="{("#ffffff" if soluble else "#986b47")}"/>' for x, y in ([(122,105),(140,120),(155,99),(131,135),(158,133),(145,89)] if soluble else [(122,137),(140,139),(158,136),(132,127),(150,129),(143,119)]))
        layer = '<rect x="280" y="83" width="70" height="20" rx="3" fill="#efc34f"/>' if oil else ""
        drawing += f'<rect x="55" y="42" width="370" height="32" rx="8" fill="{color}" opacity=".25"/><text x="240" y="63" text-anchor="middle" font-size="13" font-weight="bold" fill="currentColor">{choice.upper()} — {label}</text>{dots}{layer}<text x="240" y="183" text-anchor="middle" font-size="12" font-weight="bold" fill="{color}">{label}</text>'
    elif kind == "changes" and choice:
        physical = choice in ("Ice melting", "Water freezing", "Water evaporating", "Tearing paper", "Dissolving sugar")
        label = "PHYSICAL CHANGE" if physical else "CHEMICAL CHANGE"
        pa_label = "ਭੌਤਿਕ ਤਬਦੀਲੀ" if physical else "ਰਸਾਇਣਕ ਤਬਦੀਲੀ"
        tint = "#4c9bc4" if physical else "#c56c45"
        examples = {
            "Ice melting": "ICE → WATER",
            "Water freezing": "WATER → ICE",
            "Water evaporating": "WATER → VAPOUR",
            "Tearing paper": "PAPER → PIECES",
            "Dissolving sugar": "SUGAR + WATER",
            "Rusting iron": "IRON → RUST",
            "Curdling milk": "MILK → CURDS",
            "Paper burning (diagram only)": "PAPER → ASH + GASES"
        }
        drawing += f'<rect x="55" y="43" width="370" height="32" rx="8" fill="{tint}" opacity=".25"/><text x="240" y="64" text-anchor="middle" font-size="13" font-weight="bold" fill="currentColor">{label}</text><text x="240" y="183" text-anchor="middle" font-size="13" font-weight="bold" fill="currentColor">{examples.get(choice, choice)} — {pa_label if pa else label}</text>'
    elif kind == "transparency" and choice:
        categories = {
            "Clear glass": ("TRANSPARENT", "ਪਾਰਦਰਸ਼ੀ"),
            "Clean water": ("TRANSPARENT", "ਪਾਰਦਰਸ਼ੀ"),
            "Tracing sheet": ("TRANSLUCENT", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ"),
            "Frosted glass": ("TRANSLUCENT", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ"),
            "Thin cloth": ("TRANSLUCENT", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ"),
            "Cardboard": ("OPAQUE", "ਅਪਾਰਦਰਸ਼ੀ"),
            "Wooden board": ("OPAQUE", "ਅਪਾਰਦਰਸ਼ੀ")
        }
        category = categories.get(choice, ("SELECT MATERIAL", "ਪਦਾਰਥ ਚੁਣੋ"))
        tint = "#2e9d75" if category[0] == "TRANSPARENT" else ("#d49b2a" if category[0] == "TRANSLUCENT" else "#bd7950")
        if category[0] == "TRANSPARENT":
            rays = '<path d="M105 112 H370 M358 101 L370 112 L358 123" stroke="#e4a72e" stroke-width="4" fill="none"/>'
        elif category[0] == "TRANSLUCENT":
            rays = '<path d="M105 112 H195 M220 95 L270 112 L220 129 M270 112 L370 90 M270 112 L370 134" stroke="#e4a72e" stroke-width="3" fill="none"/>'
        else:
            rays = '<path d="M105 112 H190 M180 102 L190 112 L180 122" stroke="#e4a72e" stroke-width="4" fill="none"/><path d="M230 80 L270 145 M270 80 L230 145" stroke="#e4a72e" stroke-width="4"/>'
        drawing += f'<rect x="55" y="42" width="370" height="30" rx="8" fill="{tint}" opacity=".25"/><text x="240" y="62" text-anchor="middle" font-size="13" font-weight="bold" fill="currentColor">{choice.upper()} → {category[0]}</text>{rays}<text x="240" y="183" text-anchor="middle" font-size="12" font-weight="bold" fill="{tint}">{category[1] if pa else category[0]}</text>'
    return f"""
    <div style="border:1px solid #9bb6c4;border-radius:16px;padding:10px;margin:10px 0;background:linear-gradient(135deg,rgba(200,230,240,.25),rgba(210,245,225,.25))">
      <div style="font-weight:800;letter-spacing:.04em;text-align:center;margin-bottom:4px">{title}</div>
      <svg viewBox="0 0 480 190" role="img" aria-label="{title}" style="width:100%;height:auto;max-height:260px;color:inherit">
        <path d="M25 165 H455" stroke="#9bb6c4" stroke-width="2"/>
        {drawing}
      </svg>
    </div>
    """

def chemistry_lab():
    if st.button(tr("back"), key="chemistry_back"):
        go("home")
        st.rerun()
    pa = st.session_state.language == "pa"
    st.title("🧪 " + ("ਰਸਾਇਣ ਵਿਗਿਆਨ ਲੈਬ" if pa else "Chemistry Lab"))
    st.caption("PSEB-aligned learning topics · 25 visual experiments" if not pa else "PSEB ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਸਿੱਖਣ ਵਿਸ਼ੇ · 25 ਚਿੱਤਰਕ ਪ੍ਰਯੋਗ")
    classes = [6, 7, 8, 9, 10]
    c1, c2 = st.columns(2)
    with c1:
        cc = st.selectbox("ਜਮਾਤ ਚੁਣੋ" if pa else "Select class", classes, format_func=lambda x: f"{x}ਵੀਂ ਜਮਾਤ" if pa else f"Class {x}", key="chem_class")
    exp_list = CHEMISTRY_EXPERIMENTS[cc]
    with c2:
        ei = st.selectbox("ਪ੍ਰਯੋਗ ਚੁਣੋ" if pa else "Select experiment", list(range(5)), format_func=lambda i: f"{i+1}. {exp_list[i][1 if pa else 0]}", key=f"chem_exp_{cc}")
    en_title, pa_title, en_aim, pa_aim, kind, en_note, pa_note = exp_list[ei]
    title = pa_title if pa else en_title
    aim = pa_aim if pa else en_aim
    note = pa_note if pa else en_note
    st.markdown("---")
    st.header(f"{'ਪ੍ਰਯੋਗ' if pa else 'EXPERIMENT'} {ei+1} · {title}")
    st.markdown(f"**{'ਉਦੇਸ਼' if pa else 'Aim'}:** {aim}")
    st.markdown(f"**{'ਸਮੱਗਰੀ' if pa else 'Materials'}:** " + {
        "materials": "metal spoon, wood, plastic, clear sheet" if not pa else "ਧਾਤ ਦਾ ਚਮਚਾ, ਲੱਕੜ, ਪਲਾਸਟਿਕ, ਪਾਰਦਰਸ਼ੀ ਚਾਦਰ",
        "solubility": "water, salt, sand, transparent cups (virtual)" if not pa else "ਪਾਣੀ, ਨਮਕ, ਰੇਤ, ਪਾਰਦਰਸ਼ੀ ਕੱਪ (ਵਰਚੁਅਲ)",
        "filtration": "sand-water mixture, funnel, filter paper, beaker (virtual)" if not pa else "ਰੇਤ-ਪਾਣੀ ਮਿਸ਼ਰਣ, ਫਨਲ, ਫਿਲਟਰ ਪੇਪਰ, ਬੀਕਰ (ਵਰਚੁਅਲ)",
        "indicators": "indicator strips and labelled sample cups (virtual)" if not pa else "ਸੂਚਕ ਪੱਟੀਆਂ ਅਤੇ ਨਮੂਨਾ ਕੱਪ (ਵਰਚੁਅਲ)",
        "rusting": "iron sample, air and moisture (conceptual)" if not pa else "ਲੋਹੇ ਦਾ ਨਮੂਨਾ, ਹਵਾ ਅਤੇ ਨਮੀ (ਧਾਰਣਾਤਮਕ)",
        "combustion": "fuel, oxygen and heat icons (virtual)" if not pa else "ਇੰਧਨ, ਆਕਸੀਜਨ ਅਤੇ ਤਾਪ ਦੇ ਚਿੰਨ੍ਹ (ਵਰਚੁਅਲ)",
        "electrochemistry": "electrodes, electrolyte and coated object (virtual)" if not pa else "ਇਲੈਕਟ੍ਰੋਡ, ਇਲੈਕਟ੍ਰੋਲਾਈਟ ਅਤੇ ਪਰਤ ਵਾਲੀ ਵਸਤੂ (ਵਰਚੁਅਲ)"
    }.get(kind, "labelled sample vessels and concept diagram" if not pa else "ਨਮੂਨਾ ਭਾਂਡੇ ਅਤੇ ਧਾਰਣਾ ਚਿੱਤਰ"))
    st.markdown(f"**{'ਕਿਵੇਂ ਵੇਖੋ' if pa else 'How to explore'}:** " + ("ਚਿੱਤਰ ਨੂੰ ਧਿਆਨ ਨਾਲ ਵੇਖੋ ਅਤੇ ਨਿਰੀਖਣ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਵਿਕਲਪਾਂ ਨਾਲ ਮਿਲਾਓ। ਅਸਲ ਰਸਾਇਣ ਨਾ ਮਿਲਾਓ।" if pa else "Study the visual, then compare the observation using the controls below. Do not mix real chemicals."))
    options = {
        "materials": [("Metal spoon", "ਧਾਤ ਦਾ ਚਮਚਾ"), ("Iron nail", "ਲੋਹੇ ਦੀ ਕਿੱਲ"), ("Wood", "ਲੱਕੜ"), ("Plastic ruler", "ਪਲਾਸਟਿਕ ਦੀ ਪੈਮਾਈਸ਼ੀ ਪੱਟੀ"), ("Rubber band", "ਰਬੜ ਬੈਂਡ"), ("Cotton cloth", "ਸੂਤੀ ਕੱਪੜਾ"), ("Clear glass", "ਸਾਫ਼ ਕੱਚ"), ("Cardboard", "ਗੱਤਾ")],
        "solubility": [("Salt in water", "ਪਾਣੀ ਵਿੱਚ ਨਮਕ"), ("Sugar in water", "ਪਾਣੀ ਵਿੱਚ ਚੀਨੀ"), ("Sand in water", "ਪਾਣੀ ਵਿੱਚ ਰੇਤ"), ("Chalk powder in water", "ਪਾਣੀ ਵਿੱਚ ਚਾਕ ਦਾ ਪਾਊਡਰ"), ("Oil and water", "ਤੇਲ ਅਤੇ ਪਾਣੀ"), ("Flour in water", "ਪਾਣੀ ਵਿੱਚ ਆਟਾ")],
        "filtration": [("Sand and water", "ਰੇਤ ਅਤੇ ਪਾਣੀ"), ("Salt and water", "ਨਮਕ ਅਤੇ ਪਾਣੀ")],
        "changes": [("Ice melting", "ਬਰਫ਼ ਪਿਘਲਣਾ"), ("Water freezing", "ਪਾਣੀ ਜੰਮਣਾ"), ("Water evaporating", "ਪਾਣੀ ਦਾ ਵਾਸ਼ਪੀਕਰਨ"), ("Tearing paper", "ਕਾਗਜ਼ ਪਾੜਨਾ"), ("Dissolving sugar", "ਚੀਨੀ ਘੋਲਣਾ"), ("Rusting iron", "ਲੋਹੇ ਨੂੰ ਜੰਗ ਲੱਗਣਾ"), ("Curdling milk", "ਦੁੱਧ ਦਾ ਫਟਣਾ"), ("Paper burning (diagram only)", "ਕਾਗਜ਼ ਸੜਨਾ (ਸਿਰਫ਼ ਚਿੱਤਰ)")],
        "transparency": [("Clear glass", "ਸਾਫ਼ ਕੱਚ"), ("Clean water", "ਸਾਫ਼ ਪਾਣੀ"), ("Tracing sheet", "ਟ੍ਰੇਸਿੰਗ ਸ਼ੀਟ"), ("Frosted glass", "ਧੁੰਦਲਾ ਕੱਚ"), ("Thin cloth", "ਪਤਲਾ ਕੱਪੜਾ"), ("Cardboard", "ਗੱਤਾ"), ("Wooden board", "ਲੱਕੜ ਦਾ ਫੱਟਾ")],
        "indicators": [("Lemon juice", "ਨਿੰਬੂ ਦਾ ਰਸ"), ("Water", "ਪਾਣੀ"), ("Soap solution", "ਸਾਬਣ ਦਾ ਘੋਲ")],
        "reversible": [("Melting wax", "ਮੋਮ ਪਿਘਲਣਾ"), ("Burning paper (diagram only)", "ਕਾਗਜ਼ ਸੜਨਾ (ਸਿਰਫ਼ ਚਿੱਤਰ)")],
        "physical_chemical": [("Ice melting", "ਬਰਫ਼ ਪਿਘਲਣਾ"), ("Iron rusting", "ਲੋਹੇ ਨੂੰ ਜੰਗ ਲੱਗਣਾ")],
        "rusting": [("Iron with air and moisture", "ਹਵਾ ਅਤੇ ਨਮੀ ਵਾਲਾ ਲੋਹਾ"), ("Protected iron", "ਸੁਰੱਖਿਆ ਪਰਤ ਵਾਲਾ ਲੋਹਾ")],
        "separation": [("Sand and water", "ਰੇਤ ਅਤੇ ਪਾਣੀ"), ("Iron filings and sand", "ਲੋਹੇ ਦਾ ਬੁਰਾਦਾ ਅਤੇ ਰੇਤ"), ("Salt solution", "ਨਮਕ ਦਾ ਘੋਲ")],
        "combustion": [("All three present", "ਤਿੰਨੇ ਮੌਜੂਦ"), ("Remove oxygen", "ਆਕਸੀਜਨ ਹਟਾਓ"), ("Remove heat", "ਤਾਪ ਹਟਾਓ")],
        "flame": [("Inner dark zone", "ਅੰਦਰਲਾ ਗੂੜ੍ਹਾ ਖੇਤਰ"), ("Luminous yellow zone", "ਪੀਲਾ ਚਮਕਦਾਰ ਖੇਤਰ"), ("Outer zone", "ਬਾਹਰੀ ਖੇਤਰ")],
        "metals": [("Copper", "ਤਾਂਬਾ"), ("Sulphur (conceptual)", "ਗੰਧਕ (ਧਾਰਣਾਤਮਕ)")],
        "corrosion": [("Unprotected iron", "ਬਿਨਾਂ ਸੁਰੱਖਿਆ ਵਾਲਾ ਲੋਹਾ"), ("Painted iron", "ਰੰਗ ਕੀਤਾ ਲੋਹਾ"), ("Oiled iron", "ਤੇਲ ਲੱਗਾ ਲੋਹਾ")],
        "crystals": [("Cooling a suitable solution", "ਢੁਕਵਾਂ ਘੋਲ ਠੰਢਾ ਕਰਨਾ"), ("Evaporating solvent", "ਘੋਲਕ ਦਾ ਵਾਸ਼ਪੀਕਰਨ")],
        "mixture_compound": [("Iron and sulphur mixed", "ਲੋਹਾ ਅਤੇ ਗੰਧਕ ਮਿਲਾਏ"), ("A compound (particle model)", "ਯੋਗਿਕ (ਕਣ ਮਾਡਲ)")],
        "particles": [("Separate atoms", "ਵੱਖਰੇ ਪਰਮਾਣੂ"), ("Combined molecule", "ਜੁੜਿਆ ਅਣੂ")],
        "conservation": [("Before and after: same atoms", "ਪਹਿਲਾਂ ਅਤੇ ਬਾਅਦ: ਉਹੀ ਪਰਮਾਣੂ"), ("Open system loses some gas", "ਖੁੱਲ੍ਹੀ ਪ੍ਰਣਾਲੀ ਵਿੱਚ ਕੁਝ ਗੈਸ ਨਿਕਲਦੀ ਹੈ")],
        "mixture_types": [("Solution", "ਘੋਲ"), ("Suspension", "ਨਿਲੰਬਨ"), ("Colloid", "ਕੋਲਾਇਡ")],
        "distillation": [("Evaporation only", "ਸਿਰਫ਼ ਵਾਸ਼ਪੀਕਰਨ"), ("Distillation and collection", "ਆਸਵਨ ਅਤੇ ਇਕੱਠਾ ਕਰਨਾ")],
        "ph": [("Acidic sample", "ਤੇਜ਼ਾਬੀ ਨਮੂਨਾ"), ("Neutral sample", "ਉਦਾਸੀਨ ਨਮੂਨਾ"), ("Basic sample", "ਖਾਰੀ ਨਮੂਨਾ")],
        "reaction": [("Gas bubbles appear", "ਗੈਸ ਦੇ ਬੁਲਬੁਲੇ ਬਣਦੇ ਹਨ"), ("A new solid appears", "ਨਵਾਂ ਠੋਸ ਬਣਦਾ ਹੈ"), ("Only shape changes", "ਸਿਰਫ਼ ਆਕਾਰ ਬਦਲਦਾ ਹੈ")],
        "neutralisation": [("Acid and base react", "ਤੇਜ਼ਾਬ ਅਤੇ ਖਾਰ ਕਿਰਿਆ ਕਰਦੇ ਹਨ"), ("Acid only", "ਸਿਰਫ਼ ਤੇਜ਼ਾਬ"), ("Base only", "ਸਿਰਫ਼ ਖਾਰ")],
        "reactivity": [("More reactive metal", "ਵੱਧ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ"), ("Less reactive metal", "ਘੱਟ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ")],
        "electrochemistry": [("Metal coating model", "ਧਾਤ ਦੀ ਪਰਤ ਦਾ ਮਾਡਲ"), ("Current switched off", "ਕਰੰਟ ਬੰਦ")
        ]
    }
    selected_options = options.get(kind, [("Observe the model", "ਮਾਡਲ ਦਾ ਨਿਰੀਖਣ ਕਰੋ")])
    labels = [x[1] if pa else x[0] for x in selected_options]
    choice = st.selectbox("ਨਿਰੀਖਣ ਚੁਣੋ" if pa else "Choose an observation", labels, key=f"chem_observe_{cc}_{ei}_{st.session_state.language}")
    idx = labels.index(choice)
    chosen_en = selected_options[idx][0]
    st.markdown(chemistry_visual(kind, pa, chosen_en if cc == 6 else None), unsafe_allow_html=True)
    outcomes = {
        "materials": {"Metal spoon": ("GROUP: metals / conductors — usually lustrous and conduct heat and electricity well.", "ਸਮੂਹ: ਧਾਤਾਂ / ਚਾਲਕ — ਆਮ ਤੌਰ ਤੇ ਚਮਕਦਾਰ ਅਤੇ ਤਾਪ ਤੇ ਬਿਜਲੀ ਦੀਆਂ ਚੰਗੀਆਂ ਚਾਲਕ।"), "Iron nail": ("GROUP: metals / conductors — usually hard and good conductors.", "ਸਮੂਹ: ਧਾਤਾਂ / ਚਾਲਕ — ਆਮ ਤੌਰ ਤੇ ਸਖ਼ਤ ਅਤੇ ਚੰਗੀਆਂ ਚਾਲਕ।"), "Wood": ("GROUP: opaque, rigid materials — usually poor electrical conductors.", "ਸਮੂਹ: ਅਪਾਰਦਰਸ਼ੀ, ਸਖ਼ਤ ਪਦਾਰਥ — ਆਮ ਤੌਰ ਤੇ ਬਿਜਲੀ ਦੇ ਮਾੜੇ ਚਾਲਕ।"), "Plastic ruler": ("GROUP: lightweight insulators — usually do not conduct electricity well.", "ਸਮੂਹ: ਹਲਕੇ ਕੁਚਾਲਕ — ਆਮ ਤੌਰ ਤੇ ਬਿਜਲੀ ਚੰਗੀ ਤਰ੍ਹਾਂ ਨਹੀਂ ਲੰਘਾਉਂਦੇ।"), "Rubber band": ("GROUP: flexible insulators — rubber stretches and is a poor electrical conductor.", "ਸਮੂਹ: ਲਚਕੀਲੇ ਕੁਚਾਲਕ — ਰਬੜ ਖਿੱਚਦੀ ਹੈ ਅਤੇ ਬਿਜਲੀ ਦੀ ਮਾੜੀ ਚਾਲਕ ਹੈ।"), "Cotton cloth": ("GROUP: soft and flexible; usually opaque.", "ਸਮੂਹ: ਨਰਮ ਅਤੇ ਲਚਕੀਲਾ; ਆਮ ਤੌਰ ਤੇ ਅਪਾਰਦਰਸ਼ੀ।"), "Clear glass": ("GROUP: transparent materials — light passes through clearly.", "ਸਮੂਹ: ਪਾਰਦਰਸ਼ੀ ਪਦਾਰਥ — ਰੋਸ਼ਨੀ ਸਾਫ਼ ਲੰਘਦੀ ਹੈ।"), "Cardboard": ("GROUP: opaque materials — blocks most light.", "ਸਮੂਹ: ਅਪਾਰਦਰਸ਼ੀ ਪਦਾਰਥ — ਵੱਧਤਰ ਰੋਸ਼ਨੀ ਰੋਕਦਾ ਹੈ।")},
        "solubility": {"Salt in water": ("SOLUBLE: salt dissolves and forms a uniform solution.", "ਘੁਲਣਸ਼ੀਲ: ਨਮਕ ਘੁਲ ਕੇ ਇਕਸਾਰ ਘੋਲ ਬਣਾਉਂਦਾ ਹੈ।"), "Sugar in water": ("SOLUBLE: sugar dissolves and forms a uniform solution.", "ਘੁਲਣਸ਼ੀਲ: ਚੀਨੀ ਘੁਲ ਕੇ ਇਕਸਾਰ ਘੋਲ ਬਣਾਉਂਦੀ ਹੈ।"), "Sand in water": ("INSOLUBLE: sand remains visible and may settle.", "ਅਘੁਲਣਸ਼ੀਲ: ਰੇਤ ਦਿਖਾਈ ਦਿੰਦੀ ਹੈ ਅਤੇ ਹੇਠਾਂ ਬੈਠ ਸਕਦੀ ਹੈ।"), "Chalk powder in water": ("MOSTLY INSOLUBLE: chalk clouds the water and may settle.", "ਜ਼ਿਆਦਾਤਰ ਅਘੁਲਣਸ਼ੀਲ: ਚਾਕ ਪਾਣੀ ਨੂੰ ਧੁੰਦਲਾ ਕਰਦਾ ਹੈ ਅਤੇ ਬੈਠ ਸਕਦਾ ਹੈ।"), "Oil and water": ("IMMISCIBLE: oil forms a separate layer.", "ਨਾ-ਮਿਸ਼ਰਣਯੋਗ: ਤੇਲ ਵੱਖਰੀ ਪਰਤ ਬਣਾਉਂਦਾ ਹੈ।"), "Flour in water": ("Flour makes a cloudy mixture, not a true solution.", "ਆਟਾ ਅਸਲ ਘੋਲ ਦੀ ਬਜਾਏ ਧੁੰਦਲਾ ਮਿਸ਼ਰਣ ਬਣਾਉਂਦਾ ਹੈ।")},
        "filtration": {"Sand and water": ("Filtration can retain sand while water passes through the filter.", "ਛਾਣਨ ਨਾਲ ਰੇਤ ਫਿਲਟਰ ਵਿੱਚ ਰਹਿ ਸਕਦੀ ਹੈ ਅਤੇ ਪਾਣੀ ਲੰਘ ਜਾਂਦਾ ਹੈ।"), "Salt and water": ("Dissolved salt passes through ordinary filter paper with the water; evaporation is more suitable.", "ਘੁਲਿਆ ਨਮਕ ਆਮ ਫਿਲਟਰ ਪੇਪਰ ਵਿੱਚੋਂ ਪਾਣੀ ਨਾਲ ਲੰਘ ਜਾਂਦਾ ਹੈ; ਵਾਸ਼ਪੀਕਰਨ ਵਧੇਰੇ ਢੁਕਵਾਂ ਹੈ।")},
        "changes": {"Ice melting": ("PHYSICAL CHANGE: ice changes state; no new substance forms.", "ਭੌਤਿਕ ਤਬਦੀਲੀ: ਬਰਫ਼ ਦੀ ਅਵਸਥਾ ਬਦਲਦੀ ਹੈ; ਨਵਾਂ ਪਦਾਰਥ ਨਹੀਂ ਬਣਦਾ।"), "Water freezing": ("PHYSICAL CHANGE: water becomes ice; the substance remains water.", "ਭੌਤਿਕ ਤਬਦੀਲੀ: ਪਾਣੀ ਬਰਫ਼ ਬਣਦਾ ਹੈ; ਪਦਾਰਥ ਪਾਣੀ ਹੀ ਰਹਿੰਦਾ ਹੈ।"), "Water evaporating": ("PHYSICAL CHANGE: liquid water becomes vapour.", "ਭੌਤਿਕ ਤਬਦੀਲੀ: ਤਰਲ ਪਾਣੀ ਵਾਸ਼ਪ ਬਣਦਾ ਹੈ।"), "Tearing paper": ("PHYSICAL CHANGE: only size and shape change.", "ਭੌਤਿਕ ਤਬਦੀਲੀ: ਸਿਰਫ਼ ਆਕਾਰ ਅਤੇ ਸ਼ਕਲ ਬਦਲਦੇ ਹਨ।"), "Dissolving sugar": ("PHYSICAL CHANGE: sugar disperses and can be recovered by evaporation.", "ਭੌਤਿਕ ਤਬਦੀਲੀ: ਚੀਨੀ ਫੈਲਦੀ ਹੈ ਅਤੇ ਵਾਸ਼ਪੀਕਰਨ ਨਾਲ ਮੁੜ ਮਿਲ ਸਕਦੀ ਹੈ।"), "Rusting iron": ("CHEMICAL CHANGE: iron reacts with oxygen and moisture to form rust.", "ਰਸਾਇਣਕ ਤਬਦੀਲੀ: ਲੋਹਾ ਆਕਸੀਜਨ ਅਤੇ ਨਮੀ ਨਾਲ ਕਿਰਿਆ ਕਰਕੇ ਜੰਗ ਬਣਾਉਂਦਾ ਹੈ।"), "Curdling milk": ("CHEMICAL CHANGE: proteins change and a new texture forms.", "ਰਸਾਇਣਕ ਤਬਦੀਲੀ: ਪ੍ਰੋਟੀਨ ਬਦਲਦੇ ਹਨ ਅਤੇ ਨਵੀਂ ਬਣਤਰ ਬਣਦੀ ਹੈ।"), "Paper burning (diagram only)": ("CHEMICAL CHANGE: burning forms ash and gases; diagram only.", "ਰਸਾਇਣਕ ਤਬਦੀਲੀ: ਸੜਨ ਨਾਲ ਰਾਖ ਅਤੇ ਗੈਸਾਂ ਬਣਦੀਆਂ ਹਨ; ਸਿਰਫ਼ ਚਿੱਤਰ।")},
        "transparency": {"Clear glass": ("TRANSPARENT: most light passes through clearly.", "ਪਾਰਦਰਸ਼ੀ: ਵੱਧਤਰ ਰੋਸ਼ਨੀ ਸਾਫ਼ ਲੰਘਦੀ ਹੈ।"), "Clean water": ("TRANSPARENT: light passes through a clean, shallow sample.", "ਪਾਰਦਰਸ਼ੀ: ਸਾਫ਼ ਅਤੇ ਘੱਟ ਡੂੰਘੇ ਨਮੂਨੇ ਵਿੱਚੋਂ ਰੋਸ਼ਨੀ ਲੰਘਦੀ ਹੈ।"), "Tracing sheet": ("TRANSLUCENT: some light passes through but is scattered.", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ: ਕੁਝ ਰੋਸ਼ਨੀ ਲੰਘਦੀ ਹੈ ਪਰ ਖਿਲਰ ਜਾਂਦੀ ਹੈ।"), "Frosted glass": ("TRANSLUCENT: light passes diffusely and details look blurred.", "ਅਰਧ-ਪਾਰਦਰਸ਼ੀ: ਰੋਸ਼ਨੀ ਖਿਲਰ ਕੇ ਲੰਘਦੀ ਹੈ ਅਤੇ ਵੇਰਵੇ ਧੁੰਦਲੇ ਦਿਖਦੇ ਹਨ।"), "Thin cloth": ("OFTEN TRANSLUCENT: some light passes; result depends on thickness and weave.", "ਅਕਸਰ ਅਰਧ-ਪਾਰਦਰਸ਼ੀ: ਕੁਝ ਰੋਸ਼ਨੀ ਲੰਘਦੀ ਹੈ; ਨਤੀਜਾ ਮੋਟਾਈ ਅਤੇ ਬੁਣਾਈ ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।"), "Cardboard": ("OPAQUE: it blocks light.", "ਅਪਾਰਦਰਸ਼ੀ: ਇਹ ਰੋਸ਼ਨੀ ਰੋਕਦਾ ਹੈ।"), "Wooden board": ("OPAQUE: it blocks light.", "ਅਪਾਰਦਰਸ਼ੀ: ਇਹ ਰੋਸ਼ਨੀ ਰੋਕਦਾ ਹੈ।")},
        "indicators": {"Lemon juice": ("Lemon juice is acidic; an appropriate indicator shows an acidic colour.", "ਨਿੰਬੂ ਦਾ ਰਸ ਤੇਜ਼ਾਬੀ ਹੈ; ਢੁਕਵਾਂ ਸੂਚਕ ਤੇਜ਼ਾਬੀ ਰੰਗ ਦਿਖਾਉਂਦਾ ਹੈ।"), "Water": ("Pure water is approximately neutral under ordinary conditions.", "ਸ਼ੁੱਧ ਪਾਣੀ ਆਮ ਹਾਲਤਾਂ ਵਿੱਚ ਲਗਭਗ ਉਦਾਸੀਨ ਹੁੰਦਾ ਹੈ।"), "Soap solution": ("Many soap solutions are basic and change indicators accordingly.", "ਕਈ ਸਾਬਣ ਦੇ ਘੋਲ ਖਾਰੀ ਹੁੰਦੇ ਹਨ ਅਤੇ ਸੂਚਕ ਦਾ ਰੰਗ ਬਦਲਦੇ ਹਨ।")},
        "reversible": {"Melting wax": ("Melting and cooling wax is generally reversible as a physical change.", "ਮੋਮ ਦਾ ਪਿਘਲਣਾ ਅਤੇ ਠੰਢਾ ਹੋ ਕੇ ਜੰਮਣਾ ਆਮ ਤੌਰ ਤੇ ਉਲਟਣਯੋਗ ਭੌਤਿਕ ਤਬਦੀਲੀ ਹੈ।"), "Burning paper (diagram only)": ("Burning paper forms ash and gases; it is not readily reversible.", "ਕਾਗਜ਼ ਸੜਨ ਨਾਲ ਰਾਖ ਅਤੇ ਗੈਸਾਂ ਬਣਦੀਆਂ ਹਨ; ਇਸ ਨੂੰ ਆਸਾਨੀ ਨਾਲ ਉਲਟਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ।")},
        "physical_chemical": {"Ice melting": ("No new substance forms during melting; it is a physical change.", "ਪਿਘਲਣ ਦੌਰਾਨ ਨਵਾਂ ਪਦਾਰਥ ਨਹੀਂ ਬਣਦਾ; ਇਹ ਭੌਤਿਕ ਤਬਦੀਲੀ ਹੈ।"), "Iron rusting": ("Rusting forms new substances and is a chemical change.", "ਜੰਗ ਲੱਗਣ ਨਾਲ ਨਵੇਂ ਪਦਾਰਥ ਬਣਦੇ ਹਨ; ਇਹ ਰਸਾਇਣਕ ਤਬਦੀਲੀ ਹੈ।")},
        "rusting": {"Iron with air and moisture": ("Iron rusts more readily when both oxygen and moisture are available.", "ਆਕਸੀਜਨ ਅਤੇ ਨਮੀ ਦੋਵੇਂ ਹੋਣ ਤੇ ਲੋਹੇ ਨੂੰ ਵਧੇਰੇ ਆਸਾਨੀ ਨਾਲ ਜੰਗ ਲੱਗਦੀ ਹੈ।"), "Protected iron": ("A suitable protective coating limits contact with air and moisture.", "ਢੁਕਵੀਂ ਸੁਰੱਖਿਆ ਪਰਤ ਹਵਾ ਅਤੇ ਨਮੀ ਨਾਲ ਸੰਪਰਕ ਘਟਾਉਂਦੀ ਹੈ।")},
        "separation": {"Sand and water": ("Filtration separates insoluble sand from water.", "ਛਾਣਨ ਨਾਲ ਅਘੁਲਣਸ਼ੀਲ ਰੇਤ ਪਾਣੀ ਤੋਂ ਵੱਖ ਹੁੰਦੀ ਹੈ।"), "Iron filings and sand": ("A magnet can separate iron filings from sand.", "ਚੁੰਬਕ ਲੋਹੇ ਦੇ ਬੁਰਾਦੇ ਨੂੰ ਰੇਤ ਤੋਂ ਵੱਖ ਕਰ ਸਕਦਾ ਹੈ।"), "Salt solution": ("Evaporation can recover dissolved salt, though the water is not collected in this method.", "ਵਾਸ਼ਪੀਕਰਨ ਨਾਲ ਘੁਲਿਆ ਨਮਕ ਮਿਲ ਸਕਦਾ ਹੈ, ਪਰ ਇਸ ਤਰੀਕੇ ਵਿੱਚ ਪਾਣੀ ਇਕੱਠਾ ਨਹੀਂ ਹੁੰਦਾ।")},
        "combustion": {"All three present": ("Fuel, oxygen and sufficient heat together allow combustion.", "ਇੰਧਨ, ਆਕਸੀਜਨ ਅਤੇ ਕਾਫ਼ੀ ਤਾਪ ਇਕੱਠੇ ਹੋਣ ਤੇ ਦਹਿਨ ਹੁੰਦਾ ਹੈ।"), "Remove oxygen": ("Without oxygen, ordinary combustion cannot continue.", "ਆਕਸੀਜਨ ਤੋਂ ਬਿਨਾਂ ਆਮ ਦਹਿਨ ਜਾਰੀ ਨਹੀਂ ਰਹਿ ਸਕਦਾ।"), "Remove heat": ("If the fuel is cooled below its ignition condition, combustion stops.", "ਇੰਧਨ ਨੂੰ ਜਲਣ ਲਈ ਲੋੜੀਂਦੀ ਹਾਲਤ ਤੋਂ ਠੰਢਾ ਕਰਨ ਨਾਲ ਦਹਿਨ ਰੁਕ ਜਾਂਦਾ ਹੈ।")},
        "flame": {"Inner dark zone": ("The inner zone contains unburnt vapours and is relatively cooler.", "ਅੰਦਰਲੇ ਖੇਤਰ ਵਿੱਚ ਨਾ ਸੜੇ ਵਾਸ਼ਪ ਹੁੰਦੇ ਹਨ ਅਤੇ ਇਹ ਤੁਲਨਾਤਮਕ ਤੌਰ ਤੇ ਠੰਢਾ ਹੁੰਦਾ ਹੈ।"), "Luminous yellow zone": ("The yellow luminous zone contains glowing soot particles and incomplete combustion.", "ਪੀਲੇ ਚਮਕਦਾਰ ਖੇਤਰ ਵਿੱਚ ਚਮਕਦੇ ਕਾਰਬਨ ਕਣ ਅਤੇ ਅਧੂਰਾ ਦਹਿਨ ਹੋ ਸਕਦਾ ਹੈ।"), "Outer zone": ("The outer zone generally has more complete combustion and is the hottest region.", "ਬਾਹਰੀ ਖੇਤਰ ਵਿੱਚ ਆਮ ਤੌਰ ਤੇ ਵਧੇਰੇ ਪੂਰਾ ਦਹਿਨ ਹੁੰਦਾ ਹੈ ਅਤੇ ਇਹ ਸਭ ਤੋਂ ਗਰਮ ਖੇਤਰ ਹੁੰਦਾ ਹੈ।")},
        "metals": {"Copper": ("Copper is a metal and conducts heat and electricity well.", "ਤਾਂਬਾ ਧਾਤ ਹੈ ਅਤੇ ਤਾਪ ਤੇ ਬਿਜਲੀ ਦਾ ਚੰਗਾ ਚਾਲਕ ਹੈ।"), "Sulphur (conceptual)": ("Sulphur is a non-metal; it is generally a poor electrical conductor.", "ਗੰਧਕ ਅਧਾਤ ਹੈ; ਇਹ ਆਮ ਤੌਰ ਤੇ ਬਿਜਲੀ ਦੀ ਮਾੜੀ ਚਾਲਕ ਹੈ।")},
        "corrosion": {"Unprotected iron": ("Exposed iron can corrode when air and moisture are present.", "ਖੁੱਲ੍ਹਾ ਲੋਹਾ ਹਵਾ ਅਤੇ ਨਮੀ ਵਿੱਚ ਖਰ ਸਕਦਾ ਹੈ।"), "Painted iron": ("Paint forms a barrier that can reduce contact with air and moisture.", "ਰੰਗ ਦੀ ਪਰਤ ਹਵਾ ਅਤੇ ਨਮੀ ਨਾਲ ਸੰਪਰਕ ਘਟਾ ਸਕਦੀ ਹੈ।"), "Oiled iron": ("Oil can provide a temporary barrier against moisture.", "ਤੇਲ ਨਮੀ ਤੋਂ ਅਸਥਾਈ ਸੁਰੱਖਿਆ ਦੇ ਸਕਦਾ ਹੈ।")},
        "crystals": {"Cooling a suitable solution": ("Cooling may reduce solubility and allow crystals to form.", "ਠੰਢਾ ਕਰਨ ਨਾਲ ਘੁਲਣਸ਼ੀਲਤਾ ਘਟ ਸਕਦੀ ਹੈ ਅਤੇ ਕ੍ਰਿਸਟਲ ਬਣ ਸਕਦੇ ਹਨ।"), "Evaporating solvent": ("As solvent evaporates, dissolved material can crystallise.", "ਘੋਲਕ ਉੱਡਣ ਨਾਲ ਘੁਲਿਆ ਪਦਾਰਥ ਕ੍ਰਿਸਟਲ ਬਣਾ ਸਕਦਾ ਹੈ।")},
        "mixture_compound": {"Iron and sulphur mixed": ("A physical mixture contains the components together without chemically bonding every particle.", "ਭੌਤਿਕ ਮਿਸ਼ਰਣ ਵਿੱਚ ਅੰਸ਼ ਇਕੱਠੇ ਹੁੰਦੇ ਹਨ ਪਰ ਹਰ ਕਣ ਰਸਾਇਣਕ ਤੌਰ ਤੇ ਨਹੀਂ ਜੁੜਦਾ।"), "A compound (particle model)": ("In a compound, elements are chemically combined in a definite proportion.", "ਯੋਗਿਕ ਵਿੱਚ ਤੱਤ ਨਿਰਧਾਰਤ ਅਨੁਪਾਤ ਵਿੱਚ ਰਸਾਇਣਕ ਤੌਰ ਤੇ ਜੁੜੇ ਹੁੰਦੇ ਹਨ।")},
        "particles": {"Separate atoms": ("Separate circles represent individual atoms in this simplified model.", "ਵੱਖਰੇ ਗੋਲ ਇਸ ਸਰਲ ਮਾਡਲ ਵਿੱਚ ਅਲੱਗ ਪਰਮਾਣੂ ਦਰਸਾਉਂਦੇ ਹਨ।"), "Combined molecule": ("A group of bonded atoms represents a molecule.", "ਜੁੜੇ ਪਰਮਾਣੂਆਂ ਦਾ ਸਮੂਹ ਅਣੂ ਦਰਸਾਉਂਦਾ ਹੈ।")},
        "conservation": {"Before and after: same atoms": ("The same kinds and numbers of atoms are rearranged in a balanced reaction model.", "ਸੰਤੁਲਿਤ ਕਿਰਿਆ ਮਾਡਲ ਵਿੱਚ ਉਹੀ ਕਿਸਮਾਂ ਅਤੇ ਗਿਣਤੀ ਦੇ ਪਰਮਾਣੂ ਮੁੜ-ਵਿਉਂਤ ਹੁੰਦੇ ਹਨ।"), "Open system loses some gas": ("Gas escaping an open vessel can make the measured mass appear to decrease; the gas still has mass.", "ਖੁੱਲ੍ਹੇ ਭਾਂਡੇ ਵਿੱਚੋਂ ਗੈਸ ਨਿਕਲਣ ਨਾਲ ਮਾਪਿਆ ਪੁੰਜ ਘੱਟ ਲੱਗ ਸਕਦਾ ਹੈ; ਗੈਸ ਦਾ ਵੀ ਪੁੰਜ ਹੁੰਦਾ ਹੈ।")},
        "mixture_types": {"Solution": ("A solution is uniform at the particle scale.", "ਘੋਲ ਕਣ ਪੱਧਰ ਤੇ ਇਕਸਾਰ ਹੁੰਦਾ ਹੈ।"), "Suspension": ("Suspended particles may settle if the mixture is left undisturbed.", "ਨਿਲੰਬਿਤ ਕਣ ਮਿਸ਼ਰਣ ਅਡੋਲ ਛੱਡਣ ਤੇ ਹੇਠਾਂ ਬੈਠ ਸਕਦੇ ਹਨ।"), "Colloid": ("Colloidal particles remain dispersed and scatter light in many cases.", "ਕੋਲਾਇਡੀ ਕਣ ਫੈਲੇ ਰਹਿੰਦੇ ਹਨ ਅਤੇ ਕਈ ਹਾਲਤਾਂ ਵਿੱਚ ਰੋਸ਼ਨੀ ਖਿਲਾਰਦੇ ਹਨ।")},
        "distillation": {"Evaporation only": ("Evaporation leaves non-volatile dissolved solids behind.", "ਵਾਸ਼ਪੀਕਰਨ ਨਾਲ ਨਾ ਉੱਡਣ ਵਾਲੇ ਘੁਲਣਸ਼ੀਲ ਠੋਸ ਪਿੱਛੇ ਰਹਿ ਜਾਂਦੇ ਹਨ।"), "Distillation and collection": ("Distillation cools vapour to collect the condensed liquid.", "ਆਸਵਨ ਵਿੱਚ ਭਾਫ਼ ਠੰਢੀ ਕਰਕੇ ਸੰਘਣੇ ਤਰਲ ਨੂੰ ਇਕੱਠਾ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।")},
        "ph": {"Acidic sample": ("An acidic solution changes a suitable indicator to its acidic colour; pH is below neutral.", "ਤੇਜ਼ਾਬੀ ਘੋਲ ਢੁਕਵੇਂ ਸੂਚਕ ਨੂੰ ਤੇਜ਼ਾਬੀ ਰੰਗ ਵਿੱਚ ਬਦਲਦਾ ਹੈ; pH ਉਦਾਸੀਨ ਤੋਂ ਘੱਟ ਹੁੰਦਾ ਹੈ।"), "Neutral sample": ("A neutral sample shows the neutral indicator colour; at room conditions, pure water is near pH 7.", "ਉਦਾਸੀਨ ਨਮੂਨਾ ਉਦਾਸੀਨ ਰੰਗ ਦਿਖਾਉਂਦਾ ਹੈ; ਕਮਰੇ ਦੀ ਹਾਲਤ ਵਿੱਚ ਸ਼ੁੱਧ ਪਾਣੀ ਦਾ pH ਲਗਭਗ 7 ਹੁੰਦਾ ਹੈ।"), "Basic sample": ("A basic solution changes a suitable indicator to its basic colour; pH is above neutral.", "ਖਾਰੀ ਘੋਲ ਢੁਕਵੇਂ ਸੂਚਕ ਨੂੰ ਖਾਰੀ ਰੰਗ ਵਿੱਚ ਬਦਲਦਾ ਹੈ; pH ਉਦਾਸੀਨ ਤੋਂ ਵੱਧ ਹੁੰਦਾ ਹੈ।")},
        "reaction": {"Gas bubbles appear": ("Gas formation can be evidence of a chemical reaction.", "ਗੈਸ ਬਣਨਾ ਰਸਾਇਣਕ ਕਿਰਿਆ ਦਾ ਸਬੂਤ ਹੋ ਸਕਦਾ ਹੈ।"), "A new solid appears": ("A newly formed insoluble solid is called a precipitate.", "ਨਵਾਂ ਬਣਿਆ ਅਘੁਲਣਸ਼ੀਲ ਠੋਸ ਅਵਖੇਪ ਕਹਾਉਂਦਾ ਹੈ।"), "Only shape changes": ("A change in shape alone is usually a physical change.", "ਸਿਰਫ਼ ਆਕਾਰ ਬਦਲਣਾ ਆਮ ਤੌਰ ਤੇ ਭੌਤਿਕ ਤਬਦੀਲੀ ਹੈ।")},
        "neutralisation": {"Acid and base react": ("Neutralisation can form salt and water; the exact outcome depends on the substances used.", "ਉਦਾਸੀਨੀਕਰਨ ਨਾਲ ਲੂਣ ਅਤੇ ਪਾਣੀ ਬਣ ਸਕਦੇ ਹਨ; ਅਸਲ ਨਤੀਜਾ ਵਰਤੇ ਪਦਾਰਥਾਂ ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।"), "Acid only": ("An acid alone does not demonstrate neutralisation; a suitable base is also needed.", "ਸਿਰਫ਼ ਤੇਜ਼ਾਬ ਨਾਲ ਉਦਾਸੀਨੀਕਰਨ ਨਹੀਂ ਦਿਖਾਇਆ ਜਾਂਦਾ; ਢੁਕਵੀਂ ਖਾਰ ਵੀ ਲੋੜੀਂਦੀ ਹੈ।"), "Base only": ("A base alone does not demonstrate neutralisation; a suitable acid is also needed.", "ਸਿਰਫ਼ ਖਾਰ ਨਾਲ ਉਦਾਸੀਨੀਕਰਨ ਨਹੀਂ ਦਿਖਾਇਆ ਜਾਂਦਾ; ਢੁਕਵਾਂ ਤੇਜ਼ਾਬ ਵੀ ਲੋੜੀਂਦਾ ਹੈ।")},
        "reactivity": {"More reactive metal": ("A more reactive metal can displace a less reactive metal from a suitable salt solution.", "ਵੱਧ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ ਢੁਕਵੇਂ ਲੂਣ ਦੇ ਘੋਲ ਵਿੱਚੋਂ ਘੱਟ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ ਨੂੰ ਹਟਾ ਸਕਦੀ ਹੈ।"), "Less reactive metal": ("A less reactive metal cannot normally displace a more reactive metal from its salt solution.", "ਘੱਟ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ ਆਮ ਤੌਰ ਤੇ ਵੱਧ ਕਿਰਿਆਸ਼ੀਲ ਧਾਤ ਨੂੰ ਉਸ ਦੇ ਲੂਣ ਦੇ ਘੋਲ ਵਿੱਚੋਂ ਨਹੀਂ ਹਟਾ ਸਕਦੀ।")},
        "electrochemistry": {"Metal coating model": ("In electroplating, metal ions can deposit as a thin layer on the object connected as the cathode.", "ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਵਿੱਚ ਕੈਥੋਡ ਨਾਲ ਜੁੜੀ ਵਸਤੂ ਉੱਤੇ ਧਾਤ ਦੇ ਆਇਨ ਪਤਲੀ ਪਰਤ ਵਜੋਂ ਜਮ ਸਕਦੇ ਹਨ।"), "Current switched off": ("Without current, electroplating deposition stops in this simple model.", "ਕਰੰਟ ਬੰਦ ਹੋਣ ਤੇ ਇਸ ਸਰਲ ਮਾਡਲ ਵਿੱਚ ਇਲੈਕਟ੍ਰੋਪਲੇਟਿੰਗ ਰੁਕ ਜਾਂਦੀ ਹੈ।")}
    }
    pair = outcomes.get(kind, {}).get(chosen_en)
    if pair:
        result = pair[1] if pa else pair[0]
    else:
        result = note
    st.markdown("### " + ("ਨਿਰੀਖਣ" if pa else "Observation"))
    st.success(result)
    st.markdown("**" + ("ਵਿਗਿਆਨਕ ਵਿਆਖਿਆ" if pa else "Scientific explanation") + ":** " + note)
    with st.expander("🧠 " + ("ਸੋਚੋ ਅਤੇ ਜਵਾਬ ਦਿਓ" if pa else "Think and answer")):
        st.write("ਇਹ ਨਿਰੀਖਣ ਕਿਹੜੇ ਵਿਗਿਆਨਕ ਸਿਧਾਂਤ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ?" if pa else "Which scientific principle does this observation demonstrate?")
        st.text_input("ਤੁਹਾਡਾ ਜਵਾਬ" if pa else "Your explanation", key=f"chem_reflect_{cc}_{ei}_{st.session_state.language}")
    st.caption("Virtual educational model only. Follow teacher supervision and school laboratory safety rules for any real practical work." if not pa else "ਇਹ ਸਿਰਫ਼ ਵਰਚੁਅਲ ਸਿੱਖਣ ਮਾਡਲ ਹੈ। ਅਸਲ ਪ੍ਰਯੋਗ ਅਧਿਆਪਕ ਦੀ ਦੇਖ-ਰੇਖ ਅਤੇ ਸਕੂਲ ਦੀ ਲੈਬ ਸੁਰੱਖਿਆ ਦੇ ਨਿਯਮਾਂ ਅਨੁਸਾਰ ਹੀ ਕਰੋ।")

def planned_lab(page):
    if st.button(tr("back")):
        go("home")
        st.rerun()
    names = {"chemistry":"chemistry", "physics":"physics", "biology":"biology", "mentor":"mentor"}
    key = names[page]
    st.title({"chemistry":"🧪 ", "physics":"🚀 ", "biology":"🧬 ", "mentor":"🤖 "}[page] + tr(key))
    st.info(tr("planned"))
    st.markdown("### " + tr("planned_items"))
    topics = {
      "chemistry": ["Acid–base indicators / ਤੇਜ਼ਾਬ-ਖਾਰ ਸੂਚਕ", "pH scale / pH ਪੈਮਾਨਾ", "Separation of mixtures / ਮਿਸ਼ਰਣਾਂ ਨੂੰ ਵੱਖ ਕਰਨਾ"],
      "physics": ["Motion and speed / ਗਤੀ ਅਤੇ ਚਾਲ", "Reflection and refraction / ਪਰਾਵਰਤਨ ਅਤੇ ਅਪਵਰਤਨ", "Energy transformations / ਊਰਜਾ ਦੇ ਰੂਪਾਂਤਰ"],
      "biology": ["Cell explorer / ਕੋਸ਼ਿਕਾ ਦੀ ਖੋਜ", "Human body systems / ਮਨੁੱਖੀ ਸਰੀਰ ਦੀਆਂ ਪ੍ਰਣਾਲੀਆਂ", "Photosynthesis / ਪ੍ਰਕਾਸ਼ ਸੰਸ਼ਲੇਸ਼ਣ"],
      "mentor": ["Science questions / ਵਿਗਿਆਨਕ ਸਵਾਲ", "Experiment explanations / ਪ੍ਰਯੋਗਾਂ ਦੀ ਵਿਆਖਿਆ", "Punjabi and English support / ਪੰਜਾਬੀ ਅਤੇ ਅੰਗਰੇਜ਼ੀ ਸਹਾਇਤਾ"]
    }
    for item in topics[page]:
        st.markdown("- " + item)
    st.caption(tr("safe"))

if st.session_state.page == "home":
    show_header()
    st.title(tr("choose"))
    st.write(tr("choose_desc"))
    cards = [
      ("electricity","⚡","electricity_desc","electricity"),
      ("chemistry","🧪","chemistry_desc","chemistry"),
      ("physics","🚀","physics_desc","physics"),
      ("biology","🧬","biology_desc","biology"),
      ("mentor","🤖","mentor_desc","mentor")
    ]
    cols = st.columns(2)
    for i, (page, icon, desc_key, title_key) in enumerate(cards):
        with cols[i % 2]:
            st.markdown(f'<div class="lab-card"><div style="font-size:1.8rem">{icon}</div><h3>{tr(title_key)}</h3><p>{tr(desc_key)}</p></div>', unsafe_allow_html=True)
            st.button(tr("open") + " → " + tr(title_key), key=f"open_{page}", use_container_width=True, on_click=go, args=(page,))
    st.caption(tr("home_note"))
elif st.session_state.page == "electricity":
    show_header()
    electricity_lab()
elif st.session_state.page == "physics":
    show_header()
    physics_lab()
elif st.session_state.page == "chemistry":
    show_header()
    chemistry_lab()
elif st.session_state.page in ("biology","mentor"):
    show_header()
    planned_lab(st.session_state.page)
else:
    st.session_state.page = "home"
    st.rerun()
