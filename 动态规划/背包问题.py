class Solution:
    '''0,1 背包问题，每个物体不重复'''
    def func(self, weight, value, bagWeight):
        dp =[[0]*(bagWeight+1) for i in range(len(weight)+1)]
        # dp[i][j]: 前i个物体中，背包重为j，能装下的最大价值
        for i in range(1, len(weight)+1):
            for j in range(1, bagWeight+1):
                if j < weight[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+value[i-1])
        return dp

    '''完全背包问题，每个物体可以重复'''
    def func_all(self, weight, value, bagWeight):
        dp = [0]*(bagWeight + 1)
        # dp[i] : 背包重i的情况下，能装下的最大价值
        for i in range(bagWeight+1):
            for j in range(len(weight)):
                if weight[j] > i:
                    continue
                dp[i] = max(dp[i], dp[i-weight[j]] + value[j])
        return dp


if __name__ == '__main__':
    s = Solution()
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    print(s.func(weight, value, bagWeight))
    print(s.func_all(weight, value, bagWeight))

