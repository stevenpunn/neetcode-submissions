class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int result = 0;

        while (left < right){
            // first compute the height, so min of the two bars
            // multiply by the width, which is the diff of the indices
            int area = min(heights[left], heights[right]) * (right - left);
            // update result with the max area so far
            result = max(result, area);

            // now need to determine which pointer to move 
            // move pointer to the shorter height
            // heights[left] is the value of the bar, not the index
            // if condition shrinks every iteration, max value is already stored in result
            if (heights[left] < heights[right]){
                left++;
            }
            else {
                right--;
            }
        }
        return result;
    }
};
