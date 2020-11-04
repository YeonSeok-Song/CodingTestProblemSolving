# 미로의 최단거리 통로
#미로를 탐험할 때는 사방진으로 체크할것
#움직이기가 가능하다면 그곳으로 이동하고 아니면 말것
#움직인 뒤엔 그 전곳을 1로 바꿀것.
#스택으로 짜서 움직이고 그위치를 스택에 넣고 다시 뺴서 확인하고 이걸 반복 다만 스텍에 넣을때는
#통로로 갔을 때 그곳만 스택에 넣기.
from collections import deque
import sys
#def BFS(L, sumT):


if __name__ == "__main__":

    MX = [-1, 0, 1, 0]
    MY = [0, 1, 0, -1]

    for i in range(1, 6):
        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")
        miro = []
        for k in range(7) :
            miro.append(list(map(int, input().split(" "))))
        for b in miro :
            print(b)
        temp = [[0]*7 for _ in range(7)]
        deq = deque()
        Cx = 0
        Cy = 0
        deq.append((0, 0))
        miro[0][0] = 1

        while deq :
            for p in temp :
                print(p)
            print()
            tep = deq.popleft()
            for j in range(4) :
                Cx = tep[0] + MX[j]
                Cy = tep[1] + MY[j]
                if 0<=Cx<=6 and 0<=Cy<=6 and miro[Cx][Cy] == 0 :
                    miro[Cx][Cy] = 1
                    temp[Cx][Cy] = temp[tep[0]][tep[1]] + 1
                    deq.append((Cx, Cy))


        if temp[6][6] == 0 :
            temp[6][6] = -1

        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")

        answer = input()
        if temp[6][6] == int(answer):
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(temp[6][6]) + " 정답 : " + str(answer))
