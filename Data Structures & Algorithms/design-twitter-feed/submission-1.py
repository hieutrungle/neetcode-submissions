import heapq
from collections import deque, defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # We only need to know who a user is following to build the feed
        self.followings = defaultdict(set)
        self.feeds = defaultdict(deque)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feeds[userId].append((self.time, tweetId))
        # Cap the user's stored tweets at 10
        if len(self.feeds[userId]) > 10:
            self.feeds[userId].popleft()
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followings[userId].copy()
        users.add(userId)
        
        for u in users:
            for time, tweet_id in self.feeds[u]:
                heapq.heappush(heap, (time, tweet_id))
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
            
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].discard(followeeId)