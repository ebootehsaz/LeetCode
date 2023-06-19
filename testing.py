def tests(function, extraInfo=False):
    
    tests = []

    results = []

    for index, test in enumerate(tests):
        attempt = function(test)
        if extraInfo:
            print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
        else:
            print("Passed {}: {}".format(index, results[index] == attempt))
    print()


if __name__ == "__main__":
    solution = Solution()
    tests(solution.__funcName__)