import math
x1,y1 = map(float, input().split());
x2,y2 = map(float, input().split());
x1 = math.sqrt((x2-x1)**2 + (y2-y1)**2);
print("%.4f"%x1);

'''
#https://urisolutions.blogspot.com/2020/04/uri-problem-1015-solution-distance-between-two-points.html
'''