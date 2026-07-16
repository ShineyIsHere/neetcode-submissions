class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool dup = false;
        for(int i = 0; i < size(nums);i++){
            for (int j = 1; j < (size(nums) - i); j++){
                if (nums[i] == nums[j + i]){
                    return true;
                    dup = true;
                } 
            }
        }
        if (!dup) return false;
    }
};