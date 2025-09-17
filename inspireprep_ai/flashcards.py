import streamlit as st
import json

def show_flashcards(subject):
    st.header(f"🃏 {subject} Flashcards")
    with open("data/flashcards.json", "r", encoding="utf-8") as f:
        cards = json.load(f)

    filtered = [c for c in cards if c["subject"] == subject]
    for i, card in enumerate(filtered):
        with st.expander(f"Flashcard {i+1}"):
            st.write(f"**Q:** {card['question']}")
            if st.button(f"Show Answer {i+1}"):
                st.info(f"**A:** {card['answer']}")
