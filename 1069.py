T = int(input())
while T>0:
    Str = input()
    Count = 0
    Sign = 0
    for i in Str:
        if (i == "<"):
            Sign += 1
        if (i == ">" and Sign > 0):
            Count += 1
            Sign -= 1
    print(Count)
    T-=1

'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1069-solution-diamonds-and-sand.html
'''