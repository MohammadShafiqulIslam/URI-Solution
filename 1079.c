#include <stdio.h>
int main() {
    int T;
    float n1,n2,n3;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%f%f%f",&n1,&n2,&n3);
        n1 *= 2;
        n2 *= 3;
        n3 *= 5;
        n1 = (n1+n2+n3)/10;
        printf("%.1f\n",n1);
    }
    return 0;
}