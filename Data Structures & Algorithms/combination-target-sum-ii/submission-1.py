class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = set()
        n = len(candidates)

        def backtrack(idx, total, arr):
            if total == target:
                self.res.add(tuple(arr.copy()))
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break

                arr.append(candidates[i])
                backtrack(i + 1, total + candidates[i], arr)
                arr.pop()

        backtrack(0, 0, [])
        return [list(e) for e in self.res]