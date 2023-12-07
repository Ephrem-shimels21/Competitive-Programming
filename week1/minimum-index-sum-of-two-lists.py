class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        idx_sum = float('inf')

        for idx, word in enumerate(list1):
            if word in list2:
                if idx + list2.index(word) < idx_sum:
                    while ans:
                        ans.pop()
                    ans.append(word)
                    idx_sum = idx + list2.index(word)
                elif idx + list2.index(word) == idx_sum:
                    ans.append(word)
        return ans
        