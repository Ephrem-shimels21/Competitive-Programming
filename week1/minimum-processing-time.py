class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()

        min_time = 0
        n = len(processorTime) - 1
        for i in range(3,len(tasks),4):
            min_time = max(processorTime[n] + tasks[i],min_time)
            n -= 1
        return min_time




        