#include <stdio.h>

int main()
{
	int x = 5;
	int y = 10;
	int z = x;
	float add = x + y;
	printf("$x + $y = $add");
	float sub = y - x;
	printf("$y - $x = $sub");
	float mul = y * x;
	printf("$x * $y = $mul");
	float div = y / x;
	printf("$y / $x = $div");
}