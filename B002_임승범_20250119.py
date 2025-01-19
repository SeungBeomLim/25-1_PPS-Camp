# B002. Employee Importance - Leetcode

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


# DFS
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {employee.id: employee for employee in employees}
        
        def dfs(emp_id):
            employee = employee_dict[emp_id]

            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)
        
        return dfs(id)


# BFS
from collections import deque

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Step 1: Create a dictionary for quick lookup by ID
        employee_dict = {employee.id: employee for employee in employees}
        
        # Step 2: Initialize a queue for BFS and the total importance
        queue = deque([id])
        total_importance = 0
        
        # Step 3: Perform BFS
        while queue:
            emp_id = queue.popleft()
            employee = employee_dict[emp_id]
            total_importance += employee.importance
            # Add subordinates to the queue
            queue.extend(employee.subordinates)
        
        return total_importance
