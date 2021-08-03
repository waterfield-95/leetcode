from typing import List
import random


class Solution:
    """
    sort and compare with original nums
    """
    def quicksort(self, nums):
        if len(nums) == 0:
            return []
        pivot = random.choice(nums)
        equal, less, more = [], [], []
        for num in nums:
            if num == pivot:
                equal.append(num)
            elif num < pivot:
                less.append(num)
            else:
                more.append(num)
        return self.quicksort(less) + equal + self.quicksort(more)

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = self.quicksort(nums)
        l, r = 0, len(nums)-1
        # find the boundary index
        while l <= r:
            if nums[l] != sort_nums[l]:
                break
            l += 1
        while r >= l:
            if nums[r] != sort_nums[r]:
                break
            r -= 1
        return r-l+1

class Optimal:
    """
    Concepts: To find unsorted subarray boundary left and right which
    are not satisfied with condition:
        - l is less than all the elements on its right
        - r is larger than all the elements on its left
    """

    def findUnsortedSubarray(self, nums):
        n = len(nums)
        minn, left = float('inf'), -1
        maxn, right = float('-inf'), -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n-1 - i]:
                left = n-1-i
            else:
                minn = nums[n-1 - i]
        return 0 if right == -1 else right-left+1


if __name__ == '__main__':
    nums = [2,6,4,8,10,9,15]
    S = Solution()
    # print(S.quicksort(nums))
    print(S.findUnsortedSubarray(nums))
    print(Optimal().findUnsortedSubarray(nums))
