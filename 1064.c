#include <stdio.h>
 
int main() {
 
   int i,c=0;
    float n[6],t=0;
    for(i=0; i<6; i++)
    {
        scanf("%f",&n[i]);
        if(n[i]>=0)
        {
            t += n[i];
            c++;
        }

    }
    printf("%d valores positivos\n%.1f\n",c,t/c);
 
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1064-solution-Positives-and-Average.html