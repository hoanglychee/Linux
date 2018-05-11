/*luythua.c*/
#include <stdio.h>
#include <math.h>
double LT(double b, int c)
{
	double lt =1;
	int i;
	for(i=0;i<c;i++)
		lt*=b;
	return lt;
}
