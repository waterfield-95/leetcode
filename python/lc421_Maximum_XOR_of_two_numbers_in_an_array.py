"""
2021.5
idea:
1. hashtable to judge if the bit could be 1, otherwise 0
    - traverse 0-30 bit, to judge next bit is or is not one
    - we could find result and through result XOR one of element
    - judge whether or not there exists another element to make certain bit 1
[TODO]2. dict Tree
"""

from typing import List

class Solution:
    def findMaximumXOR(self, nums):
        # 最高位的二进制索引编号为30 [0,30]
        HIGH_BIT = 30
        
        x = 0
        for k in range(HIGH_BIT, -1, -1):
            seen = set()
            # 将所有pre^k(a_j)放入hashtable
            for num in nums:
                # 只保留从最高位开始到k个二进制部分，将其右移k位，低位自动消失，高位补0
                seen.add(num >> k)

            # 目前x包含从最高位开始到第k+1个二进制位为止的部分
            # 我们将x的第k个二进制位设置为1，即x=x*2+1 将x左移一位，低位补1
            x_next = x*2 + 1
            found = False

            # 枚举i
            for num in nums:
                if x_next ^ (num >> k) in seen:
                    found = True
                    break

            if found:
                x = x_next
            else:
                # 如果没有找到满足等式的a_i和a_j，那么x的第k个二进制位只能为0，即x=x*2
                x = x_next - 1
        return x


    def findMaximumXOR_BF(self, nums: List[int]) -> int:
        max_ = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                max_ = max(nums[i]^nums[j], max_)
        return max_
                

if __name__ == '__main__':
    nums = [3, 10, 5, 25, 2, 8]
    S = Solution()
    print(S.findMaximumXOR(nums))