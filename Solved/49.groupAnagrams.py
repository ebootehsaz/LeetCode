from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    setOfAnograms = defaultdict(list)

    for str in strs:
        key = ''.join(sorted(str))
        setOfAnograms[key].append(str)

    return list(setOfAnograms.values())


tests = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"]
]

for test in tests:
    print("\nTest: {} \nResult: {}".format(test, groupAnagrams(test)))
print()