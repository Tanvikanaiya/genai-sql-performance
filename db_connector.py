import pyodbc
import streamlit as st

def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={st.secrets['DB_SERVER']};"
        f"DATABASE={st.secrets['DB_NAME']};"
        f"UID={st.secrets['DB_USER']};"
        f"PWD={st.secrets['DB_PASSWORD']};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=30;"
    )
    return pyodbc.connect(conn_str)

def execute_query_with_stats(query):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SET STATISTICS IO ON; SET STATISTICS TIME ON;")
    cursor.execute(query)

    try:
        cursor.fetchall()
    except:
        pass

    conn.close()
