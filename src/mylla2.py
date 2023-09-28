board = []
for _ in range(3):
    board.append(list(input()))

winner = ""
for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
        winner = board[i][0]
        break
    elif board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
        winner = board[0][i]
        break

if board[0][0] == board[1][1] == board[2][2] and board[1][1] != "_":
    winner = board[1][1]
elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != "_":
    winner = board[1][1]

if winner == "O":
    winner = "Jebb"
else:
    winner = "Neibb"

print(winner)
