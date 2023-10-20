<figure markdown>
![Logo](https://open.kattis.com/images/site-logo){ width="100" }
</figure>

# Kattis

## Summary by Difficulty

> as of 2023-10-20

```vegalite
{
  "data": {
    "values": [
      {"Difficulty": "Easy", "Count": 424},
      {"Difficulty": "Medium", "Count": 26}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "Difficulty", "type": "nominal", "axis": {"labelAngle": 0}, "sort": "-y"},
    "y": {"field": "Count", "type": "quantitative"}
  }
}
```

## Summary by Initial

```vegalite
{
  "data": {
    "values": [
      {"Initial": "S", "Count": 59},
      {"Initial": "C", "Count": 38},
      {"Initial": "A", "Count": 33},
      {"Initial": "P", "Count": 33},
      {"Initial": "B", "Count": 31},
      {"Initial": "T", "Count": 29},
      {"Initial": "M", "Count": 25},
      {"Initial": "H", "Count": 20},
      {"Initial": "E", "Count": 19},
      {"Initial": "D", "Count": 18},
      {"Initial": "R", "Count": 18},
      {"Initial": "F", "Count": 17},
      {"Initial": "G", "Count": 14},
      {"Initial": "L", "Count": 12},
      {"Initial": "I", "Count": 10},
      {"Initial": "O", "Count": 10},
      {"Initial": "V", "Count": 10},
      {"Initial": "W", "Count": 9},
      {"Initial": "J", "Count": 9},
      {"Initial": "K", "Count": 9},
      {"Initial": "N", "Count": 5},
      {"Initial": "Q", "Count": 5},
      {"Initial": "U", "Count": 5},
      {"Initial": "1", "Count": 2},
      {"Initial": "Y", "Count": 2},
      {"Initial": "Z", "Count": 2},
      {"Initial": "3", "Count": 1},
      {"Initial": "4", "Count": 1},
      {"Initial": "9", "Count": 1},
      {"Initial": "Ö", "Count": 1},
      {"Initial": "Ó", "Count": 1},
      {"Initial": "Ú", "Count": 1}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "Initial", "type": "nominal", "axis": {"labelAngle": 0}, "sort": "-y"},
    "y": {"field": "Count", "type": "quantitative"}
  }
}
```

## Summary by Language

```vegalite
{
  "data": {
    "values": [
      {"Language": "Python", "Count": 447},
      {"Language": "Go", "Count": 36},
      {"Language": "Java", "Count": 25},
      {"Language": "C++", "Count": 16},
      {"Language": "JavaScript", "Count": 8},
      {"Language": "Haskell", "Count": 3},
      {"Language": "Kotlin", "Count": 2},
      {"Language": "Rust", "Count": 2}
    ]
  },
  "mark": {"type": "bar", "tooltip": true},
  "encoding": {
    "x": {"field": "Language", "type": "nominal", "axis": {"labelAngle": 0}, "sort": "-y"},
    "y": {"field": "Count", "type": "quantitative"}
  }
}
```

---

!!! note ""

    Thanks to all 5 [contributors](https://github.com/coding-armadillo/kattis#contributors-).
