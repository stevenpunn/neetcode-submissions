class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # in this case, we need a dynamic sliding window
        # this window expands from the right when unique elements are found
        # the window will shrink from the left if we find a repeated character
        '''
        acbacbbb
        so we see that we can move the sliding window, once we reach the second 'a',
        we can remove the 'a' on the left so the window is 'bca', still valid
        So we move and see bcab, so we remove the front b and are left with cab
        once we reeach abcb, we have to remove the front so a gets removed, as well as b
        '''
        charSet = set()
        left = 0    # this will start at the left edge
        result = 0  # this stores the result

        for right in range(len(s)):     # right = right pointer that we move through the string
            # check if the right char is already in the set (duplicate)
            # this while loop runs while the duplicate remains in the set
            while s[right] in charSet:
                # if it is a duplicate, we need to update our sliding window
                # remove left pointer from the set and move the pointer 1 to the  right
                charSet.remove(s[left])
                left += 1
            # add the right value to the set only when all duplicates have been removed
            charSet.add(s[right])
            # this result updates every cycle, and updates to store max
            # 
            result = max(result, right - left + 1)
        return result



