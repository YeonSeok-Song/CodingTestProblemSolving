def DFS(x, y) :
    global answer

    for k in board :
        print(k)
    print()

    if board[6][6] == 1:
        answer += 1
        print("answer =" + str(answer))

    else :
        for i in range(4) :
            dx = x+Dx[i]
            dy = y+Dy[i]
            if 0 <= dx < 7 and 0 <= dy < 7 and board[dx][dy] == 0 and miro[dx][dy] == 0:
                board[dx][dy] = 1
                DFS(dx, dy)
                board[dx][dy] = 0


Dx = [-1, 0, 1, 0 ]
Dy = [0, -1, 0, 1]
answer = 0
board = [[0] * 7 for _ in range(7)]
miro = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0]]

board[0][0] = 1
DFS(0, 0)
print(answer)
"""
miro = []
for _ in range(7) : 
    miro.append(list(map(int, input().split(" "))))
"""




