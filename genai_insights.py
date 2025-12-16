import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_ai_insights(query):
    prompt = f"""
    You are a SQL Server performance tuning expert.

    Analyze the SQL query below and provide:
    1. Performance bottlenecks
    2. Index recommendations
    3. Query rewrite suggestions
    4. Best practices

    SQL Query:
    {query}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
