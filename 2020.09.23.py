#단지번호붙이기

"""
n = int(input())

for _ in range(n) :
    board.append(list(int(input())))
"""
Dx = [-1, 0, 1, 0]
Dy = [0, -1, 0, 1]
goXY = []

def DFS(x, y) :
    global answer
    global count

    if board[x][y] == 0 and chboard[x][y] == 1 :
        return
    else :
        goXY.append((x, y))
        chboard[x][y] = answer
        board[x][y] = 0
        count += 1
        for i in range(4) :
            Nx = x+Dx[i]
            Ny = y+Dy[i]
            if 0<=Nx<7 and 0<=Ny<7 and board[Nx][Ny] == 1 and chboard[Nx][Ny] == 0:
                DFS(Nx, Ny)




board = [[0, 1, 1, 0, 1, 0, 0],
         [0, 1, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 1, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 0]]

chboard = [[0]*7 for _ in range(7)]
n = 7
answer = 0
count = 0

#DFS(1, 1, answer)
answerL = []
for i in range(n) :
    for j in range(n) :
        if board[i][j] == 1 :
            answer += 1
            DFS(i, j)
            answerL.append(count)
            count = 0

for r in board:
    print(r)
print("")
for w in chboard:
    print(w)
print("")

print(answer)
print(answerL)
