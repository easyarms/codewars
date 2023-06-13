def xo(s):
    s = s.lower().strip()
    if 'x' or 'o' in s:
        return s.count('x') == s.count('o')
    return False
