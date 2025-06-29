from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        def helper(l, r):
            if l == r:
                return 0, [prefix[l]]
            mid = (l + r) // 2
            count_left, left_arr = helper(l, mid)
            count_right, right_arr = helper(mid + 1, r)
            
            count_cross = 0
            j = 0
            k = 0
            for x in left_arr:
                while j < len(right_arr) and right_arr[j] < x + lower:
                    j += 1
                while k < len(right_arr) and right_arr[k] <= x + upper:
                    k += 1
                count_cross += (k - j)
            
            merged = []
            p1, p2 = 0, 0
            while p1 < len(left_arr) and p2 < len(right_arr):
                if left_arr[p1] <= right_arr[p2]:
                    merged.append(left_arr[p1])
                    p1 += 1
                else:
                    merged.append(right_arr[p2])
                    p2 += 1
            if p1 < len(left_arr):
                merged.extend(left_arr[p1:])
            if p2 < len(right_arr):
                merged.extend(right_arr[p2:])
                
            total_count = count_left + count_right + count_cross
            return total_count, merged
        
        count, _ = helper(0, len(prefix) - 1)
        return count