"""
2021.8
Given an integer array and k, return the kth largest element
idea: 
- quick sort in reverse and return the kth element
"""

from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def quick_select(left, right, n_smallest):
            if left == right:
                return
            
            pivot_idx = random.randrange(left, right)   # right
            pivot_idx = partition(left, right, pivot_idx)
            
            if pivot_idx == n_smallest:
                return
            elif pivot_idx < n_smallest:
                quick_select(pivot_idx+1, right, n_smallest)
            else:
                quick_select(left, pivot_idx-1, n_smallest)
                
        def partition(left, right, pivot_idx):
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            stored_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[stored_idx] = nums[stored_idx], nums[i]
                    stored_idx += 1
            
            nums[stored_idx], nums[right] = nums[right], nums[stored_idx]
            
            return stored_idx
        
        quick_select(left=0, right=n-1, n_smallest=n-k)
        return nums[n-k]

    # Test,n-small:4: [3,2,1,4,5,6],3<4, [5,6] -> 5>4,[5] == 4,return nums[4]=5
    # Test,n-small:9-4=5, [3,2,3,1,2,4,5,5,6],i=8>5 -> go left [3,2,3,1,2,4,5,5],i=6>5 -> left [3,2,3,1,2,4],i=5==5 return

class Solution:
    """
    Time: O(Nlogk)
    Space: O(1)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        import heapq
        heapq.heapify(min_heap)
        for num in nums[k:]:
            heapq.heappushpop(min_heap, num)
        
        return min_heap[0]
            

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        import heapq
        heapq.heapify(max_heap)
        for i in range(k-1):
            heapq.heappop(max_heap)
        
        return - heapq.heappop(max_heap)


        

if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]  # 4
    k = 4
    S = Solution()
    print(S.findKthLargest(nums, k))
    