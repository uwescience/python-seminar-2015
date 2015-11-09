def increment(int num, int offset):
    return num + offset

def increment_sequence(seq, offset):
    result = []
    for val in seq:
        res = increment(val, offset)
        result.append(res)
    return result
