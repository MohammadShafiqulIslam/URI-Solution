X,Y = map(float,input().split())
if X==0.0 and Y==0.0:
    print("Origem")
elif X == 0.0 and Y != 0.0:
    print("Eixo Y")
elif X!=0.0 and Y == 0.0:
    print("Eixo X")
elif X >0.0 and Y > 0.0:
    print("Q1")
elif X>0.0 and Y<0.0:
    print("Q4")
elif X<0.0 and Y>0.0:
    print("Q2")
elif X<0.0 and Y<0.0:
    print("Q3")


'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1041-solution-Coordinates-of-a-Point.html
'''