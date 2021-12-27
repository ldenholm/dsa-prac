def isPalindrome(x: int) -> bool:
    # lets convert int into string list
    print(x)
    l = [int(i) for i in str(x)]
    new = ""
    for i in range(len(l)):
        new += str(l.pop())
        print(new)
    return int(new) == x 

print(isPalindrome(121))