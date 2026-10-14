class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use a sliding window, instead of checking every string, we fix a target character
        # slide a window and count how many characters inside already match x
        # if num. characters that don't match c and > k, window is invalid, shrink from left

        result = 0
        # put all of the unqiue characters from the string into a charSet
        charSet = set(s)

        for c in charSet:
            # set count (count of c inside window) and left = 0
            count = left = 0
            # slide the right pointer across the string
            for right in range(len(s)):
                # increase count when the right pointer == char
                if s[right] == c:
                    count += 1

                # if the window needs more than k replacements, move left forward
                # then adjust the count
                while (right - left + 1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1


                result = max(result, right - left + 1)
        return result