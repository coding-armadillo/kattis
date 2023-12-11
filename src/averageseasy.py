for _ in range(int(input())):
    input()
    ncs, ne = [int(d) for d in input().split()]
    students_cs, students_e = [], []

    while len(students_cs) < ncs or len(students_e) < ne:
        iq = [int(d) for d in input().split()]
        if len(students_cs) <= ncs:
            if len(iq) + len(students_cs) <= ncs:
                students_cs.extend(iq)
            else:
                ind = ncs - len(students_cs)
                students_cs.extend(iq[:ind])
                students_e.extend(iq[ind:])
        else:
            students_e.extend(iq)

    ave_cs, ave_e = sum(students_cs) / ncs, sum(students_e) / ne
    print(sum(p < ave_cs and p > ave_e for p in students_cs))
