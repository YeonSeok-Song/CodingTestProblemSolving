#송아지 찾기 내코드
import sys

def DFS(L, currentP):
    global count

    if currentP == E :
        if count > temp :
           count = temp

    else :
        DFS(L + 1, currentP+1)
        DFS(L + 1, currentP-1)
        DFS(L + 1, currentP+5)



if __name__ == "__main__":

    for i in range(1, 6):
        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        S, E = map(int, input().split(" "))
        temp = 0
        count = 99999999
        DFS(0, 0, 0)
        """
        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")

        answer = input()
        if len(res) == answer:
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(N) + "원 정답 : " + str(answer))
        """


