class MergeSort:
    def sortIntegers(self, A):
        if not A:
            return A
        self.merge_sort(A, 0, len(A) - 1)
    
    def merge_sort(self, A, start, end):
        if start >= end:
            return
        
        # divide
        mid = start + (end - start) // 2
        self.merge_sort(A, start, mid)
        self.merge_sort(A, mid + 1, end)
        # combine
        self.merge(A, start, end)
    
    def merge(self, A, start, end):
        mid = start + (end - start) // 2
        left = start
        right = mid + 1
        temp = [0] * (end - start + 1)
        idx = 0
        
        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[idx] = A[left]
                idx += 1
                left += 1
            else:
                temp[idx] = A[right]
                idx += 1
                right += 1
        
        while left <= mid:
            temp[idx] = A[left]
            idx += 1
            left += 1
        
        while right <= end:
            temp[idx] = A[right]
            idx += 1
            right += 1
        
        A[start:end + 1] = temp
        # for i in range(start, end + 1):
        #     A[i] = temp[i - start]

if __name__ == "__main__":
    A = [1, 10, 22, 33, 5,6,7,88,99,66,77,55]
    S = MergeSort()
    S.sortIntegers(A)
    print(A)
