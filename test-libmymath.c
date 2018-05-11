#include <stdio.h>
#include "libmymath.h"
int main()
{
	int a=100,c=4;
	double b=8;
	printf("%d!= %d\n",a,GT(a));
	printf("Tong chan tu 1 den %d= %d\n",a,TC(a));
	printf("Tong le tu 1 den %d= %d\n",a,TL(a));	
	printf("%f^%d= %f\n",b,c, LT(b,c));
	return 0;
}
