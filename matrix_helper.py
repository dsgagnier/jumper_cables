'''
Note: given a permutation \sigma, we are going to call \sigma(i) to be perm[i]
'''

import itertools

def make_matrix(size):
    '''This function makes a 2-D matrix such that the size of it is size x size. The
    matrix is populated with 0s.
    '''
    return [[0 for j in range(size)] for k in range(size)]

def print_m(matrix):
    '''Prints a matrix more nicely.'''
    for row in matrix:
        print(row)
    print()

def int_list(n):
    '''Makes a list where the entries are 0, 1, ... , n-1 '''
    int_list = []
    i = 0
    while i < n:
        int_list.append(i)
        i += 1
    return int_list

def get_perms(a_list):
    '''Given a list, returns all possible permutations of its entries as a list of tuples.
    '''
    return list(itertools.permutations(a_list))

def permute_list(a_list, perm):
    '''Given a list and a permutation, applies the permutation to the list. For example,
    ['a','b','c','d'], [0,2,3,1] -> ['a','c','d','b']
    '''
    new = []
    for i in range(len(a_list)):
        new.append(a_list[perm[i]])
        i += 1
    return new

def symmetric_permute(matrix, perm):
    '''Given a 2-D matrix, applies a permutation to its rows and its columns'''
    matrix = permute_list(matrix, perm) #permute the rows
    for i in range(len(matrix)):
        matrix[i] = permute_list(matrix[i], perm)
    return matrix

def make_adj(num_nodes, edges):
    '''
    Given the number of nodes in a graph and a list of edges (where an edge is a list of
    length 2 wherein the entries numbers less than num_nodes), this function returns the
    adjacency matrix of the corresponding graph.
    '''
    adj = make_matrix(num_nodes)
    i = 0
    while i < len(edges):
        adj[edges[i][0]][edges[i][1]] += 1
        i += 1
    return adj

if __name__ == "__main__":
    # Testing make_adj()
    adj = make_adj(3, [[0, 2], [1, 1], [2, 0], [0, 0], [1, 2], [2, 1]])
    print("The final result is:")
    print_m(adj)

    # Test permute_list()
    print(permute_list(['a','b','c','d'], [0,2,3,1]))

    # Test symmetric_permute()
    print(symmetric_permute( [ [0,1,0],
                               [1,0,0],
                               [0,0,1] ], [2,1,0]))
