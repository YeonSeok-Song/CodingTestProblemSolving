#송아지 찾기 내코드
import sys

def DFS(L, sumT):
    global answerT

    if L == N :
        answerT = sumT
        return

    else : #1, 2, 3, 4, 5

        if L <= M :
            print(tree[L][M - L:(M + L) + 1])
            DFS(L + 1, sumT + sum(tree[L][M - L:(M + L) + 1]))
            #                          0  2 : 3
            #                          1  1 : 4
            #                          2  0 : 5

        else :
            print(tree[L][L - M:N - (L - M)])
            DFS(L + 1, sumT + sum(tree[L][L - M:N - (L - M)]))
            #                          3  (F) : (F) + 1 = 1 : 4 , f == 1 = L3 - m2
            #                          4  (F) : (F) + 1 = 2 : 3 , f == 0 != L4 - m2
            #                                               4 = 5 - (L3-M2)1 5 - 2
            #                                                 [l - m][N - (l - m)]

if __name__ == "__main__":
    #N = 5
    #tree = [[10, 13, 10, 12, 15], [12, 39, 30, 23, 11], [11, 25, 50, 53, 15],
    #        [19, 27, 29, 37, 27], [19, 13, 30, 13, 19]]


    for i in range(1, 6):
        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")
    
        N = int(input())
        M = N // 2
        answerT = 0
        tree = []

        #print(input().split(" ")[:-1])
        #print(input().split(" ")[:-1])

        for j in range(N) :
            tree.append(list(map(int, input().split(" ")[:-1])))
        

        DFS(0, 0)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")

        answer = input()
        if answerT == int(answer):
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(N) + "원 정답 : " + str(answer))
