# 1. Find the sum of the first 30 even numbers.
sum_of_even = 0
count = 30
i = 1
while True:
    if i%2==0:
        sum_of_even = i + sum_of_even
        count = count - 1
        if count == 0:
            break
    i = i + 1

print("Sum of first 30 even numbes: ", sum_of_even)
