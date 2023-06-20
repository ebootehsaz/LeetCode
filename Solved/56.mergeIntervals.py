class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(intervals): return intervals

        intervals = sorted(intervals)

        begin, end = intervals[0][0], intervals[0][1]
        result = []

        for index in range(1, len(intervals)):
            left, right = intervals[index][0], intervals[index][1]
            if left <= end:
                end = max(end, right)
            else:
                result.append([begin, end])
                begin, end = left, right

        result.append([begin, end])

        return result




def tests(function, extraInfo=False):
    
    tests = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,3],[0,6],[8,10],[15,18]],
        [[1,4],[4,5]],
        [[1,4]],
    ]

    results = [
        [[1,6],[8,10],[15,18]],
        [[0,6],[8,10],[15,18]],
        [[1,5]],
        [[1,4]],
    ]

    for index, test in enumerate(tests):
        attempt = function(test)
        if extraInfo:
            print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
        else:
            print("Passed {}: {}".format(index, results[index] == attempt))
    print()

if __name__ == "__main__":
    solution = Solution()
    tests(solution.merge, 0)


# [[1,3],[2,6],[8,10],[15,18]] # [[1,6],[8,10],[15,18]]

# [[1,4],[4,5]] # [[1,5]]