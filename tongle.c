/*tongle.c*/
#include <stdio.h>
int TL(int a)
{
	int tl=0;
	for(int i=0;i<=a;i++)
		if(i%2!=0)
			tl+=i;
	return tl;
}
