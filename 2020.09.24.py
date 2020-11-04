Dx = [-1, 0, 1, 0]
Dy = [0, -1, 0, 1]
place = []
def BFS(x, y) :
    global up
    print(x, y)
    if N*N-chCount == len(place) :
        return
    else :
        for i in range(4) :
            Px = x + Dx[i]
            Py = y + Dy[i]
            print(Px, Py)
            if 0<=Px<N and 0<=Py<N and board[Px][Py] > up and (Px, Py) not in place:
                place.append((Px, Py))
                BFS(Px, Py)

#board = []
N = 5

board = [[6, 8, 2, 6, 2],
         [3, 2, 3, 4, 6],
         [6, 7, 3, 3, 2],
         [7, 2, 5, 3, 6],
         [8, 9, 5, 2, 7]]
count = 0
cL = []

boardC = {}

for i in board :
    for k in i :
        if k not in boardC :
            boardC[k] = 1
        else :
            boardC[k] += 1

MaxC = max(boardC)
MinC = min(boardC)
keys = sorted(boardC.keys())
print(keys)
chCount = 0

for up in range(MinC, MaxC) :
    print("new : " + str(up))
    chCount += boardC[up]
    for k in range(N) :
        for l in range(N) :
            if (k, l) not in place and board[k][l] > up:
                BFS(k, l)
                print("what")
                count += 1
    print("count : " + str(count))
    print(place)
    cL.append(count)
    count = 0
    place = list()

print(max(cL))
"""
n = int(input())
for _ in range(n) : 
    board.append(list(map(int, input().split(" "))))
"""