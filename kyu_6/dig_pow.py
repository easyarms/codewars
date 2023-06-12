def dig_pow(n, p):
    n = str(n)
    result = 0
    for i in n:
        tmp = int(i) ** p
        p += 1
        result += tmp
    is_k = result % int(n)
    if is_k == 0:
        return result // int(n)
    return -1
