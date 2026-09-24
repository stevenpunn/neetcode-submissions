class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # we can use a hashmap to store the frequency of elements
        # then track the elements with the max count seen so far
        count = defaultdict(int)
        # res and maxCount store the current best candidates
        res = maxCount = 0

        for num in nums:
            # increment the count in the hashmap for each number
            count[num] += 1
            # if the count exceeds maxCount, update res = num and maxCount = count[num]
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res