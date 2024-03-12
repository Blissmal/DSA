#include <stdio.h>

int binary_search(int list[], int length, int target) {
    int first = 0;
    int last = length - 1;

    while (first <= last) {
        int midpoint = (first + last) / 2;

        if (list[midpoint] == target) {
            return midpoint;
        } else if (list[midpoint] < target) {
            first = midpoint + 1;
        } else {
            last = midpoint - 1;
        }
    }
    return -1;
}

void verify(int index) {
    if (index != -1) {
        printf("Target found at index: %d\n", index);
    } else {
        printf("Target not found in the list\n");
    }
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int length = sizeof(numbers) / sizeof(numbers[0]);
    int target = 6;

    int result = binary_search(numbers, length, target);
    verify(result);

    return 0;
}
