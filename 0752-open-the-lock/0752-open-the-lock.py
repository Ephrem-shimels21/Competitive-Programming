class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        qeue = deque()
        qeue.append(["0000",0])
        visited = set(deadends)
        if "0000" in deadends:
            return -1
       
        while qeue:
            lock,turns = qeue.popleft()
            if lock == target:
                return turns
            
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                if (lock[:i] + digit + lock[i + 1: ])not in visited:
                    visited.add(lock[:i] + digit + lock[i + 1: ])
                    qeue.append([lock[:i] + digit + lock[i + 1: ], turns + 1])
                digit = str((int(lock[i]) - 1) % 10)
                if (lock[:i] + digit + lock[i + 1: ])not in visited:
                    visited.add(lock[:i] + digit + lock[i + 1:])
                    qeue.append([lock[:i] + digit + lock[i + 1: ], turns + 1])
        return -1
                
                
               
                    
                    
                
            
        
                
            
            
        