"""
2021.7
"""

class Solution:
    """
    Conditional judgement: bitwise judge
        - The first two bit: 2?/1?/?9/?3/??
        - The last two bit: there is no special condition
    """
    def maximumTime(self, time: str) -> str:
        time_list = list(time)
        for i, digit in enumerate(time_list):
            if digit != '?':
                continue

            if i == 0:
                if  '9'>= time_list[1] > '3':
                    time_list[i] = '1'
                else:
                    time_list[i] = '2'
            if i == 1:
                if time_list[0] == '2':
                    time_list[i] = '3'
                else:
                    time_list[i] = '9'
            if i == 3:
                time_list[i] = '5'
            if i == 4:
                time_list[i] = '9'
        return ''.join(time_list)

    def maximumTime_official(self, time: str) -> str:
        time_lst = list(time)
        if time_lst[0] == '?':
            time_lst[0] = '1' if '4' <= time_lst[1] <= '9' else '2'
        
        if time_lst[1] == '?':
            time_lst[1] = '3' if time_lst[0] == '2' else '9'

        if time_lst[3] == '?':
            time_lst[3] = '5'
        
        if time_lst[4] == '?':
            time_lst[4] = '9'
        return ''.join(time_lst)


if __name__ == '__main__':
    time = '2?:?0'
    S = Solution()
    print(S.maximumTime(time))