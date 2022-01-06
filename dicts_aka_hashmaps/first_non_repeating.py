def first_non_repeating(str):
    h = {}
    # we now have the non repeating elements 
    for idx, letter in enumerate(str):
        if letter in h:
            h.pop(letter)
        h[letter] = idx
        print(h)
    return next(iter(h))


s = "hello"
print(first_non_repeating(s))