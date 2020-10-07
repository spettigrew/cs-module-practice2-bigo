"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci(n):       #O(n)
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i-2] + lst[i-1])
    
    return lst[n-1]



"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci_two(n):       #O(n)
    x, y, z = 0, 1, None
    
    if n == 0:
        return x
    if n == 1:
        return y
    
    for i in range(2, n):
        z = x + y
        x, y = y, z

    return z



"""
Use Big O notation to classify the space complexity of the function below.
"""
def do_something(n):        #O(1)
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(i + j)
    
    return lst