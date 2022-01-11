def remove_even(lst):
    # Write your code here!
    for x in lst:
        # check for odd
        if (x % 2) != 0:
            # mod by 2 leaves a remainder so its odd
            lst.remove(x)
    return lst

print(remove_even([1, 2, 3, 4]))

