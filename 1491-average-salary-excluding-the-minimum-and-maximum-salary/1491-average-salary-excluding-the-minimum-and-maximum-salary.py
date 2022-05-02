class Solution:
    def average(self, salary: List[int]) -> float:
        min_s = min(salary)
        max_s = max(salary)
        sum_s = sum(salary) - min_s - max_s
        
        return (sum_s / (len(salary) - 2))
        