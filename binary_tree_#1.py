class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right: TreeNode = None
        self.left: TreeNode = None


def create_node_from_tuble(data: tuple) -> TreeNode:
    node = TreeNode(data[1])
    if type(data[0]) == tuple:
        node.left = create_node_from_tuble(data[0])
    if type(data[2]) == tuple:
        node.right = create_node_from_tuble(data[2])
    if type(data[0]) == int:
        node.left = TreeNode(data[0])
    if type(data[2]) == int:
        node.right = TreeNode(data[2])
    return node


if __name__ == "__main__":
    tree = create_node_from_tuble((1, 2, (3, 4, 5)))
    print(tree.left.key, tree.key, tree.right.key)
    print(tree.right.left.key, tree.right.key, tree.right.right.key)
