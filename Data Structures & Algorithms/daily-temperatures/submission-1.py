class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        return an array result where result[i] is the number of days after
        ith day before a warmer temp appears on a future day
        '''
        # use a stack, scan foward if we find a temp higher than on top of the stack
        # Pop it, compute the difference in days, and continue 

        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        # iterate through the temperature list
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:   # stack not empty & temp warmer than top of stack
                stackT, stackInd = stack.pop()  # pop the top element
                res[stackInd] = i - stackInd    # how many days passed, update result
            stack.append((t, i))                
        return res