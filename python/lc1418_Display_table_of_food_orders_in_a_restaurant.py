"""
2021.7
idea: hashtable to build SQL table
"""

from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # defaultdict parameter needs to be a constructor
        table_info = defaultdict(lambda: defaultdict(int))
        food_headers = set()
        for _, table, food in orders:
            table_info[table][food] += 1
            food_headers.add(food)

        food_headers = sorted(food_headers)
        res = [['Table'] + food_headers]

        for table_num in sorted(table_info, key=lambda x: int(x)):
            items = [table_num]
            for food in food_headers:
                items.append(str(table_info[table_num][food]))
            res.append(items)
        return res


if __name__ == '__main__':
    orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
    S = Solution()
    print(S.displayTable(orders))

