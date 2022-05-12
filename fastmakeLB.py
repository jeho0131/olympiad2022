num = int(input())
t = list(map(int, input().split()))
lent = len(t)

ml = []
lt = 0

def makeLB(st):
    global ml, lt
    
    l = [0 for i in range(lent)]
    l[0] = int(st / t[0])
    p = 0
    for i in range(1, lent):
        p += int(st / t[i])
        l[i] = int(st / t[i])

    if num - (st / t[0]) <= p:
        if makeLB(st - t[0]):
            lt = st
            ml = l
            
    else:
        return True

def LB
    
makeLB(t[0] * num)
print(lt)
