#Find the largest  digit in a number
number=int(input("Enter your numbers : "))
max_digit=0
while number>0:
    digit=number%10
    max_digit=digit
    number=number//10
print("The largest digit is : ",max_digit)
