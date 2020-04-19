T = int(input())
for i in range(T):
    ND = input().split()
    N = int(ND[0])
    D = int(ND[1])
    X = list(map(int, input().rstrip().split()))
    # print(N)
    # print(D)
    # print(X)
    r = D
    for j in range(N-1, -1, -1):
        day = X[j] * (D // X[j])
        if day <= r:
            r = day
            # print('r1', r)
        else:
            # print('reach')
            divisor = (D // X[j]) - 1
            while divisor > 0:
                # print('reach 2')
                day = X[j] * divisor
                # print('day2', day)
                if day <= r:
                    r = day
                    # print('r2', r)
                    break
                divisor -= 1
    print('Case #' + str(i+1) + ': ' + str(r))
