# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        qeue = deque([root])
        average = [root.val]
        summ = 0
        count = 0
        temp = []
        
        while qeue:
            current = qeue.popleft()
            if current:
                if current.left:
                    summ += current.left.val
                    count += 1
                if current.right:
                    summ += current.right.val
                    count += 1
                if count and len(qeue) == 0:
                    average.append(float(summ) / count )
                    
                if current.left and current.right:
                    temp.append(current.left)
                    temp.append(current.right)
                elif current.left:
                    temp.append(current.left)
                elif current.right:
                    temp.append(current.right)
                    
                if len(qeue) == 0:
                    qeue.extend(temp)
                    summ = 0
                    count = 0
                    temp = []
        return average