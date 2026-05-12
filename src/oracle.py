def oracle_linear_search(v, key):
    try:
        return v.index(key)
    except ValueError:
        return -1