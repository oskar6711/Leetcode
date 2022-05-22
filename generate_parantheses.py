class Solution(object):
    def generate_parenthesis(self, n):
        if n == 0:
            return ['']
        ans = []
        for i in range(n):
            for left in self.generate_parenthesis(i):
                for right in self.generate_parenthesis(n-1-i):
                    ans.append(f'({left}){right}')
        return ans


obj = Solution()
print(obj.generate_parenthesis(10))
