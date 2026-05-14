class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pos_speed = list(zip(position, speed))
        pos_speed = sorted(pos_speed, key=lambda x: x[0], reverse=True)
        res = 0
        stack = []
        for pos, speed in pos_speed:
            time = (target - pos) / speed
            if not stack:
                stack.append(time)
                continue
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)