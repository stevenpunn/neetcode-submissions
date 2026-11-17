class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # we can approach using sorting + 2 pointers

        people.sort()
        left = 0
        right = len(people) - 1
        result = 0

        while left <= right:
            # after placing heaviest person, calculate weight remaining
            remainingWeight = limit - people[right]
            # move right pointer, increase boat count
            right -= 1
            result += 1
            # now check if the lightest person (on the left) can fit and if left is valid
            if left <= right and remainingWeight >= people[left]:
                # move the left pointer in
                left += 1
        return result
