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
            '''
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
                  #  set root children?
            
            # recursive cases    
            elif lc.value > rc.value:
                parent = lc.p
                lc.p = rc
                compare(parent, rc)
                
            elif rc.value > lc.value:
                parent = rc.p
                rc.p = lc
                compare(parent, lc)
        '''
            
    def add(self,new_node):
        return compare(self.p,new_node)
        
    def compare(self, d, h):  # d is 
        if h.p.value > h.value: # h is the root
            if d.value < h.value: # d needs to be the new root
                temp_child = d.c
                d.p = h.p # set new root (d) parent to the old root parent(h)  which is the leftmost
                d.c = h.c  # set new root (d) child to the old root child(h)  which is the rightmost
                h.p = d
                h.c = temp_child
                self.root = d  
                
        elif d.p.value > d.value: #  d is the root 
            temp_child = h.c   # save new root child
            h.p = d.p # set new root parent to the old root parent which is the leftmost
            h.c = d.c  # set new root child to the old root child which is the rightmost
            d.p = h
            d.c = temp_child
            self.root = h

        elif d.value < h.value:   # don't need to iterate up
            h.p = d  # set h parent
            if self.root.p == d: 
                self.root.p = h # change root to point to new smallest
                h.c = h  # set h child to itself
            elif self.root.c == d:  # check if d is smallest 
                self.root.c = h # change root to point to new smallest
                h.c = h  # set h child to itself

        elif d.value > h.value: # h needs to be moved higher up. 
            h.p = d.p  
            d.p = h    
            self.compare(h,h.p)





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
        
        


    