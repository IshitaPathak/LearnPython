# python is case sensitive language
print("hello world")


# types of bool
name = "Ishita" # string
age = 22 # integer
price = 434.9 # float
is_adult = True # bool
is_adult = False

print(is_adult)
print(name)

# input
old_age =  input("What is your age?")
# new_age = old_age + 2
# print(new_age)

# in the above code it is taking old_age as a string so it will give 
# type error: can concatenate only string , so we have to do type convesion


# In python3 when you are taking input form the user it takes the input as a string 
# regardless of whether you enter an integer or any other datatype
# type convesion
new_age = int(old_age) + 2 # so here old_age is now converted into integer
print(new_age)


number = 18
print(float(number))
print(float(43))

