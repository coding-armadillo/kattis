for _ in range(int(input())):
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    largest = max(votes)
    if votes.count(largest) > 1:
        print("no winner")
    else:
        total = sum(votes)
        winner = votes.index(largest)
        print(
            "majority" if votes[winner] > total / 2 else "minority",
            "winner",
            winner + 1,
        )
