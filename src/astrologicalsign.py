for _ in range(int(input())):
    d, m = input().split()
    d = int(d)
    if (m == "Mar" and d >= 21) or (m == "Apr" and d <= 20):
        print("Aries")
    elif (m == "Apr" and d >= 21) or (m == "May" and d <= 20):
        print("Taurus")
    elif (m == "May" and d >= 21) or (m == "Jun" and d <= 21):
        print("Gemini")
    elif (m == "Jun" and d >= 22) or (m == "Jul" and d <= 22):
        print("Cancer")
    elif (m == "Jul" and d >= 23) or (m == "Aug" and d <= 22):
        print("Leo")
    elif (m == "Aug" and d >= 23) or (m == "Sep" and d <= 21):
        print("Virgo")
    elif (m == "Sep" and d >= 22) or (m == "Oct" and d <= 22):
        print("Libra")
    elif (m == "Oct" and d >= 23) or (m == "Nov" and d <= 22):
        print("Scorpio")
    elif (m == "Nov" and d >= 23) or (m == "Dec" and d <= 21):
        print("Sagittarius")
    elif (m == "Dec" and d >= 22) or (m == "Jan" and d <= 20):
        print("Capricorn")
    elif (m == "Jan" and d >= 21) or (m == "Feb" and d <= 19):
        print("Aquarius")
    elif (m == "Feb" and d >= 20) or (m == "Mar" and d <= 20):
        print("Pisces")
