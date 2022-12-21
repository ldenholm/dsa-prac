# Hash map strategies:

*Given an array of strings strs, group the anagrams together.*

For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]].

- sort the strings and store as keys in a hash map.
- append each unsorted string to its corresponding sorted key.
- return the hashmap.values()
---
*Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.*

- essentially we need to find the shortest distance between two elements of the same identity.
- create a hashmap to track the index (location) of each item.
- the item will be the hashmap key and the indexes form the values.
- this can be improved to O(n) space complexity for the worst case if we only store the previous
index for each key (rather than storing a list of indexes for each key).
---

*Given an array of integers nums, find the maximum value of nums[i] + nums[j], where nums[i] and nums[j] have the same digit sum (the sum of their individual digits). Return -1 if there is no pair of numbers with the same digit sum.*

- define a function to determine digit sum:
  ```py
  getdigitsum(n):
    digit_sum = 0
    while(n):
        digit_sum += n % 10
        num //= 10
    return digit_sum
  ```

- iterate through nums[] and populate keys of hashmap
with the digit_sums.
- for each element in nums[] append num to a list of 
its corresponding digit sum key in hashmap.
- for each member in the hashmap having > 1 entries,
sort it in desc (reverse=true) then
return max(ans, curr[0] + curr[1]).
- the above algorithm can be improved by only storing
the most recent entry for each digit_sum rendering the
sort() useless.
```py
for num in nums:
    digit_sum = get_digit_sum(num)
    if digit_sum in dic:
        ans = max(ans, num + dic[digit_sum])
    dic[digit_sum] = max(dic[digit_sum], num)
```