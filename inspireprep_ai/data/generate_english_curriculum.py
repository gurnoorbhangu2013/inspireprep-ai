import json

topics = [
    "Synonyms", "Antonyms", "Homophones", "Homonyms", "Prefixes", "Suffixes", "Root Words", "Compound Words",
    "Contractions", "Plurals", "Possessives", "Punctuation Rules", "Capitalisation", "Sentence Types",
    "Subject–Verb Agreement", "Tenses", "Active vs Passive Voice", "Direct and Indirect Speech",
    "Clauses and Phrases", "Connectives and Conjunctions", "Paragraph Structure", "Topic Sentences",
    "Descriptive Writing", "Narrative Writing", "Persuasive Writing", "Instructional Writing",
    "Formal vs Informal Language", "Figurative Language", "Similes", "Metaphors", "Personification",
    "Alliteration", "Onomatopoeia", "Idioms", "Proverbs", "Inference Skills", "Deduction Skills",
    "Comprehension Strategies", "Skimming and Scanning", "Summarising Texts", "Identifying Main Ideas",
    "Fact vs Opinion", "Author’s Purpose", "Tone and Mood", "Vocabulary Building", "Spelling Patterns",
    "Common Confusions", "Editing and Proofreading", "Creative Writing Prompts", "Planning a Story",
    "Writing a Conclusion"
]

curriculum = {}
for i, topic in enumerate(topics, start=1):
    lesson = {
        "title": f"English – {topic}",
        "summary": f"Learn about {topic.lower()} and how to use them effectively.",
        "explanation": f"This lesson explains the concept of {topic.lower()} with examples and practice.",
        "items": [f"{topic} example {j+1}" for j in range(50)]
    }
    curriculum[f"lesson{i}"] = lesson

with open("curriculum_english.json", "w", encoding="utf-8") as f:
    json.dump(curriculum, f, indent=2)
