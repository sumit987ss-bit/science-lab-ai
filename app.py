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
("Electrical Power and Energy","ਬਿਜਲੀ ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ","Calculate power and energy from voltage, current and time.","ਵੋਲਟੇਜ, ਕਰੰਟ ਅਤੇ ਸਮੇਂ ਤੋਂ ਸ਼ਕਤੀ ਅਤੇ ਊਰਜਾ ਦੀ ਗਣਨਾ ਕਰੋ।","power","Power is the rate of energy transfer; for a DC load P = V × I.","ਸ਼ਕਤੀ ਊਰਜਾ ਦੇ ਤਬਾਦਲੇ ਦੀ ਦਰ ਹੈ; DC ਲੋਡ ਲਈ P = V × I।"),
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
    left, right = st.columns([1, 1.2], gap="large")
    with left:
        st.markdown("### " + tr("controls"))
        # Keep controls aligned with the class level: Classes 6–9 use qualitative models.
        # Numerical voltage, resistance, coil-turn and current controls are shown only
        # for relevant Class 10 quantitative experiments.
        quantitative_class10 = selected_class == 10 and kind in ("ohms", "series_parallel", "power", "heating")
        voltage = st.slider(tr("voltage"), 0, 24, 12, 1, key=f"v_{selected_class}_{exp_index}") if quantitative_class10 else 12
        resistance = st.slider(tr("resistance"), 1, 100, 6, 1, key=f"r_{selected_class}_{exp_index}") if quantitative_class10 else 6
        closed = st.checkbox(tr("switch"), value=True, key=f"sw_{selected_class}_{exp_index}") if kind in ("circuit", "fuse", "motor", "electromagnet", "magnetic_field", "ohms", "series_parallel", "power", "heating") else True
        turns = 10
        current_control = 1.0
        material = None
        liquid = None
        if kind == "conductors":
            material_options = {
                "en": ["Copper", "Aluminium", "Iron", "Rubber", "Plastic", "Wood"],
                "pa": ["ਤਾਂਬਾ", "ਐਲੂਮੀਨੀਅਮ", "ਲੋਹਾ", "ਰਬੜ", "ਪਲਾਸਟਿਕ", "ਲੱਕੜ"]
            }
            material = st.selectbox(tr("material"), material_options[st.session_state.language], key=f"mat_{selected_class}_{exp_index}")
        if kind == "liquids":
            liquids = ["water", "salt", "sugar", "lemon"]
            liquid = st.selectbox(tr("liquid"), liquids, format_func=lambda x: tr(x), key=f"liq_{selected_class}_{exp_index}")
        if kind == "ohms":
            prediction = st.selectbox(tr("predict_q"), [tr("select_prediction"), tr("double"), tr("same"), tr("half")], key=f"pred_{selected_class}_{exp_index}")
            if prediction != tr("select_prediction"):
                st.success(tr("correct") if prediction == tr("half") else tr("incorrect"))
    current = voltage / resistance if closed else 0.0
    power = voltage * current if closed else 0.0
    with right:
        st.markdown("### " + tr("result"))
        if kind == "circuit":
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
            st.metric(tr("conductivity"), tr("conductor") if is_conductor else tr("insulator"))
            st.write("💡 " + note)
        elif kind == "electromagnet":
            strength = turns * current_control
            st.metric(tr("magnetic"), f"{strength:.1f} relative units")
            st.write(f"{tr('turns')}: {turns} · {tr('current_control')}: {current_control:.1f} A")
        elif kind == "magnetic_field":
            st.metric(tr("magnetic"), f"{current_control*10:.1f} illustrative units")
            st.write(note)
        elif kind == "liquids":
            score = {"water": 0.05, "salt": 1.0, "sugar": 0.08, "lemon": 0.75}[liquid]
            st.metric(tr("conductivity"), f"{score:.2f} relative units")
            st.caption("Qualitative teaching model; real conductivity varies with concentration and composition.")
        elif kind == "electrolysis":
            st.metric(tr("amount"), f"{voltage*current_control:.1f} illustrative units")
            st.write(note)
        elif kind == "electroplating":
            st.metric(tr("amount"), f"{voltage*current_control*0.5:.1f} illustrative coating units")
            st.write(note)
        elif kind == "cell":
            st.metric(tr("voltage"), f"{voltage} V")
            st.write(note)
        elif kind == "charge":
            st.metric(tr("magnetic"), f"{voltage*current_control:.1f} illustrative interaction units")
            st.write(note)
        elif kind == "fuse":
            st.metric(tr("current"), f"{current:.2f} A")
            st.info("Illustrative fuse model: a protection device opens a circuit when current exceeds its specified rating. No real fuse is tested.")
        elif kind == "motor":
            st.metric("Motor model", "Rotating" if closed and voltage > 0 else "Stopped")
            st.write(note)
        elif kind == "magnet":
            st.write("Iron and steel are usually attracted by a magnet; wood, plastic and rubber are not.")
            st.write(note)
        else:
            st.write(note)
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
