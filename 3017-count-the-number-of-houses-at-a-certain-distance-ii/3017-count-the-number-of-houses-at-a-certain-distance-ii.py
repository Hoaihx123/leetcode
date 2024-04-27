class Solution(object):
    def countOfPairs(self, n, x, y):
        """
        :type n: int
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        if x>y:
            x,y = y,x
        ans = [0 for _ in range(n)]
        def solve_for_line(k):
            temp = k-1
            for i in range(k-1):
                ans[i] = temp*2
                temp -= 1
        if y-x<=1:
            solve_for_line(n)
            return ans
        solve_for_line(n-y+x+1)
        cicle = y-x+1
        for i in range((cicle-1)//2):
            ans[i] += cicle*2
        if (cicle-1)%2:
            ans[(cicle-1)//2] += cicle
        ans[0] -= 2
        def solve_for_cicle(a, b, space):
            if a<=0 or b<=0:
                return
            for i in range(a+b-1):
                ans[space + i] += (b-max(0, i+1-a)-max(0, b-i-1))*2
        solve_for_cicle(x-1, (y-x+1)//2, 1)
        solve_for_cicle(x-1, (y-x)//2-1, 2)
        solve_for_cicle(n-y, (y-x+1)//2, 1)
        solve_for_cicle(n-y, (y-x)//2-1, 2)
        return ans
        