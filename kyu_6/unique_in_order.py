def unique_in_order(sequence):
    result = []
    if len(sequence) != 0:
        result = [sequence[0]]
        for s in sequence:
            if s == result[-1]:
                continue
            result.append(s)

    return result
