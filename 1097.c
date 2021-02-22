#include <stdio.h>
int main() {
    int i,j,p=7,q=5;
    for(i=1; i<=9; i+=2)
    {
        for(j=p; j>=q; j--)
        {
            printf("I=%d J=%d\n",i,j);
        }
        p+=2;
        q+=2;
    }
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1097-solution-sequence-ij-3.html