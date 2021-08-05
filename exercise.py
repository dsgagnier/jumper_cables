import copy as copy

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

if __name__ == "__main__":
    words = make_words(['a','b','c'], 2)
    print("Time to print the results!")
    for word in words:
        print(word)
