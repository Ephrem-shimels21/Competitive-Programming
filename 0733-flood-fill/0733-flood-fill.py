class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        stack = deque()
        stack.append([sr,sc])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        starting_color = image[sr][sc]
        visited = set()
        
        while stack:
            c1,c2 = stack.pop()
            visited.add((c1,c2))
            if image[c1][c2] == starting_color:
                image[c1][c2] = color
            
            for x,y in directions:
                if min(c1 + x, c2+ y) < 0 or c1 + x > len(image) or c2 + y > len(image[0]):
                    continue
                elif c1 + x < len(image) and c2 + y < len(image[0]):
                    if image[c1 + x][c2 + y] == starting_color and (c1 +x, c2 + y) not in visited and (c1 + x, c2 + y) not in stack:
                        stack.append([c1 + x,c2 + y])
        return image
            
        