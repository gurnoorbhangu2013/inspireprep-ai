import json

topics = [
    "Letter Sequences", "Word Codes", "Analogies", "Compound Words", "Logic Puzzles", "Word Meanings", "Odd One Out",
    "Sentence Completion", "Hidden Words", "Word Classification", "Alphabetical Order", "Word Building", "Word Pairs",
    "Word Opposites", "Word Synonyms", "Word Associations", "Word Patterns", "Word Chains", "Word Transformations",
    "Word Substitutions", "Word Matching", "Word Splits", "Word Merges", "Word Reversals", "Word Jumbles",
    "Word Analogies", "Word Connections", "Word Families", "Word Prefixes", "Word Suffixes", "Word Roots",
    "Word Definitions", "Word Contexts", "Word Usage", "Word Errors", "Word Corrections", "Word Logic",
    "Word Deduction", "Word Inference", "Word Reasoning", "Word Completion", "Word Puzzles", "Word Sequences",
    "Word Codes (Advanced)", "Word Analogies (Advanced)", "Word Logic (Advanced)", "Word Deduction (Advanced)",
    "Word Inference (Advanced)", "Word Reasoning (Advanced)", "Mixed Verbal Practice", "Verbal Reasoning Revision"
]

curriculum = {}
for i, topic in enumerate(topics, start=1):
    lesson = {
        "title": f"Verbal Reasoning – {topic}",
        "summary": f"Practise {topic.lower()} to improve reasoning and vocabulary skills.",
        "explanation": f"This lesson introduces {topic.lower()} with examples and practice questions.",
        "items": [f"{topic} example {j+1}" for j in range(50)]
    }
    curriculum[f"lesson{i}"] = lesson

with open("curriculum_verbal.json", "w", encoding="utf-8") as f:
    json.dump(curriculum, f, indent=2)
