#Google Kick Start round A

import sys

#t is the number of test cases
t = int(input())
for j in range(t):
    k_list = []
    #n: the number of seats, q: the number of bookings
    n, q = [int(x) for x in input().split()]
    n_list = [x for x in range(1, n+1)]
    l_list = []
    r_list = []
    diff_list = []
    k = 0
    for i in range(q):
        #l, r: the i-th booking all seats from l-i to r-i
        l,r = [int(y) for y in input().split()]
        if 1 <= l <= n and 1 <= r <= n:
            l_list.insert(i, l)
            r_list.insert(i, r)

    for diff_i in range(len(l_list)):
        diff_list.insert(diff_i, abs(l_list[diff_i] - r_list[diff_i]))

    for list_j in range(len(diff_list)):
        if n_list !=[]:
            for list_i in range(len(diff_list)):
                if abs(l_list[list_i] - r_list[list_i]) == min(diff_list):
                    if l_list[list_i] < r_list[list_i]:
                        for booked_item in range(l_list[list_i], r_list[list_i] +1):
                            if booked_item in n_list:
                                n_list.remove(booked_item)
                                k += 1
                        k_list.append(k)
                        k = 0
                    elif l_list[list_i] > r_list[list_i]:
                        for booked_item in range(r_list[list_i], l_list[list_i] +1):
                            if booked_item in n_list:
                                n_list.remove(booked_item)
                                k += 1
                        k_list.append(k)
                        k = 0
                    elif  l_list[list_i] == r_list[list_i]:
                        booked_item = l_list[list_i]
                        if booked_item in n_list:
                            n_list.remove(booked_item)
                            k += 1
                        k_list.append(k)
                        k = 0
                    diff_list = [e for e in diff_list if e not in [abs(l_list[list_i] - r_list[list_i])]]
    print("Case #{0}: {1}".format(j + 1, min(k_list), flush = True))
