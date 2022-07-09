class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_reuslt = 0
        num1, num2 = 0, 0
        
        # [1,2,1,3,2,5]
        # - 3: 0011
        # - 5: 0101
        # - 3 XOR 5 = 6: 0110
        # Find most right '1' position, because '1' in result of XOR means someone has this position bit and another one do not have it
        # So, we can seperate two group -> [1, 1, 5] and [2 ,3, 3]
        # Finally, use XOR method to get two numbers
        
        for num in nums:
            xor_reuslt ^= num
        
        shift_num = self.get_least_right_pos(xor_reuslt)
        
        for num in nums:
            if self.check_bit(num, shift_num): num1 ^= num
            else:  num2 ^= num      
        return [num1, num2]     
        
    
    def check_bit(self, num, shift):
        if (num & (1 << shift)) != 0: return True
        else: return False
    
    def get_least_right_pos(self, num):
        for shift in range(32):
            if self.check_bit(num, shift):
                return shift