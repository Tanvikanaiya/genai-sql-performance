import streamlit as st
from db_connector import execute_query_with_stats
from optimizer import rule_based_analysis
from genai_insights import generate_ai_insights

st.set_page_config(
    page_title="GenAI SQL Performance Analyzer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 GenAI-Driven SQL Query Performance Analyzer")
st.write("Analyze SQL Server queries and get AI-powered optimization insights.")

query = st.text_area(
    "Enter SQL Query",
    height=200,
    placeholder="SELECT * FROM Orders WHERE OrderDate > '2024-01-01'"
)

if st.button("Analyze Query 🚀"):
    if not query.strip():
        st.warning("Please enter a SQL query.")
    else:
        try:
            execute_query_with_stats(query)
            st.success("Query executed successfully.")

            st.subheader("⚙️ Rule-Based Analysis")
            rules = rule_based_analysis(query)
            if rules:
                for r in rules:
                    st.write(f"• {r}")
            else:
                st.write("No obvious issues detected.")

            st.subheader("🤖 GenAI Optimization Insights")
            insights = generate_ai_insights(query)
            st.write(insights)

        except Exception as e:
            st.error(f"Error: {e}")
