#n = 5
n = 100

eL = [0, 25, 4, 9, 16, 1]
hL = [0, 3, 4, 2, 2, 5]
wL = [0, 4, 6, 3, 5, 2]

dy = [0] * (n+1)
Maxh = 0

for i in range(1, n+1) :
    k = hL[i]
    j = 1
    m = i
    while j < n+1 :
        if eL[m] > eL[j] and wL[m] > wL[j] :
            print(m, j)
            k = k + hL[j]
            m = j
            j = 1
        else :
            j += 1

    print(k)
    dy[i] = k

print(dy)