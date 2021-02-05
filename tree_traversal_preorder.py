class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while True:
            while root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            root = node.right