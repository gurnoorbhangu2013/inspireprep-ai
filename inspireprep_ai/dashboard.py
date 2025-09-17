import streamlit as st
import json

def show_dashboard():
    st.header("📊 Parent Dashboard")
    with open("data/user_progress.json", "r", encoding="utf-8") as f:
        progress = json.load(f)

    for user, stats in progress.items():
        st.subheader(f"Student: {user}")
        st.write(f"Lessons Completed: {stats['lessons']}")
        st.write(f"Quizzes Taken: {stats['quizzes']}")
        st.write(f"Average Score: {stats['score']}%")

import json

def get_user_progress(email):
    with open("data/user_progress.json", "r") as f:
        progress = json.load(f)
    return progress.get(email, {})
