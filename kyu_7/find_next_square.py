def find_next_square(sq):
    sqrt = sq ** 0.5
    if sqrt.is_integer():
        return int((sqrt + 1) ** 2)
    return -1
