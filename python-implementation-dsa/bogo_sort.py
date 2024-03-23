import random
import sys
#from load import load_numbers


def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):

    attempts = 0

    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values


numbers = [2,5,8,3,4,1,4,6]
print(bogo_sort(numbers))