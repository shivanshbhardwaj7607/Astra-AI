import streamlit as st
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="ASTRA-AI PRO", page_icon="🚀")

# --- 2. LOVELY UI STYLE ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #000428, #004e92); color: white; }
    .stChatMessage { background: rgba(255, 255, 255, 0.08); border-radius: 20px; border: 1px solid #00d2ff; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE COMPLETE KNOWLEDGE BRAIN ---
data = {
    "name": "Pragyan Public School, Jewar",
    "principal": "Mrs. Deepti Sharma (M.Sc., M.Ed., M.C.A., M.Phil.)",
    "timings": "Summer: 7:50 AM - 2:10 PM | Winter: 8:20 AM - 2:20 PM",
    "fees": "Admission Fee: ₹5500-₹6500. Annual Fee starts at ₹29,800.",
    "mobile": "Strictly prohibited. If caught, a ₹1000 fine is charged for early return.",
    "results": "Excellent CBSE Results! The school consistently achieves 100% pass results with many students scoring 95%+ every year.",
    "motto": "Empowering every child. Dare to dream, Learn to excel."
}

st.title("🚀 ASTRA-AI PRO")
st.write(f"Official Intelligence for **{data['name']}**")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("Ask me about board results, fees, etc..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    with st.chat_message("assistant"):
        q = p.lower()
        # ULTIMATE LOGIC
        if any(x in q for x in ["result", "pass", "score", "topper"]):
            ans = f"**Board Results:** {data['results']}"
        elif any(x in q for x in ["name", "which school"]):
            ans = f"This is the official AI assistant for **{data['name']}**."
        elif "principal" in q or "deepti" in q:
            ans = f"The Principal is **{data['principal']}**."
        elif "fee" in q or "cost" in q:
            ans = f"**Fee Structure:** {data['fees']}"
        elif "time" in q or "timing" in q:
            ans = f"School Timings: {data['timings']}"
        elif "mobile" in q or "phone" in q:
            ans = f"**Mobile Policy:** {data['mobile']}"
        elif "hi" in q or "hello" in q:
            ans = "Hello! I am Astra-AI. I know about PPS results, fees, and rules. Ask me anything!"
        else:
            ans = "I have info on CBSE results, fees, principal, and rules. Try: 'What are the board results?'"
        
        # Typing animation
        res = ""
        placeholder = st.empty()
        for word in ans.split():
            res += word + " "
            time.sleep(0.06)
            placeholder.markdown(res)
            
    st.session_state.messages.append({"role": "assistant", "content": ans})
