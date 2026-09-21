class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we can use a stack to store the temperatures 
        # we store the number of zeroes needed for 
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res