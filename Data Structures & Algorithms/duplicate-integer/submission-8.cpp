class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> found;
        for(int num: nums){
            if (found.count(num)){
                return true;
            }
            else{
                found.insert(num);
            }
        }
        return false;
    }
};