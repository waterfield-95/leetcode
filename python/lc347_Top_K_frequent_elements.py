from typing import List
import collections
import random
        

class Optimal:
    """
    Time: O(N)
    Space: O(N)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        unique = list(count.keys())
        
        # lomuto's partition scheme
        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]
            
            # 1. move pivot to the end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]
            
            return store_index
        
        
        def quickselect(left, right, k_smallest):
            """
            Sort a list within left..right till k-th less frequent element takes its place
            """
            # base case: the list contains only one element
            if left == right:
                return
            
            # select a random pivot_index
            pivot_index = random.randint(left, right)
            
            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)
            
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
            
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            
            # go right
            else:
                quickselect(pivot_index+1, right, k_smallest)
            
            
        n = len(unique)
        # k-th top frequent element is (n-k)th less frequent
        # Do a partial sort: from less frequent to the most frequent, till (n-k)th less frequent element takes its place (n-k) in a sorted array
        # All element on the left are less frequent
        # All the elements on the right are more frequent
        quickselect(left=0, right=n-1, k_smallest=n-k)
        # return top K frequent elements
        return unique[n-k:]
            

class Heap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        
        max_heap = [[-freq, num] for num, freq in cnt.items()]
        import heapq
        heapq.heapify(max_heap)
        
        res = []
        for i in range(k):
            _, num = heapq.heappop(max_heap)
            res.append(num)
        return res
# Time: O(N + KlogN)
# Space: O(N)

class Hashtable:
    """
    Time: O(NlogN)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ht = collections.defaultdict(int)
        for num in nums:
            ht[num] += 1
        
        sort_l = sorted(ht.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sort_l[i][0])
        print(res)
        return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    S = Solution()
    print(S.topKFrequent(nums, k))
