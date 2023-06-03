"""
Provide 1 of the shortest ways that the values in arr can sum to target.
If they can't, return None.
memoized
"""
def bestSum(target, arr):
    def bestSumHelper(target, arr, memo):
        if target in memo: return memo[target]
        if target == 0: return []
        if target < 0: return None 
        waysToSum = []
        for num in arr:
            remainder = target - num 
            result = bestSumHelper(remainder, arr, memo)
            if result != None:
                result.append(num)
                waysToSum.append(result)

        if waysToSum:
            shortest_list = min(waysToSum, key=len)
            memo[target] = shortest_list.copy()
        else:
            shortest_list=None
            memo[target]=None
        return shortest_list

    memo = {}
    return bestSumHelper(target, arr, memo)

# no memoization
# def bestSum(target, arr):
#     if target == 0: return []
#     if target < 0: return None 
#     waysToSum = []
#     for num in arr:
#         remainder = target - num 
#         result = bestSum(remainder, arr)
#         if result != None:
#             result.append(num)
#             waysToSum.append(result)

#     if waysToSum:
#         shortest_list = min(waysToSum, key=len)
#     else:
#         shortest_list=None
#     return shortest_list

# tests
print(bestSum(8, [1,4,5]))   # [4,4] 
print(bestSum(7, [2,3]))     # [3,2,2] 
print(bestSum(7, [5,3,4,7])) # [7]
print(bestSum(7, [2,4]))     # None  
print(bestSum(8, [2,3,5]))   # [5,3] 
print(bestSum(0, [2,3,4,7])) # []
print(bestSum(1, [2,3,4,7])) # None
print(bestSum(7, [2,3,4,7])) # [7] 
print(bestSum(5, [2,3,4,7])) # [3,2]
print(bestSum(8, [2,3,4,7])) # [4,4] 
print(bestSum(40, [26,7,14,3,2]))  # [14, 26]
print(bestSum(300, [7,14]))  # None
print(bestSum(300, [26,7,14,3,2]))  # [14, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]
