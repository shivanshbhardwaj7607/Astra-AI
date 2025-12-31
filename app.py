import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ASTRA-AI: Pragyan Public School",
    page_icon="🎓",
    layout="centered"
)

# --- 2. LOVELY 3D GLASSMORPHISM UI ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #000428, #004e92);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stChatMessage {
        background: rgba(255, 255, 255, 0.07);
        border-radius: 20px;
        border: 1px solid rgba(0, 210, 255, 0.3);
        margin-bottom: 15px;
    }
    h1 { text-shadow: 2px 2px 4px #000000; color: #00d2ff !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE COMPLETE SCHOOL BRAIN (DATABASE) ---
school_data = {
    "name": "Pragyan Public School, Jewar",
    "location": "Jewar, Gautam Budh Nagar, Uttar Pradesh - 203135",
    "principal": "Mrs. Deepti Sharma (M.Sc., M.Ed., M.C.A., M.Phil.)",
    "timings": "Summer: 7:50 AM to 2:10 PM | Winter: 8:20 AM to 2:20 PM",
    "fees_2025": "Admission Fee: ₹5500-₹6500. Annual Composite Fee starts at ₹29,800. For XII Science, it's approx ₹43,600+.",
    "mobile_policy": "Strictly prohibited. Confiscated phones require a ₹1000 fine for early return.",
    "results": "Excellent CBSE Results! The school consistently achieves 100% pass results. Many students score 95%+, with toppers consistently securing admissions in top Indian universities and professional colleges.",
    "achievements": "Ranked No. 1 School Leaders in Greater Noida (TimesNow 2024). Awarded the prestigious British Council International School Award.",
    "motto": "Empowering every child. Dare to dream, Learn to excel."
}

# --- 4. CHATBOT INTERFACE ---
st.markdown("<h1>🚀 ASTRA-AI PRO</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Intelligence for <b>{school_data['name']}</b></p>", unsafe_allow_html=True)
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am Astra-AI. I know about the results, fees, timings, and rules of Pragyan Public School. How can I help?"}
    ]

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("Ask about past results, fees, etc..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        query = prompt.lower()
        
        # LOGIC ENGINE
        if any(word in query for word in ["result", "pass", "percent", "score", "topper", "board"]):
            response = f"**Academic Results:** {school_data['results']}"
        
        elif any(word in query for word in ["name", "which school"]):
            response = f"This is the official bot for **{school_data['name']}**."
        
        elif any(word in query for word in ["principal", "deepti"]):
            response = f"The Principal is **{school_data['principal']}**."
        
        elif any(word in query for word in ["fee", "cost", "money"]):
            response = f"**Fee Structure (2025-26):** {school_data['fees_2025']}"
        
        elif any(word in query for word in ["time", "timing", "hours"]):
            response = f"School Timings: {school_data['timings']}"
        
        elif any(word in query for word in ["mobile", "phone", "fine"]):
            response = f"**Mobile Policy:** {school_data['mobile_policy']}"
            
        elif any(word in query for word in ["hi", "hello"]):
            response = "Greetings! I am Astra-AI. How can I help you today?"

        else:
            response = "I have information on CBSE results, fees, principal, and school rules. Ask me: 'Tell me about the board results'!"

        # Typing Animation
        full_res = ""
        placeholder = st.empty()
        for word in response.split():
            full_res += word + " "
            time.sleep(0.06)
            placeholder.markdown(full_res)
            
    st.session_state.messages.append({"role": "assistant", "content": response})
