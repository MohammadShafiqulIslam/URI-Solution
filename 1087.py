import sys
for line in sys.stdin:
    X1, Y1, X2, Y2 = map(int,line.split())
    if X1 + Y1 + X2 + Y2 == 0:
        break
    if X1 == X2 and Y1 == Y2:
        print("%d" % 0)
        continue
    if X1 == X2 or Y1 == Y2:
        print("%d" % 1)
        continue
    if abs(X1 - X2) == abs(Y1 - Y2):
        print("%d" % 1)
        continue
    print("%d" % 2)

//https://urisolutions.blogspot.com/2020/04/uri-problem-1087-solution-queen.html