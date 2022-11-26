class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Runtime 904 ms, Beats 75.12% 
        Memory 30.1 MB, Beats 47.44%
        """
        # sort + binary serach + dp
        dp = [[0,0]] # end_idx, total_profit
        data = list(zip(startTime, endTime, profit))
        data.sort(key=lambda x: x[1])

        def get_total_profit(idx):
            idx = bisect_left(dp, [idx+1])
            return dp[idx-1][1]

        for idx in range(0, len(profit)):
            start_time_idx, end_time_idx, tmp_profit = data[idx][0], data[idx][1], data[idx][2]
            total_profit = max(get_total_profit(end_time_idx), get_total_profit(start_time_idx)+tmp_profit)
            dp.append([end_time_idx, total_profit])

        return dp[-1][1]