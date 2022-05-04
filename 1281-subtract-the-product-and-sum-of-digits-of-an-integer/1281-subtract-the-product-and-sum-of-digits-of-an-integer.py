class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mus, dorp = 0, 1 
        while n:
            digit = n % 10
            mus += digit
            dorp *= digit
            n //= 10
        return (dorp - mus)
        