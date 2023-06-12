def narcissistic(value):
    result = 0
    value = str(value)
    e = len(value)

    for i in value:
        result += int(i) ** e
    return result == int(value)