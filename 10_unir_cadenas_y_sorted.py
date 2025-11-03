def longest(a1, a2):
    combined = a1 + a2
    unique_chars = set(combined)
    sorted_chars = sorted(unique_chars)
    result = ''.join(sorted_chars)
    return result

print (longest("aretheyhere", "yestheyarehere"))