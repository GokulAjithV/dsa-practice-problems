class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int,int> dic;
        int n = nums.size();
        for(int i=0;i<n;i++){
            dic[nums[i]]++;
        }

        for(auto it: dic){
            if(it.second > n/2){
                return it.first;
            }
        }
        return -1;
    }
};