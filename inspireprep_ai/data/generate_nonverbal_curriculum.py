import json

topics = [
    "Shape Sequences", "Reflections", "Rotations", "Odd One Out", "Matrices", "Pattern Completion", "3D Visualisation",
    "Code Breaking", "Grid Puzzles", "Spatial Reasoning", "Mirror Symmetry", "Horizontal Symmetry", "Vertical Symmetry",
    "Shape Matching", "Shape Classification", "Shape Transformation", "Shape Rotation (Clockwise)",
    "Shape Rotation (Anti-clockwise)", "Shape Enlargement", "Shape Reduction", "Shape Folding", "Cube Nets",
    "Dice Faces", "Hidden Shapes", "Embedded Figures", "Overlapping Shapes", "Transparent Layers", "Shape Counting",
    "Line Counting", "Dot Patterns", "Arrow Patterns", "Directional Reasoning", "Positioning in Grids",
    "Shape Movement", "Shape Tracing", "Shape Completion", "Shape Elimination", "Shape Inference", "Shape Deduction",
    "Shape Logic", "Shape Sequences (Advanced)", "Reflections (Advanced)", "Rotations (Advanced)", "Matrices (Advanced)",
    "Pattern Completion (Advanced)", "3D Visualisation (Advanced)", "Spatial Reasoning (Advanced)",
    "Mixed Non-Verbal Practice", "Non-Verbal Reasoning Revision", "Timed Practice", "Exam Simulation"
]

curriculum = {}
for i, topic in enumerate(topics, start=1):
    lesson = {
        "title": f"Non-Verbal Reasoning – {topic}",
        "summary": f"Practise {topic.lower()} to improve visual reasoning and pattern recognition.",
        "explanation": f"This lesson introduces {topic.lower()} with visual examples and logic-based tasks.",
        "items": [f"{topic} example {j+1}" for j in range(50)]
    }
    curriculum[f"lesson{i}"] = lesson

with open("curriculum_nonverbal.json", "w", encoding="utf-8") as f:
    json.dump(curriculum, f, indent=2)
