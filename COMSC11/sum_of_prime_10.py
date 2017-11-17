def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


count = 9
x = 3
sum_of_prime = 2
while(True):
    if(is_prime(x)):
        sum_of_prime = sum_of_prime + x
        count = count - 1
        if count == 0:
            break;
    x = x + 1
print("sum of first 10 prime numbers: ", sum_of_prime)
