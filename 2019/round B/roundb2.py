#roundb2

t = int(input())

def sortStones(a_list):
    return (-a_list[1], a_list[0], a_list[2])

for m in range(t):
    n = int(input())
    a_list = []
    for i in range(n):
        si, ei, li = input().split()
        si = int(si)
        ei = int(ei)
        li = int(li)
        a_list.append([si,ei,li])
    
    a_list = sorted(a_list, key = sortStones)
    print(a_list)
    total_en = 0

    flag = True
    while flag:
        for j in range(len(a_list)-1):
            total_en += a_list[j][1]
            for k in range(j+1, len(a_list),1):
                a_list[k][1] -= a_list[k][2] * a_list[j][0]
            if a_list[j+1][1] <= 0:
                flag = False
        if a_list[len(a_list) - 1][1] > 0:
            total_en += a_list[len(a_list) - 1][1]
    print(total_en)
        
            
    
        
        
    
