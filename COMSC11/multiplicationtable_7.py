# This program print multiplication table in the below format. 
# =================
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10
# =================

till = int(input("enter the number[till which you want to pring multiplication table]: "))
for i in range(1, till+1):
    print("=================")
    for j in range(1, 11):
        print("%d x %d = %d"%(i, j, i*j))
