#kickstart round B

import sys

def no_duplicates(listObj):
    return len(listObj) == len(set(listObj))

def canMakePalindrom(li):
    dup_list = []
    repeat_count = []
    count = 0
    for item in li:
        if item not in dup_list:
            dup_list.append(item)
    for item1 in dup_list:
        repeat_count.append(li.count(item1))
    for i in range(len(repeat_count)):
        if repeat_count[i] % 2 == 1:
            count += 1
    if count > 1:
        return False
    else:
        return True         

t = int(input())

for j in range(t):
    n, q = input().split()
    n = int(n)
    q = int(q)
    uppercase_str = input()
    str_li = list(uppercase_str)
    
    if len(str_li) == 1:
        print("Case #" + str(j + 1) + ":" + str(q))
    elif no_duplicates(str_li):
        print("Case #" + str(j + 1) + ": 0")
    else:
        count = 0
        for i in range(q):
            li, ri = input().split()
            li = int(li)
            ri = int(ri)
            li -= 1
            if canMakePalindrom(str_li[li:ri]):
                count += 1
        print("Case #" + str(j + 1) + ": " + str(count))
            
