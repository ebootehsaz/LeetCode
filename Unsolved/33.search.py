"""
O(log N) time to find pivot index
O(log N) binary search on left and right array
altogether 3*O(log N) = O(log N)
"""
def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    def binarySearch(arr, target, lo, hi):
        while hi >= lo:
            mid = (hi + lo) // 2
            if arr[mid] == target:
                return mid 
            elif arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid+1

        return -1

    n = len(nums)
    rightMost = nums[-1]
    if n==1:
        return (0 if nums[0] == target else -1)
    
    lo, hi = 0, n

    while hi >= lo:
        pivot = (hi + lo) // 2

        if nums[pivot] < nums[pivot-1]: # pivot found
            if rightMost < target: # target in left arr
                return binarySearch(nums, target, 0, pivot)
            else: # target in right arr
                return binarySearch(nums, target, pivot, n)

        if nums[pivot] > rightMost: # pivot is to the right
            lo = pivot + 1
        else: # pivot is to the left 
            hi = pivot - 1

    return -1



# tests
# print(search([2,1],1))
# print(search([4,5,6,7,0,1,2],5))
print(search([1],1))

