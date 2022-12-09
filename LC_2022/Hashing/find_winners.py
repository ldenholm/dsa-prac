from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:        
        losses_map = defaultdict(int)
        not_lost_any = []
        for match in matches:
            losses_map[match[1]] += 1
        # get those indexes having only count() == 1
        lost_only_one = [k for k in losses_map if losses_map[k] == 1]
        for match in matches:
            if match[0] not in losses_map:
                not_lost_any.append(match[0])
        return [sorted(set(not_lost_any)), sorted(lost_only_one)]