from typing import List

class Recursive_mem_2:
    def __init__(self) -> None:
        self.profits = []

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.profits = [ None for _ in range(n)]
        return self.rob_from(0, nums)


    # profit list is immutable so that we can use it as input, but we recommend regard it as private class variable
    def rob_from(self, i, nums):
        if i >= len(nums):
            return 0

        if self.profits[i] is not None:
            return self.profits[i]

        
        self.profits[i] = max(self.rob_from(i+1, nums), self.rob_from(i+2, nums) + nums[i])
        return self.profits[i]
    

class Recursive_mem:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        profits = [ None for _ in range(n)]
        return self.rob_from(0, nums, profits)


    # profit list is immutable so that we can use it as input, but we recommend regard it as private class variable
    def rob_from(self, i, nums, profits):
        if profits[i] is not None:
            return profits[i]
        if i == len(nums) - 1:
            profit = nums[i]
        elif i == len(nums) - 2:
            profit = max(nums[i], nums[i+1])
        else:
            profit = max(self.rob_from(i+1, nums, profits), self.rob_from(i+2, nums, profits) + nums[i])
        
        profits[i] = profit
        print(profits)
        return profits[i]


class Bottom_to_up_DP_1:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_amount = [0] * (n+1)
        max_amount[1] = nums[0]
        for i in range(2, n+1):
            max_amount[i] = max(max_amount[i-1], max_amount[i-2]+nums[i-1])
        return max_amount[n]

class Bottom_to_up_DP_2:
    def rob_list(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        max_robbed_amount = [None for _ in range(n+1)]
        max_robbed_amount[n] = 0
        max_robbed_amount[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            max_robbed_amount[i] = max(max_robbed_amount[i+1], max_robbed_amount[i+2]+nums[i])
        return max_robbed_amount[0] # since rob from 0 house

    def rob(self, nums):
        """
        T: O(n)
        S: O(1)
        """
        if not nums:
            return 0
        n = len(nums)
        current, next_ = nums[n-1], 0
        for i in range(n-2, -1, -1):
            current, next_ = max(current, next_ + nums[i]), current
        return current



if __name__ == "__main__":
    nums = [1,2,3,1]      #output:4
    S = Bottom_to_up_DP_2()
    print(S.rob(nums))
    