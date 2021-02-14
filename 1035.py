A,B,C,D = map(int,input().split())
if B>C and D>A:
    if C+D>A+B:
        if C>=0 and D>=0:
            if A%2==0:
                print("Valores aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")

'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1035-solution-Selection-test-1.html
'''