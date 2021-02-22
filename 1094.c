#include <stdio.h>
int main() {
    int T,sum,frog,rat,rabbits;
    sum = frog = rat = rabbits = 0;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        char a;
        scanf("%d %c",&n,&a);
        sum += n;
        if(a=='C')
            rabbits += n;
        else if(a=='R')
            rat += n;
        else if(a=='S')
            frog += n;
    }
    printf("Total: %d cobaias\nTotal de coelhos: %d\nTotal de ratos: %d\nTotal de sapos: %d\n",sum,rabbits,rat,frog);
    printf("Percentual de coelhos: %.2f %%\n",((float)(rabbits)/(float)(sum))*100);
    printf("Percentual de ratos: %.2f %%\n",((float)(rat)/(float)(sum))*100);
    printf("Percentual de sapos: %.2f %%\n",((float)(frog)/(float)(sum))*100);
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1094-solution-experiments.html