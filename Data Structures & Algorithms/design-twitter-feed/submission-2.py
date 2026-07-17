class Twitter:

    def __init__(self):
        self.users = defaultdict(list)
        self.following_list = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.users[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        for person in self.following_list[userId]:
            for tweet in self.users[person]:
                maxHeap.append(tweet)
        for t in self.users[userId]:
            maxHeap.append(t)
        heapq.heapify(maxHeap)
        res = []
        for ans in range(10):
            if not maxHeap:
                break
            ans = heapq.heappop(maxHeap)
            res.append(ans[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_list[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)