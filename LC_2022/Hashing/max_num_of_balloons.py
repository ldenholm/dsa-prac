from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq_map = Counter(text)
        return int(min(freq_map['b'], freq_map['a'], (freq_map['l'] // 2), (freq_map['o'] // 2), freq_map['n']))
        
        # scrap all this and go with my original plan:
        # even more simple, use a counter and return min 
        # with the added arithmetic of dividing 'l' and 'o' by 2..