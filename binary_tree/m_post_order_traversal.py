######################################################################
# LeetCode Problem Number : 145
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/binary-tree-postorder-traversal/
######################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # runtime --> 77.59%, memory --> 50.59%
    def postOrderRecursive(self, root: TreeNode) -> [int]:
        if not root:
            return []

        res = []

        """ post - order traversal

            visit left sub - tree
            visit right sub - tree
            visit node
        """
        res += self.postOrderRecursive(root.left)
        res += self.postOrderRecursive(root.right)
        res.append(root.val)

        """ return visited node + child nodes """
        return res

    def postorderTraversal(self, root: TreeNode) -> [int]:
        if not root:
            return []

        ret = []

        """ on visiting a node, push 2 copies to the stack.

            use 1st copy to process the child nodes
            use 2nd copy to insert into result
        """
        st = [root] * 2

        while st:
            cur = st.pop()

            """ if current node is the last node in the stack,
                then visit it's child nodes

                if current node is not the last node in the stack,
                then current node is the 2nd copy. Insert node into
                result list
            """
            if st and st[-1] is cur:
                """insert right child node followed by left.

                this ensures processing is done from left to right.
                """
                if cur.right:
                    st += [cur.right] * 2
                if cur.left:
                    st += [cur.left] * 2
            else:
                ret.append(cur.val)

        return ret
