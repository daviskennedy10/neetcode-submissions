class Solution {
    

    public String encode(List<String> strs) {
        StringBuilder word = new StringBuilder();
        for(int i = 0; i < strs.size(); i++){
            String element = strs.get(i);
            int length = element.length();
            word.append(length + "#" + element);

        }
        String sender = word.toString();
        return sender;

    }

    public List<String> decode(String str) {
        List<String> result = new ArrayList<>();
        int l = 0;
        int n = str.length() -1;
        while(l < n){
            int j = l;
            while(str.charAt(j) != '#'){
                j++;
            }
            Integer number = Integer.parseInt(str.substring(l, j));
            l = j+number;
            result.add(str.substring(j+1, l+1));
            l++;

        }
        return result;


    }
}
