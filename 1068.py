while True:
    try:
        List1 = input()
        List2 = []
        correct = False
        P1 = 0
        P2 = 0
        for v in List1:
            if (v == '('):
                P1 += 1
                List2.append(v)
            if (v == ')'):
                P2 += 1
                List2.append(v)
        if(len(List2)%2 != 0):
            correct = False
        else:
            if(List2[0] == ')'):
                correct = False
            else:
                if (List2[len(List2) - 1] == '('):
                    correct = False
                else:
                    if (P1 != P2):
                        correct = False
                    else:
                        correct = True
        if(correct):
            print("correct")
        else:
            print("incorrect")
    except (EOFError):
        break

'''
https://urisolutions.blogspot.com/2020/04/uri-problem-1068-solution-parenthesis-balance-i.html
'''