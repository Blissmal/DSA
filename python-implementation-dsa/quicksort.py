import sys

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    

numbers = [4,6,3,2,9,7,3,5]
print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)