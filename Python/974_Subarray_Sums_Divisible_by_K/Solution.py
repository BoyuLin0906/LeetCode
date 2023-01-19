class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_dict = collections.defaultdict(int)
        prefix_dict[0] = 1

        # prefix_dict[i] % k == prefix_dict[j] % k
        for num in nums:
            prefix_sum += num
            count += prefix_dict[prefix_sum % k]
            prefix_dict[prefix_sum%k] += 1

        return count