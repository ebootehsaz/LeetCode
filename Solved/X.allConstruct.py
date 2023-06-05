import copy
"""
all ways can target be contructed using wordbank
memoized
m :- target
n :- wordbank
time:  O(m*(n*n))
space: O(m^2)
"""
def allConstruct(target, wordbank):
    def allConstructHelper(target, wordbank, memo):
        if target in memo: return memo[target]
        if target == "": return [[]]

        result = []
        for word in wordbank:
            if target.endswith(word):
                remainder = target[:-len(word)] # "le"
                combinations = allConstructHelper(remainder, wordbank, memo) # [["purp"], ["pur", "p"]]
                for combo in combinations:
                    result.append(combo + [word])
        
        memo[target] = copy.deepcopy(result)
        return result
    
    memo = {}
    return allConstructHelper(target, wordbank, memo)


"""
all ways can target be contructed using wordbank
non-memoized
m :- target
n :- wordbank
time:  O(n^m)
space: O(m), height of tree
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
print(allConstruct("eeeeeeeeeeeeeeefeeeeeeeeeeeeeeeeeeeeeee",["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))# 0
print(allConstruct("eeeeeeeeeeef",["ef", "ee", "eee", "eeee", "eeeee", "eeeee"])) # unknown
print(len(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeef",["e", "ee", "eee", "eeee", "eeeeef", "eeeee"]))) # 203513


"""
Without Dynamic Programming:
When the problem is solved without dynamic programming, the time complexity can be exponential. 
This is because the recursive solution explores all possible combinations by considering 
each word in the word bank for each position in the target string. 
In the worst case, if the word bank consists of single-character words and the target 
string has length n, the number of recursive calls can be on the order of O(m^n), 
where m is the length of the word bank. Each recursive call can take O(n) time to 
construct the remainder of the target string by removing a word, resulting in a total time complexity of O(m^n * n).

With Dynamic Programming (Memoization):
By applying dynamic programming with memoization, the time complexity can be significantly improved. 
Memoization allows us to store previously computed results and reuse them when needed, avoiding redundant computations.
With memoization, the time complexity of allConstruct is reduced to O(m * n * t), where m is the length of the word bank, 
n is the length of the target string, and t is the number of unique subproblems. 
The t term represents the number of distinct target strings that are encountered during the recursive calls. 
Since we store the results of each subproblem in the memoization table, we can avoid redundant 
computations for the same target string. As a result, the time complexity is greatly reduced compared to the non-DP solution.
"""