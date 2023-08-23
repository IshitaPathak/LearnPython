print("Enter two number")

num1 = input("number one : ")
num2 = input("number two : ")

operator = input("enter the operator : +,-,*,/,%  \n")
num1=int(num1)
num2=int(num2)
if operator == "+" :
    print(num1+num2)
elif operator == "-" :
    print(num1-num2)
elif operator == "*" :
    print(num1*num2)
elif operator == "/" :
    print(num1/num2)
elif operator == "%" :
    print(num1%num2)
else:
    print("Invalid Operation")