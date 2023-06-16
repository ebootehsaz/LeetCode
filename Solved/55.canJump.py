def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 0: return False

    target = len(nums)-1
    farthest = nums[0]

    for index, jump in enumerate(nums):
        if farthest >= target: return True
        if index > farthest: return False
        curr = jump + index
        farthest = max(curr, farthest)

    return farthest >= target

tests = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [3,2,1,2,4,3,2,1,2,4,3,2,1,2,4,3,2,1,2,4,3,2,1,2,4],
    [3,2,1,2,4,3,2,1,0,4,3,2,1,2,4,3,2,1,2,4,3,2,1,2,4],
    [],
    [0],
    [0, 0, 0, 0, 5],
    [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6],
]
results = [
    True,
    False,
    True,
    False,
    False, # [],
    True,  # [0],
    False,
    False,
]
extraInfo = False
for index, test in enumerate(tests):
    attempt = canJump(test)
    if extraInfo:
        print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
    else:
         print("Passed {}: {}".format(index, results[index] == attempt))
print()