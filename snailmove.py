x, y = map(int, input().split())
path = set(())

def snail(sx, sy, d):
    global path
    
    if d == 0:
        if sx + 1 >= x or (sy, sx+1) in path:
            print("(",sy+1,",",sx,")")
            path.add((sy+1,sx))
            if (sy+1, sx) not in path and sy + 1 < y:
                snail(sx, sy+1, d+1)
        else:
            print("(",sy,",",sx+1,")")
            path.add((sy,sx+1))
            snail(sx+1, sy, d)

    elif d == 1:
        if sy + 1 >= y or (sy+1, sx) in path:
            print("(",sy,",",sx-1,")")
            path.add((sy,sx-1))
            if (sy, sx-1) not in path and sy + 1 < y:
                snail(sx, sy+1, d+1)
        else:
            print("(",sy,",",sx+1,")")
            path.add((sy,sx+1))
            snail(sx+1, sy, d)
