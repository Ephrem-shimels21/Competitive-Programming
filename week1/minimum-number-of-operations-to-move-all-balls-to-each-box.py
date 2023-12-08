class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            ball_count = 0
            for idx, box in enumerate(boxes):
                if i != idx and box == "1":
                    ball_count += abs(idx - i)
            ans.append(ball_count)
        return ans
                    
        