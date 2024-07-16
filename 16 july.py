# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'

    def getDirections(self, root: Optional[TreeNode], start_value: int, dest_value: int) -> str:

        def _dfs(node, prev):
            if node is None:
                return None

            if prev is not None:
                parent[node] = prev

            if node.val == start_value:
                return node

            return _dfs(node.left, node) or _dfs(node.right, node)

        def _reconstruct_path(node, prev):
            path = deque()
            while node in prev.keys():
                path.appendleft(prev[node][1])
                node = prev[node][0]
            return ''.join(path)

        def _get_path(node):
            queue = deque([node])
            seen = set([node])
            path = dict()
            while queue:
                node = queue.popleft()

                if node.val == dest_value:
                    return _reconstruct_path(node, path)

                if node.left and node.left not in seen:
                    path[node.left] = (node, self.LEFT)
                    seen.add(node.left)
                    queue.append(node.left)
                if node.right and node.right not in seen:
                    path[node.right] = (node, self.RIGHT)
                    seen.add(node.right)
                    queue.append(node.right)
                if node in parent.keys() and parent[node] not in seen:
                    path[parent[node]] = (node, self.UP)
                    seen.add(parent[node])
                    queue.append(parent[node])

            return ''

        parent = dict()
        start = _dfs(root, None)
        return _get_path(start)
