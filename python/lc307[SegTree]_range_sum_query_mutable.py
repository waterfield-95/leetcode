"""
2021.5
idea: Segment Tree, O(logN)
"""

from typing import List

class NumArray_BF:
    """
    brute force, time out
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [0]
        for num in self.nums:
            self.prefix_sum.append(self.prefix_sum[-1]+num) 

    def update(self, index: int, val: int) -> None:
        origin = self.nums[index]
        self.nums[index] = val
        for i in range(index+1, len(self.prefix_sum)):
            self.prefix_sum[i] = self.prefix_sum[i] + val - origin
            
    def sumRange(self, left: int, right: int) -> int:       
        # 前缀和数组，第i个val表示self.nums中前i个元素的和，包括第i个元素
        sum = self.prefix_sum[right+1] - self.prefix_sum[left]
        return sum


class NumArray_tree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * self.n * 2
        self.__build_tree()
    
    def __build_tree(self):
        """
        构建线段树，线段树节点总和约等于2n个（等比数列求和）
        从下至上构建树，使tree[i] = tree[2*i] + tree[2*i + 1]
        """
        for i in range(self.n):
            self.tree[self.n+i] = self.nums[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[i*2] + self.tree[i*2 + 1]

    def update(self, index, val):
        index = self.n + index
        self.tree[index] = val
        while index > 0:
            left, right = index, index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            
            # 更新上一级变更节点的值
            index = index // 2
            self.tree[index] = self.tree[left] + self.tree[right]
    
    def sumRange(self, left, right):
        """
        从下至上一层一层求和
            - self.tree中每一个上层节点i等于下层2i+2i+1节点元素和
            - 对于下层左节点，如果为奇数，表示只包含2i+1的点，没有2i所以无法使用上层元素，直接将此层元素和加入total
            - 对于下层右节点，如果为偶数，表示无上层聚合节点，加和此节点值
            - 直到left<=right不满足时，完成全部区间加和
        """
        left = self.n + left
        right = self.n + right
        total = 0
        # 等号用于加和最上层元素
        while left <= right:
            if left % 2 == 1:
                total += self.tree[left]
                left += 1
            if right % 2 == 0:
                total += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return total
            

if __name__ == '__main__':
    num_array = NumArray_tree([1,3,5])
    print(num_array.sumRange(0,2)) # 9
    num_array.update(1,2)   # nums = [1,2,5]
    print(num_array.sumRange(0,2)) # 8
