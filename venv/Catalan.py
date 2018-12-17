def factorial(n):
    value = 1
    for p in range(1,n+1):
        value = value*p
    return value


print(factorial(5))