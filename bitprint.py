num = int(input())

def p(l):
    if len(l) == num:
        print(l)
    else:
        p(l + [0])
        p(l + [1])

p([])
