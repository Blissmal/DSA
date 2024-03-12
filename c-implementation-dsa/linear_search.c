#include <stdio.h>

int linear_search(int array[], int n, int target)
{
    for (int i = 0; i < n; i++)
    {
        if (array[i] == target)
        {
            return i;
        }
    }
    return -1;
}

void verify(int index)
{
    if (index != -1)
    {
        printf("Target found at index %d\n", index);
    }else
    {
        printf("Target not found\n");
    }
}

int main(void)
{
    int array[] = {1,2,3,4,5,6,7,8,9,10};
    int n = sizeof(array) / sizeof(array[0]);

    // line 29 takes the total size of elemnts of the array in bytes then divide by bytes of a single element

    int result = linear_search(array, n, 10);
    verify(result);
    return 0;
}
