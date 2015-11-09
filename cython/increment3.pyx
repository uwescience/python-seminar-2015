cpdef int increment_either(int num, int offset):
    return num + offset
def fast_increment_sequence(seq, offset):
    result = []
    for val in seq:
        res = increment_either(val, offset)
        result.append(res)
    return result
