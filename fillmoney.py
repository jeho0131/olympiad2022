'''bill = [1,2,5,10,20,50]
numof = 0

def money(m, bn):
    global numof
    
    if bn < 0:
        if m == 0:
            numof += 1
    else:
        if bill[bn] < m:
            for k in range(0, int(m/bill[bn])+1):
                money(m - bill[bn]*k, bn - 1)
            
money(100, 5)
print(numof)'''
bill = [1,2,3]
numof = 0
s = 10

def money(m, bn):
    global numof
    
    if bn < 0:
        if m == 0:
            numof += 1
    else:
        if bill[bn] < m:
            for k in range(0, int(m/bill[bn])+1):
                money(m - bill[bn]*k, bn - 1)
            
money(s, 2)
print(numof)
