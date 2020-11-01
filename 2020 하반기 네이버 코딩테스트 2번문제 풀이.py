"""
def solution(S):
    # write your code in Python 3.6
    count = 0
    countA = 0

    if "aaa" in S :
        return -1

    elif S == "aa" :
        return 0

    else :
        for i in S :
            if i != "a" :
                count += 1
            else :
                countA += 1

        return (2 * count + 2) - countA
"""
"""
S = ["abcd", "efgh"]
print(S)
n = len(S)
m = len(S[0])
breakC = False
answer = []

for i in range(m) :
    checkL = set()
    for j in range(n) :
        if S[j][i] not in checkL :
            checkL.add(S[j][i])
        else :
            checkL = list(checkL)
            answer.extend([checkL.index(S[j][i]), j, i])
            breakC = True
            break
    if breakC == True :
        break

print(answer)
"""
"""
A = []
B = [i for i in range(1, len(A)+1)]
A.sort()
count = 0

for i in range(len(A)) :
    count += abs(A[i] - B[i])

print(count)
"""