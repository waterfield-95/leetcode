class Solution:
    """
    Time: O(n^2)
    Space: O(logn) to O(n) based on sorting process (recursive stack)
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_ = float("inf"), sum(nums[:3])
        nums.sort()
        n = len(nums)
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                deviation = abs(target - summation)
                if deviation < min_[0]:
                    min_ = deviation, summation
                
                if target > summation:
                    left += 1
                elif target < summation:
                    right -= 1
                else:
                    return min_[1]
        return min_[1]

        
# -4 -1 1 2 -> 1
# -4+x=1, x=5
# -1, 2 -> 1, 5-1=4>0 want to increase, move left forward
# 1 ,2 -> 3, 5-3=2 next loop
# -1 + x = 1, x=2
# 1,2 -> 3, |2-3|=1 min