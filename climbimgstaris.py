class Solution(object):
    def climbstairs(self,n):
        stair_number = {}
        return self.ways(n, stair_number)
    def ways(slef,n, stair_number):
        if n == 1 or n == 2:
            return n
        elif n in stair_number:
            return stair_number[n]
        else:
            stair_number[n]= helper(n-1) + helper (n-2)
            return stair_number[n]
        return n