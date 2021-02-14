S = int(input())
H = int(S/(60*60))
S = S%(60*60)
M = int(S/60)
S = S%60
print("%d:%d:%d"%(H,M,S))

'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1019-solution-time-conversion.html
'''