class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length *2;
        int[] newArr = new int[length];
        int numsLength = nums.length;

        for(int i= 0; i< nums.length; i++){
            newArr[i] = nums[i];
            newArr[i+numsLength] = nums[i];
        }

        return newArr;
    }
}