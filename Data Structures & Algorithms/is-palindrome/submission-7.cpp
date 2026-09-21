class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right){
            // this moves left pointer until it finds an alphanumeric character
            while (left < right && !alphaNum(s[left])){
                left++;
            }
            // moves right pointer until it finds an alphanumeric character
            while (right > left && !alphaNum(s[right])){
                right--;
            }
            // if the characters don't match, return false
            if (tolower(s[left]) != tolower(s[right])){
                return false;
            }
            // move pointers inwards
            left++;
            right--;
        }
        return true;
    }


    bool alphaNum(char c) {
        return (c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z' ||
                c >= '0' && c <= '9');
    }
};
