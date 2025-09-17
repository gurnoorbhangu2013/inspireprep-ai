import streamlit as st

try:
    from inspireprep_ai import app
    app.run()
except Exception as e:
    st.error("⚠️ The app encountered an error and some features may be disabled.")
    st.text(f"Details: {e}")
