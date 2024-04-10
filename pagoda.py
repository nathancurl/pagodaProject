# Python Program to implement Pagoda

# Class for creating a single node
class NodeClass:
    def __init__(self, val):
        # Node stores the value as data
        self.data = val
        # Left pointer is initially set as None
        self.left = None
        # Right pointer initially set as None
        self.right = None

# Pagoda class
class Pagoda:
    def __init__(self):
        # Initializing the root in the Pagoda as None
        self.root = None


    # To check if Pagoda is empty
    def isEmpty(self):
        # Returns True if root is equal to None
        # else returns False
        return self.root is None


    # To clear the entire Pagoda
    def clear(self):
        # Clears or Empties the entire Pagoda
        self.root = None


    # To insert node into the Pagoda
    def insert(self, val):
        # Creates a new node with data as val
        node = NodeClass(val)
        # Inserts into Pagoda
        self.root = self.insert_helper(node, self.root)

    def insert_helper(self, node, queue):
        # Initially the new node has no left child
        # so the left pointer points to itself
        node.left = node
        # Initially the new node has no right child
        # so the right pointer points to itself
        node.right = node
        # Calling merge to attach new node to Pagoda
        return self.merge(queue, node)


    # To merge new node to Pagoda
    # New node is inserted as a leaf node
    # and to maintain the heap property
    # if the new node is greater than its parent
    # both nodes are swapped and this continues till
    # all parents are greater than its children
    # TODO: See is this works lol
    def merge(self, root, newnode):
        if root is None:
            # If root is None, after merge - only newnode
            return newnode
        elif newnode is None:
            # If newnode is None, after merge - only root
            return root
        else:
            # Bottom of root's rightmost edge
            botroot = root.right
            root.right = None
            # bottom of newnode's leftmost edge - mostly itself
            botnew = newnode.left
            newnode.left = None
            r = None
            # Iterating via loop for merging
            while botroot is not None and botnew is not None:
                # Comparing parent and child
                if botroot.data < botnew.data:
                    temp = botroot.right
                    if r is None:
                        botroot.right = botroot
                    else:
                        botroot.right = r.right
                        r.right = botroot
                    r = botroot
                    botroot = temp
                else:
                    # Comparing parent and child
                    temp = botnew.left
                    if r is None:
                        botnew.left = botnew
                    else:
                        # Swapping of child and parent
                        botnew.left = r.left
                        r.left = botnew
                    r = botnew
                    botnew = temp
            # Merging stops after either
            # botnew or botroot becomes None
            # Condition check when
            # node(botnew) is None
            if botnew is None:
                root.right = r.right
                r.right = botroot
                return root
            else:
                # botroot is None
                newnode.left = r.left
                r.left = botnew
                return newnode


    # To delete a particular node
    def delete(self):
        self.root = self.delete_helper(self.root)

    def delete_helper(self, queue):
        # Deleting when Pagoda is already empty
        if queue is None:
            # Display message
            print("Empty")
            return None
        # Deleting a left child
        else:
            if queue.left == queue:
                l = None
            else:
                l = queue.left
                while l.left != queue:
                    l = l.left
                l.left = queue.left
            # Deleting a right child
            if queue.right == queue:
                r = None
            else:
                r = queue.right
                while r.right != queue:
                    r = r.right
                r.right = queue.right
            # Merging Pagoda after deletion
            return self.merge(l, r)

  
    # To print root of Pagoda
    def printRoot(self):
        if self.root is not None:
            # Display and print the data of the root
            print(self.root.data)
        else:
            # Display message when root doesn't exist
            # This implies Pagoda is empty
            print("Empty")

# Main class
if __name__ == "__main__":
    # Creating an object of Pagoda type
    # Object is created of user defined type
    p = Pagoda()

    # Operation 1 on Pagoda
    # Input 1
    # Inserting element - 10
    p.insert(10)
    # Display message
    print("Root Element :", end=" ")
    # Printing Root
    p.printRoot()

    # Operation 2 on Pagoda
    # Input 2
    # Inserting element - 30
    p.insert(30)
    # Display message
    print("Root Element :", end=" ")
    # Printing Root
    p.printRoot()

    # Operation 3 on Pagoda
    # Input 3
    # Inserting element - 20
    p.insert(20)
    # Display message
    print("Root Element :", end=" ")
    # Printing Root
    p.printRoot()

    # Operation 4 on Pagoda
    # Input 4
    # Inserting element - 50
    p.insert(50)
    # Display message
    print("Root Element :", end=" ")
    # Printing Root
    p.printRoot()

    # Operation 5 on Pagoda
    # Input 5
    # Inserting element - 40
    p.insert(40)
    # Display message
    print("Root Element :", end=" ")
    # Printing Root
    p.printRoot()

    # Operation 6 on Pagoda
    # Now, deleting an element from above
    # inserted elements
    p.delete()
    # Display message
    print("Root Element :", end=" ")
    # Printing Root
    p.printRoot()

    # Operation 7 on Pagoda
    # Again deleting an element from above
    # inserted elements using delete() method
    p.delete()
    # Display message
    print("Root Element :", end=" ")
    # Printing the Root
    p.printRoot()

    # Operation 8 on Pagoda
    # Condition check using isEmpty()
    # Checking whether the Pagoda is empty or not
    # by calling isEmpty() over Pagoda
    print("Empty status:", p.isEmpty())

    # Emptying out the Pagoda
    # using clear() method
    p.clear()

    # Again checking if Pagoda is empty
    # using the isEmpty() method
    print("Empty status:", p.isEmpty())

