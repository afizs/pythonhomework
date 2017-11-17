# factorial program
num = int(input("enter the number: "))

fact = 1
if(num > 0):
    for i in range(num, 0, -1):
        fact = fact * i

print("factorial of %d is: %d"%(num, fact))
