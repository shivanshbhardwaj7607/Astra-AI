import streamlit as st
import time

# This part makes it look 'Lovely' and '3D'
st.set_page_config(page_title="ASTRA-AI", page_icon="✨")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #000428, #004e92); color: white; }
    .stChatMessage { background: rgba(255,255,255,0.1); border-radius: 15px; border: 1px solid #00d2ff; }
    </style>
    """, unsafe_allow_html=True)

# This is your School Database
data = {
    "principal": "Mrs. Deepti Sharma",
    "timings": "Summer: 7:50 AM - 2:10 PM",
    "fees": "Admission Fee is approx ₹5500-₹6500.",
    "admission": "Based on written test and interview.",
    "mobile": "Strictly prohibited. ₹1000 fine for early return."
}

st.title("🚀 ASTRA-AI PRO")
st.write("Official Bot for Pragyan Public School")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if p := st.chat_input("Ask me about the school..."):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    
    with st.chat_message("assistant"):
        q = p.lower()
        if "time" in q: ans = f"School Timings: {data['timings']}"
        elif "fee" in q: ans = f"Fee Detail: {data['fees']}"
        elif "principal" in q: ans = f"The Principal is {data['principal']}"
        elif "mobile" in q: ans = f"Mobile Rules: {data['mobile']}"
        else: ans = "I am ASTRA-AI. Ask me about Fees, Timings, or Admissions!"
        
        # This creates the 'Gemini' typing effect
        res = ""
        placeholder = st.empty()
        for word in ans.split():
            res += word + " "
            time.sleep(0.1)
            placeholder.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": ans})