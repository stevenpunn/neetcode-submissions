class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // start with an unordered map (hashmap)
        unordered_map<int, int> indices;

        for(int i=0; i < nums.size(); i++){
            // first nums[i] return the value at index i
            // second, indicies[i] now stores the value at that key, i 
            // this stores the index of each number using the number itself as the key
            indices[nums[i]] = i;
        }

        for (int i=0; i < nums.size(); i++){
            // diff = target - value at index i
            int diff = target - nums[i];
            // if diff exists in nums && index of diff is not same as current element
            if (indices.count(diff) && indices[diff] != i){
                return {i, indices[diff]};
            }
        }
        return {};
    }
};
