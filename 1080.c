#include <stdio.h>
int main() {
   int n[100],i,m,p;
    for(i=0; i<100; i++)
    {
        scanf("%d",&n[i]);
        if(i==0)
        {
            m = n[i];
            p = i;
        }
         else
        {
            if(m<n[i])
            {
                m = n[i];
                p = i;
            }
        }
    }
    printf("%d\n%d\n",m,p+1);
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1080-solution-highest-and-position.html