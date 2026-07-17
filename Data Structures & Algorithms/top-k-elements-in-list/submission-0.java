class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new TreeMap<>();
        for(int i = 0; i < nums.length; i++){
            int count = 1;
            Integer checker = freq.put(nums[i], count);
            if(checker != null){
                freq.put(nums[i], checker + 1);
            }
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(freq.entrySet());
        list.sort((a, b) -> b.getValue() - a.getValue());
        int[] last = new int[k];
        for(int j = 0; j < last.length; j++){
            last[j] = list.get(j).getKey();

        }
        return last;

    }
}
