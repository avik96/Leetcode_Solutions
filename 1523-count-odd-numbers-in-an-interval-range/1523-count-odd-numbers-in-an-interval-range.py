class Solution:
    def countOdds(self, low: int, high: int) -> int:
        nums = (high - low + 1)
        
        if (nums %2 == 0):
            return (nums//2)
        else:
            if (low % 2 == 0):
                return (nums//2)
            else:
                return ((nums//2) +1)
        