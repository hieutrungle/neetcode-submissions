class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            tmp = list(adj[src])
            for i, airport in enumerate(tmp):
                adj[src].pop(i)
                res.append(airport)
                if dfs(airport):
                    return True
                adj[src].insert(i, airport)
                res.pop()
            return False

        dfs('JFK')
        return res