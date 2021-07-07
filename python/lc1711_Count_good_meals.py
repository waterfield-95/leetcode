"""
2021.7
idea: Given food deliciousness list, find the number of different good meals which the sum is equal to pow of 2
    - hashtable to store number counts
    - traverse one time with traverse all target which is the pow of 2
    - result % int(1e9 + 7)
"""


from typing import List
from collections import defaultdict, Counter

class Solution2:
    def countPairs(self, deliciousness):
        cnts = Counter(deliciousness)
        ans = 0
        for key in cnts:
            for i in range(22):
                target = 2 ** i
                if key == target / 2:
                    # 两个同一个数为2的幂，本身需要除以2
                    ans += cnts[key] * (cnts[key]-1) / 2
                else:
                    # 默认cnts如果没有key，val=0，遍历两次，需要结果除以2
                    ans += cnts[key] * cnts[target - key] / 2
        # Prevent overflow
        return int(ans % (1e9+7))


# Limited Time Exceeded
class Solution:
    def number_of_1(self, n):
        if n >= 0:
            return bin(n).count('1')
        else:
            return bin(n & 0xffffffff).count('1')

    def countPairs(self, deliciousness: List[int]) -> int:
        mod = int(1e9+7)
        counter = defaultdict(int)
        for val in deliciousness:
            counter[val] += 1
        
        res = 0
        sort_list = sorted(counter)
        for i in range(len(sort_list)):
            x1_ = sort_list[i]
            for j in range(i, len(sort_list)):
                x2_ = sort_list[j]
                # judge whether result is a power of two
                if self.number_of_1(x1_ + x2_) == 1:
                    if sort_list[i] == sort_list[j]:
                        res += int(counter[sort_list[i]] * (counter[sort_list[i]] - 1) / 2)
                    else:
                        res += counter[sort_list[i]] * counter[sort_list[j]]
        return res % mod

                
if __name__ == '__main__':
    deliciousness = [1,1,1,3,3,3,7]
    S = Solution()
    print(S.countPairs(deliciousness))