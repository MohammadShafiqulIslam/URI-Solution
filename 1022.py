def GetDivisor(X,Y):
    Divisor = Dividendo = Z = 0
    if X == 0:
        return 1
    if Y>X:
        Dividendo = Y;
        Divisor = X;
    else:
        Dividendo = X;
        Divisor = Y;
    while (Dividendo % Divisor != 0):
        Z = Dividendo % Divisor
        Dividendo = Divisor;
        Divisor = Z;

    return Divisor;

T = int(input())
while T>0:
    N1,C1, D1,C2, N2,C3, D2 = map(str,input().split())
    N1 = int(N1)
    N2 = int(N2)
    D1 = int(D1)
    D2 = int(D2)
    if C2 == '+':
        Numerator = ((N1 * D2) + (N2 * D1));
        Denominator = (D1 * D2);
    elif C2 == '-':
        Numerator = ((N1 * D2) - (N2 * D1));
        Denominator = (D1 * D2);
    elif C2=='*':
        Numerator = (N1 * N2);
        Denominator = (D1 * D2);
    else:
        Numerator = (N1 * D2);
        Denominator = (N2 * D1);

    D = GetDivisor(Numerator, Denominator)

    NumeratorSum = Numerator / D
    DenominatorSum = Denominator / D

    if NumeratorSum > 0 and DenominatorSum > 0:
        print("%i/%i = %i/%i"%(Numerator, Denominator, NumeratorSum, DenominatorSum))
    else:
        if DenominatorSum < 0:
            DenominatorSum = -DenominatorSum;
            NumeratorSum = -NumeratorSum;

        print("%i/%i = %i/%i"%(Numerator, Denominator, NumeratorSum, DenominatorSum))

    T-=1

'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1022-solution-tda-rational.html
'''