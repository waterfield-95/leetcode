"""
2021.7.5
idea: bracket sequence problem solved by stack or recursion
1. stack + counter-dict
    - taverse the chemical formula, records the atom counts in the current layer through dict
    for current character:
        - left bracket: push empty dict into stack and move to next layer
        - if not bracket: read a name of atom and the following number, and then add to dict at the top of stack
        - right bracket means current layer traversal completed, if followed by number, multiply
    - Finally, sort atom name and concatenate string (notice: don't show number if it's 1)

    - Time complexity: traverse string with stack O(n^2) + sort O(nlogn)
"""

from collections import defaultdict


class Solution:
    def parse_atom(self):
        """
        parse current index atom and move index to next character
        """
        atom = ''
        atom += self.formula[self.i]
        self.i += 1
        while self.i < self.n and self.formula[self.i].islower() == True:
            atom += self.formula[self.i]
            self.i += 1
        return atom

    def parse_num(self):
        """
        parse current index digits and move index to next character
        """
        # if it's not digit, return 1 which is default number
        if self.i == self.n or self.formula[self.i].isdigit() != True:
            return 1
        num = 0
        while self.i < self.n and self.formula[self.i].isdigit() == True:
            num = num * 10 + int(self.formula[self.i])
            self.i += 1
        return num

    def countOfAtoms(self, formula: str) -> str:
        self.i = 0
        self.n = len(formula)
        self.formula = formula
        
        stk = [defaultdict(int)]
        while self.i < self.n:
            char_ = formula[self.i]
            if char_ == '(':
                self.i += 1
                stk.append(defaultdict(int))  # add next layer hashtable to count number of atoms
            
            elif char_ == ')':
                self.i += 1
                after_num = self.parse_num()
                atoms_num = stk.pop()   # pop the current layer counter of hashtable
                for atom, num in atoms_num.items():
                    stk[-1][atom] += num * after_num    # add current layer count of atom to last layer with number after the ')'
            
            else:
                atom = self.parse_atom()
                num = self.parse_num()
                stk[-1][atom] += num

        counter = stk[-1]
        res = ''
        for atom in sorted(counter):
            if counter[atom] == 1:
                res += str(atom)
            else:
                res += str(atom) + str(counter[atom])
        return res
            

if __name__ == '__main__':
    formula_ = 'K4(ON(SO3)2)2'   # 'K4N2O14S4'
    S = Solution()
    print(S.countOfAtoms(formula_))