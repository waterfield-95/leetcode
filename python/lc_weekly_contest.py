import collections

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hashmap = collections.Counter(s)
        last = "#"
        res = []
        flag = True
        while flag:
            flag = False
            for i in range(ord("z"), ord("a") - 1, -1):
                c = chr(i)
                if c in hashmap and hashmap[c] != 0 and c != last:
                    num = min(hashmap[c], repeatLimit)
                    res.append(c * num)
                    hashmap[c] -= num
                    last = c
                    flag = True
                    break
        print(hashmap)
        print(res)
        return "".join(res)

if __name__ == "__main__":
    s = "cczazcc"
    n = 3
    S = Solution()
    print(S.repeatLimitedString(s, n))