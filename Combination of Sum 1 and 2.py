# Combination of Sum 1
class Solution:
    def combinationSum(self, candidates, target):
        def generate(ind, curr_subset, ans, candidates, target):
            if target == 0:
                ans.append(curr_subset.copy())
                return
            if target < 0 or ind == len(candidates):
                return
            curr_subset.append(candidates[ind])
            generate(ind, curr_subset, ans, candidates, target - candidates[ind])
            curr_subset.pop()
            generate(ind + 1, curr_subset, ans, candidates, target)
        ans = []
        generate(0, [], ans, candidates, target)
        return ans

# Combination of Sum 2
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        def generate(ind, curr_subset, target):
            if target == 0:
                ans.append(curr_subset[:])
                return
            if target < 0:
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                curr_subset.append(candidates[i])
                generate(i + 1, curr_subset, target - candidates[i])
                curr_subset.pop()
        generate(0, [], target)
        return ans
