import time
import random

# why do we have big o notation?
# To evaluate performance
# to find out the time it takes to complete a function (relative to other input sizes)
# different computers run at different speeds
# because we care about efficiency
# O(n) -- linear
# O(n^2) -- quadratic
# O(1) -- constant -- the performance doesn't change regardless of input
# O(log n) -- logarithmic -- every time we double the input size, we only add one extra step
# O(2^n) -- exponential
# O(n!) factorial -- as the input size increases, the runtime will grow astronomically, even with relatively small inputs. The solution is exceptionally inefficient.
# O(n log n) -- linearithmic


"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""
def number_of_steps(num):
    # overall: O(log n)
    # O(1) + O(log n * c) --> O(c log n + 1) --> O(log n)
    steps = 0                  # constant O(1)
    while num > 0:             # how many times does the loop run? log n times
        if num % 2 == 0:       # code w/in the loop is constant
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps
#
# for i in [8, 16, 32, 64]:
#     print(f"number_of_steps | N: {i} \tsteps: {number_of_steps(i)}")




"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def sorted_squares(A): 
    # overall runtime complexity? 0( 4 N + 5) --> 0(n)
    N = len(A)                  # 0(1)
    j = 0                       # 0(1)
    while j < N and A[j] < 0:   # how many times does this loop run? at most N times -- 0(N)
        j += 1                  # 0(1)
    i = j - 1                   

    ans = []                    # 0(1)
    while 0 <= i and j < N:     # how many times does this loop run? At most N -- 0(N)
        if A[i]**2 < A[j]**2:   # 0(1)
            ans.append(A[i]**2) # appending to the end of the list is usually constant
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1

    while i >= 0:               # how many times does this loop run? At most N -- 0(N)
        ans.append(A[i]**2)     # 0(1) --> constant
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans

for i in [100, 1000, 10000]:
    a = [j for j in range(-i // 2, i // 2)]
    start = time.time()
    sorted_squares(a)
    end = time.time()
    print(f"Sorted Squares | N: {i} \ttime: {end - start}")


"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""
def insertion_sort(arr):
    # O(n*n) --> O(n^2)
    for i in range(1, len(arr)):    # O(n)
        key = arr[i]                # O(1)
        j = i - 1                   # O(1)
        while j >= 0 and key < arr[j]:  # at most N --> O(n)
            arr[j + 1] = arr[j]     # O(1)
            j -= 1                  # O(1)
            for k in range(len(arr)):
                # this makes it O(n^3)
                # do stuff
                   arr[j + 1] = key
print("-------")
for i in [100, 1000, 10000]:
    a = [random.randint(0, j) for j in range(i)]
    start = time.time()
    insertion_sort(a)
    end = time.time()
    print(f"insertion_sort | N: {i} \ttime: {end - start}")