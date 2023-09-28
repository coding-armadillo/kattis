def translate(w):
    if w[0] in "aeiouy":
        return w + "yay"
    else:
        i = 1
        while i < len(w):
            if w[i] in "aeiouy":
                break
            i += 1
        return w[i:] + w[:i] + "ay"


while True:
    try:
        text = input()
        print(" ".join([translate(w) for w in text.split()]))
    except:
        break
