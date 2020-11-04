#알파코드 내코드
#정답코드는 포문으로 알파벳을 전부 일일이 찾게 만들어버림
#내꺼는 두개나 한개씩 잘라서 인덱스번호로 바꾸고 바로 조회하게끔 함.
import sys

def DFS(L, Code):

    global N
    global res
    #print(L)
    if L > len(N) :
        return

    if L == len(N) :
        res.add(Code)

    else :
        #여기 if문을 1자리와 10자리로 구분함
        #그래서 1자리일때는 그냥 비교하고 끝
        #10자리일때는 10자리 숫자와 1자리 숫자가 해당 포문 숫자와 일치할 때만
        #비교하게 만듬
        check = int("".join(N[L:L + 1])) - 1
        if check != 0 :
            DFS(L + 1, Code + alphabet[check])
        else :
            DFS(L + 1, Code)

        check = int("".join(N[L:L + 2])) - 1

        if check < 26 :
            DFS(L + 2, Code + alphabet[check])

        #영은 10, 20밖에 없음 나머지는 상관없음 영앞을 봐라

        """
        if "".join(N[L+1:L + 2]) == '0' :
            DFS(L+2, Code + alphabet[int("".join(N[L:L + 2]))-1])

        elif "".join(N[L:L + 1]) == '0':
            DFS(L + 1, Code)

        else :
            DFS(L + 1, Code + alphabet[int("".join(N[L:L + 1])) - 1])
            if int("".join(N[L:L + 2])) < 26:
                DFS(L + 2, Code + alphabet[int("".join(N[L:L + 2])) - 1])
        """

if __name__ == "__main__":

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']

    for i in range(1, 6):
        inA = "in" + str(i) + ".txt"
        sys.stdin = open(inA, "r")

        res = set()

        N = list(input())
        N.insert(len(N), -1) #2개잘라 비교할 때 해결책: 무조건 맨 뒤값에 false가 되서
                            #마지막에 도달했을때 두개씩 자르지 않게 만들기 .
        DFS(0, "")
        #print(res)
        print(len(res))
        """
        outA = "out" + str(i) + ".txt"
        sys.stdin = open(outA, "r")

        answer = input()
        if len(res) == answer:
            print("정답 " + str(i))
        else:
            print("틀림 계산결과 : " + str(N) + "원 정답 : " + str(answer))
        """


