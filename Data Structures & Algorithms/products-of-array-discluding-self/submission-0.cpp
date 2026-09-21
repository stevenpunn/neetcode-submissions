class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // the output should be the product of all elements except for the self index
        // use prefixes and suffixes
        // prefix = product of elements left of i
        // suffix = product of elements right of i

        int n = nums.size();
        vector<int> res(n);
        vector<int> pref(n);
        vector<int> suff(n);

        pref[0] = 1;        // nothing to the left of index 0
        suff[n-1] = 1;      // nothing to the right of last index

        // build the prefix product arrayy
        // for each i from 1 to n-1
        for(int i = 1; i < n; i++){
            pref[i] = nums[i - 1] * pref[i - 1];
        }

        // build the suffix product array
        // from each i from n-2 down to 0
        for (int i = n - 2; i >= 0; i--){
            suff[i] = nums[i + 1] * suff[i + 1];
        }

        // build the result: for each index i compute
        // res[i] = pref[i] * suff[i]
        for (int i = 0; i < n; i++){
            res[i] = pref[i] * suff[i];
        }
        return res;
    }
};
