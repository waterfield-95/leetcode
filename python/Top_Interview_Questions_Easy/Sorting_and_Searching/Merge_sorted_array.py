from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        idx = m+n-1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[idx] = nums2[j]
                j -= 1
            else:
                nums1[idx] = nums1[i]
                i -= 1
            idx -= 1
        
        if i == -1 and j != -1:
            nums1[:j+1] = nums2[:j+1]
            
if __name__ == '__main__':
    S = Solution()
    