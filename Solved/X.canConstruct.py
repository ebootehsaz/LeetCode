"""
given a wordbank, can target word be constructed
memoized
"""
def canConstruct(target, wordbank):
    def canConstructHelper(target, wordbank, memo):
        if target in memo: return memo[target]
        if target == "": return True

        for word in wordbank:
            if target.endswith(word):
                remainder = target[:-len(word)]
                if canConstructHelper(remainder, wordbank, memo):
                    memo[target] = True
                    return True

        memo[target] = False
        return False
    
    memo = {}
    return canConstructHelper(target, wordbank, memo)
"""
n :- target
m :- wordbank
time: O(m*n^2)
space: O(n^2)
"""  


# no memo
# def canConstruct(target, wordbank):
#     if target == "": return True

#     for word in wordbank:
#         if target.endswith(word): # extra n time
#            remainder = target[:-len(word)]
#            if canConstruct(remainder, wordbank):
#                return True

#     return False   
"""
n :- target
m :- wordbank
time: O(n*m^n)
space: O(n^2)
"""  



print(canConstruct("abcdef",["ab", "abc", "cd", "def", "abcd"]))                                            # true
print(canConstruct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "boar"]))                             # false
print(canConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"]))                           # true
print(canConstruct("feeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))# false
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeeef", "eeeee"]))# true