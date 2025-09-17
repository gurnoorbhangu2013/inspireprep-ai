import streamlit as st
import pyttsx3
import json
import random

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def narrate_lesson(subject):
    st.header(f"🎙️ Live Tutor Mode – {subject}")
    mode = st.radio("Choose Mode", ["Test Me", "Quiz Me", "Explain", "Ask Me Questions"])

    with open("data/questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    filtered = [q for q in questions if q["subject"] == subject]

    if mode == "Test Me":
        selected = random.sample(list(questions), len(questions))
        for i, q in enumerate(selected, 1):
            st.write(f"**Q{i}:** {q}")
            speak(q)
            st.write("Answer:", questions[q])
     
    elif mode == "Ask Me Questions":
        selected = random.sample(filtered, min(5, len(filtered)))
        for i, q in enumerate(selected):
            st.write(f"**Q{i+1}: {q['question']}**")
            speak(f"Question {i+1}: {q['question']}")
            answer = st.radio("Choose:", q["options"], key=f"ask_{i}")
            if st.button(f"Submit Q{i+1}", key=f"submit_ask_{i}"):
                if answer == q["answer"]:
                    st.success("Correct!")
                    speak("Correct!")
                else:
                    st.error(f"Incorrect. Answer: {q['answer']}")
                    speak(f"The correct answer is {q['answer']}")
