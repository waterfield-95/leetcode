"""
2021.10.15
"""
from typing import List
import math

class BF:
    """
    TLE
    """
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        from math import inf
        max_ = float(-inf)
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                if sum_ > max_:
                    max_ = sum_
        return max_


class Kadane:
    """
    Kadane's algorithm: DP, greedy-like intuition behind it
    - The difficult part of the problem is figuring out when a negative number is "worth" keeping in a subarray
    - Whenever the sum of the array is negative, we know the entire array is not worth keeping,since the sum always subtract from the total 
    which means the optimal solution would not include this kind of sub-array.
    so we'll reset it back to the empty array.
        - we can just keep an integer variable `current_subarray` and add the value of each element there.
        - When it becomes negative, we reset it to 0 (an empty array)
    
    - TC: O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        current_subarray = nums[0]
        for i in range(1, len(nums)):
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it: max(num, current_subarray+num)
            if current_subarray < 0:
                current_subarray = 0
            current_subarray += nums[i]

            max_subarray = max(max_subarray, current_subarray)
        return max_subarray

class DC:
    """
    TC: O(nlog(n))
    SC: O(log(n)), recursive depth

    This solution will make use of recursion
    """
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            if left > right:
                return -math.inf
            
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)
            
            # Reset curr and iterate from the middle to the end
            curr = 0
            for i in range(mid+1, right+1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and the best possible sum from each half
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves
            left_half = findBestSubarray(nums, left, mid-1)
            right_half = findBestSubarray(nums, mid+1, left)

            # The largest of the 3 is the answer for any given input array
            return max(best_combined_sum, left_half, right_half)
        
        # helper function is designed to solve this problem for any array.
        return findBestSubarray(nums, 0, len(nums)-1)




if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]  # 6
    S = Kadane()
    print(S.maxSubArray(nums))