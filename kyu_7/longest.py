def longest(a1, a2):
    given = [a1, a2]
    result = []
    for g in given:
        for s in g:
            if s not in result:
                result.append(s)
    result.sort()
    return ''.join(result)


a = "inmanylanguages"
b = "theresapairoffunctions"
print(longest(a, b))
