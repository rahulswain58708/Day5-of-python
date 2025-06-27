#Find factorial
num=int(input("Enter a number : "))

if num<0:
    print("Factorial is not defined for negative number")
else:
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    print("factorial of",num, "is:",factorial)