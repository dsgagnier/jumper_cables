import Graph
import copy
import matrix_helper as mat

def make_words(letters, length, words = [], current_length = 0):
    '''
    given a list of letters and a length, this function returns a list wherien each entry
    is a list of the elements in letters. All possible lists of the specified length appear
    exactly once in the returned list.

    Example:
    letters = [1,2]
    length = 3
    returns: [ [1,1,1], [1,1,2], [1,2,1], [1,2,2], [2,1,1], [2,1,2], [2,2,1], [2,2,2] ]
    '''
    if current_length == length:
        return words

    if current_length == 0:
        words = [ [i] for i in letters]
        return make_words(letters, length, words = words, current_length = 1)

    new_words = []
    for word in words:
        for letter in letters:
            new_words.append(word + [letter])
    current_length += 1
    return make_words(letters, length, words = new_words, current_length = current_length) 

def make_graphs_n_d(num_nodes, num_cols, connected = False):
    '''Returns a list of all graphs (up to symmetry if the nodes are considered identical)
    with num_nodes nodes and num_cols colours. The graphs may or may not be connected.
    '''
    graphs = []
    n = num_nodes
    d = num_cols
    all_n_perms = mat.get_perms(mat.int_list(n))
    col_perms = make_words(all_n_perms, num_cols)

    for perm in col_perms:
        new_graph = Graph.Graph(n, d, perm)

        if not connected or new_graph.is_connected(): 
            current_graphs = len(graphs)
            i = 0
            new = True
            while i < current_graphs:
                if new_graph.is_equiv(graphs[i]):
                    new = False
                i += 1
            if new:
                graphs.append(new_graph)
            if len(graphs) % 10 == 0:
                print(len(graphs))
    return graphs

if __name__ == "__main__":
    #graphs = make_graphs_n_d(2,2)
    #for g in graphs:
    #    g.print_graph()
    #    print()

    graphs = make_graphs_n_d(4,2)

##    n = 1
##    while True:
##        print(len(make_graphs_n_d(n,3)))
##        print(f"The result for n = {n} is the one above.")
##        n += 1
##        input()
#    print(len(make_graphs_n_d(4,3)))
