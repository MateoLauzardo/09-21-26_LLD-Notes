
class Solution:
    def firstBadVersion(self, n: int) -> int:


        start = 0 
        end = n

        while start <= end:

            middle = (start + end) // 2
            

            if isBadVersion(middle) == False:
                start = middle + 1 

            else:
                end = middle - 1  

            
        return start 


