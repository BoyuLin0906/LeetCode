from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    	"""
    	Runtime: 96 ms, faster than 98.18% of Python3 online submissions for Group Anagrams.
		Memory Usage: 17.2 MB, less than 80.96% of Python3 online submissions for Group Anagrams.
    	"""
        if len(strs) == 1: return [strs]
        
        str_dict = defaultdict(list)
        
        for _str in strs:
             str_dict[''.join(sorted(_str))].append(_str)
        
        res = list()
        for _, str_list in str_dict.items():
            res.append(str_list)
            
        return res