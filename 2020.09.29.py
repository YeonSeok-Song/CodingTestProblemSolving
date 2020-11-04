n = 7
a = 0
b = 1

for i in range(1, n+2) :
    temp = b
    b = b + a
    a = temp
    print(a, b)

print(b)



