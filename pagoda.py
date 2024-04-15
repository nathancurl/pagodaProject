import networkx as nx

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
        # Assign a depth attribute to each node that is created and set to 0
        self.depth = 0
# Pagoda class
class Pagoda:
    def __init__(self):
        # Initializing the root in the Pagoda as None
        self.root = None
        self.nodes = []


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
        self.nodes.append(node)
        # Inserts into Pagoda
        if self.root is None:
            node.depth = 0
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
    # TODO: See if this works lol
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

            # Update depth for merged nodes
            temp = r
            max_depth = 0  # Use this to track the maximum depth of merged nodes
            while temp is not None:
                temp.depth = max_depth  # Set depth
                max_depth += 1  # Increment for next node
                temp = temp.left if temp.left != r else None  # Avoid cycling indefinitely
                
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

    def draw(self):
        edges = []
        G = nx.MultiDiGraph()

        for node in self.nodes:
            edges.insert(-1, (node.data, node.left.data), )
            edges.insert(-1, (node.data, node.right.data))
            G.add_node(node.data)
        G.add_edges_from(edges)

        nx.draw_networkx(G, connectionstyle = 'arc3, rad = 0.1')

            

if __name__ == "__main__":
    p = Pagoda()
    p.insert(5)
    p.insert(4)
    p.insert(6)
    p.insert(3)

    p.draw()
    
