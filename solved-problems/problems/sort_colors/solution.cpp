class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> temp;
        int n = nums.size();
        int count0 = 0;
        int count1 = 0;
        int count2 = 0;
        for(int i=0;i<n;i++){
            if(nums[i] == 0){
                count0++;
            }
            else if(nums[i] == 1){
                count1++;
            }
            else{
                count2++;
            }
        }
        for(int i=0;i<count0;i++){
            temp.push_back(0);
        }
        for(int i=0;i<count1;i++){
            temp.push_back(1);
        }
        for(int i=0;i<count2;i++){
            temp.push_back(2);
        }    

        nums = temp;
        }
};