
# NOTE: Question 1.)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
# return True if the input string is valid and False otherwise.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def is_valid(s: str):
	
    stack = []
    
    for char in s:
        if char in "([{":
            stack.append(char)
            
        else:
            if char == "}":
                if stack[-1] == "{":
                    stack.pop()
            
            if char == "]":
                if stack[-1] == "[":
                    stack.pop()
            
            if char == ")":
                if stack[-1] == "(":
                    stack.pop()
            
    return len(stack) == 0 
    
    
    
    # add every instance of "[,{, (" to the stack
    # if its not that, than we are going to grab last thing in the stack and see if its the opposite 
    # if it is, pop that from stack and continue 
    # if not return False


# answer = is_valid("(]")
# print(answer)

# Example #2:
# s = "()[]{}"
# Expected Output: True

#________________________________________________________________________________________


#NOTE: Question 2.)
# You are given a list of integers prices where prices[i] is the price of a given stock on the "i"th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the "maximum" profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def max_profit(prices: list):

    # loop through prices
    # have a variable to store max_profit = 0
    # loop and look for lowest # and save it in varaible 
    # each iteration we subtract lowest from the next number, and if its greater than max replace it
    # return max 
    
    highest_profit = 0 
    lowest_value = prices[0]
    
    for price in prices:
        
        if price < lowest_value:
            lowest_value = price
            
        highest_profit = max(highest_profit, price - lowest_value)
        
        
    return highest_profit



# answer2 = max_profit([7,6,4,3,1])
# print(f"max profit is: {answer2}")

    


# Example #1:
# Input: prices = [7,1,5,3,6,4]
# Expected Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


#________________________________________________________________________________________


#NOTE: Question 3 
# Given the heads of two singly linked lists of integers, merge 
# their nodes to make one list. 

# taking nodes alternately between the two lists. 

# If either list runs out of elements before the 
# other, all nodes from the list with remaining nodes should be 
# appended onto the end of the merged list. 

# Return the head of the merged list.


class Node():
    def __init__(self, val:int):
        self.val = val 
        self.next = None

        
node1_1 = Node(1)
node1_2 = Node(2)
node1_3 = Node(3)
node1_1.next = node1_2
node1_2.next = node1_3


class Node2():
    def __init__(self, val:int):
        self.val = val
        self.next = None 

node2_1 = Node(4)
node2_2 = Node(5)
node2_3 = Node(6)
node2_1.next = node2_2
node2_2.next = node2_3




def shuffle_merge(head_a, head_b):
	
    
    # create a new empty linked list to store new values 
    # while there values to traverse from list 1 and 2 
    # add value from list 1 to new list and value from list 2 to new list
    # once while loop ends, make if statement if list1 -> add values
    # underneath if list2 -> add values 
    
    new_list = Node(0)
    current = new_list
    
    while head_a and head_b:
        
        current.next = head_a
        current = current.next         
        head_a = head_a.next
 
        
        current.next = head_b
        current = current.next     
        head_b = head_b.next 

        
    if head_a:
        current.next = head_a
        current = current.next 

    if head_b:
        current.next = head_b
        current = current.next 
        
    
    return new_list.next
    
    

# saves value of the head
answer3 = shuffle_merge(node1_1, node2_1)


result = ""

# while answer3:
#     result += f"{str(answer3.val)} -> "
#     answer3 = answer3.next 
    
# print(result)


# Input Lists: List 1: 1 —> 2 —> 3, List 2: 4 —> 5 —> 6
# Input: head_a = 1, head_b = 4
# Expected Return value: 1
# Expected Result List: 1 —> 4 —> 2 —> 5 —> 3 —> 6

#________________________________________________________________________________________


# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the 
# letters of a different word or phrase, typically using all the 
# original letters exactly once.

def group_anagrams(strs:list[str]):
    
    # loop through strs 
    # hashmap = {bat: 1, tan: 2, ate: 3
    # if new i would make list []
    # if value matches with a value from hashmap, append it to list 
    # one list = to all the ther other list  
    
    hashmap = {}
    answer = []
    
    # hashmap: [abt: bat / atn: nat, tan / aet: ate, eat, tea]
    for word in strs:
        sorted_word = "".join(sorted(word))
        
        if sorted_word in hashmap:
            hashmap[sorted_word] += [word]
        else:
            hashmap[sorted_word] = [word]
        

    for key, value in hashmap.items():
        answer.append(value)
    
    
    # return hashmap
    return answer 



answer4 = group_anagrams(["eat","tea","tan","ate","nat","bat"])
print(answer4)


# Example #1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Expeced Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

#________________________________________________________________________________________