class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        h, w = len(matrix), len(matrix[0])
        if w == 0:
            return False

        print(h, w)

        x, y = w-1, 0
        while (y < h and x >= 0):
            if matrix[y][x] > target:
                x -= 1
            elif matrix[y][x] < target:
                y += 1
            elif matrix[y][x] == target:
                return True
        
        return False