class Two_Sum_Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numIndex=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int partner=target-nums[i];
            if(numIndex.containsKey(partner))
                return new int[] { numIndex.get(partner), i };
            numIndex.put(nums[i],i);
            
        }
        return new int[] { 0, 0 };
    }
}
