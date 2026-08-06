class Twitter:

    def __init__(self):
        self.tweets = []
        self.followmap = collections.defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.followmap[userId].add(userId)
        for author, tweetId in reversed(self.tweets):
            if author in self.followmap[userId]:
                res.append(tweetId)
            if len(res) == 10:
                break
                
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None: 
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].discard(followeeId)

