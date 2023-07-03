#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> seenMap;
        unordered_map<char, int> needMap;
        int fPtr = 0, bPtr = 0;

        int lenOfS = s.length();
        int lenOfT = t.length();

        for (int i = 0; i < lenOfT; ++i) {
            char letter = t[i];
            needMap[letter] = needMap[letter] + 1;
        }

        int left = 0, right = -1; // will be index when minWindow is found
        int matchedCount = 0;

        while (fPtr < lenOfS) {
            char currLetter = s[fPtr];
            int timesNeeded = needMap[currLetter];
            int timesSeen = seenMap[currLetter];

            if (timesNeeded) {
                if (timesNeeded > timesSeen) {
                    ++matchedCount;
                }
                seenMap[currLetter] = seenMap[currLetter] + 1;
            }
            
            while (matchedCount >= lenOfT) {
                char lastLetter = s[bPtr];
                timesNeeded = needMap[lastLetter];
                timesSeen = seenMap[lastLetter];

                if (fPtr - bPtr < right - left || right == -1) {
                    right = fPtr;
                    left = bPtr;
                }

                if (timesNeeded) {
                    if (timesSeen == timesNeeded) {
                        --matchedCount;
                    }
                    seenMap[lastLetter] = seenMap[lastLetter] - 1;
                }
                    ++bPtr;
            }
            ++fPtr;
        }
        return s.substr(left, right-left+1);
    }
};


int main() {
    Solution* solution = new Solution();

    string s = "ADOBECODEBANC"; 
    string t = "ABC";
    cout << solution->minWindow(s,t) << endl; // Output: "BANC"
    
    s = "a"; 
    t = "a";
    cout << solution->minWindow(s,t) << endl; // Output: "a"

    s = "a"; 
    t = "aa";
    cout << solution->minWindow(s,t) << endl; // Output: ""

    s = "aaflslflsldkalskaaa";
    t = "ala";
    cout << solution->minWindow(s,t) << endl; // Output: "aafl"

}