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
        self.position = 0
        
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

            
            #Update depth for merged nodes
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


    def update_depths(self):
        
        for node in self.nodes:
            # check if node is the root. If it is, give it depth 0 and position it in the middle of the screen
            if self.root == node:
                node.depth = 0
                node.position = 0
                
            else:
                cur_depth = 0
                cur_node = node
                # calculate how far node is from root
                running = True
                while running:
                   
                    # if left is larger, left is node's parent. Move it's position to the left
                    if cur_node.left.data > cur_node.data:
                        #node.position -= 1/(cur_depth+1)
                        node.position -= 2^cur_depth
                        # parent is root
                       
                        if cur_node.left == self.root:
                            cur_depth +=1
                            running = False
                            
                        else:
                            cur_depth += 1
                            cur_node = cur_node.left
                            
                    # right is parent        
                    elif cur_node.right.data > cur_node.data:
                        #node.position += 1/(cur_depth+1)
                        node.position += 2^cur_depth
                        
                        if cur_node.right == self.root:
                            cur_depth +=1
                            running = False
                            
                            
                        else:
                            cur_depth += 1
                            cur_node = cur_node.right
                    else:
                        None
                
                node.depth = cur_depth

        
    def draw(self):
        edges = []
        G = nx.MultiDiGraph()
        self.update_depths()
        
        pos = {}
        for node in self.nodes:
            pos[node.data] = (node.position, -1* node.depth )
            

        for node in self.nodes:
            edges.insert(-1, (node.data, node.left.data, 'b'))
            edges.insert(-1, (node.data, node.right.data, 'r'))
            G.add_node(node.data)
        G.add_edges_from(edges)

        colors = [edge[2] for edge in edges]
        print("Red: right pointer. Blue: left pointer")
        nx.draw_networkx(G, edge_color = colors, connectionstyle = 'arc3, rad = 0.2', pos = pos)

        
        
        

if __name__ == "__main__":
    p = Pagoda()
    p.insert(5)
    p.insert(6)

    p.insert(2)

    print("root: ", p.root.data)
    for node in p.nodes:
        print(node.data, "--  (", node.depth, ", ", node.position, ")"," L: ",node.left.data," R: ",node.right.data )

    p.draw()
    