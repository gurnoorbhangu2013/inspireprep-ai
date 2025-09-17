import streamlit as st
import json
from pdf_export import export_lesson_as_pdf

def show_curriculum(subject):
    file_map = {
        "English": "curriculum_english.json",
        "Maths": "curriculum_maths.json",
        "Verbal Reasoning": "curriculum_verbal.json",
        "Non-Verbal Reasoning": "curriculum_nonverbal.json"
    }
    filename = file_map[subject]
    with open(f"data/{filename}", "r", encoding="utf-8") as f:
        curriculum = json.load(f)

    st.header(f"📚 {subject} Lessons")
    for key, lesson in curriculum.items():
        st.subheader(lesson["title"])
        st.write(lesson["summary"])
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(f"Full Lesson – {lesson['title']}", key=f"lesson_{key}"):
                for item in lesson["items"]:
                    st.markdown(f"- {item}")
        with col2:
            if st.button(f"Quick Explanation – {lesson['title']}", key=f"explain_{key}"):
                st.info(f"Explanation: {lesson['explanation']}")
        with col3:
            if st.button(f"Download PDF – {lesson['title']}", key=f"pdf_{key}"):
                export_lesson_as_pdf(lesson)
                st.success("PDF exported.")
