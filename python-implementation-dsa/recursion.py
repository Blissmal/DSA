def sum(numbers):
    if not numbers:
        return 0
    # total = 0
    # for number in numbers:
    #     total += number
    # return total
    print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum(numbers[1:])
    print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum([1,2,7,9]))