class Solution:
    """
    Time: O(N^2)
    Space: O(C), c is length of lower-case letter, we use extra set to store it in each iteration
    """
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        n = len(word)
        cnt = 0
        for left in range(n):
            for right in range(left+4, n):
                if set(word[left:right+1]) == vowels:
                    cnt += 1
                    
        return cnt