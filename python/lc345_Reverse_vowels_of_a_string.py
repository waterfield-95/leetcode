"""
2021.8
Reverse all the vowels in a string
idea: double pointer
"""

class DoublePointer:
    """
    using two pointer left and right, look for the vowel element
    from the front and the back respectively:
        - traveres all elemnents: while l < r
        - move l to find next vowel: while l < n and char not vowel -> l++
        - move r to find next vowel: while r > 0 and char not vowel -> r--
        - after find double vowel and l < r: exchange element
        - return while loop
    """
    def isVowels(self, char: str) -> bool:
        return char in 'aeuioAEUIO'
        
    def reverseVowels(self, s:str) -> str:
        n = len(s)
        sl = list(s) 
        l, r = 0, n-1
        # if there are no vowels in the string, return the original string when l == r
        while l < r:
            # move l pointer to the right until l = n to make l equal to vowels
            while l < n and not self.isVowels(sl[l]):
                l += 1
            # find next vowel r
            while r > 0 and not self.isVowels(sl[r]):
                r -= 1
            if l < r:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1
        return ''.join(sl)

 
if __name__ == '__main__':
    s = 'leetcode'
    S = DoublePointer()
    print(S.reverseVowels(s))