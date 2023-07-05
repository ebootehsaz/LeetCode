#include <iostream>
#include <vector>
#include "../TreeNode.h"

using namespace std;

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) { return 1; }
        else if (!p || !q || p->val != q->val) { return 0; }
        else {
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};


int main() {
    Solution solution;


    vector<int> l1{ 1, 2, 3 };
    vector<int> l2 = {1, 2, 3};
    TreeNode* p = TreeNode::createTreeFromList(l1);
    TreeNode* q = TreeNode::createTreeFromList(l2);

    cout << solution.isSameTree(p, q) << endl;
}