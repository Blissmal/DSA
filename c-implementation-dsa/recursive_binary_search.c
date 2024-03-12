#include <stdio.h>

int recursive_binary_search(int list[], int start, int end, int target) {
    if (start > end) {
        return 0; // False
    } else {
        int midpoint = (start + end) / 2;

        if (list[midpoint] == target) {
            return 1; // True
        } else {
            if (list[midpoint] < target) {
                return recursive_binary_search(list, midpoint + 1, end, target);
            } else {
                return recursive_binary_search(list, start, midpoint - 1, target);
            }
        }
    }
}

void verify(int result) {
    if (result) {
        printf("Target found.\n");
    } else {
        printf("Target not found.\n");
    }
}

int main() {
    int numbers[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int length = sizeof(numbers) / sizeof(numbers[0]);

    int result = recursive_binary_search(numbers, 0, length - 1, 12);
    verify(result);

    result = recursive_binary_search(numbers, 0, length - 1, 6);
    verify(result);

    return 0;
}
