mapping = {
    1: "Januar",
    2: "Februar",
    3: "Marts",
    4: "April",
    5: "Maj",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "December",
}
m, d, y = [int(d) for d in input().split("/")]
print(f"{d}. {mapping[m]} {y}")
