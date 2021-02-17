#include <stdio.h>
 
int main() {
 
    int start,end;
    scanf("%d%d",&start,&end);
    if(start>=end)
        end+=24;
    start = end - start;
    printf("O JOGO DUROU %d HORA(S)\n",start);
 
    return 0;
}

//https://urisolutions.blogspot.com/2020/04/uri-problem-1046-solution-Game-Time.html