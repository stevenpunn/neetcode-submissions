class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
         return false;
      }

      // map the character to how often it appears so
      // countS['c'] = 1
      unordered_map<char, int> countS;
      unordered_map<char, int> countT;

      for (int i = 0; i < s.length(); i++){
         // s[i] is the value: the char sitting at index i in string s
         // countS[s[i]] uses the character as a key to loop up, so countS['c'] gives the curr count for the char 'c'
         // ++ increments the lookup returned
         countS[s[i]]++;
         countT[t[i]]++;
      }
      // if the character counts match, return true or else return false
      if (countS == countT){
         return true;
      } else {
         return false;
      }
   }
};
