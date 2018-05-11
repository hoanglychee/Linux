/*tongchan.c*/
#include <stdio.h>
int TC(int a)
{
	int tc=0;
	for(int i=0;i<=a;i++)
		if(i%2==0)
			tc+=i;
	return tc;
}
