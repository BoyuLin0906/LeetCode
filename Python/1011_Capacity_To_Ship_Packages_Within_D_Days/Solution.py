class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Runtime 430 ms / Beats 98.8%
        Memory 17 MB / Beats 97.87%
        
        (N : number of weights, S : total weight of all the packages)
        time complexity : O(N*log(S-max(weights)))
        space complexity : O(1)
        """
        # get min ship capacity, and total weight
        left_value = max(weights)
        right_value = sum(weights)

        def can_ship_in_target_days(ship_capacity):
            shipping_day = 0
            temp_ship_capacity = ship_capacity
            # get shipping day
            for weight in weights:
                if temp_ship_capacity < weight:
                    temp_ship_capacity = ship_capacity
                    shipping_day += 1
                temp_ship_capacity -= weight
            return shipping_day+1 <= days

        # binary search
        while left_value < right_value:
            mid_value = (left_value + right_value) // 2
            if can_ship_in_target_days(mid_value):
                # too fast, then reduce weight
                right_value = mid_value
            else:
                # too slow, then increase weight
                left_value = mid_value + 1
            
        return left_value