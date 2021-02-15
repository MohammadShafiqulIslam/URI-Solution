A,B,C = map(float,input().split())
if (A+B)>C and (A+C)>B and (B+C)>A:
    A = (A+B+C)
    print("Perimetro = %.1f"%A)
else:
    A = 0.5*(A+B)*C
    print("Area = %.1f"%A)

'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1043-solutrion-triangle.html
'''