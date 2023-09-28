case_num = 0
while True:
    try:
        line = input()
    except:
        break
    case_num += 1
    numbers = [int(d) for d in line.split()[1:]]
    print(f"Case {case_num}: {min(numbers)} {max(numbers)} {max(numbers)-min(numbers)}")
