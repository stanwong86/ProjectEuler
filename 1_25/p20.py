def factorial(n):
    product = 1
    for i in range(1,n+1):
        product *= i
    print sum(int(digit) for digit in str(product))
    
factorial(100)
