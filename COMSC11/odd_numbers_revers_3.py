# 3. Write a for loop that prints all odd numbers from 1 through which user indicate in reverse order.

n = int(input("enter the number: "))

for i in range(n, 0, -1):
    if i % 2 !=0:
        print(i)
