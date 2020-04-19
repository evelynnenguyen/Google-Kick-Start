T = int(input())
for i in range(T):
    N = int(input())
    H = list(map(int, input().rstrip().split()))
    # print('N', N)
    # print('H', H)
    count = 0
    for j in range(1, N-1):
        if H[j] > H[j-1] and H[j] > H[j+1]:
            count += 1
    print('Case #' + str(i+1) + ': ' + str(count))
