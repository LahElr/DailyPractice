import BinaryTree


tree = BinaryTree.build_tree([3,5,1,6,2,0,8,None,None,7,4])

print(BinaryTree.dfs_tree(tree))

print(BinaryTree.lfs_tree(tree))
print(BinaryTree._lfs_tree(tree))