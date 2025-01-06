len("Hello") # 5

#type() function : Returns the type of the object

print(type(6/3)) # <class 'float'>
print(type(6+3.0)) # <class 'float'>
print(type(6//3)) # <class 'int'>
print(type(123456789)) # <class 'int'>
print(type("6" + "3")) # <class 'str'>
print(type("123" * 3)) # <class 'str'>
print(type("6" + 3)) # Error
print(type(6/3 == 2)) # <class 'bool'>
print(type(6/3 == 2.0)) # <class 'bool'>
print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>

#type casting (conversion) : Changing the type of the object

print(int(3.14)) # 3   : Truncates the decimal part
print(int("3")) # 3    : Converts the string to integer

int()
float()
str()
bool()

print("Numbers of letter in your name: " + str(len(input("What is your name? "))))
#            "str"                       + converted to string = "str"
value = 4
value -= 3.14
print(value) # 0.859999999999
print(round(value)) # 1
print("the value is : " + value) # Error
print("the value is : " + str(value)) # the value is : 0.8599999999999   

#round function : Rounds the number to the nearest integer
print(round(3.14)) # 3
print(round(3.54)) # 4
