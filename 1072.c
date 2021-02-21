#include <stdio.h>
int main() {
    int T,num,in,out;
    in = out = 0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&num);
        if(num>=10 && num <= 20)
            in++;
        else
            out++;
    }
    printf("%d in\n%d out\n",in,out);
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1072-solution-Interval-2.html