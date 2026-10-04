
#NOTE: Question 1.) Given an integer array nums, return True if any value appears at least twice in the array, and return False if every element is distinct.

def contains_duplicate(nums):
	
    hashmap = {}
    
    for num in nums:
        
        if num in hashmap:
            return True
        else:
            hashmap[num] = 1
            
        
    return False     
    
        

answer1 = contains_duplicate([1,2,3,])
# print(answer1)



# Example Usage:
# Example #1: 
# Input: nums = [1,2,3,1]
# Output: True

# Example #2:
# Input: nums = [1,2,3,4]
# Output: False


#________________________________________________________________________________________

#NOTE: Question 2) 

# Given a list of integers nums and an integer val, remove all occurrences of val in nums in-place. 

# The order of the elements may be changed. 

# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, for your response to be acceptable, you need to do the following things:

# - Change the list nums such that the first k elements of nums contain the elements which are not equal to val. 
# - The remaining elements of nums are not important as well as the size of nums.
# - Return k


def remove_element(nums: list[int], val: int):
	
    # [2, 2]
    list = []
    
    k = 0 
    
    for num in nums:
        if num == val:
            continue 
        else:
            list.append(num)

    for values in list:
        k += 1 
        
    
    return k 
        

answer2 = remove_element([0,1,2,2,3,0,4,2], 2)
# print(answer2)


# Example #1:
# Input: nums = [3,2,2,3], val = 3
# Expected Output: 2 -> the amount of numbers left that are NOT val
# nums should be [2,2,_,_]
# Explanation: Your function should return k = 2,
# with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


#________________________________________________________________________________________


#NOTE: Question 3) 

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

from math import gcd

def gcd_of_stings(str1, str2):
 
    
    # Step 1: if a common chunk exists, both orders give the same string
    if str1 + str2 != str2 + str1:
        return ""

    # Step 2: (gives you the SIZE of common chuncks) -> returns 3
    length = gcd(len(str1), len(str2))

    # Step 3: slice that many characters off the front
    return str1[:length]
     
    
        



answer3 = gcd_of_stings("ABCABC", "ABC")
# print(answer3)


# Example #1:
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"


#________________________________________________________________________________________




            
#________________________________________________________________________________________


