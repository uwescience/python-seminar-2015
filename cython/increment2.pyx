cdef int fast_increment(int num, int offset):
    return num + offset

def fast_increment_sequence(seq, offset):
    result = []
    for val in seq:
        res = fast_increment(val, offset)
        result.append(res)
    return result
