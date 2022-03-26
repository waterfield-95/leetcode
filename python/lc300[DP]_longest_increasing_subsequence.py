from typing import List

class DP:
    """
    Time: O(N^2)
    Space: O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):
            for j in range(len(nums[:i])):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
            
class Solution:
    """
    Time: O(N^2)
    Space: O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [nums[0]]
        
        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            
            #sub [1,3,6], 2 -> replace 3
            j = 0
            while nums[i] > sub[j]:
                j += 1
            
            sub[j] = nums[i]
        
        return len(sub)


class Optimal:
    """
    Time: O(NlogN)
    Space: O(N)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search(l, r, target, sub):
            while l < r:
                mid = l + (r - l) // 2
                if sub[mid] == target:
                    return mid
                elif sub[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        sub = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                idx = binary_search(0, len(sub) - 1, nums[i], sub)
                sub[idx] = nums[i]
        
        return len(sub)
    

    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [nums[0]]
        
        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            
            #sub [1,3,4,6], 2 -> replace 3
            # binary search the smallest element in sub that is larger than or equal to num[i]
            # final result the binary search range is 1
            else:
                l, r = 0, len(sub) - 1
                while l < r:
                    mid = l + (r - l) // 2
                    if sub[mid] == nums[i]:
                        l = mid
                        break
                    elif sub[mid] > nums[i]:
                        r = mid # we need to keep the first element which larget than num[i]
                    else:
                        l = mid + 1
                    
                sub[l] = nums[i]
        
        return len(sub)
    


if __name__ == '__main__':
    nums = [3,5,6,2,5,4,19,5,6,7,12]
    S = Optimal()
    print(S.lengthOfLIS(nums))
    