class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_dist = 0

        for arr in arrays[1:]:
            curr_min = arr[0]
            curr_max = arr[-1]

        
            max_dist = max(
                max_dist, abs(curr_max - min_val), abs(max_val - curr_min)
        )

        
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)

        return max_dist



        
        