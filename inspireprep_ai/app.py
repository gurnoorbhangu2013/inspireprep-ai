import streamlit as st
from style import set_custom_style
from login import login
import streamlit as st
from register import register_user
from search import search_lessons
from dashboard import get_user_progress
from tutor_mode import narrate_lesson
from quiz_engine import generate_quiz, start_timed_quiz
from pdf_export import export_lesson_to_pdf
set_custom_style()
login()


subject = st.sidebar.selectbox("Choose Subject", ["English", "Maths", "Verbal Reasoning", "Non-Verbal Reasoning"])
menu = st.sidebar.radio("Navigate", [
    "Curriculum Lessons",
    "Take a Quiz",
    "Flashcards",
    "Generate Lesson",
    "Live Tutor Mode",
    "Weekly Challenge",
    "Parent Dashboard"
])

if menu == "Curriculum Lessons":
    from curriculum import show_curriculum
    show_curriculum(subject)

elif menu == "Take a Quiz":
    from quiz_engine import run_quiz
    run_quiz(subject)

elif menu == "Flashcards":
    from flashcards import show_flashcards
    show_flashcards(subject)

elif menu == "Generate Lesson":
    from generator import generate_lesson
    generate_lesson(subject)

elif menu == "Live Tutor Mode":
    from tutor_mode import tutor_mode
    tutor_mode(subject)

elif menu == "Weekly Challenge":
    from challenge_mode import run_challenge
    run_challenge(subject)

elif menu == "Parent Dashboard":
    from dashboard import show_dashboard
    show_dashboard()

st.sidebar.title("InspirePrep AI")
choice = st.sidebar.selectbox("Choose an action", [
    "Login / Register", "View Curriculum", "Search Topics",
    "Start Quiz", "Download Lesson PDF", "Narrate Lesson", "Timed Challenge", "Dashboard"
])

if choice == "Login / Register":
    with st.form("register_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Register")
        if submitted:
            st.success(register_user(name, email, password))

elif choice == "Search Topics":
    keyword = st.text_input("Enter keyword")
    if st.button("Search"):
        results = search_lessons(keyword)
        for r in results:
            st.write(r["title"])
            st.write(r["summary"])

elif choice == "Dashboard":
    email = st.text_input("Enter your email")
    if st.button("View Progress"):
        progress = get_user_progress(email)
        st.json(progress)

elif choice == "Narrate Lesson":
    subject = st.selectbox("Choose subject", ["english", "maths", "verbal", "nonverbal"])
    lesson_key = st.text_input("Enter lesson key (e.g. lesson1)")
    if st.button("Narrate"):
        try:
            with open(f"data/curriculum_{subject}.json", "r") as f:
                lesson = json.load(f)[lesson_key]
            narrate_lesson(lesson["title"], lesson["summary"], lesson["explanation"])
            st.success("Narration complete.")
        except Exception as e:
            st.error(f"Error: {e}")

elif choice == "Start Quiz":
    subject = st.selectbox("Choose subject", ["english", "maths", "verbal", "nonverbal"])
    lesson_key = st.text_input("Enter lesson key")
    num_questions = st.slider("Number of questions", 5, 50, 10)
    if st.button("Generate Quiz"):
        try:
            questions = generate_quiz(subject, lesson_key, num_questions)
            st.subheader("Quiz Questions")
            for i, q in enumerate(questions, 1):
                st.write(f"{i}. {q}")
        except Exception as e:
            st.error(f"Error: {e}")

elif choice == "Timed Challenge":
    subject = st.selectbox("Choose subject", ["english", "maths", "verbal", "nonverbal"])
    lesson_key = st.text_input("Enter lesson key")
    time_limit = st.slider("Time limit (seconds)", 30, 300, 60)
    if st.button("Start Timed Quiz"):
        try:
            questions = generate_quiz(subject, lesson_key)
            st.subheader("Timed Quiz Started")
            answers = start_timed_quiz(questions, time_limit)
            st.write("Answers submitted:", answers)
        except Exception as e:
            st.error(f"Error: {e}")

elif choice == "Download Lesson PDF":
    subject = st.selectbox("Choose subject", ["english", "maths", "verbal", "nonverbal"])
    lesson_key = st.text_input("Enter lesson key")
    if st.button("Export PDF"):
        try:
            export_lesson_to_pdf(subject, lesson_key)
            st.success("PDF exported successfully.")
        except Exception as e:
            st.error(f"Error: {e}")

def run():
    # All your existing Streamlit code goes here
    ...
            

