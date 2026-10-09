class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 10/9/26
        # using a stack approach
        # when we find a temp higher than the top of the stack, we found a warmer day
        # use a result list filled with zeroes
        result = [0] * len(temperatures)

        # using a stack to store pairs of temps and indices for days not found a warmer temp
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            # while stack not empty and current temp is warmer than the top of the stack
            while stack and t > stack[-1][0]:
                # pop the top element
                stackTemp, stackIndex = stack.pop()
                # count how many days passed
                result[stackIndex] = i - stackIndex
            # append the current day onto the stack
            stack.append((t, i))
        # return the filled result list
        return result