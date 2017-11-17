# 2. Find the product of the first 10 odd numbers.
product_of_odd = 1
count = 10
i = 1
while True:
    if i%2!=0:
        product_of_odd = i * product_of_odd
        count = count - 1
        if count == 0:
            break
    i = i + 1

print("Product of first 10 odd numbers: ", product_of_odd)
