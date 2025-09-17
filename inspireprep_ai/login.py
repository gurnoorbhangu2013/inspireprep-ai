import streamlit as st
import json

def login():
    st.sidebar.header("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    with open("data/users.json", "r") as f:
        users = json.load(f)

    if st.sidebar.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state["user"] = username
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid credentials")
