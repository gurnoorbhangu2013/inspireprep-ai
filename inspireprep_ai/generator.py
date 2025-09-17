import streamlit as st
import json

def generate_lesson(subject):
    st.header(f"⚙️ Generate New {subject} Lesson")
    topic = st.text_input("Enter a topic")

    if st.button("Generate Lesson"):
        with open("data/generated_lessons.json", "r", encoding="utf-8") as f:
            lessons = json.load(f)

        match = lessons.get(topic.lower())
        if match and match["subject"] == subject:
            st.subheader(match["title"])
            st.write(match["summary"])
            st.write(match["content"])
        else:
            st.warning("No generated lesson found.")
