#include <stdio.h>

int main()
{
	int x = 5;
	int y = 10;
	int z = x;
	float add = x + y;
	printf("%d + %d = %d",x,y,add);
	float sub = y - x;
	printf("%d - %d = %d",y,x,sub);
	float mul = y * x;
	printf("%d * %d = %d",x,y,mul);
	float div = y / x;
	printf("%d / %d = %d",y,x,div);
}
