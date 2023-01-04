import subprocess
from pathlib import Path
import pickle

import requests
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
folders = ["easy", "medium", "hard"]
language_map = {
    "py": "Python",
    "cpp": "C++",
    "java": "Java",
    "rs": "Rust",
    "go": "Go",
    "hs": "Haskell",
}
summary = {}

try:
    with open("docs/.cache", "rb") as f:
        cache = pickle.load(f)
except:
    cache = {}

for folder in folders:
    uri = f"src/{folder}"
    if not Path(uri).exists():
        Path(uri).mkdir(exist_ok=True)
    subprocess.call(["black", uri])
    files = list(Path(uri).glob("*"))
    solutions = {}

    for file in files:
        if file.stem not in solutions:
            solutions[file.stem] = [file.name]
        else:
            solutions[file.stem].append(file.name)

    total = len(solutions)
    s = "s" if total > 1 else ""
    print()
    print(f"Found {total} solution{s} from {uri}")
    print()

    summary[folder] = total

    text = f"# Difficulty - {folder.capitalize()}\n"
    for solution, languages in tqdm(sorted(solutions.items())):
        url = f"https://open.kattis.com/problems/{solution}"
        if solution in cache:
            name = cache[solution]
        else:
            html = requests.get(url, verify=False)
            soup = BeautifulSoup(html.content, "html.parser")
            name = soup.find("h1").text
            cache[solution] = name
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
        --8<-- "{uri}/{language}"
        ```
"""
        text += card

    with open(f"docs/{folder}.md", "w", encoding="utf-8") as f:
        f.write(text)

with open("docs/index.md", "w") as f:
    text = "# Kattis\n"

    for folder, total in summary.items():
        text += f"""
- [{folder.capitalize()} ^{total}^]({folder}.md)
"""
    f.write(text)

with open("docs/.cache", "wb") as f:
    pickle.dump(cache, f)
