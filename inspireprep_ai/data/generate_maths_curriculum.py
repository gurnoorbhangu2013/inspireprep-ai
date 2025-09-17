import json

topics = [
    "Fractions", "Decimals", "Percentages", "Place Value", "Number Lines", "Rounding Numbers", "Negative Numbers",
    "Factors and Multiples", "Prime Numbers", "Square and Cube Numbers", "Times Tables", "Division Strategies",
    "Long Multiplication", "Long Division", "Mental Maths", "Word Problems", "Estimation", "Ratio", "Proportion",
    "Algebra Basics", "Expressions and Equations", "Coordinates", "Graphs and Charts", "Mean, Median, Mode",
    "Probability", "Time", "Money", "Measurement Units", "Length", "Weight", "Capacity", "Area", "Perimeter",
    "Volume", "Angles", "Shapes and Properties", "Symmetry", "Transformations", "Nets of 3D Shapes",
    "Roman Numerals", "Order of Operations (BIDMAS)", "Sequences and Patterns", "Venn Diagrams", "Carroll Diagrams",
    "Bar Charts", "Pie Charts", "Line Graphs", "Conversion Tables", "Speed, Distance, Time",
    "Problem Solving Strategies", "Mixed Topic Revision"
]

curriculum = {}
for i, topic in enumerate(topics, start=1):
    lesson = {
        "title": f"Maths – {topic}",
        "summary": f"Learn about {topic.lower()} and how to apply it in problem solving.",
        "explanation": f"This lesson covers the concept of {topic.lower()} with examples and practice tasks.",
        "items": [f"{topic} example {j+1}" for j in range(50)]
    }
    curriculum[f"lesson{i}"] = lesson

with open("curriculum_maths.json", "w", encoding="utf-8") as f:
    json.dump(curriculum, f, indent=2)
