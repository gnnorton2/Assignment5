def FibonacciConversion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise ValueError("Invalid number (negative number)")
    else:
        x = 0
        y = 1
        for i in range(1, n):
            z = x + y
            x = y
            y = z
        return y




