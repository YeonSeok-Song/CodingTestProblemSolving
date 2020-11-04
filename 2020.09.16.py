#동전교환 내코드
import sys

def DFS(L, sumT):
    global res
    global count
    if sumT > T :
        return

    if L == n :
        if sumT == T:
            count += 1

    else:
        for i in range(nlist[L]+1) :
            DFS(L + 1, sumT + plist[L]*i)

if __name__ == "__main__":
    for i in range(1, 6):

        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        count = 0

        T = int(input())
        n = int(input())
        res = []
        plist = []
        nlist = []
        for j in range(n) :
            K, M = map(int, input().split(" "))
            plist.append(K)
            nlist.append(M)
        print(plist)
        print(nlist)
        DFS(0, 0)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")
        answer = int(input())

        if (count) == answer:
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(count) + "원 정답 : " + str(answer))



