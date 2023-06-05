"""
how many times can target be contructed using wordbank
memoized
m :- target
n :- wordbank
time: O()
space: O()
"""
def countConstruct(target, wordbank):
    def countConstructHelper(target, wordbank, memo):
        if target in memo: return memo[target]
        if target == "": return 1

        count = 0
        for word in wordbank:
            if target.endswith(word):
                remainder = target[:-len(word)]
                subCount = countConstructHelper(remainder, wordbank, memo)
                count += subCount
        
        memo[target]=count
        return count
    
    memo={}
    return countConstructHelper(target, wordbank, memo)



"""
how many times can target be contructed using wordbank
non-memoized
m :- target
n :- wordbank
time:  O(m*n^m)
space: O(m^2)
"""
# def countConstruct(target, wordbank):
#     if target == "": return 1

#     count = 0
#     for word in wordbank:
#         if target.endswith(word):
#             remainder = target[:-len(word)]
#             subCount = countConstruct(remainder, wordbank)
#             count += subCount
    
#     return count


print(countConstruct("purple",["purp", "p", "ur", "le", "purpl"]))                                            # 2
print(countConstruct("abcdef",["ab", "abc", "cd", "def", "abcd"]))                                            # 1
print(countConstruct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "boar"]))                             # 0
print(countConstruct("enterapotentpot",["a", "p", "ent", "enter", "ot", "o", "t"]))                           # 4
print(countConstruct("feeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))# 0
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeeef", "eeeee"]))# x