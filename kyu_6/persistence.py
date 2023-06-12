def persistence(n):
    counter = 0
    while n > 9:
        digit = 1
        n = str(n)
        for i in n:
            digit *= int(i)
        n = digit
        counter += 1
    return counter
