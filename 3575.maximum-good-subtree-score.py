from typing import List
from collections import defaultdict

#
# @lc app=leetcode id=3575 lang=python3
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:

        n = len(vals)
        tree = defaultdict(list)
        root = -1
        for i in range(n):
            if par[i] == -1:
                root = i
            else:
                tree[par[i]].append(i)

        def dfs(u):
            total = vals[u]
            for v in tree[u]:
                child_sum = dfs(v)
                total += child_sum
            self.max_score = max(self.max_score, total)
            return total

        self.max_score = 0
        dfs(root)
        return self.max_score
# @lc code=end

