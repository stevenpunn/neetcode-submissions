class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        /*
        We can sort the list then iterate through until we find a value that is skipped
        Better idea is to use a hashset, start counting only when we find beginning of 
        a consecutive sequence
        A number is the start of a sequence if num - 1 is not in the set
        */

        // Convert the list into a set of numSet
        // this deletes duplicates and has O(1) lookup time
        unordered_set<int> numSet(nums.begin(), nums.end());

        // initialize longest to track length of consecutive sequence
        int longest = 0;

        // loop through all values, not indices
        for(int num : numSet){
            // check if num-1 is NOT in the set
            if(numSet.find(num-1) == numSet.end()){
                // if true, num = start of sequence
                int length = 1;
                // update while num + length exists
                while (numSet.find(num + length) != numSet.end()){
                    length++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};
