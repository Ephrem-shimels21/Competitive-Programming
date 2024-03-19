class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def find_it_row(row):
            row.sort()
            idx = bisect_left(row, target)
            if (idx < len(row) - 1 and row[idx + 1] == target) or (idx < len(row) and row[idx] == target):
                return True
            return False
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target and  target <= matrix[mid][-1]:
                return find_it_row(matrix[mid])
            
            elif matrix[mid][0] < target:
                l = mid + 1
            
            elif matrix[mid][0] > target:
                r = mid - 1
        return False
        