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
    magnetic_experiment = kind == "magnet" and selected_class == 6 and exp_index == 4
    symbol_experiment = selected_class == 7 and exp_index == 0
    heating_experiment = selected_class == 7 and exp_index == 1 and kind == "heating"
    wide_experiment = magnetic_experiment or symbol_experiment or heating_experiment
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
        closed = st.checkbox(tr("switch"), value=True, key=f"sw_{selected_class}_{exp_index}") if (kind in ("circuit", "fuse", "motor", "electromagnet", "magnetic_field", "ohms", "series_parallel", "power", "heating") and not (selected_class == 6 and exp_index == 1)) else True
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
