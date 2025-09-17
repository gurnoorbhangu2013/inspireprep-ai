import streamlit as st
import json
import random

def run_challenge(subject):
    st.header(f"🏆 Weekly Challenge – {subject}")
    with open("data/questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    filtered = [q for q in questions if q["subject"] == subject]
    selected = random.sample(filtered, min(5, len(filtered)))
    score = 0

    for i, q in enumerate(selected):
        st.write(f"**Q{i+1}: {q['question']}**")
        answer = st.radio("Choose:", q["options"], key=f"challenge_{i}")
        if st.button(f"Submit Q{i+1}", key=f"submit_challenge_{i}"):
            if answer == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. Correct answer: {q['answer']}")

    st.write(f"🏅 Final Score: {score} / {len(selected)}")
    if score == len(selected):
        st.balloons()
