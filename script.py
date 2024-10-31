
from math_mod import add, subtract, multiply, divide
from string_mod import concatenate, create_string_from_list, has_digit

# Test math functions
print("Result of adding 4 and 17 is", add(4, 17))
print("Result of subtracting 33 and 19 is", subtract(33, 19))
print("Result of multiplying 3 and 23 is", multiply(3, 23))
print("Result of dividing 44 by 3 is", divide(44, 3))

# Test string functions
print("Result of concatenation of 'Hello' and 'DCI' is", concatenate('Hello', 'DCI'))
print("Result of creating string from list ['Hello', 'DCI'] is", create_string_from_list(['Hello', 'DCI']))

test_string = 'HelloDCI007'
print("There is a digit in your string!" if has_digit(test_string) else "There is no digit in your string!")
print("Result of checking digits in the string", repr(test_string), "is", has_digit(test_string))
