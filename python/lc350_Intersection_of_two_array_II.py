from typing import List

class Hashtable:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter()
        for num in nums1:
            counter[num] += 1        
        result = []
        for num in nums2:
            if counter[num] != 0:
                result.append(num)
                counter[num] -= 1        
        return result


class DoublePointer:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

if __name__ == '__main__':
    S = Hashtable()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(S.intersect(nums1, nums2))