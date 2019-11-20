class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, _root):
        traverse_list = []
        print_elements = []
        if _root is not None:
            traverse_list.append(_root)
        while len(traverse_list) != 0:
            _root = traverse_list.pop(0)
            if _root is not None:
                print_elements.append(_root.data)
            if _root.left is not None:
                traverse_list.append(_root.left)
            if _root.right is not None:
                traverse_list.append(_root.right)
        print(' '.join([str(item) for item in print_elements]))


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    myTree.levelOrder(root)
