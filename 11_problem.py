#check armstrong numbers
num=int(input("Enter your number : "))
n=len(str(num))
temp=num
sum_of_power = 0
while temp>0:
    digit= temp%10
    sum_of_power+= digit**n
    temp= temp // 10
if num==sum_of_power:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")