class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        min_rabbits = 0
        similars = 0
        prev = None

        for num in answers:
            if num == 0:
                min_rabbits += 1
            elif prev and num > similars and num != prev:
                min_rabbits += prev + 1
                prev = num
                similars = 1
            elif num == similars:
                min_rabbits += num + 1
                prev = None
                similars = 0
            elif prev == None or prev == num:
                prev = num
                similars += 1
        
        if similars:
            min_rabbits += num + 1
        
        return min_rabbits
    




        