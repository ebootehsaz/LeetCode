def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree_from_list(lst):
    if not lst:
        return None

    # Create a queue to store TreeNode objects
    queue = []

    # Create the root node
    root = TreeNode(lst[0])
    queue.append(root)

    i = 1
    while i < len(lst):
        node = queue.pop(0)

        # Create the left child
        if lst[i] is not None:
            left_child = TreeNode(lst[i])
            node.left = left_child
            queue.append(left_child)
        i += 1

        # Create the right child
        if i < len(lst) and lst[i] is not None:
            right_child = TreeNode(lst[i])
            node.right = right_child
            queue.append(right_child)
        i += 1

    return root


def tests(function, extraInfo=False):
    
    
    tests = [ 
        create_tree_from_list([1, 2, 3, 4, None, 5, 6]),
        create_tree_from_list([3,9,20,None,None,15,7]),
        create_tree_from_list([1, None, 3]),
        create_tree_from_list([3,9,20,None,None,15,7,8,None,None,None,None,None]),
        ]

    results = [
        3,
        3,
        2,
        4,
    ]

    print()
    for index, test in enumerate(tests):
        attempt = function(test)
        if extraInfo:
            print("\nTest: {} \nAttempt: {} \nPassed: {}".format(test, attempt, results[index] == attempt))
        else:
            print("Passed {}: {}".format(index, results[index] == attempt))
    print()

if __name__ == "__main__":
    tests(maxDepth)