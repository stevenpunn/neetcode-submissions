class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        # defaultdict creates default values of 0: {number, freq}
        count = defaultdict(int)
        # count occurrances of each number, frequency map
        for num in nums:
            count[num] += 1

        res = []
        # choose the first number of the triplet
        for i in range(len(nums)):
            count[nums[i]] -= 1
            # skips duplicate first numbers
            if i and nums[i] == nums[i-1]:
                continue

            # pick the second number
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                # calculate the third number
                target = -(nums[i] + nums[j])
                # check if the third number exists
                # then add to the result
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
                    
            # restore the counts, so i can iterate normally
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1
        return res