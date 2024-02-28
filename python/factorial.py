def factorial(n):
    if n == 0:  # Basfall
        return 1
    else:
        return n * factorial(n-1)  # Rekursivt anrop

print(factorial(3))  # Beräknar fakulteten av 5
