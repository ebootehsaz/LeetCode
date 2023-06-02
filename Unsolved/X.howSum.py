"""
Provide 1 way that the values in arr can sum to target.
If they can't, return None.
Memoized version
"""
def howSum(target, arr, memo={}):
    if target == 0: return []
    if target < 0:  return None 
    if target in memo: return memo[target]
    
    for num in arr:
        remainder = target - num 
        result = howSum(remainder, arr)
        if result != None:
            result.append(num)
            memo[target] = result
            return result
        
    return None



# tests
print(howSum(0, [2,3,4,7])) # []
print(howSum(1, [2,3,4,7])) # None
print(howSum(7, [2,3,4,7])) # [3,2,2] 
print(howSum(5, [2,3,4,7])) # [3,2]
print(howSum(8, [2,3,4,7])) # [2,2,2,2] 
print(howSum(300, [7,14]))  # None

# howSum No Memoization
# def howSum(target, arr):
#     if target == 0: return []
#     if target < 0:  return None 

#     for num in arr:
#         remainder = target - num 
#         result = howSum(remainder, arr)
#         if result != None:
#             result.append(num)
#             return result
        
#     return None