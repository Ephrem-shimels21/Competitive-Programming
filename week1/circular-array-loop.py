class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # moves = {}
        # n = len(nums)
        # for idx,num in enumerate(nums):
        #     moves[idx] = (idx + num) % n
        # print(moves)
       
        # for id in moves:
        #     cur = id
        #     count = 0
        #     touched = set()
        #     while cur in moves and count < n:
        #         if cur in touched:
        #             return True
        #         if cur != moves[cur]:
        #             touched.add(cur)
        #         cur = moves[cur]
        #         count += 1
        #     # if len(touched) >= 2:
        #     #     return True
        # return False
        def get_next_index(i):
            return (i + nums[i]) % len(nums)

        for i in range(len(nums)):
            slow, fast = i, i
            while nums[slow] * nums[get_next_index(fast)] > 0 and nums[slow] * nums[get_next_index(get_next_index(fast))] > 0:
                slow = get_next_index(slow)
                fast = get_next_index(get_next_index(fast))

                if slow == fast:
                    if slow == get_next_index(slow):
                        break  
                    return True

        return False

            