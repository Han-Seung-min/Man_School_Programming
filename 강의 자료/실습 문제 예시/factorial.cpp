#include <stdio.h>

int main(void)
{
	int i, num;
	int result = 1;

	printf("입력:");
	scanf_s("%d", &num);

	for (i = 1; i <= num; i++)
	{
		result *= i;
	}

	printf("결과: %d", result);

	printf("\n\n");
	return 0;
}