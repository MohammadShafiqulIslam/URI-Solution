from bisect import bisect_left
def GetPosition(Num, arr):
    index = (bisect_left(arr, Num))

    if index < len(arr) and arr[index] == Num:
       return index + 1
    else:
       return -1

Case = 1
while True:
    N, Q = list(map(int, input().split()))
    if N == 0 and Q == 0:
        break

    print("CASE# %d:" % Case)
    Case += 1
    List1 = []
    for i in range(N + Q):
        if i < N:
            List1.append(int(input()))

        if i == (N - 1):
            List1.sort()

        if i >= N:
            Qvalue = int(input())
            Position = GetPosition(Qvalue, List1)

            if Position == -1:
                print(str(Qvalue) + " not found")
            else:
                print(str(Qvalue) + " found at " + str(Position))


'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1025-solution-where-is-the-marble.html
'''