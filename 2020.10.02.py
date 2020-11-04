n = 10

ml = [0, 4, 1, 2, 3, 9, 7, 5, 6, 10, 8]
dy = [0] * (n+1)

dy[1] = 1

for i in range(1, n+1) :
    k = 0
    for j in range(1, i+1) :
        if ml[i] > ml[j] :
            if k < dy[j] :
                k = dy[j]
    dy[i] = k+1

print(max(dy))