class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        can = capacity

        for index, plant in enumerate(plants):
            can = can - plant
            steps += 1
            if index + 1 < len(plants)  and plants[index + 1] > can:
                steps += (index + 1) * 2
                can = capacity
        return steps
        