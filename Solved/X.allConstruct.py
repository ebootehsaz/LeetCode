import copy
"""
all ways can target be contructed using wordbank
memoized
m :- target
n :- wordbank
time:  O(?)
space: O(m^2)
"""
def allConstruct(target, wordbank):
    def allConstructHelper(target, wordbank, memo):
        if target in memo: return memo[target]
        if target == "": return [[]]

        result = []
        for word in wordbank:
            if target.endswith(word):
                remainder = target[:-len(word)]
                combinations = allConstructHelper(remainder, wordbank, memo)
                for combo in combinations:
                    combo.append(word)
                result += combinations
        
        memocopy = copy.deepcopy(result)
        memo[target] = memocopy
        return result
    
    memo = {}
    return allConstructHelper(target, wordbank, memo)


"""
all ways can target be contructed using wordbank
non-memoized
m :- target
n :- wordbank
time:  O(m*n^m)
space: O(m^2)
"""
# def allConstruct(target, wordbank):
#     if target == "": return [[]]

#     result = []
#     for word in wordbank:
#         if target.endswith(word):
#             remainder = target[:-len(word)]
#             combinations = allConstruct(remainder, wordbank)
#             for combo in combinations:
#                 combo.append(word)
#             result += combinations
    
#     return result


print(allConstruct("purple",["purp", "p", "ur", "le", "purpl"]))                                            # 2
print(allConstruct("abcdef",["ab", "abc", "cd", "def", "abcd"]))                                            # 1
print(allConstruct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "boar"]))                             # 0
print(allConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"]))                           # 4
# print(allConstruct("feeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))# 0
# print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeeef", "eeeee"]))# 2621810068