<figure markdown>
![Logo](https://open.kattis.com/images/site-logo){ width="100" }
</figure>

# Kattis

## Summary by Difficulty

> as of 2023-11-10

```vegalite
{
  "data": {
    "values": [
      {"Difficulty": "Easy", "Count": 436},
      {"Difficulty": "Medium", "Count": 28}
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

## Summary by Initial

```vegalite
{
  "data": {
    "values": [
      {"Initial": "S", "Count": 60},
      {"Initial": "C", "Count": 39},
      {"Initial": "A", "Count": 35},
      {"Initial": "P", "Count": 34},
      {"Initial": "B", "Count": 31},
      {"Initial": "T", "Count": 31},
      {"Initial": "M", "Count": 26},
      {"Initial": "H", "Count": 20},
      {"Initial": "E", "Count": 20},
      {"Initial": "F", "Count": 19},
      {"Initial": "D", "Count": 18},
      {"Initial": "R", "Count": 18},
      {"Initial": "G", "Count": 15},
      {"Initial": "L", "Count": 12},
      {"Initial": "I", "Count": 10},
      {"Initial": "O", "Count": 10},
      {"Initial": "V", "Count": 10},
      {"Initial": "W", "Count": 9},
      {"Initial": "J", "Count": 9},
      {"Initial": "K", "Count": 9},
      {"Initial": "U", "Count": 6},
      {"Initial": "N", "Count": 5},
      {"Initial": "Q", "Count": 5},
      {"Initial": "1", "Count": 2},
      {"Initial": "Y", "Count": 2},
      {"Initial": "Z", "Count": 2},
      {"Initial": "3", "Count": 1},
      {"Initial": "4", "Count": 1},
      {"Initial": "9", "Count": 1},
      {"Initial": "Á", "Count": 1},
      {"Initial": "Ö", "Count": 1},
      {"Initial": "Ó", "Count": 1},
      {"Initial": "Ú", "Count": 1}
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

## Summary by Language

```vegalite
{
  "data": {
    "values": [
      {"Language": "Python", "Count": 461},
      {"Language": "Go", "Count": 38},
      {"Language": "Java", "Count": 27},
      {"Language": "C++", "Count": 18},
      {"Language": "JavaScript", "Count": 9},
      {"Language": "Haskell", "Count": 4},
      {"Language": "Kotlin", "Count": 3},
      {"Language": "Rust", "Count": 3}
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

---

!!! note ""

    Thanks to all 5 [contributors](https://github.com/coding-armadillo/kattis#contributors-).
