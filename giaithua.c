/*giaithua.c*/
#include <stdio.h>
int GT(int a)
{
	int gt=1;
	for(int i=1;i<=a;i++)
		gt*=i;
	return gt;		
}
