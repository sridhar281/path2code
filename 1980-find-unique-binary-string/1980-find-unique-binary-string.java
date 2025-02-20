class Solution {
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder re=new StringBuilder();
        for(int i=0;i<nums.length;i++){
            if(nums[i].charAt(i)=='0'){
                re.append('1');
            }
            else{
                re.append('0');
            }
        }
        return re.toString();
    }
}