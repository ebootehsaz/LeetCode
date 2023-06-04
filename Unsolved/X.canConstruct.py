"""
given a wordbank, can target word be constructed
"""
def canConstruct(target, wordbank):
    if target == "": return True

    for word in wordbank:
        if target.endswith(word):
           remainder = target[:-len(word)]
           if canConstruct(remainder, wordbank):
               return True

    return False     


print(canConstruct("abcdef",["ab", "abc", "cd", "def", "abcd"]))                                            # true
print(canConstruct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "boar"]))                             # false
print(canConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"]))                           # true
print(canConstruct("feeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))# false
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeeef", "eeeee"]))# true