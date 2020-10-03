/*
 * date: 201003
 * idea: 
 * 1. enumerate by dfs
 * - dfs：recurs to update next element and sum, there are two   possibility +/-. If traverse all elements, judge whether sum is equal to target.
 */

class Solution {
    int count = 0;
public:
    void dfs(vector<int>& nums, int S, int i, int sum){
        if(i == nums.size()){
            if(sum == S) count++;
        }
        else{
            dfs(nums, S, i+1, sum+nums[i]);
            dfs(nums, S, i+1, sum-nums[i]);
        }
    }

    int findTargetSumWays(vector<int>& nums, int S) {
        dfs(nums, S, 0, 0);
        return count;
    }
};
