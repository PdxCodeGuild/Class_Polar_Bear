# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled

def double_numbers(nums):
    doubled_nums = []
    for number in nums:
        number *= 2
        doubled_nums.append(number)
    return doubled_nums


def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]

test_double_numbers()
# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    return '*' * n

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'

test_stars()
# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    less_than_10 = []
    for num in nums:
        if num < 10:
           # remove num from nums
           less_than_10.append(num) 
           # add num to new list
    return less_than_10 

def test_extract_less_than_ten(nums):
    extract_less_than_ten([2, 8, 12, 18]) == [2, 8]

print(extract_less_than_ten([2, 8, 12, 18])) # True