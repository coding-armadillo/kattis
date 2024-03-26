import json
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path

import requests
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
language_map = {
    "cpp": "C++",
    "go": "Go",
    "hs": "Haskell",
    "java": "Java",
    "jl": "Julia",
    "js": "JavaScript",
    "kt": "Kotlin",
    "lua": "Lua",
    "py": "Python",
    "rb": "Ruby",
    "rs": "Rust",
}
level_map = {
    "Easy": ":green_circle:",
    "Medium": ":yellow_circle:",
    "Hard": ":red_circle:",
}

cache = {}

files = [f for f in list(Path("src").glob("*")) if not f.name.startswith(".")]
solutions = {}
for file in files:
    if file.stem not in solutions:
        solutions[file.stem] = [file.name]
    else:
        solutions[file.stem].append(file.name)


try:
    subprocess.call(
        [
            "black",
            "src",
        ]
    )
except:
    pass

try:
    subprocess.call(
        [
            "clang-format",
            "-i",
            f"{Path('src')/'*.cpp'}",
            "-style=Microsoft",
        ]
    )
except:
    pass

for name, languages in tqdm(solutions.items(), desc="🌐 Caching", mininterval=10):
    url = f"https://open.kattis.com/problems/{name}?tab=metadata"
    html = requests.get(url, verify=False, timeout=30)
    soup = BeautifulSoup(html.content, "html.parser")
    title = soup.find("h1").text
    metas = soup.find("div", class_="metadata-difficulty-card")
    difficulty = metas.text.replace("Difficulty", "-").split("-")
    score, level = difficulty[-2], difficulty[-1]
    cache[name] = (title, score, level)

total = len(solutions)
s = "s" if total > 1 else ""
print()
print(f"🔍 Found {total} solution{s}")
print()


summary = Counter(level for _, _, level in cache.values())

with open(".all-contributorsrc") as f:
    num_contributors = len(json.load(f)["contributors"])

with open("docs/index.md", "w", encoding="utf-8") as f:
    text = """
<figure markdown>
![Logo](https://open.kattis.com/images/site-logo){ width="100" }
</figure>

# kattis

About the solutions to [Kattis Problem Archive](https://open.kattis.com/)

## Summary by Difficulty
"""

    data = ",\n      ".join(
        f'{{"Difficulty": "{level}", "Count": {total}}}'
        for level, total in summary.most_common()
    )
    text += """
```vegalite
{
  "data": {
    "values": [
      %%data%%
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "Difficulty", "type": "nominal", "axis": {"labelAngle": 0}, "sort": "-y"},
    "y": {"field": "Count", "type": "quantitative"},
    "color": {"field": "Difficulty", "legend": null}
  }
}
```
""".replace(
        "%%data%%", data
    )

    data = ",\n      ".join(
        f'{{"Initial": "{initial}", "Count": {count}}}'
        for initial, count in Counter(
            [title[0] for title, _, _ in cache.values()]
        ).most_common()
    )
    text += """
## Summary by Initial

```vegalite
{
  "data": {
    "values": [
      %%data%%
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "Initial", "type": "nominal", "axis": {"labelAngle": 0}, "sort": "-y"},
    "y": {"field": "Count", "type": "quantitative"},
    "color": {"field": "Initial", "legend": null}
  }
}
```
""".replace(
        "%%data%%", data
    )

    data = ",\n      ".join(
        f'{{"Language": "{language}", "Count": {count}}}'
        for language, count in Counter(
            [language_map[f.name.split(".")[-1]] for f in files]
        ).most_common()
    )
    text += """
## Summary by Language

```vegalite
{
  "data": {
    "values": [
      %%data%%
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "Language", "type": "nominal", "axis": {"labelAngle": 0}, "sort": "-y"},
    "y": {"field": "Count", "type": "quantitative"},
    "color": {"field": "Language", "legend": null}
  }
}
```
""".replace(
        "%%data%%", data
    )

    text += f"""
---

!!! note ""

    Thanks to all {num_contributors} [contributors](https://github.com/coding-armadillo/kattis#contributors-).

---

> Last update: {date.today()}
"""

    f.write(text.lstrip())


text = f"""---
hide:
  - toc
---

# {len(solutions)} Problems, {sum(len(v) for v in solutions.values())} Solutions, {len(language_map)} Languages
"""
for name, languages in tqdm(sorted(solutions.items()), desc="📖 Refreshing Docs"):
    url = f"https://open.kattis.com/problems/{name}"
    title, score, level = cache[name]

    if len(languages) > 1:
        suffix = f"s in {len(languages)} languages"
    else:
        ext = languages[0].split(".")[-1]
        suffix = f" in {language_map[ext]}"

    card = f"""
## {level_map[level]} [{title}]({url})

??? success "Solution{suffix}"
"""
    for language in sorted(languages):
        ext = language.split(".")[-1]
        card += f"""
    === "{language_map[ext]}"

        ```{ext} linenums="1"
        --8<-- "src/{language}"
        ```
"""
    text += card

with open("docs/solutions.md", "w", encoding="utf-8") as f:
    f.write(text)
