# Simple Binary Tree
# Rules
# 1. Each node has atmost two children - left and right
# 2. Each node has a numeric value
# 3. children to the left must have lesser values than their parents [this means all element on the left side need to be lesser than the root !]
# 4. children to the right must have values greater than their parents [this means all element on the right side need to be lesser than the root !]
# 5. No duplicate values

# btree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(10)
node.right.right = Node(10000)


print(node.right.data)
print(node.right.right.data)

myTree = Tree(node, 'Shantanu\'s Tree')

print(myTree.root.right.left.data)
print(myTree.root.left.right.data)
