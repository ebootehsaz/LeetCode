def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    setOfAnograms = {}

    for str in strs:
        key = tuple(sorted(str))
        if key in setOfAnograms:
            setOfAnograms[key] = setOfAnograms[key] + [str]
        else:
            setOfAnograms[key] = [str]

    return list(setOfAnograms.values())




tests = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]

for test in tests:
    print("\nTest: {} \nResult: {}".format(test, groupAnagrams(test)))
print()