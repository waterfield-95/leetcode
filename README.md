# leetcode
Cpp and Python Solution for Leetcode with Basic idea. And the specific method is described in the first solution.



| Title | Solution | Difficulty | Basic idea |
| ----- | -------- | :--------: | ---------- |
| [1. Two Sum](https://leetcode-cn.com/problems/two-sum/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/1.%20Two%20Sum.py) | Easy | 1. two-pointer<br>2. hashtable to store <value: index>, traverse once |
| [20. Valid Parentheses](https://leetcode-cn.com/problems/valid-parentheses/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/20_Valid_Parentheses.cpp) [Python](https://github.com/Fieldwater/leetcode/blob/master/python/20_Valid_Parentheses.py) | Easy | stack |
| [24. Swap Nodes in Pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/24_Swap_Nodes_in_Pairs.cpp) | Medium | recursion |
| [33. Search in Rotated Sorted Array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/33.%20Search%20in%20Rotated%20Sorted%20Array.py) | Medium | binary search |
| [80. Remove Duplicates from Sorted Array II](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II.py) | Medium | two pointer |
| [88. Merge Sorted Array](https://leetcode-cn.com/problems/merge-sorted-array/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/88.%20Merge%20Sorted%20Array.py) | Easy | two pointer, reverse insertion |
| [94. Binary Tree Inorder Traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/94_Binary_Tree_Inorder_Traversal.cpp) [Python](https://github.com/Fieldwater/leetcode/blob/master/python/94_Binary_Tree_Inorder_Traversal.py) | Medium | 1. DFS recursion<br>2. explicit stack |
| [118. Pascal's Triangle](https://leetcode-cn.com/problems/pascals-triangle/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/118_Pascal's_Triangle.py) | Easy | iter/recur |
| [119. Pascal's Triangle II](https://leetcode-cn.com/problems/pascals-triangle-ii/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/119_Pascal's_Triangle_II.py) | Easy | iter/recur |
| [130. Surrounded Regions](https://leetcode-cn.com/problems/surrounded-regions/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/130.%20Surrounded%20Regions.py) | Medium | BFS-2dimension |
| [133. Clone Graph](https://leetcode-cn.com/problems/clone-graph/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/133_Clone_Graph.cpp) | Medium | 1. DFS, visited hashmap<br>2. BFS: add all neighbors to queue and traverse |
| [150. Evaluate Reverse Polish Notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/150_Evaluate_Reverse_Polish_Notation.py) | Medium | stack |
| [153. Find Minimum in Rotated Sorted Array](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.py) | Medium | binary search |
| [155. Min Stack](https://leetcode-cn.com/problems/min-stack/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/155_Min_Stack.cpp) | Easy | 1. two stack to store data and minimum<br>2. pair<data, minimum>, and var *min* to store current minimum. |
| [179. Largest Number](https://leetcode-cn.com/problems/largest-number/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/179.%20Largest%20Number.py) | Medium | sort through splicing two number as string |
| [200. Number of Islands](https://leetcode-cn.com/problems/number-of-islands/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/200_Number_of_Islands.cpp) [Python](https://github.com/Fieldwater/leetcode/blob/master/python/200_Number_of_Islands.py) | Medium | 1. DFS: search to the depth of one element<br>2. BFS: search all neighbors of one element |
| [204. Count Primes](https://leetcode-cn.com/problems/count-primes/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/204.%20Count%20Primes.py) | Easy | set multiple of prime as composite number through prime list |
| [208. Implement Trie (Prefix Tree)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/208.%20Implement%20Trie%20(Prefix%20Tree).py) | Medium | char list as trie children, set end flag for word |
| [225. Implement Stack using Queues](https://leetcode-cn.com/problems/implement-stack-using-queues/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/225.%20Implement%20Stack%20using%20Queues.py) | Easy | two queue operation to implement stack when pushing elements |
| [232. Implement Queue using Stacks](https://leetcode-cn.com/problems/implement-queue-using-stacks/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/232.%20Implement%20Queue%20using%20Stacks.py) | Easy | twice stack operation to implement queue |
| [263. Ugly Number](https://leetcode-cn.com/problems/ugly-number/) | [Python](https://github.com/Fieldwater/leetcode/tree/master/python/263.%20Ugly%20Number.py) | Easy | factorization through 2,3,5 |
| [264. Ugly Number II](https://leetcode-cn.com/problems/ugly-number-ii/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/264.%20Ugly%20Number%20II.py) | Medium | minimum heap |
| [232. Implement Queue using Stacks](https://leetcode-cn.com/problems/implement-queue-using-stacks/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/232.%20Implement%20Queue%20using%20Stacks.py) | Easy | twice stack operation to implement queue |
| [279. Perfect Squares](https://leetcode-cn.com/problems/perfect-squares/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/279_Perfect_Squares.cpp) | Medium | BFS |
| [344. Reverse String](https://leetcode-cn.com/problems/reverse-string/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/344_Reverse_String.cpp) | Easy | iteration or recursion of swap in place |
| [394. Decode String](https://leetcode-cn.com/problems/decode-string/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/394.%20Decode%20String.py) | Medium | 1. assistant stack<br>2. DFS |
| [395. Longest Substring with At Least K Repeating Characters](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/395.%20Longest%20Substring%20with%20At%20Least%20K%20Repeating%20Characters.py) | Medium | DC |
| [424. Longest Repeating Character Replacement](https://leetcode-cn.com/problems/longest-repeating-character-replacement/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/424.%20Longest%20Repeating%20Character%20Replacement.py) | Medium | slide window with two pointer<br> - char number counter with list<br> - r-l+1-window_maxn > k |
| [485. Max Consecutive Ones](https://leetcode-cn.com/problems/max-consecutive-ones/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/485.%20Max%20Consecutive%20Ones.py) | Easy | traverse and find max_count: return max(max_count, count)|
| [494. Target Sum](https://leetcode-cn.com/problems/target-sum/) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/494_Target_Sum.cpp) | Medium | 1. DFS: enumerate all possibility<br> |
| [509. Fibonacci Number](https://leetcode-cn.com/problems/fibonacci-number/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/509_Fibonacci_Number.py) | Easy | recur+hashmap (memerization to reduce repeated calculation) |
| [561. Array Partition I](https://leetcode-cn.com/problems/array-partition-i/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/561.%20Array%20Partition%20I.py) | Easy | sort and combine |
| [567. Permutation in String](https://leetcode-cn.com/problems/permutation-in-string/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/567_Permutation_in_String.py) | Medium | slide window |
| [643. Maximum Average Subarray I](https://leetcode-cn.com/problems/maximum-average-subarray-i/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/643.%20Maximum%20Average%20Subarray%20I.py) | Easy | slide window, start pointer is outside of initial window |
| [665. Non-decreasing Array](https://leetcode-cn.com/problems/non-decreasing-array/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/665.%20Non-decreasing%20Array.py) | Easy | tranverse to find valley and judge index of i-1, i, i+1 |
| [697. Degree of an Array](https://leetcode-cn.com/problems/degree-of-an-array/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/697.%20Degree%20of%20an%20Array.py) | Easy | hashtable records [counts, left_one right_one] |
| [703. Kth Largest Element in a Stream](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/703.%20Kth%20Largest%20Element%20in%20a%20Stream.py) | Easy | python heapq in no need of sorted operation |
| [704. Binary Search&hearts;](https://leetcode-cn.com/problems/binary-search/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/704.%20Binary%20Search.py) | Easy | 1. two pointer <br>2. recursive |
| [739. Daily Temperatures](https://leetcode-cn.com/problems/daily-temperatures/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/739_Daily_Temperatures.py) | Medium | Monotonic stack |
| [743. Network Delay Time](https://leetcode-cn.com/problems/network-delay-time/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/743.%20Network%20Delay%20Time.py) | Medium | Dijkstra |
| [752. Open the Lock&hearts;](https://leetcode-cn.com/problems/open-the-lock) | [Cpp](https://github.com/Fieldwater/leetcode/blob/master/cpp/752_open_the_lock.cpp) | Medium | BFS: transform to graph to find the shortest path |
| [783. Minimum Distance Between BST Nodes](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/783.%20Minimum%20Distance%20Between%20BST%20Nodes.py) | Easy | in-order traverse |
| [832. Flipping an Image](https://leetcode-cn.com/problems/flipping-an-image/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/832.%20Flipping%20an%20Image.py) | Easy | 1. double pointer to reverse list<br>2. ^ XOR |
| [888. Fair Candy Swap](https://leetcode-cn.com/problems/fair-candy-swap/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/888.%20Fair%20Candy%20Swap.py) | Easy | hash table |
| [896. Monotonic Array](https://leetcode-cn.com/problems/monotonic-array/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/896.%20Monotonic%20Array.py) | Easy | set inc and des flags |
| [978. Longest Turbulent Subarray](https://leetcode-cn.com/problems/longest-turbulent-subarray/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/978.%20Longest%20Turbulent%20Subarray.py) | Medium | 1. slide window <br> 2. Dynamic Programming |
| [1006. Clumsy Factorial](https://leetcode-cn.com/problems/clumsy-factorial/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/1006.%20Clumsy%20Factorial.py) | Medium | 1. stack to expression calculator with operator |
| [1052. Grumpy Bookstore Owner](https://leetcode-cn.com/problems/grumpy-bookstore-owner/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/1052.%20Grumpy%20Bookstore%20Owner.py) | Medium | 1. slide window 生气的老板<br> |
| [1423. Maximum Points You Can Obtain from Cards](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/1423.%20Maximum%20Points%20You%20Can%20Obtain%20from%20Cards.py) | Medium | slide window + reverse thinking |
| [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | [Python](https://github.com/Fieldwater/leetcode/blob/master/python/1438.%20Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit.py) | Medium | slide window + sortedlist(sortedcontainer) |
