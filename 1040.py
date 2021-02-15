A,B,C,D = map(float,input().split())
A = (A*2+B*3+C*4+D*1)/10
print("Media: %.1f"%A)
if A>=7.0:
    print("Aluno aprovado.")
elif A<5.0:
    print("Aluno reprovado.")
elif A>=5.0 and A<7.0:
    print("Aluno em exame.")
    N = float(input())
    print("Nota do exame: %.1f"%N)
    N = (A+N)/2
    if N>=5.0:
        print("Aluno aprovado.")
        print("Media final: %.1f"%N)
    else:
        print("Aluno reprovado.")
        print("Media final: %.1f"%N)


'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1040-solution-average-3.html
'''