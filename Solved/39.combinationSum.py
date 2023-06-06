def combinationSum(candidates, target):
    def combinationSumHelper(candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0: return [[]]
        if target < 0: return []

        result = []

        for index, num in enumerate(candidates):
            remainder = target - num
            combinations = combinationSumHelper(candidates[index:], remainder)
            for combo in combinations:
                result.append([num]+ combo)

        return result

    candidates.sort()
    return combinationSumHelper(candidates, target)





print(combinationSum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(combinationSum([2,3,5], 8))   # [[2,2,2,2],[2,3,3],[3,5]]
print(combinationSum([7,3,2], 18))  # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
print(combinationSum([2], 1))       # []
