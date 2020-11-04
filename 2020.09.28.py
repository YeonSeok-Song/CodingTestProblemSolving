n = 7

mL = [0] * (n+1)

def DFS(L) :
    global mL
    print(L)
    if L == 1 or L == 2 :
        return L
    if mL[L] > 0 :
        return mL[L]
    else :
        mL[L] = DFS(L-1) + DFS(L-2)
        return mL[L]


DFS(n)
print(mL)