class Solution:
    """
    Time: O(NlogN, MlogM)
    Space: O(1) not take result space into account
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n, m = len(nums1), len(nums2)
        i = j = 0
        k = 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        
        return nums1[:k]

class Solution:
    """
    T: O(N+M)
    S: O(min(M, N))
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # keep nums1.length < nums2.length
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        h = collections.Counter(nums1)
        ptr = 0
        for i in range(len(nums2)):
            print(nums2[i])
            if h[nums2[i]] > 0:
                nums1[ptr] = nums2[i]
                h[nums2[i]] -= 1
                ptr += 1
        return nums1[:ptr]
            
        