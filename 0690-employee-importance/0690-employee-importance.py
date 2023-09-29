"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        importance = 0
        for i in range(len(employees)):
            if employees[i].id == id:
                stack = deque([i])
                break
        
        while stack:
            current = stack.pop()
            importance += employees[current].importance
            subordinates = employees[current].subordinates
            for subordinate in subordinates:
                for employee in employees:
                    if subordinate == employee.id:
                        stack.append(employees.index(employee))
        return importance
            
            
        