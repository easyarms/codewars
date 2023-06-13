def is_isogram(string):
    isogram = []
    for s in string.lower():
        if s not in isogram:
            isogram.append(s)
        else:
            return False
    return True
