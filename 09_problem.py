#fibonic series
n=int(input("Enter The number: "))

a,b=0,1
count=0

print("fibonic series")

while count < n:
    print(a, end=" ")
    a,b=b,a+b
    count +=1