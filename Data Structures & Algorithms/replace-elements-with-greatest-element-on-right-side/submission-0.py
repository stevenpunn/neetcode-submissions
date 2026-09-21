class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # using a suffix map, we can traverse right to left and maintain a running max of all elements seen in rightMax
        # when in pos. i, current running max = greatest element to the right of i
        # update rightMax to include arr[i] fo the next iteration

        # ans is the result array that has the same size as the input
        n = len(arr)
        ans = [0] * n

        # rightMax represents the value of the last position
        rightMax = -1

        # traverse the array right to left using index i 
        for i in range(n - 1, -1, -1):
            # for each index i, store current rightMax in ans
            ans[i] = rightMax
            # update rightMax to be the max of itself and arr[i]
            rightMax = max(arr[i], rightMax)
        return ans