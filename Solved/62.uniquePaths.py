class Solution(object):
    def uniquePaths(self, m, n):
        grid = [[0 for x in range(n+1)] for i in range(2)]
        grid[1][n-1] = 1
        
        curr = n-2
        end = m

        while end > 0:
            grid[0], grid[1] = grid[1], grid[0]
            while curr >= 0:
                grid[0][curr] = grid[0][curr+1] + grid[1][curr]
                curr -= 1 
            end -= 1
            curr = n-1

        return grid[0][0]

def tests(function, extraInfo=False):
    
    tests = [
        (1,1),
        (4,1),
        (3,7),
        (3,2),
        (2,1),
        (1,2),
        (5,5),
        (13,17),
    ]

    results = [1,1,28,3,1,1,70,30421755]

    for index, test in enumerate(tests):
        attempt = function(*test)
        if extraInfo:
            print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
        else:
            print("Passed {}: {}".format(index, results[index] == attempt))
    print()


if __name__ == "__main__":
    solution = Solution()
    tests(solution.uniquePaths)