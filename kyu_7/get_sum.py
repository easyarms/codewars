def get_sum(a, b):
    counter = 0
    if a == b:
        return a
    if a < b:
        for i in range(a, b+1):
            counter += i
    else:
        for i in range(b, a+1):
            counter += i
    return counter


print(get_sum(0, -1))
