class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        qeue = deque([0])
        
        while qeue:
            current = qeue.popleft()
            visited.add(current)
            for key in rooms[current]:
                if key not in qeue and key not in visited:
                    qeue.append(key)
        
        sorted_visits = sorted(visited)
        is_difference_one = all(sorted_visits[i] - sorted_visits[i - 1] == 1 for i in range(1,len(sorted_visits)))
        if (len(rooms) - 1) not in visited:
            return False
        if is_difference_one:
            return True
     
        return False
            
            
        