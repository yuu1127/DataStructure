"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        employee = emap[id]
        total_importance = employee.importance

        for id in employee.subordinates:
            total_importance += self.getImportance(employees, id)

        return total_importance
