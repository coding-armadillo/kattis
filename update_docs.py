import pickle
import subprocess
from datetime import date
from pathlib import Path

import requests
import seaborn as sns
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
    "js": "JavaScript",
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
    try:
        subprocess.call(
            [
                "black",
                uri,
            ]
        )
    except:
        pass
    try:
        subprocess.call(
            [
                "clang-format",
                "-i",
                f"{Path('src')/folder/'*.cpp'}",
                "-style=Microsoft",
            ]
        )
    except:
        pass
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
    now = date.today()
    text = f"# Difficulty - {folder.capitalize()} (as of {now})\n"
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
        for language in sorted(languages):
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
    text = """# Kattis

## Summary by Difficulty of Problems Solved
"""

    for folder, total in summary.items():
        text += f"""
- [{folder.capitalize()} ^{total}^]({folder}.md)
"""
    text += f"""
## Summary by First Character of Problems Solved

![summary-by-first-char](summary-by-first-char.png)
"""
    f.write(text)

with open("docs/.cache", "wb") as f:
    pickle.dump(cache, f)

from collections import Counter

s = Counter([k[0] for k in cache.values()])
ax = sns.barplot(x=list(s.keys()), y=list(s.values()))
ax.get_figure().savefig("docs/summary-by-first-char.png", bbox_inches="tight")
