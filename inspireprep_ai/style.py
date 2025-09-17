import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
        html, body {
            font-family: 'Comic Sans MS', cursive;
            background-color: #f0f8ff;
        }
        .stButton>button {
            background-color: #ff8c00;
            color: white;
            border-radius: 20px;
            padding: 0.5em 1em;
            font-size: 16px;
            border: none;
        }
        .stSelectbox, .stRadio {
            border-radius: 15px;
        }
        .stMarkdown {
            background-color: #ffffff;
            border-radius: 15px;
            padding: 1em;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        </style>
    """, unsafe_allow_html=True)
