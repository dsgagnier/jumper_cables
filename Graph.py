import matrix_helper as mat
import copy

class Graph:
    '''A graph contains a list of nodes, a list of permutations, and a list of
    lists of pairs of those nodes in different colours.

    nodes - a list [0, 1, ..., n-1], to be considered the vertices of the graph

    col_edges - each list of pairs of nodes should be considered as edges in the graph
    of a specific colour. When restricted to any one colour, the graph should be the
    graph of a permutation given by the permutation of the same index in perms

    all_edges - a list of pairs of nodes. these are all of the edges irrespective of colour

    col_matrix - a list of matrices, which are the adjacency matrices in each colour

    matrix - the adjacency matrix irrespective of colour
    '''

    def __init__(self, num_nodes, num_cols, perms):
        if len(perms) != num_cols:
            raise IndexError("Incorrect number of permutations")
        self.nodes = mat.int_list(num_nodes) # list of nodes [0, 1, ..., n-1]
        '''
         each element of col_edges is a list corresponding to a colour. each element
         in col_edges[i] is a list corresponding to an edge. we start with an empty list of
         lists
        '''
        self.col_edges = [ [ [] for _ in range(num_nodes) ] for _ in range(num_cols) ]
        self.all_edges = []

        d = 0
        while d < num_cols:
            n = 0
            while n < num_nodes:
                self.col_edges[d][n] = [n, perms[d][n]]
                self.all_edges.append([n, perms[d][n]])
                n += 1
            d += 1

        self.col_matrix = []
        d = 0
        while d < num_cols:
            self.col_matrix.append(mat.make_adj(num_nodes, self.col_edges[d]))
            d += 1
            
        self.matrix = mat.make_adj(num_nodes, self.all_edges)

    def print_graph(self):
        '''Prints the colour edges and some other info nicely.'''
        print("Number of nodes: " + str(self.nodes[-1]))
        print("Number of colours: " + str(len(self.col_edges)) + "\n")
        i = 0
        while i < len(self.col_edges):
            print(f"Edges in colour {i}:")
            print(self.col_edges[i])
            i += 1

    def is_equiv_old(self, graph2): # IS BROKEN
        '''
        Given two graphs, this function determines if they are equal up to relabling of
        the nodes.
        '''
        if len(self.nodes) != len(graph2.nodes) or \
           len(self.col_edges) != len(graph2.col_edges):
            return False
        n = len(self.nodes)
        cols = len(self.col_edges)
        perms = mat.get_perms(mat.int_list(n)) # all possible permutations

        for perm in perms:
            d = 0
            # Take a deep copy of the colour matrix of graph2 so we can permute it
            permuted = copy.deepcopy(graph2.col_matrix)
            while d < cols:
                # Permute colour matrices one at a time
                mat.symmetric_permute(permuted[d], perm)
                d += 1
            print(permuted)
            if self.col_matrix == permuted:
                return True
        return False

    def is_equiv(self, graph2):
        '''
        Given two graphs, this function determines if they are equal up to relabling of
        the nodes.
        '''
        if len(self.nodes) != len(graph2.nodes) or \
           len(self.col_edges) != len(graph2.col_edges):
            return False
        n = len(self.nodes)
        cols = len(self.col_edges)
        perms = mat.get_perms(mat.int_list(n)) # all possible permutations

        for perm in perms:
            d = 0
            permuted = []
            while d < cols:
                # Permute colour matrices one at a time
                permuted.append(mat.symmetric_permute(graph2.col_matrix[d], perm))
                d += 1
            if self.col_matrix == permuted:
                return True
        return False

if __name__ == "__main__":
    # Testing constructor and print_graph()
    g1 = Graph(3, 2, [[0,1,2],[0,1,2]])
    g1.print_graph()
    mat.print_m(g1.matrix)

    
    g2 = Graph(3, 2, [[2,1,0],[0,2,1]])
    g2.print_graph()
    mat.print_m(g2.matrix)

    # Test is_equiv()
    #print(g1.is_equiv(g1)) # True
    #print(g2.is_equiv(g2)) # True
    print(g1.is_equiv(g2)) # False
    
