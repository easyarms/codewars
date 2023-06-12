def unique_in_order(sequence):
    result = [sequence[1]]

    for s in sequence:
        if s == result[-1]:
            continue
        result.append(s)
    return result
