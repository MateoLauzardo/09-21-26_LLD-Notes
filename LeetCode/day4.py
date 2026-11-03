
#! Two Pointer - a technique that uses two index variables to traverse a linear data structure—such as an:
#! array, string, or list—to solve problems efficiently in linear time



# ---------------------------------------------------------------------------------------------

# Write a function has_pair_sum() that takes in a sorted list of integers nums and an integer target as parameters.
# Return True if there are two different elements in nums that add up to target. 
# Return False otherwise.
# Use two pointers, one starting at the beginning of the list and one at the end, to solve this without checking every possible pair.

def has_pair_sum(nums, target):
    
    start = 0 
    end = len(nums) - 1 
    
    while start < end:
        
        current_sum = nums[start] + nums[end]
        
        if current_sum < target:
            start += 1
            
        if current_sum > target:
            end -= 1
            
        if current_sum == target:
            return True
    
    
    return False 
        

# Example Usage:
nums = [1, 3, 4, 6, 9]
# print(has_pair_sum(nums, 10))
# print(has_pair_sum(nums, 7))
# print(has_pair_sum(nums, 2))


# Example Output:
# True
# True
# False




# ---------------------------------------------------------------------------------------------


# Write a function reverse_list() that takes in a list lst as a parameter and reverses it in place, 
# without using the built-in reverse() method, slicing ([::-1]), or creating a new list. 
# Use two pointers, one starting at the first element and one at the last, swapping elements as the pointers move toward each other. 
# The function should return the reversed list.

def reverse_list(lst):
    
    first = 0 
    end = len(lst) - 1
    
    answer = [] 
    
    while first <= end:
        answer.append(lst[end])
        end -= 1 
        
    return answer 
    
    
    

lst_1 = [1, 2, 3, 4, 5]
lst_2 = ["a", "b", "c", "d"]
lst_3 = [7]
# print(reverse_list(lst_1))
# print(reverse_list(lst_2))
# print(reverse_list(lst_3))

# [5, 4, 3, 2, 1]
# ['d', 'c', 'b', 'a']
# [7]


# ---------------------------------------------------------------------------------------------


# Write a function move_zeros() that takes in a list of integers nums as a parameter 
# and moves all the 0s to the end of the list while keeping the order of the non-zero elements the same. 
# Modify the list in place, without creating a new list. 
# Use two pointers: one that scans through every element, and one that tracks the position where the next non-zero element should go. 
# The function should return the modified list.

def move_zeros(nums):
    
    start = 0 
    
    # x is your second pointer     
    for x in range(len(nums)):
        
        if nums[x] != 0: 
            nums[x], nums[start] = nums[start], nums[x]     
            start += 1 
                    
    return nums
    
nums_1 = [0, 1, 0, 3, 12]
nums_2 = [4, 0, 0, 2]
nums_3 = [0, 0, 0]
print(move_zeros(nums_1))
print(move_zeros(nums_2))
print(move_zeros(nums_3))


# [1, 3, 12, 0, 0]
# [4, 2, 0, 0]
# [0, 0, 0]