from typing import List

class Optimal:
    """
    If there are many mapping relation, 7->Hiss, 11->Bass ....
    Hash table would help you a lot
    """
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        mapping = {
            3: "Fizz",
            5: "Buzz"
        }
        
        for i in range(n):
            idx = i + 1
            ans_str = ""
            
            for key in mapping.keys():
                if idx % key == 0:
                    ans_str += mapping[key]
            
            if ans_str == "":
                ans.append(str(idx))
            else:
                ans.append(ans_str)

        
        return ans


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        for i in range(n):
            idx = i+1
            if idx % 3 == 0 and idx%5==0:
                ans.append("FizzBuzz")
            elif idx % 3 == 0:
                ans.append("Fizz")
            elif idx % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(idx))
        return ans
        