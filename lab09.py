# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
   


def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_prof = 0
    
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        
        current_profit = prices[i] - min_price
        if current_profit > max_prof:
            max_prof = current_profit
            
    return max_prof


def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        if current_sum + nums[i] < nums[i]:
            current_sum = nums[i]
        else:
            current_sum = current_sum + nums[i]
            
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    stack = []
    
    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '}':
            if len(stack) == 0:
                return False
            
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            if char == ']' and top != '[':
                return False
            if char == '}' and top != '{':
                return False
                
    return len(stack) == 0


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass

if __name__ == "__main__":
    main()
