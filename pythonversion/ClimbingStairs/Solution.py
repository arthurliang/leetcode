# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        # Fibonacci_number
        # matrix form : multiplication solution for getting O(log(n)) time consuming
        # {(Fn+1, Fn), (Fn, Fn-1)} = {(Fn+1, Fn), (Fn, Fn+1 - Fn)}
        # ={(a,b), (b,a-b)} = ((1,1), (1,0))^n
        a,b,x,y = 1,1,1,0
        while n>0:
            if n&1: x, y = a*x + b*y, b*x + y*(a-b)
            a,b,n = a*a + b*b, 2*a*b - b*b, n>>1;
        return x;