class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        ArrayList<Integer> arr = new ArrayList<>();
        int[] res = new int[k];
        for(int i = 0; i < nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort((a, b) -> b.getValue().compareTo(a.getValue()));
        Map<Integer, Integer> sortedMap = new LinkedHashMap<>();
        for (Map.Entry<Integer, Integer> entry : list) {
            sortedMap.put(entry.getKey(), entry.getValue());
        }
        int count = 0;

        for(int c : sortedMap.keySet()){
            arr.add(c);
            count++;
            if(count == k){
                break;
            }

        }
        for(int j = 0; j < arr.size(); j++){
            res[j] = arr.get(j);
        }
        return res;
    }
}
