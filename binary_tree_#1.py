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


def display_keys(node, space="\t", level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + "∅")
        return

    # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


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


def traversal_pre_order(node, data=[]):
    if node.key != 0:
        data.append(node.key)
    if node.left != None:
        data = traversal_pre_order(node.left, data)
    if node.right != None:
        data = traversal_pre_order(node.right, data)
    return data


if __name__ == "__main__":
    data = ((1, 3, 0), 2, ((0, 3, 4), 5, (6, 7, 8)))
    tree = create_node_from_tuple(data)
    display_keys(tree)
    # print("richtig: 231534768")
