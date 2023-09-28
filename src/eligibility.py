for _ in range(int(input())):
    name, pss, dob, courses = input().split()
    courses = int(courses)
    pss = [int(d) for d in pss.split("/")]
    dob = [int(d) for d in dob.split("/")]
    if pss[0] >= 2010 or dob[0] >= 1991:
        print(name, "eligible")
    elif courses > 40:
        print(name, "ineligible")
    else:
        print(name, "coach petitions")
