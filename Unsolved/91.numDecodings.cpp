#include <string>

using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        int p1 = 0, p2 = 1, p3 = 0;

        for(int i = 0; i < s.size(); ++i) {
            p3 = p2 + p1;
            p1 = p2;
            p2 = p3;
        }

        return p3;


    }
};