#include <stdio.h>
 
int main() {
 
    int num[5],e,o,p,n,i;
    e = o = p = n = 0;
    for(i=0; i<5; i++)
    {
        scanf("%d",&num[i]);
        if(num[i]%2 == 0)
            e++;
        else
            o++;

        if(num[i]>0)
            p++;
        else if(num[i]<0)
            n++;
    }
    printf("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)\n",e,o,p,n);
    
     return 0;
}
//https://urisolutions.blogspot.com/2020/04/uri-problem-1066-solution-even-odd-positive-and-negative.html