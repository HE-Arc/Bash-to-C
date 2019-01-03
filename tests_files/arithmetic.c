#include <stdio.h>

int main()
{
	int x = 5;
	int y = 10;
	int z = x;
	float add = x + y;
	printf("%d + %d = %d",5,10,x + y);
	float sub = y - x;
	printf("%d - %d = %d",10,5,y - x);
	float mul = y * x;
	printf("%d * %d = %d",5,10,y * x);
	float div = y / x;
	printf("%d / %d = %d",10,5,y / x);
}