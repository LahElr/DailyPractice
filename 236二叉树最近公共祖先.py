r'''
公共祖先尽可能靠下
一个节点可以是它自己的祖先
题目保证所有节点都不同
'''
from BinaryTree import TreeNode,build_tree,search_in_tree

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # 0: 都没有
        # 1: 有p无q
        # 2: 有q无p
        if root is None:
            return 0
        lres = self.lowestCommonAncestor(root.left,p,q)
        rres = self.lowestCommonAncestor(root.right,p,q)
        if isinstance(lres,TreeNode):
            return lres
        if isinstance(rres,TreeNode):
            return rres

        if root == p:
            if lres == 2 or rres == 2:
                return root
            else:
                return 1
        if root == q:
            if lres == 1 or rres ==1:
                return root
            else:
                return 2
        if lres+rres ==3:
            return root
        return lres+rres


data = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
tree = build_tree(data)
p = search_in_tree(tree,p)
q = search_in_tree(tree,q)
print(Solution().lowestCommonAncestor(tree,p,q).val)