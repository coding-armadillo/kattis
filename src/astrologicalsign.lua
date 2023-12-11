for _ = 1, io.read("*n") do
    d = io.read("*n")
    m = io.read():gsub("%s+", "")

    if (m == "Mar" and d >= 21) or (m == "Apr" and d <= 20) then
        print("Aries")
    elseif (m == "Apr" and d >= 21) or (m == "May" and d <= 20) then
        print("Taurus")
    elseif (m == "May" and d >= 21) or (m == "Jun" and d <= 21) then
        print("Gemini")
    elseif (m == "Jun" and d >= 22) or (m == "Jul" and d <= 22) then
        print("Cancer")
    elseif (m == "Jul" and d >= 23) or (m == "Aug" and d <= 22) then
        print("Leo")
    elseif (m == "Aug" and d >= 23) or (m == "Sep" and d <= 21) then
        print("Virgo")
    elseif (m == "Sep" and d >= 22) or (m == "Oct" and d <= 22) then
        print("Libra")
    elseif (m == "Oct" and d >= 23) or (m == "Nov" and d <= 22) then
        print("Scorpio")
    elseif (m == "Nov" and d >= 23) or (m == "Dec" and d <= 21) then
        print("Sagittarius")
    elseif (m == "Dec" and d >= 22) or (m == "Jan" and d <= 20) then
        print("Capricorn")
    elseif (m == "Jan" and d >= 21) or (m == "Feb" and d <= 19) then
        print("Aquarius")
    elseif (m == "Feb" and d >= 20) or (m == "Mar" and d <= 20) then
        print("Pisces")
    end
end
