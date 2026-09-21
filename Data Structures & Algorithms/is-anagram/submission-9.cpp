class Solution {
public:
    bool isAnagram(string s, string t) {
        // first, base case
        if (s.length() != t.length()){
            return false;
        }

         // if this is an anagram, they use the same chars with same frequencies
         unordered_map<char, int> countS;
         unordered_map<char, int> countT;

         for(int i = 0; i < s.length(); i ++){
            // iterate through both strings same time and increase count
            countS[s[i]]++;
            countT[t[i]]++;
         }
         // if counts are equal, return true
         if (countS == countT){
            return true;
         }
         else {
            return false;
         }
    }
};
