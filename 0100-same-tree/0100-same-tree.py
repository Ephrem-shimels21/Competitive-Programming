# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:  
        qeue_p = deque([])
        qeue_q = deque([])
        
        if not p and not q:
            return True
        else:
            qeue_p.append(p)
            qeue_q.append(q)
        
        while qeue_p and qeue_q:
            current_p = qeue_p.popleft()
            current_q = qeue_q.popleft()
            
            if current_p and current_q:
                if current_p.val != current_q.val:
                    return False
                if current_p.left or current_p.right:
                    qeue_p.append(current_p.left)
                    qeue_p.append(current_p.right)
                    
                if current_q.left or current_q.right:
                    qeue_q.append(current_q.left)
                    qeue_q.append(current_q.right)
                    
                if len(qeue_p) > len(qeue_q)  or len(qeue_q) > len(qeue_p):
                    return False
                
            elif not current_p and not current_q:
                continue
            else:
                return False

           
        return True
                
            