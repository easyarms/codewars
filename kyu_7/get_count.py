def get_count(sentence):
    count = []
    for s in sentence:
        if s in 'aeiou':
            count.append(s)
    return len(count)
