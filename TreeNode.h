#ifndef TREENODE_H
#define TREENODE_H

#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
    static TreeNode* createTreeFromList(const std::vector<int>& nums, int start, int end);
    static TreeNode* createTreeFromList(const std::vector<int>& nums);
};

inline TreeNode* TreeNode::createTreeFromList(const std::vector<int>& nums, int start, int end) {
    if (start > end) {
        return nullptr;
    }

    int mid = (start + end) / 2;
    TreeNode* root = new TreeNode(nums[mid]);
    root->left = createTreeFromList(nums, start, mid - 1);
    root->right = createTreeFromList(nums, mid + 1, end);

    return root;
}

inline TreeNode* TreeNode::createTreeFromList(const std::vector<int>& nums) {
    int n = nums.size();
    return createTreeFromList(nums, 0, n - 1);
}

#endif 