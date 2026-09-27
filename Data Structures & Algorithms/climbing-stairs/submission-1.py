class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

#recursion and we are using memo map as we would exceed time for above 45 since recurssion time is o(2^n)