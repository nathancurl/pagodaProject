class Node():
    
    def __init__(self, value):
        self.c = null
        self.p = null
        self.value = value

class Pagoda():

    def __init__(self):
        self.root = null
        self.size = 0
 
    
    def merge(self, treeA, treeB):
            # base case
            # if node above is the root
            if rc.p.p.value > rc.p.value or lc.p.p.value > lc.p.value:   # only the root node's parent is greater than the node
                if rc.value > lc.value:
                    self.root = lc
                    rc.p = lc
                    lc.p = ?   # how do we set the root children?
                    lc.c = ?  
                if lc.value > rc.value:
                    self.root = rc
                    lc.p = rc
                    rc.p = null
                    set root children?
            
            # recursive cases    
            elif lc.value > rc.value:
                parent = lc.p
                lc.p = rc
                compare(parent, rc)
                
            elif rc.value > lc.value:
                parent = rc.p
                rc.p = lc
                compare(parent, lc)
    
    def add(self,new_node):
        pass

    def remove_min(self):
        '''
        1. Compare(self.root.c, self.root.p):
            # base case
            # if node above is the min
            a. if rc.p.p.value > rc.p.value or lc.p.p.value > lc.p.value:   # only the root node's parent is greater than the node
                i. if rc.value > lc.value:
                    i. self.root = lc
                    ii. rc.p = lc
                    iii. lc.p = ?   # how do we set the root children?
                    iv. lc.c = ?  
                i. if lc.value > rc.value:
                    i. self.root = rc
                    ii. lc.p = rc
                    iii. rc.p = null
                    iv. set root children?
            
            # recursive cases    
            b. elif lc.value > rc.value:
                i. parent = lc.p
                ii. lc.p = rc
                iii. compare(parent, rc)
                
            c. elif rc.value > lc.value:
                i. parent = rc.p
                ii. rc.p = lc
                iii. compare(parent, lc)
        '''
        pass
        
        
        

    