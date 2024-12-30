from random import randint
n = int(input("N:"))
n_simple = True
lst = []

def nearest_simple_num():
    flag = 0 
    for i in range(2, n - 1):
        pass

if n != 1:
    for i in range(2,n-1):
        if(n/i).is_integer():
            n_simple = False
print(n, n_simple)