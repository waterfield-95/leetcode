from typing import List

class Optimal:
    """
    T: O(n^2)
    Space: O(k) k possible result for ans
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        for i in range(n):
            # special case to improve time complexity
            # if nums[i] > 0:
            #     break
            # if i != 0 and nums[i - 1] == nums[i]:
            #     continue
            target = -nums[i]
            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[left] + nums[right] 
                if sum_ == target:
                    ans.add(tuple([nums[i], nums[left], nums[right]]))
                    left + 1
                    right -= 1
                    # remove this probability of duplicates, we can directly use list to append our result instead of set
                    # while left < right and nums[left] == nums[left - 1]:
                    #     left += 1
                elif sum_ < target:
                    left += 1
                else:
                    right -= 1
        
        return list(ans)
                

# [-4, -1, -1, 0, 1, 2]

class No_sort:
    """
    O(n^2)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dups = set()
        res = []
        for i in range(n):
            if nums[i] in dups:
                continue
            dups.add(nums[i])
            
            j = i+1
            hash_table = {}
            while j < n:
                complement = - nums[i] - nums[j]
                if nums[j] in hash_table:
                    res.append(tuple(sorted([nums[i], complement, nums[j]])))
                hash_table[complement] = j
                j += 1
                
        return list(set(res))


class Hash:
    """
    O(nlogn + n^2)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if sort_nums[i] > 0:
                break
            if i != 0 and sort_nums[i] == sort_nums[i-1]:
                continue

            hash_table = {}
            j = i + 1
            while j < n:
                complement = - sort_nums[i] - sort_nums[j]
                if sort_nums[j] in hash_table:
                    res.append([sort_nums[i], complement, sort_nums[j]])
                    while j+1<n and sort_nums[j] == sort_nums[j+1]:
                        j += 1
                hash_table[complement] = j
                j += 1   
        return res



class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        if n < 3:
            return []
        
        s = set()
        sort_nums = sorted(nums)
        for i, first in enumerate(sort_nums):
            target = - first
            new_nums = sort_nums[:i] + sort_nums[i+1:]
            flag, res = self.twoSum(new_nums, target)
            if not flag:    # flag to identify if finding a solution
                continue
            
            for l in res:
                s.add(tuple(sorted([first] + l)))
            
        return list(s)
                
    
    def twoSum(self, nums, target):
        n = len(nums)
        i, j = 0, n-1
        found = True
        res = []
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                res.append([nums[i],nums[j]])
                i += 1
                j -= 1
            if s > target:
                j -= 1
            else:
                i += 1
        
        if i == j:
            found = False
        
        return (found, res)
            
            
if __name__ == "__main__":
    nums = [0,0,0]
    S = Solution()
    print(S.threeSum(nums))
