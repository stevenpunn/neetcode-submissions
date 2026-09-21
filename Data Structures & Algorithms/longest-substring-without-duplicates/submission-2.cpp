class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // create an empty charSet with 2 pointers
        unordered_set<char> charSet;
        int left = 0;
        int res = 0;

        // right pointer iterating through list
        for (int r = 0; r < s.size(); r++){
            // while the right pointer char exists in the set (duplicate)
            while(charSet.find(s[r]) != charSet.end()){
                // remove the left char from the set and move left to the right
                charSet.erase(s[left]);
                left++;
            }
            // add the right char to the set
            charSet.insert(s[r]);
            res = max(res, r - left + 1);
        }
        return res;
    }
};
/*
abcabcbb

If we iterate, we can move and the first subarray has abc
When we move right, we can see that a is a duplicate, so we need to shrink the list
We shrink from the left, so we remove s[left] from the charset
We go all the way until it has been erased
*/