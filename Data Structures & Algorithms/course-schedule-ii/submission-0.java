class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] indegree = new int[numCourses];
        int finish = 0;
        List<Integer> res = new ArrayList<>();
        int[] ans = new int[numCourses];

        for(int i = 0; i < numCourses; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] pre : prerequisites){
            indegree[pre[1]]++;
            adj.get(pre[0]).add(pre[1]);
        }
        Queue<Integer> q = new LinkedList<>();
        for(int z = 0; z < numCourses; z++){
            if(indegree[z] == 0){
                q.offer(z);
            }
        }
        while(!q.isEmpty()){
            int course = q.poll();
            ans[numCourses - finish - 1] = course;
            finish++;
            for(int prereq : adj.get(course)){
                indegree[prereq]--;
                if(indegree[prereq] == 0){
                    q.offer(prereq);
                }
            }
        }
        if(finish != numCourses){
            return new int[]{};
        }
        return ans;
    }
}
