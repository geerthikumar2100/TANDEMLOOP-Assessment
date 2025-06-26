def get_odd_series(a):
    result = []
    for i in range(1, a + 1):
        if i % 2 != 0:
            result.append(i)
    return result
