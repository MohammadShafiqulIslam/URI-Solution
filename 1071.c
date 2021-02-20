#include <stdio.h>
int main() {
    int x,y,i,s=0,t;
    scanf("%d%d",&x,&y);
    if(x>y)
    {
        t = x;
        x = y;
        y = t;
    }
    for(i=x+1; i<y; i++)
    {
        if(i%2 != 0)
            s += i;
    }
    printf("%d\n",s);
    return 0;
}


'''
https://urisolutions.blogspot.com/2020/04/uri-1071-sum-of-consecutive-odd-numbers-i.html
'''