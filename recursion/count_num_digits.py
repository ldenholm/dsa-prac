def count_num_digits(num):
    #n  = 99999
    #Output: 5
    print('init val of num', num)
    len = 1
    # if num == 0:
    #     return len + 1
    if num < 10:
        return 1
    
    else:
        return count_num_digits(num//10) + (len)


n = 999
print(count_num_digits(n))
# print(999//10)
# print(99 // 10)
# print(9//10)