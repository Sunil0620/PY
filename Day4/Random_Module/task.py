import random
import my_module

# print(my_module.my_fav_color)
random_integer = random.randint(1, 10) #randint() method
print(random_integer)

#random module generates a random float number between 0.0000000 and 0.9999999(random()method)
random_float = random.random() * 5 # 0.0000000 - 4.9999999  
print(random_float)

#random.uniform() method
random_float = random.uniform(1, 10) 
print(random_float)

random_head_tail = random.randint(0, 1)
if random_head_tail == 0:
    print("Heads")
else:
    print("Tails")

#random.choice() method
names = ["Jack", "Jill", "John", "James", "Jessica"] #list
random_name = random.choice(names) 
print(random_name)
