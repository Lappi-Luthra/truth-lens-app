import streamlit as st
import google.generativeai as genai
from groq import Groq
from PIL import Image, ExifTags

# --- 1. SETUP ---
st.set_page_config(page_title="Truth Lens AI", layout="wide")

# --- 2. SECRETS ---
# Make sure these names match exactly what you typed in Streamlit Secrets
GEMINI_KEY = st.secrets["GEMINI_KEY"]
GROQ_KEY = st.secrets["GROQ_KEY"]

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
groq_client = Groq(api_key=GROQ_KEY)

st.title("🛡️ Truth Lens Intelligence")
# ... rest of your code ...
