#include <iostream>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n==1) {return 1;}

        int p1 = 1;
        int p2 = 2, curr = 2;
        n = n - 2;

        while (n > 0) {
            curr = p2 + p1;
            p1 = p2;
            p2 = curr;
            --n;
        }

        return curr;
    }
};

int main() {
    Solution* solution = new Solution();
    int limit = 45;

    for(int j = 1; j < limit; j = j*2) {
        cout << solution->climbStairs(j) << "\n";
    }
    cout << solution->climbStairs(limit) << "\n";
}
