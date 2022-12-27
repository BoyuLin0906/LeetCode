class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        Runtime 973 ms / Beats 84.87%
        Memory 21.7 MB / Beats 99.34%
        """
        rocks_len = len(rocks)
        count = 0

        for idx in range(rocks_len):
            capacity[idx] -= rocks[idx]
        capacity.sort()

        for idx in range(rocks_len):

            if additionalRocks >= capacity[idx]:
                additionalRocks -= capacity[idx]
                capacity[idx] = 0
                count += 1
            else:
                break

        return count