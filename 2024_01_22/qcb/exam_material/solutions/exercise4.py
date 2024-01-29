class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree_in_order(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left or root.right:
            print_tree_in_order(root.left, level + 1, "L-- ")
            print_tree_in_order(root.right, level + 1, "R-- ")


def mirror_binary_tree(root):
    if root is None:
        return None

    # Swap left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively mirror the left and right subtrees
    mirror_binary_tree(root.left)
    mirror_binary_tree(root.right)

    return root
def get_width_and_sum(tree):
    """for each level, gets the width of the tree and its sum"""
    if tree == None:
        return 0

    level = [tree]
    res = [(0,1,1)]
    lev = 0
    while len(level) > 0:
        lev += 1
        tmp = []
        for t in level:
            r = t.right
            l = t.left
            if r != None:
                tmp.append(r)
            if l != None:
                tmp.append(l)
        res.append((lev, len(tmp), sum([n.value for n in tmp])))
        level = tmp

    return res


if __name__ == "__main__":
    BT = BinaryTree("Root")
    bt1 = BinaryTree(1)
    bt2 = BinaryTree(2)
    bt3 = BinaryTree(3)
    bt4 = BinaryTree(4)
    bt5 = BinaryTree(5)
    bt6 = BinaryTree(6)
    bt7 = BinaryTree(7)
    bt8 = BinaryTree(8)
    bt9 = BinaryTree(9)
    bt10 = BinaryTree(10)
    bt11 = BinaryTree(11)
    bt12 = BinaryTree(12)

    BT.left = bt1
    BT.right = bt2
    bt1.right = bt7
    bt1.left = bt8
    bt8.right = bt9
    bt2.left = bt6
    bt2.right = bt3
    bt3.right = bt5
    bt3.left = bt4
    bt6.right = bt10
    bt10.right = bt12
    bt10.left = bt11

    print_tree_in_order(BT)
    original_tree_ws = get_width_and_sum(BT)
    
    print("\nMirrored tree:\n")
    mirror_binary_tree(BT)
    print_tree_in_order(BT)
    mirror_tree_ws = get_width_and_sum(BT)
    
    print("\nAre levels of the two trees the same??\n")
    print(f"{'===========================':<30}")
    if len(mirror_tree_ws) == len(original_tree_ws):
        for l in range(len(mirror_tree_ws)):
            if mirror_tree_ws[l] != original_tree_ws[l]:
                print("Nope!")
                break
            else:
                print(f"{'Level '+str(l):<8} {'level':>5} {'width':>5} {'sum':>5}")
                print(f"{'Original':8} {l:5} {original_tree_ws[l][1]:5} {original_tree_ws[l][2]:5}")
                print(f"{'Mirrored':8} {l:5} {original_tree_ws[l][1]:5} {original_tree_ws[l][2]:5}")
                print(f"{'===========================':<30}")
        print("\nYaaaaas!, good job!")
    else:
        print("Nope!")
   
 
