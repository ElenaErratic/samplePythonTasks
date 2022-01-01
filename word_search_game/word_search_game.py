"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""

#1
def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    """

    return word in wordlist


#2
def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """
    
    row_string = ''
    for column in range(len(board[row_index])):
        row_string += board[row_index][column]
    return row_string


#3
def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """

    column_string = ''
    for row in range(len(board)):
        column_string += board[row][column_index]
    return column_string



#4
def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False

#5
def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """

        
    for row in range(len(board)):
        for column_index in range(len(board[row])):
            if word in make_str_from_column(board, column_index):
                return True

    return False

#6
def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    """

    if board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word) == True:
        return True
    else:
        return False


#7
def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """

    if len(word) < 3:
        return 0

    if len(word) in range(3, 7):
        return len(word)

    if len(word) in range(7, 10):
        return len(word)*2

    if len(word) > 10:
        return len(word)*3



#8
def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """

    player_info[1] += word_score(word)




#9
def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    num_words_on_board = 0
    for word in words:
        if board_contains_word(board, word) == True:
            num_words_on_board += 1 
    return num_words_on_board


#10
def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """

    words_list = []
    line = words_file.readline()
    while line != '':
        if line[-1] == '\n':
            line = line[:-1]
        words_list.append(line)
        line = words_file.readline()
    return words_list
    



#11
def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.

    >>> board_list = ['EFJAJCOWSS\n', 'SDGKSRFDFF\n', 'ASRJDUSKLK\n', 'HEANDNDJWA\n', 'ANSDNCNEOP\n', 'PMSNFHHEJE\n', 'JEPQLYNXDL']

    [['E', 'F', 'J', 'A', 'J', 'C', 'O', 'W', 'S', 'S'], ['S', 'D', 'G', 'K', 'S', 'R', 'F', 'D', 'F', 'F'], ['A', 'S', 'R', 'J', 'D', 'U', 'S', 'K', 'L', 'K'], ['H', 'E', 'A', 'N', 'D', 'N', 'D', 'J', 'W', 'A'], ['A', 'N', 'S', 'D', 'N', 'C', 'N', 'E', 'O', 'P'], ['P', 'M', 'S', 'N', 'F', 'H', 'H', 'E', 'J', 'E'], ['J', 'E', 'P', 'Q', 'L', 'Y', 'N', 'X', 'D', 'L']]
    """
    
    board_list = board_file.readlines()
    rows_list = []
    row_index_list = []
    row_index = 0
    row = board_list[row_index]
    #column = row[column_index]

    for row in board_list:

        row = board_list[row_index]
        if row[-1] == '\n':
            row = row[:-1]
        
        
        for column in row:
            row_index_list.append(column)

        row_index += 1
        rows_list.append(row_index_list)
        row_index_list = []
        
    board = rows_list
    return board

