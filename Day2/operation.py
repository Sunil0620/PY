# Description: This file contains the basic operations in python
#implicit type casting

print(6 / 2) # 3.0 (float) python default float division
print(type(6 / 2)) # <class 'float'>

print(6 // 2) # 3 (int) integer division
print(type(6 // 2)) # <class 'int'>
print(5 // 3) # 1    5/3 = 1.6666666666666667  
print( 5%3 ) # 2     5%3 = 2  <remainder> modulus
print( 5** 3) # 125  5^3 = 125 <power> exponent

#priority - PEMDAS
# () -> Parentheses
# ** -> Exponent
# * / // % -> Multiplication, Division, Floor division, Modulus
# + - -> Addition, Subtraction
print(2 * 3 + 4 / 4 - 5) # 2.0
