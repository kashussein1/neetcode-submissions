class Solution {
    public int removeDuplicates(int[] nums) {
        int length = nums.length - 1;
        int counter = 0;
        int pre = 0;
        int [] noDupes = new int[length+1];
        HashSet<Integer> noDu = new HashSet<>();
        for(int i = 0; i <= length; i++ ){ 
        if(!noDu.contains(nums[i])){
            noDupes[counter] = nums[i];
            counter++;
        }
        noDu.add(nums[i]);
        
        }

        for(int k = 0; k<=length; k++){
            nums[k] = noDupes[k];
        }




        return counter;
    }
}