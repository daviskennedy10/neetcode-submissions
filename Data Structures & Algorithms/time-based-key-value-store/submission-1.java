class TimeMap {
    Map<String, TreeMap<Integer, String>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.computeIfAbsent(key, k -> new TreeMap<>()).put(timestamp, value);

        
    }
    
    public String get(String key, int timestamp) {
        String res = "";
        if(!map.containsKey(key)){
            return res;
        }
        TreeMap<Integer, String> timestamps = map.get(key);
        Map.Entry<Integer, String> entry = timestamps.floorEntry(timestamp);
        if(entry == null){
            return "";
        }
        else{
            return entry.getValue();
        }


    }
}
