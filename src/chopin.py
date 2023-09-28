alternatives = [("A#", "Bb"), ("C#", "Db"), ("D#", "Eb"), ("F#", "Gb"), ("G#", "Ab")]


m = dict(alternatives + [(b, a) for a, b in alternatives])

i = 1
while True:
    try:
        s = input()
    except:
        break
    key, tone = s.split()
    if key in m:
        print(f"Case {i}: {m[key]} {tone}")
    else:
        print(f"Case {i}: UNIQUE")

    i += 1
