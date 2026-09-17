def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b):
        return -1
    n = len(a)
    k = len(b)
    m = len(b[0])

    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            sum_ = 0
            for l in range(k):
                sum_ += a[i][l] * b[l][j]
            c[i][j] = sum_
    
    return c