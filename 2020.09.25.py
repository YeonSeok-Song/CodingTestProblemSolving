import sys

Dx = [-1, 0, 1, 0]
Dy = [0, -1, 0, 1]


def BFS(L):
    global countZ
    global answerT
    #print(countZ)
    """
    for v in board :
        print(v)
    print("")
    """
    if L > n * m:
        answerT = -1

    elif countZ == 0 :
        answerT = L-1
    #쭉 탐색하지 말구 큐에 넣는건 어떤가?
    else :
        for i in range(n):
            for j in range(m):
                if board[i][j] == L:
                    #print("i : " + str(i) + " j : " + str(j))
                    for k in range(4):
                        Px = j + Dx[k]
                        Py = i + Dy[k]
                        #print("py : " + str(Py) + " px : " + str(Px))
                        if 0 <= Px < m and 0 <= Py < n and board[Py][Px] == 0:
                            board[Py][Px] = L+1
                            countZ -= 1

        BFS(L+1)


if __name__ == "__main__":
    # N = 5
    # tree = [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15],
    #        [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]

    for i in range(1, 6):
        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")
        Lxy = input().split(" ")
        m, n = int(Lxy[0]), int(Lxy[1])

        board = []
        answerT = 0
        countZ = 0

        for _ in range(n) :
            board.append(list(map(int, input().split(" ")[:-1])))

        """
        m, n = 6, 4
        board = [[0, 0, -1, 0, 0, 0],
                 [0, -1, 0, -1, -1, 0],
                 [0, 0, -1, 0, 0, 0],
                 [0, 0, 0, 0, -1, 1]]
        """

        for u in range(n):
            for l in range(m):
                if board[u][l] == 0:
                    countZ += 1

        if countZ == 0:
            answerT = 0

        else:
            BFS(1)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")

        answer = input()
        if answerT == int(answer):
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(answerT) + "원 정답 : " + str(answer))