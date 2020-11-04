#피자배달거리
def DFS(L, s) :
    global Citylen
    global res
    if L == m :
        total = 0
        for j in range(len(HousePoint)):
            x2, y2 = HousePoint[j]
            #print("-------------")
            #print(x2, y2, (abs(x1 - x2) + abs(y1 - y2)))
            #print("-------------")
            MinCheck = 999
            for i in range(m):
                x1, y1 = res[i]
                print(res)
                print(x1, y1)
                if MinCheck > (abs(x2 - x1) + abs(y2 - y1)) :
                    MinCheck = (abs(x2 - x1) + abs(y2 - y1))

            print("Min : " + str(MinCheck))
            total += MinCheck
        print("total : " + str(total))
        if total < Citylen :
            Citylen = total

    else :
        for i in range(s, len(PizzaPoint)):
            res[L] = PizzaPoint[i]
            DFS(L+1, i+1)


#n, m = map(int, input().split(" "))
#print(m, n)
n, m = 4, 4
#board = []
"""
for _ in range(n) : 
    board.append(list(map(int, input().split(" "))))
"""
Citylen = 9999

board = [[0, 1, 2, 0],
         [1, 0, 2, 1],
         [0, 2, 1, 2],
         [2, 0, 1, 2]]
res = [0] * (m)

PizzaPoint = []
HousePoint = []

for i in range(n) :
    for j in range(n) :
        if board[i][j] == 2 :
            PizzaPoint.append((j, i))
        elif board[i][j] == 1:
            HousePoint.append((j, i))

#F E D C B A
print(PizzaPoint)
print(HousePoint)
DFS(0, 0)
print(Citylen)



