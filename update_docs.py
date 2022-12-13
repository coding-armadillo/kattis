from pathlib import Path

import requests
from bs4 import BeautifulSoup

folders = ["easy", "medium", "hard"]
language_map = {
    "py": "Python",
    "cpp": "C++",
}
summary = {}

for folder in folders:
    files = list(Path(f"src/{folder}").glob("*"))
    solutions = {}

    for file in files:
        if file.stem not in solutions:
            solutions[file.stem] = [file.name]
        else:
            solutions[file.stem].append(file.name)

    total = len(solutions)
    s = "s" if total > 1 else ""
    print(f"Found {total} solution{s} from src/{folder}")

    summary[folder] = total

    text = f"# Difficulty - {folder.capitalize()}\n"
    for solution, languages in sorted(solutions.items()):
        url = f"https://open.kattis.com/problems/{solution}"
        html = requests.get(url, verify=False)
        soup = BeautifulSoup(html.content, "html.parser")
        name = soup.find("h1").text
        card = f"""
??? success "{name}"

    === "Problem"

        See detail at [{url}]({url}).
"""
        for language in languages:
            ext = language.split(".")[-1]
            card += f"""
    === "{language_map[ext]}"

        ```{ext} linenums="1"
        --8<-- "src/{folder}/{language}"
        ```
"""
        text += card

    with open(f"docs/{folder}.md", "w") as f:
        f.write(text)

with open("docs/index.md", "w") as f:
    text = "# Kattis\n"

    for folder, total in summary.items():
        text += f"""
- [{folder.capitalize()} ^{total}^]({folder}.md)
"""
    f.write(text)
