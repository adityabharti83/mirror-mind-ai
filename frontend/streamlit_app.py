import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.profile_builder import analyze_text_profile
from src.response_engine import generate_response

st.set_page_config(page_title="MirrorMind AI", layout="centered")
st.title("🪞 MirrorMind AI")
st.subheader("Talk to yourself... literally!")

user_text = st.text_area("🗣️ Enter some of your past thoughts or messages:", height=150)

if user_text:
    st.markdown("### 🤖 Analyzing your personality...")
    profile = analyze_text_profile(user_text)
    st.json(profile)

    query = st.text_input("Ask something to your AI twin:")
    if query:
        response = generate_response(query, profile)
        st.markdown("### 🧠 Response from your AI mirror:")
        st.success(response)
