import streamlit as st
import json
import random

def generate_quiz(subject):
    st.header(f"🧠 {subject} Quiz")
    with open("data/questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    filtered = [q for q in questions if q["subject"] == subject]
    selected = random.sample(filtered, min(10, len(filtered)))
    score = 0

    for i, q in enumerate(selected):
        st.write(f"**Q{i+1}: {q['question']}**")
        answer = st.radio("Choose an answer:", q["options"], key=i)
        if st.button(f"Submit Q{i+1}", key=f"submit{i}"):
            if answer == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. Correct answer: {q['answer']}")

    st.write(f"### Final Score: {score} / {len(selected)}")
def start_timed_quiz(subject):
    st.header(f"⏱ Timed {subject} Quiz")
    with open(f"{subject}.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    filtered = [q for q in questions if q["subject"] == subject]
    score = 0

    for i, q in enumerate(filtered):
        st.write(f"Q{i+1}: {q['question']}")
        options = q["options"]
        selected = st.radio("Choose an option:", options, key=f"timed_{i}")
        if selected:
            if selected == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. Correct answer: {q['answer']}")

    st.write(f"### Final Score: {score} / {len(filtered)}")
