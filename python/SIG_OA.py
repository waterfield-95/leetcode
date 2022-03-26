class Solution:
    def sort_integer(self, A):
        self.quick_sort(A, 0, len(A) - 1)
    
    def quick_sort(self, A, start, end):
        if start >= end:
            return
        
        left, right = start, end
        pivot = A[start + (end - start) // 2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            
            while left <= right and A[right] > pivot:
                right -= 1
            
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        
        self.quick_sort(A, start, right)
        self.quick_sort(A, left, end)