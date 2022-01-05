def is_palindrome(arr):
    rev = ''
    for i in range(len(arr)-1, -1, -1):
        rev += arr[i]
        print(rev)
    if rev == arr:
        return True
    else:
        return False

s = "elle"
print(is_palindrome(s))

def palindrome_permutation(str):
    freq = {i : 0 for i in str}
    for i in str:
        freq[i] += 1
    # now we have a dictionary containing all letters in the string, and the total frequence of each letter's occurance.
    # the rules are as follows
    # there can only be one letter which an odd frequency. if there is more than one letter with odd frequency a palindrome is impossible.
    # there can be only even frequencies and a palindrome will be valid, for example a:2, b:2 = abba or baab
    # we can create a list of all even and all odd members of the dict.
    #even = [x for x in str if freq[x] % 2 == 0]
    odd = [x for x in str if freq[x] % 2 > 0]
    if len(odd) > 1:
        return False
    return True

s1 = "eellab"
print('permutation exist: ', palindrome_permutation(s1))