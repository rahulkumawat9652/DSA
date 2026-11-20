class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return
        total = total + nums[index]
        subset.append(nums[index])
        self.solve(index, total, subset, nums, target, result)
        subset.pop()
        total = total - nums[index]
        self.solve(index + 1, total, subset, nums, target, result)
candidates = [2, 3, 6, 7]
target = 7
s1 = Solution()
print(s1.combinationSum(candidates, target))