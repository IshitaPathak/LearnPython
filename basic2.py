# strings

name = "Ishita Pathak"

# to print string in upper case and lower case
print(name.lower())
print(name.upper())

# to search any character or substring in a string
print(name.find('S'))
print(name.find("Patha"))

print(name.replace("Ishita", "Manas"))
print(name)

# checks whether a character or substring exits in a string 
# .find gives the index , this gives true or false 
print("pathak" in name)
print("Ishita" in name)

# arthematic operations
print(5+2)
print(5-2)
print(5*2)
print(5/2)

# if we dont want value after integer in decimal then we put // in place of /
print(5//2)

print(5%2)

# 5 to the power 2 
print(5**2)

# logical operator
print(2>3 or 6<7)
print(2>4 and 5<6)

print(not 4>9)
#  yha pe 4 is greater than 9 ka output aana chaiye false but
#  uske aage hamne not laga diya to output true aaega

# if-else statement 
#  note - indentation is important we dont use curly braces
age = 5


if age >=18:
  print("you are an adult")
  print("you can vote")
elif age<18 and age>4:
  print("you are in school")
else:
  print("you are a child")

print("thankyou")