"""
a1 = 50
a2 = 22
a3 = 28
a1 = a2+a3
ak = a(k+1) + a(k+2)

a2 = a4 + a5 2를 나눈 몫
a3 = a5 + a6

a4 = a7 + a8 2
a5
a6

a7 = 3

"""
"""
a1 = 50
a2 = 22
a3 = 28
a2 = a1 - a3
a3 = a1 - a2

a4 = a2 - a5
a5 = a3 - a6 or a2 - a4
ak = a(k+1) + a(k+2)
"""


"""

def DFS(L, checkL):
    global check

    if L == len(blocks):
        return
    else:
        while len(checkL) < L+1 :
            index = 0
            i = 0
            for i in range(L + 1):
                if check[L][i] != 0 and i not in checkL:
                    index = i
                    checkL.append(i)
                    break

            print("+++++++++++++++++++++++++")
            print(index)
            print(checkL)
            print(check)
            print("L : " + str(L))
            if 0<=index-1<len(check[L]) and  check[L][index - 1] == 0:
                check[L][index - 1] = check[L - 1][index - 1] - check[L][index]
                print(check[L][index - 1])
            else :
                if index not in checkL :
                    checkL.append(index)

            if 0<=index+1<len(check[L]) and check[L][index + 1] == 0 :
                check[L][index + 1] = check[L - 1][index] - check[L][index]
                print(check[L][index + 1])

            else :
                if index not in checkL:
                    checkL.append(index)

            print(checkL)




        DFS(L + 1, [])



blocks = [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]
result = [92, 72, 20, 63, 9, 11, 144, -81, 90, -79, 217, -73, -8, 98, -177]
check = [[0] * i for i in range(1, len(blocks)+1)]

for index, i in enumerate(blocks) :
    print(index)
    print(i[1])
    check[index][i[0]] = i[1]

if check[1][0] != 0 :
    check[1][1] = check[0][0] - check[1][0]
elif check[1][1] != 0 :
    check[1][0] = check[0][0] - check[1][1]


DFS(2, [])
answer = sum(check, [])

print(answer)

"""

n = 19
edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]
answer = 7

board = [[i] for i in range(edges[-1][0]+1)]
for i in range(len(edges)+1) :
    board[edges[i][0]].append(edges[i][1])

print(board)




def DFS(L) :

    for i in range(1, len(board)) :
        DFS(board[L][i])

