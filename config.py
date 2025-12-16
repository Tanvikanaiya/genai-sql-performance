import streamlit as st

DB_CONFIG = {
    "host": st.secrets["DB_HOST"],
    "user": st.secrets["DB_USER"],
    "password": st.secrets["DB_PASSWORD"],
    "database": st.secrets["DB_NAME"]
}

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

