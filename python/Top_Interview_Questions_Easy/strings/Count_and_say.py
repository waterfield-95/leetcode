class Recursion:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = ''
        count = 1
        last = self.countAndSay(n-1)
        for i, char in enumerate(last):
            if i != (len(last)-1) and last[i] == last[i+1]:
                count += 1
            else:
                res += str(count) + char
                count = 1
        return res

class Iteration:
    def countAndSay(self, n: int) -> str:
        idx, string = 1, '1'
        # whether calculate next (idx+1), if not return string with idx
        while idx < n:
            tmp = ''
            count = 1
            # through string to calculate next string
            for i, char in enumerate(string):
                if i != len(string) - 1 and string[i] == string[i+1]:
                    count += 1
                else:
                    tmp += str(count) + char
                    count = 1
            string = tmp
            idx += 1
        return string

class Solution:
    def countAndSay(self, n: int) -> str:
        idx, string = 1, '1'
        while idx < n: 
            count = 1
            tmp = ''
            n_ = len(string)
            for i in range(n_):
                if i != n_-1 and string[i] == string[i+1]:
                    count += 1
                else:
                    tmp += str(count) + string[i]
                    count = 1
            string = tmp
            idx += 1
        return string


if __name__ == '__main__':
    n_ = 6
    S = Solution()
    S1 = Iteration()
    print(S.countAndSay(n_))
    print(S1.countAndSay(n_))