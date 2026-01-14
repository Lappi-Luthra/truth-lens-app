import streamlit as st
import google.generativeai as genai  # Changed this line
from groq import Groq
from PIL import Image, ExifTags

# --- 1. SETUP ---
st.set_page_config(page_title="Vera Forensic AI", layout="wide")

# --- 2. SECRETS & CLIENTS ---
GEMINI_KEY = st.secrets.get("GEMINI_KEY")
GROQ_KEY = st.secrets.get("GROQ_KEY")

if not GEMINI_KEY or not GROQ_KEY:
    st.error("API Keys missing in Secrets!")
    st.stop()

# Updated initialization for the standard library
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # Using stable flash model
groq_client = Groq(api_key=GROQ_KEY)

# ... (rest of your UI code) ...

# Inside your button click, change the "vision_resp" line to this:
# vision_resp = model.generate_content([v_prompt, img])
