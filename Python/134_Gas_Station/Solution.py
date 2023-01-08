class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Runtime 677 ms / Beats 92.20%
        Memory 19 MB / Beats 90.40%
        """
        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_gas < total_cost: return -1

        route_len = len(gas)
        start_idx = 0
        gas_amount = 0
        for idx in range(route_len):
           gas_amount = gas_amount + gas[idx] - cost[idx]
           
           if gas_amount < 0:
               gas_amount = 0
               start_idx = idx + 1

        return start_idx