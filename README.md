# pagodaProject
We are building a Pagoda, doing runtime research, and experimenting with the capabilities.

A Pagoda is composed of individual nodes, each with a priority number. The Pagoda meets the heap property, so parent nodes must be larger than descendants if the Pagoda is a max Pagoda or the opposite for a min Pagoda. 
so  Each node has a left and a right pointer. Nodes have the following properties:
1. The root pointer points to the leftmost and rightmost nodes.
2. The right pointer of a right descendent points to its parent and the left pointer points to its leftmost descendent.
3. The left pointer of a left descendent points to its parent and the right pointer points to its rightmost descendent. 


Files: 
pagoda.py -- The pagoda data structure

pagodaTest.py -- Test script for insertion and deletion. Tested the speed and number of insertion and deletion operations for different depths.

pagoda_performace_tests.txt -- Contains all test information
