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
        quantitative_class10 = selected_class == 10 and kind in ("ohms", "series_parallel", "power", "heating")
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
        if kind == "magnet" and selected_class == 6 and exp_index == 4:
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
            if closed:
                st.success(qualitative_result)
            else:
                st.info(qualitative_result)
            st.write("💡 " + note)
            st.caption("Qualitative visual only — no numerical values, units, calculated readings or graph." if not is_pa_ohms else "ਸਿਰਫ਼ ਗੁਣਾਤਮਕ ਦ੍ਰਿਸ਼ — ਕੋਈ ਸੰਖਿਆਤਮਕ ਮੁੱਲ, ਇਕਾਈਆਂ, ਗਣਨਾ ਜਾਂ ਗ੍ਰਾਫ ਨਹੀਂ।")
        elif kind == "series_parallel" and selected_class == 9 and exp_index == 2:
            # Class 9 Experiment 3: independent switch controls for series and parallel circuits.
            is_pa_series = st.session_state.language != "en"
            series_switch = st.checkbox("ਲੜੀਵਾਰ ਸਰਕਟ ਦਾ ਸਵਿੱਚ" if is_pa_series else "Series circuit main switch", value=True, key="c9_exp3_series_switch")
            st.markdown("**" + ("ਸਮਾਂਤਰ ਸ਼ਾਖਾਂ ਦੇ ਸਵਿੱਚ" if is_pa_series else "Parallel branch switches") + "**")
            pcol1, pcol2 = st.columns(2)
            with pcol1:
                parallel_switch_1 = st.checkbox("ਸ਼ਾਖਾ 1" if is_pa_series else "Branch 1", value=True, key="c9_exp3_parallel_switch_1")
            with pcol2:
                parallel_switch_2 = st.checkbox("ਸ਼ਾਖਾ 2" if is_pa_series else "Branch 2", value=True, key="c9_exp3_parallel_switch_2")
            series_title = "ਲੜੀਵਾਰ ਜੋੜ" if is_pa_series else "SERIES CONNECTION"
            parallel_title = "ਸਮਾਂਤਰ ਜੋੜ" if is_pa_series else "PARALLEL CONNECTION"
            series_note = ("ਇੱਕੋ ਸਵਿੱਚ ਪੂਰੇ ਲੜੀਵਾਰ ਸਰਕਟ ਨੂੰ ਚਾਲੂ ਜਾਂ ਬੰਦ ਕਰਦਾ ਹੈ।" if is_pa_series else "One switch controls the entire series circuit; opening it turns both bulbs off.")
            parallel_note = ("ਹਰ ਸ਼ਾਖਾ ਦਾ ਆਪਣਾ ਸਵਿੱਚ ਹੈ; ਇੱਕ ਸ਼ਾਖਾ ਬੰਦ ਹੋਣ ਤੇ ਦੂਜੀ ਚੱਲ ਸਕਦੀ ਹੈ।" if is_pa_series else "Each branch has its own switch; one bulb can stay on when the other branch is off.")
            series_wire = "#16a34a" if series_switch else "#94a3b8"
            series_bulb = "#fde047" if series_switch else "#e2e8f0"
            series_glow = "filter:drop-shadow(0 0 8px #facc15);" if series_switch else ""
            p1_wire = "#16a34a" if parallel_switch_1 else "#94a3b8"
            p2_wire = "#16a34a" if parallel_switch_2 else "#94a3b8"
            p1_bulb = "#fde047" if parallel_switch_1 else "#e2e8f0"
            p2_bulb = "#fde047" if parallel_switch_2 else "#e2e8f0"
            p1_glow = "filter:drop-shadow(0 0 8px #facc15);" if parallel_switch_1 else ""
            p2_glow = "filter:drop-shadow(0 0 8px #facc15);" if parallel_switch_2 else ""
            series_status = ("ਸਵਿੱਚ ਬੰਦ — ਦੋਵੇਂ ਬਲਬ ਬੰਦ" if is_pa_series else "Main switch open — both bulbs off") if not series_switch else ("ਸਰਕਟ ਪੂਰਾ — ਦੋਵੇਂ ਬਲਬ ਚਾਲੂ" if is_pa_series else "Circuit complete — both bulbs on")
            if is_pa_series:
                parallel_status = f"ਸ਼ਾਖਾ 1: {'ਚਾਲੂ' if parallel_switch_1 else 'ਬੰਦ'} | ਸ਼ਾਖਾ 2: {'ਚਾਲੂ' if parallel_switch_2 else 'ਬੰਦ'}"
            else:
                parallel_status = f"Branch 1: {'ON' if parallel_switch_1 else 'OFF'} | Branch 2: {'ON' if parallel_switch_2 else 'OFF'}"
            series_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:14px;padding:8px;background:rgba(128,128,128,.035)">
            <svg viewBox="0 0 340 220" width="100%" role="img" aria-label="Series circuit with one main switch controlling two bulbs">
              <g fill="none" stroke="{series_wire}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
                <path d="M52 48 H95 M139 48 H201 M245 48 H288 V174 H210 M155 174 H52 V118 M52 48 V82"/>
                <path d="M155 174 L174 162 L193 174" stroke="#64748b" stroke-width="3"/>
              </g>
              <g stroke="#334155" stroke-width="3"><line x1="34" y1="82" x2="70" y2="82"/><line x1="41" y1="101" x2="63" y2="101"/></g>
              <circle cx="117" cy="48" r="22" fill="{series_bulb}" stroke="#475569" stroke-width="3" style="{series_glow}"/><path d="M107 38 l20 20 M127 38 l-20 20" stroke="#475569" stroke-width="3"/>
              <circle cx="223" cy="48" r="22" fill="{series_bulb}" stroke="#475569" stroke-width="3" style="{series_glow}"/><path d="M213 38 l20 20 M233 38 l-20 20" stroke="#475569" stroke-width="3"/>
              <text x="52" y="137" fill="currentColor" font-size="11" text-anchor="middle">{"ਸੈੱਲ" if is_pa_series else "CELL"}</text>
              <text x="174" y="151" fill="currentColor" font-size="10" text-anchor="middle">{"ਮੁੱਖ ਸਵਿੱਚ" if is_pa_series else "MAIN SWITCH"}</text>
              <text x="170" y="202" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">{("ਇੱਕ ਸਵਿੱਚ — ਦੋਵੇਂ ਬਲਬ" if is_pa_series else "ONE SWITCH CONTROLS BOTH")}</text>
            </svg></div>"""
            parallel_svg = f"""<div style="border:1px solid rgba(120,140,160,.35);border-radius:14px;padding:8px;background:rgba(128,128,128,.035)">
            <svg viewBox="0 0 340 220" width="100%" role="img" aria-label="Parallel circuit with independent switch in each bulb branch">
              <g fill="none" stroke="#16a34a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">
                <path d="M52 48 H288 V174 H52 V118 M52 48 V82"/>
              </g>
              <path d="M105 48 V67 M105 85 V91 M105 131 V174" fill="none" stroke="{p1_wire}" stroke-width="4" stroke-linecap="round"/>
              <path d="M235 48 V67 M235 85 V91 M235 131 V174" fill="none" stroke="{p2_wire}" stroke-width="4" stroke-linecap="round"/>
              <g stroke="#64748b" stroke-width="3" stroke-linecap="round"><circle cx="105" cy="68" r="2" fill="#64748b"/><circle cx="105" cy="84" r="2" fill="#64748b"/><line x1="105" y1="68" x2="105" y2="{84 if parallel_switch_1 else 58}"/><circle cx="235" cy="68" r="2" fill="#64748b"/><circle cx="235" cy="84" r="2" fill="#64748b"/><line x1="235" y1="68" x2="235" y2="{84 if parallel_switch_2 else 58}"/></g>
              <circle cx="105" cy="111" r="20" fill="{p1_bulb}" stroke="#475569" stroke-width="3" style="{p1_glow}"/><path d="M96 102 l18 18 M114 102 l-18 18" stroke="#475569" stroke-width="3"/>
              <circle cx="235" cy="111" r="20" fill="{p2_bulb}" stroke="#475569" stroke-width="3" style="{p2_glow}"/><path d="M226 102 l18 18 M244 102 l-18 18" stroke="#475569" stroke-width="3"/>
              <g stroke="#334155" stroke-width="3"><line x1="34" y1="82" x2="70" y2="82"/><line x1="41" y1="101" x2="63" y2="101"/></g>
              <text x="52" y="137" fill="currentColor" font-size="11" text-anchor="middle">{"ਸੈੱਲ" if is_pa_series else "CELL"}</text>
              <text x="105" y="151" fill="currentColor" font-size="10" text-anchor="middle">{"ਸਵਿੱਚ 1" if is_pa_series else "SWITCH 1"}</text><text x="235" y="151" fill="currentColor" font-size="10" text-anchor="middle">{"ਸਵਿੱਚ 2" if is_pa_series else "SWITCH 2"}</text>
              <text x="170" y="202" fill="currentColor" font-size="12" font-weight="700" text-anchor="middle">{("ਹਰ ਸ਼ਾਖਾ ਦਾ ਵੱਖਰਾ ਸਵਿੱਚ" if is_pa_series else "INDEPENDENT BRANCH SWITCHES")}</text>
            </svg></div>"""
            st.markdown("#### " + ("ਲੜੀਵਾਰ ਅਤੇ ਸਮਾਂਤਰ ਸਰਕਟਾਂ ਦੀ ਤੁਲਨਾ" if is_pa_series else "Compare Series and Parallel Circuits"))
            col_series, col_parallel = st.columns(2)
            with col_series:
                st.markdown("**" + series_title + "**")
                st.markdown(series_svg, unsafe_allow_html=True)
                st.caption(series_note)
                st.info(series_status)
            with col_parallel:
                st.markdown("**" + parallel_title + "**")
                st.markdown(parallel_svg, unsafe_allow_html=True)
                st.caption(parallel_note)
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
                    '<g fill="#fef3c7" stroke="#b45309" stroke-width="1.5">'
                    '<path d="M275 179 l18 -7 8 16 -17 6 Z"/><path d="M308 184 l17 -4 5 15 -19 4 Z"/></g>'
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
elif st.session_state.page in ("chemistry","physics","biology","mentor"):
    show_header()
    planned_lab(st.session_state.page)
else:
    st.session_state.page = "home"
    st.rerun()
