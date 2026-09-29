class Solution:
    def validPalindrome(self, s: str) -> bool:
        # we can only delete at most 1 character, check if it is still a palindrome

        # use 2 pointers
        left = 0
        right = len(s) - 1

        while left < right:
            # this means that they differ so we check
            if s[left] != s[right]:
                # skip the left character and check if the remaining is a palindrome
                skipL = s[left + 1 : right + 1]
                # skip the right character and check if it is a palindrome
                skipR = s[left : right]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            # if s[left] and s[right] are equal (same character), then move pointers inwards
            left, right = left + 1, right - 1
        
        return True