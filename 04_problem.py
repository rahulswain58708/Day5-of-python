#Q1.Reverse a number(e.g.input-1,2,3,4-output:4,3,2,1)
num=int(input("Enter your numbers : "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Output
print("Reversed number:", reversed_num)
