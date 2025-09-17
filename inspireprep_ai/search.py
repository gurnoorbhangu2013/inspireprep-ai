import json
import os

def search_lessons(keyword):
    results = []
    for file in os.listdir("data"):
        if file.startswith("curriculum_") and file.endswith(".json"):
            with open(f"data/{file}", "r") as f:
                lessons = json.load(f)
                for key, lesson in lessons.items():
                    if keyword.lower() in lesson["title"].lower() or keyword.lower() in lesson["summary"].lower():
                        results.append(lesson)
    return results
