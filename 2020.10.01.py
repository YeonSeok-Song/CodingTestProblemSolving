n = 8
dL = [0, 5, 3, 7, 8, 6, 2, 9, 4]
dy = [0] * (n+1)
dy[1] = 1
for i in range(2, n+1) :
    k = 0
    for j in range(1, i+1) :
        if dL[i] > dL[j] :
            if dy[j] > k :
                k = dy[j]

    dy[i] = k+1

print(dy)


