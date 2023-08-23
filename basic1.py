first = input("enter first number : ")
second = input("enter second number : ")
# sum = first + second
# print(sum)

# In the above code, it treats the both input as string so we have to typecast it
sum = int(first) + int(second)
print("the sum is : " + str(sum))


# range(5) 0,1,2,3,4,5
numbers = range(8)
print(numbers)

for item in range(7):
    print(item)


# loops
i=1
while i<=5:
    print(i)
    i=i+1

marks = [43,43,34,54]
print(marks[-2]) # minus means piche se ginti suru kr rhe hai

# if you want only first two element then
print(marks[0:2]) #here (last index) which is index two is not included


# for loop
for score in marks:
    print(score)

marks.append(99) #append se hm list ke last me kuch add kr pate hai
# marks = [43,43,34,54,99]

marks.insert(0,99) #marks.insert(index,what you want to add)
print(marks)

# checks whether marks 99 is present in marks list
print(99 in marks)

# lenght of marks list
print(len(marks))


# while loops
i=0
while i <len(marks):
    print(marks[i])
    i=i+1

# .clear remove the all the elements in list
marks.clear()
print(marks)