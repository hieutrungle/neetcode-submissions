import heapq
from collections import deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count task frequencies
        buckets = [0 for _ in range(26)]
        for task in tasks:
            buckets[ord(task) - ord('A')] += 1
        
        # 2. Build the max-heap for AVAILABLE tasks (using negative counts)
        heap = []
        for cnt in buckets:
            if cnt > 0:
                heapq.heappush(heap, -cnt)
        
        # 3. Queue to store tasks on cooldown: pairs of (count_remaining, available_time)
        cooldown_queue = deque()
        time = 0
        
        while heap or cooldown_queue:
            time += 1
            
            # If we have available tasks, process the most frequent one
            if heap:
                cnt = heapq.heappop(heap)
                cnt += 1 # Decrement the count (add 1 because it's negative)
                
                # If the task still has remaining executions, put it on cooldown
                if cnt != 0:
                    cooldown_queue.append((cnt, time + n))
            
            # Check if the task at the front of the cooldown queue is ready to jump back into the heap
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_task_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(heap, ready_task_cnt)
                
            # Optimization: If the heap is empty, the CPU is idle. Fast-forward time to the next available task.
            if not heap and cooldown_queue:
                time = cooldown_queue[0][1] - 1 # -1 because the loop will increment time by 1 at the start
                
        return time