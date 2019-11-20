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

    def getHeight(self, root):
        if root is None:
            return 0
        else:
            if root.right is not None:
                height_right = 1 + self.getHeight(root.right)
            else:
                height_right = 0
            if root.left is not None:
                height_left = 1 + self.getHeight(root.left)
            else:
                height_left = 0
            return max(height_right, height_left)


if __name__ == '__main__':
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    height = myTree.getHeight(root)
    print(height)
