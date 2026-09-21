class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // maps value -> index 
        unordered_map<int, int> indices;

        // for every num in nums, record where it lives
        // nums[i] looks up the actual value at position i
        // indices[nums[i]] = using the actual value nums[i] as the map's key, store i (index) as the corresponding value
        for(int i = 0; i < nums.size(); i++){
            indices[nums[i]] = i;
        }

        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];    // value = value - index's value

            // checks if value diff exists anywhere in nums
            // indices[diff] gives the index of diff, compare against current index
            // this is an index vs index comparison
            // if diff's value exists && doesn't equal the current index's value
            if(indices.count(diff) && indices[diff] != i){
                return {i, indices[diff]};
            }
        }
        return {};
    }
};
