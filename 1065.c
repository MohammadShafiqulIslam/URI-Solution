#include <stdio.h>
 
int main() {
 
    int i,n[5],c=0;

    for(i=0; i<5; i++)
    {
        scanf("%d",&n[i]);
        if(n[i]%2==0)
        {
            c++;
        }
    }
    printf("%d valores pares\n",c);
 
    return 0;
}
//https://urisolutions.blogspot.com/2020/04/uri-problem-1065-solution-even-between-five-numbers.html