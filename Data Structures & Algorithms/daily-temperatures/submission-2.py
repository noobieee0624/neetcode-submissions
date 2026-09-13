class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store values as [temp, index]
        ans = [0] * len(temperatures) 

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                pair = stack.pop()
                ind = pair[1]
                ans[ind] = i-pair[1]
            
            stack.append([t, i])
        
        return ans
                
            



