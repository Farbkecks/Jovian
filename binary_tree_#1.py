class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right: TreeNode = None
        self.left: TreeNode = None


def create_node_from_tuple(data: tuple) -> TreeNode:
    node = TreeNode(data[1])
    if type(data[0]) == tuple:
        node.left = create_node_from_tuple(data[0])
    if type(data[2]) == tuple:
        node.right = create_node_from_tuple(data[2])
    if type(data[0]) == int:
        node.left = TreeNode(data[0])
    if type(data[2]) == int:
        node.right = TreeNode(data[2])
    return node


def create_tuple_from_node(node: TreeNode) -> tuple:
    def check_for_leef(node: TreeNode):
        if node.left == None and node.right == None:
            return True
        else:
            return False

    def get_value_from_note(node: TreeNode):
        if check_for_leef(node):
            return node.key
        else:
            return create_tuple_from_node(node)

    return (get_value_from_note(node.left), node.key, get_value_from_note(node.right))


if __name__ == "__main__":
    data = ((1, 3, 0), 2, ((0, 3, 4), 5, (6, 7, 8)))
    tree = create_node_from_tuple(data)
    # print(tree.left.key, tree.key, tree.right.key)
    # print(tree.right.left.key, tree.right.key, tree.right.right.key)
    reversed_data = create_tuple_from_node(tree)
    print(reversed_data == data)
