from typing import List
from collections import defaultdict


class SlideWindow:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        left1, left2, right = 0, 0, 0
        sum1, sum2 = 0, 0
        res = 0
        
        while right < n:
            sum1 += nums[right]
            while left1 <= right and sum1 > goal:
                sum1 -= nums[left1]
                left1 += 1
            
            sum2 += nums[right]
            while left2 <=right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            
            res += left2 - left1
            right += 1
        return res

                
class PrefixSumHash:
    """
    2021.7
    Idea: Prefix sum with counter hashtable.
        - sum_[j] - sum_[i] = goal
        - traverse num as j of right boundary
        - update the hashtable in the real time to avoid the condition that i >= j
        for (i,j) or (j,i),  cnt increase once.

    Special case: 
        - empty list -> zero condition
    """
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_ = 0
        cnt = defaultdict(int)
        res = 0
        for num in nums:
            cnt[sum_] += 1
            sum_ += num
            res += cnt[sum_ - goal]
        return res


if __name__ == '__main__':
    nums = [1,0,1,0,1]
    goal = 2
    S1 = SlideWindow()
    S2 = PrefixSumHash()
    print(S1.numSubarraysWithSum(nums, goal))
    print(S2.numSubarraysWithSum(nums, goal))
