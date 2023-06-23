# key: given non-overlapping intervals
"""
:type intervals: List[List[int]]
:type newInterval: List[int]
:rtype: List[List[int]]
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            intervals.pop(i)

        intervals.insert(i, newInterval)
        return intervals


def tests(function, extraInfo=False):    
    tests = [
        ([[1,3],[6,9]], [4,10]),
        ([[1,3],[6,9],[11,15]], [5,10]),
        ([[1,3],[6,9]], [5,8]),
        ([[1,3],[6,9]], [2,5]),
        ([[1,3],[6,9]], [0,1]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
    ]

    results = [
        [[1,3],[4,10]],
        [[1,3],[5,10],[11,15]],
        [[1,3],[5,9]],
        [[1,5],[6,9]],
        [[0,3],[6,9]],
        [[1,2],[3,10],[12,16]],
    ]

    for index, test in enumerate(tests):
        attempt = function(*test)
        if extraInfo:
            print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
        else:
            print("Passed {}: {}".format(index, results[index] == attempt))
    print()


if __name__ == "__main__":
    solution = Solution()
    tests(solution.insert)