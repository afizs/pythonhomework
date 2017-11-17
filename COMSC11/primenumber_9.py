
def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


count = 9
x = 3
print(x-1)
while(True):
    if(is_prime(x)):
        print(x)
        count = count - 1
        if count == 0:
            break;
    x = x + 1
