import math
try:
    N = int(input("Введите число пространств: " ))
    A = []
    for i in range(N):
        A.append(int(input("введите координату точки А: ")))
    B = []
    for i in range(N):
        B.append(int(input('введите координату точки В: ')))
    print(A, B)

    x = 0
    dist = 0
    while (N - 1) != x:
        dist = dist + math.sqrt((B[x]- A[x])**2)
        x = x + 1
    print(round(dist, 3))
except:
    print('Введите числа')
