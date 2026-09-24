email_line = None
while True:
    try:
        l = input()
        if l.startswith("To:") or l.startswith("Til:"):
            email_line = l
    except:
        break
email = email_line.split(":")[-1].strip()
addr, domain = email.split("@")
addr = addr.split("+")[0]
print(f"{addr}@{domain}")
