from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list) 
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        relevante_user = set(self.following[userId])
        relevante_user.add(userId)
        
        alle_tweets = []
        for user in relevante_user:
            alle_tweets.extend(self.tweets[user])
            
        alle_tweets.sort(key=lambda x: x[0], reverse=True)
        
        ergebnis = []
        for tweet_paket in alle_tweets[:10]:
            ergebnis.append(tweet_paket[1])
            
        return ergebnis

    def follow(self, followerId: int, followeeId: int) -> None: 
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)