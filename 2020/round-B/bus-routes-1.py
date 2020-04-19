T = int(input())
for i in range(T):
    ND = input().split()
    N = int(ND[0])
    D = int(ND[1])
    X = list(map(int, input().rstrip().split()))
    r = D
    for j in range(N-1, -1, -1):
        day = X[j] * (r // X[j])
        if day <= r:
            r = day
    print('Case #' + str(i+1) + ': ' + str(r))
