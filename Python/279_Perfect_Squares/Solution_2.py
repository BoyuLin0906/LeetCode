from math import isqrt, floor

class Solution:
    def numSquares(self , n):
        
        # Single Square
        if isqrt(n)**2 == n : return 1
        # Fermat's Two Square Theorem
        for i in range(1, isqrt(n)+1):
            val_square = i**2
            j = n - val_square
            if isqrt(j)**2 == j : return 2
        
        # Legendre's Four Square Theorem 4^a*(8b+7)
        while n % 4 == 0: n /= 4                    
        if n % 8 == 7:  return 4                  
        
        return 3   