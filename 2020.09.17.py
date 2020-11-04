#동전분배 내코드
import sys

def DFS(L):
    #global res
    #global count
    global MS
    #print(culc)
    if L == N :
        #print("ddd")
        #print(culc)
        #print(max(culc) - min(culc))
        if max(culc) - min(culc) < MS:
            #print(max(culc) - min(culc))
            MS = max(culc) - min(culc)

    else:
        for i in range(3):
            if culc[i] + mList[L] not in culc :
                culc[i] += mList[L]
                #print(culc)
                DFS(L + 1)
                culc[i] -= mList[L]


if __name__ == "__main__":
    for i in range(1, 6):

        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        count = 0
        MS = 999999
        N = int(input())
        culc = [0]*3
        #res = []
        mList = []

        for j in range(N) :
            mList.append(int(input()))

        print(mList)

        DFS(0)

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")
        answer = int(input())

        if (MS) == answer:
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(MS) + "원 정답 : " + str(answer))



