def descending_order(num):
    num = str(num)
    num = list(num)
    num.sort()
    num.reverse()
    return int(''.join(num))
