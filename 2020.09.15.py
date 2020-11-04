# 휴가 2020 09 15
"""
import sys
def DFS(L, sumC):

    print(L + T[L], end="")
    print("sssssss", end="")
    print(sumC + P[L])

    global total
    if L+T[L] > n+1:
        if total < sumC:
            total = sumC

    elif L+T[L] == n+1:
        if total < sumC+P[L]:
            total = sumC+P[L]

    else:
        DFS(L + T[L], sumC + P[L])
        DFS(L + 1, sumC)


if __name__=="__main__":

    for i in range(1, 6):
        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        n = int(input())
        T = [0]
        P = [0]
        total = 0

        for j in range(n):
            check = input().split(" ")
            T.append(int(check[0]))
            P.append(int(check[1]))

        DFS(1, 0)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")
        answer = int(input())
        if total == answer :
            print("정답 " + str(i))
        else :
            print("틀림 계산결과 : " + str(total) + "원 정답 : " + str(answer))

"""
#내 풀이는 완전 오래거림
#어떤게 분기가 되는지 잘 생각해보자
#여기선 저울이 분기가 된다 오른쪽 왼쪽 안올림 이렇게
#양팔저울 2020 09 15
#내코드
"""
import sys

def DFS(L, sumT):
    global res
    global temp
    global ch
    if sumT > S :
        return
    if L == n+1 :
        if sumT not in res and sumT != 0 and sumT <= S:
            print(sumT)
            res.append(sumT)
    else :
        for i in range(0, n+1):
            if i > 0 :
                if ch[i] == 0 :
                    ch[i] = 1
                    DFS(L + 1, abs(sumT + Weight[i]))
                    DFS(L + 1, abs(sumT - Weight[i]))
                    ch[i] = 0
            else : DFS(L + 1, sumT)


if __name__ == "__main__":
    for i in range(1, 6):

        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        count = 0

        n = int(input())
        #n = 3
        ch = [0] * (n+1)
        WeightSelect = [[],[]]
        res = []
        temp = [0] * n
        Weight =  list(map(int, input().split(" ")))
        #Weight = [1, 5, 7]

        Weight.insert(0, 0)
        S = sum(Weight)
        DFS(0, 0)

        print(res)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")
        answer = int(input())
        
        if (S - len(res)) == answer:
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(count) + "원 정답 : " + str(answer))
"""
#강의 코드
import sys

def DFS(L, sumT):
    global res

    if L == n:
        if sumT > 0 and sumT <= S:
            res.add(sumT)
    else:
        DFS(L + 1, sumT + Weight[L])
        DFS(L + 1, sumT - Weight[L])
        DFS(L + 1, sumT)


if __name__ == "__main__":
    for i in range(1, 6):

        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        count = 0

        n = int(input())
        # n = 3
        ch = [0] * (n + 1)
        res = set()
        temp = [0] * n
        Weight = list(map(int, input().split(" ")))
        # Weight = [1, 5, 7]

        S = sum(Weight)
        DFS(0, 0)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")
        answer = int(input())

        if (S - len(res)) == answer:
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(count) + "원 정답 : " + str(answer))



