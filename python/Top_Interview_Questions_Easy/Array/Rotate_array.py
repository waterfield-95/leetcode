from typing import List

class Reverse:
    """
    1. reverse the first n-k elements
    2. reverse the rest of them
    3. reverse the entire array
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start+1, end-1
        n = len(nums)
        if k > n:
            k %= n  # when k > n, take the remainder
        reverse(nums, 0, n-1-k)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)
        return nums

class CyclicReplacement:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = 0   # number of replacement element
        start = 0
        # avoid endless loop
        while count < n:
            current = start
            prev = nums[start]
            while True:
                current = (current + k) % n
                tmp = nums[current]
                nums[current] = prev
                prev = tmp
                count += 1
                
                if current == start:
                    break
            
            start += 1

        
if __name__ == '__main__':
    S = CyclicReplacement()
    nums_ = [1,2,3,4,5,6]
    k_ = 2
    S.rotate(nums_, k_)
    print(nums_)