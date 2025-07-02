import string

m = {
    "Á": "a",
    "á": "a",
    "Ð": "d",
    "ð": "d",
    "É": "e",
    "é": "e",
    "Í": "i",
    "í": "i",
    "Ó": "o",
    "ó": "o",
    "Ú": "u",
    "ú": "u",
    "Ý": "y",
    "ý": "y",
    "Þ": "th",
    "þ": "th",
    "Æ": "ae",
    "æ": "ae",
    "Ö": "o",
    "ö": "o",
}
s = input()
s = [c for c in s if c in string.ascii_letters or c in string.digits or c in m]
s = [m.get(c, c).lower() for c in s]
print(*s, ".is", sep="")
