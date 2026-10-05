
#NOTE: Question 5) 

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarray_sum(nums, k):
    
    count = 0 
    
    #[1, 2, 3]
    for x in range(len(nums)):
        
        total = 0
        
        for z in range(x, len(nums)):
        
            #addition
            total += nums[z]
            
            if total == k:
                count += 1
                
            
    return count 


answer5 = subarray_sum([1, 2, 3], 3)     
# print(answer5)
    
                
# Example Usage:

# Example #1:
# Input: nums = [1, 1, 1], k = 2
# Output: 2

# Example #2:
# Input: nums = [1, 2, 3], k = 3
# Output: 2

#________________________________________________________________________________________

#NOTE: Question 6) 

# Given an integer array nums
# return True if any value appears at least twice in the array
# and return False if every element is distinct.


def contains_duplicate(nums):
    
    hashmap = {}
 
    for num in nums:
        if num in hashmap:
            return True
        else:
            hashmap[num] = 1
            
        
    return False 

answer6 = contains_duplicate([1,2,3,4])
# print(answer6)

# Example #1: 
# Input: nums = [1,2,3,1]
# Output: True

# Example #2:
# Input: nums = [1,2,3,4]
# Output: False

# Example #3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: True

#________________________________________________________________________________________

#NOTE: Question 7) 

# Given a list of integers nums and an integer val,
# remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.


# Consider the number of elements in nums which are not equal to val be k, 
# for your response to be acceptable, you need to do the following things:

# Change the list nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k

def remove_element(nums, val):
    
    hold_numbers = []
    
    # loop thoughr nums
    # keep count of when nums != val 
    # save those values in a new list 
    # once your done loop grab len of list - len of nums
    # in loop thorough said value to add_'s
    
    for num in nums:
        if num != val:
            hold_numbers.append(num)
        
    dif = abs(len(nums) - len(hold_numbers))
    
    for x in range(dif):
        hold_numbers.append("_")
        
    return hold_numbers 
        
    
        
answer7 = remove_element([0,1,2,2,3,0,4,2], 2)
print(answer7)

# Example #1:
# Input: nums = [3,2,2,3], val = 3
# Expected Output: 2
# nums should be [2,2,_,_]
# Explanation: Your function should return k = 2,
# with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


#________________________________________________________________________________________
