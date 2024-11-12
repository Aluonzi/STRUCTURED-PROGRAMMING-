#prog that finds largest number witout using max() function

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
#
    return largest

numbers = [20, 2, 3, 35, 5, 80,10]
print(find_largest(numbers))