class Node:
    '''
    implements a node
    '''
    def __init__(self, key):
        self.value = key  
        self.left = None  
        self.right = None
    
    def __str__(self):
        return str(self.value)

class BST:
    '''
    implements a Binary Search Tree
    '''
    def __init__(self):
        self.root = None
    
    def add(self, key):
        # adds a new node to the BST
        newNode = Node(key)        # create new node to be added
       
        if self.root is None: self.root = newNode    # BST is empty
        else:                                   # MST is not empty
            parent = current = self.root
            while current is not None:
                # locate where the new node will be inserted
                parent = current
                if key < current.value: current = current.left
                else: current = current.right
            # parent points to the parent of the node to be inserted
            # if key to be inserted is less than its parent, insert
            # new node as parent's left child; else, insert as its 
            # right child
            if key < parent.value: parent.left = newNode
            else: parent.right = newNode
        
    def search(self, searchKey):
        # if searckKey not found search returns None
        current = self.root
        while current is not None and current.value != searchKey:
            if searchKey < current.value:
                current = current.left
            else: 
                current = current.right
        return current

    def delete(self, key):
        # delNode           -> node to be deleted
        # parent            -> parent of delNode
        # replaceNode       -> node that will replace delNode
        # parentSuccessor   -> parent of replaceNode
        # successor         -> inorder successor of delNode

        parent = delNode = self.root
        while delNode is not None and delNode.value != key:
            # while node to be deleted has not been found and not reached None
            parent = delNode
            if key < delNode.value: delNode = delNode.left
            else: delNode = delNode.right
        # delNode points to the node to be deleted or None if the node is not found in the BST;
		# parent points to the parent of delNode
		
        # set replaceNode to the node that will replace delNode
        if delNode is None:
            print("The node is not found in this BST...")
        else:
            # Cases 1 and 2: No children or 1 child
            if delNode.left is None:
                replaceNode = delNode.right
            elif delNode.right is None:
                replaceNode = delNode.left
            else: 
                # Case 3: delNode has 2 children
                # Set replaceNode to the inorder successor of delNode and parentSuccessor to the parent of replaceNode 
                parentSuccessor = delNode
                replaceNode = delNode.right
                successor = replaceNode.left
                # find the inorder successor of delNode - loop while there is still a left subtree
                while successor is not None:
                    parentSuccessor = replaceNode
                    replaceNode = successor
                    successor = replaceNode.left
                # at this point replaceNode is the inorder successor of delNode      

                if parentSuccessor != delNode:
                    # delNode is not the parent of replaceNode and replaceNode == parentSuccessor.getLeft()
                    parentSuccessor.left = replaceNode.right
                    # remove replaceNode from its current position and replace it with the right child of replaceNode
                    # replaceNode takes the place of delNode
                    replaceNode.right = delNode.right
				
				# set the left child of replaceNode so that replaceNode takes the place of delNode
                replaceNode.left = delNode.left
            
            # insert replaceNode in the position formerly occupied by delNode
            if delNode == self.root:
                # if node to be deleted is root, set root to replaceNode
                self.root = replaceNode
            elif delNode == parent.left:
                parent.left = replaceNode
            else: parent.right = replaceNode
        
    def preOrder(self, node):
        if node is not None:
            print(node, end="\t")
            self.preOrder(node.left)
            self.preOrder(node.right)
	
    def inOrder(self, node):
        if node is not None:            
            self.inOrder(node.left)
            print(node, end="\t")
            self.inOrder(node.right)
            
    def postOrder(self, node):
        if node is not None:            
            self.postOrder(node.left)            
            self.postOrder(node.right)
            print(node, end="\t")
	
def main():
    myBST = BST()
    myBST.add(10)
    myBST.add(5)
    myBST.add(8)
    myBST.add(13)
    myBST.add(7)
    myBST.add(12)
    
    print("Inorder traversal:", end="\t")
    myBST.inOrder(myBST.root)
    print()

    print("Preorder traversal:", end="\t")
    myBST.preOrder(myBST.root)
    print()

    print("Postorder traversal:", end="\t")
    myBST.postOrder(myBST.root)
    print()

    searchKey = 23
    print("Searching for", searchKey, "...")
    print(myBST.search(searchKey))

    searchKey = 8
    myBST.delete(searchKey)
    print("Inorder traversal after deleting", searchKey, ":", end="\t")
    myBST.inOrder(myBST.root)
    print()

if __name__ == "__main__":
    main()