notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
offset = [2, 2, 1, 2, 2, 2]
majors = {}
for i in range(len(notes)):
    name = notes[i]
    progression = [name]
    for i in offset:
        index = (notes.index(progression[-1]) + i) % len(notes)
        progression.append(notes[index])
    majors[name] = progression

_ = input()
scales = set(input().split())
print(" ".join([n for n in majors if scales < set(majors[n])]) or "none")
