n = int(input("enter the size of the set(n): "))
r = int(input("enter the size of the subset(r): "))

n_fac = 1
r_fac = 1
n_r_fac = 1

for i in range(n, 0, -1):
    n_fac = n_fac * i

for i in range(r, 0, -1):
    r_fac = r_fac * i

for i in range(n-r, 0, -1):
    n_r_fac = n_r_fac * i

c = n_fac / r_fac * n_r_fac
p = n_fac / n_r_fac

print("combination: %d \npermutation: %d " % (c, p))
