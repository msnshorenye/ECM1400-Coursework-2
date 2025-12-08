from Components import initialise_board, print_board, legal_move


def cli_coords_input():
    """
    Takes the inputs of the x and y coordinate the user wants and returns them as 
    a list that can be plugged into the legal move
    """

    try:
        x = int(input('enter the x coordinate you want'))
        y = int(input('enter the y coordinate you want'))
    except TypeError:
        print('cant be done')


    coord_list = [x,y]
    return coord_list

def check_if_any_possible_move(board,colour, size =8):
    """
    Docstring for check_if_any_possible_move
    
    :param board: The gameboard which is a 2d array that represents the current game board state 
    in Ascii
    :param colour: The colour that's currently being checked to have any available moves to play
    :param size: This is the width and the length of the board.
    It is set to a default value of 8 for a 8x8 board
    This function checks through every space on the board to find empty ones.
    It then checks for an adjacent space with an opponent counter 
    then it checks for the colour given in the same direciton of opposite one if not true return
    """
    # return(True)
    to_flip = []
    legal_turn = False
    opposite_colour = ""
    actual_colour = ""
    for x in range(0,size):
        for y in range(0,size):

            if colour == "Light":
                opposite_colour = "Dark   "
                actual_colour = "Light  "
            elif colour == "Dark":
                opposite_colour = "Light  "
                actual_colour = "Dark   "

            if board[x][y] == "None   ":
                if x+1 <= 7 and board[x+1][y] == opposite_colour:
                    y_distance = 0
                    x_distance = 1
                    a = x+1
                    b = y
                    while 0 <= a  <= 7 and  0<= b <= 7:
                        a = a + x_distance
                        b = b + y_distance
                        to_flip.append((a, b))
                        if 0 <= a  <= 7 and  0<= b <= 7:
                            if board[a][b] == opposite_colour:
                                continue
                            if board[a][b] == actual_colour:
                                legal_turn = True
                            if board[a][b] == "None   ":
                                break
                if x-1 >= 0 and board[x-1][y] == opposite_colour:
                    print('x-1 and y opposite')
                    y_distance = 0
                    x_distance = -1
                    a = x-1
                    b = y
                    to_flip.append((a, b))
                    to_flip.append((x, y))
                    while 0 <= a  <= 7 and  0<= b <= 7:
                        a = a + x_distance
                        b = b + y_distance
                        to_flip.append((a, b))
                        if 0 <= a  <= 7 and  0<= b <= 7:
                            if board[a][b] == opposite_colour:
                                continue
                            if board[a][b] == actual_colour:
                                legal_turn = True
                            if board[a][b] == "None   ":
                                break

                if  y+1 <= 7 and board[x][y+1] == opposite_colour:
                    print('hi')
                    y_distance = 1
                    x_distance = 0
                    a = x
                    b = y+1
                    to_flip.append((a, b))
                    to_flip.append((x, y))
                    while 0 <= a  <= 7 and  0<= b <= 7:
                        a = a + x_distance
                        b = b + y_distance
                        to_flip.append((a, b))
                        if 0 <= a  <= 7 and  0<= b <= 7:
                            if board[a][b] == opposite_colour:
                                continue
                            if board[a][b] == actual_colour:
                                legal_turn = True
                            if board[a][b] == "None   ":
                                break

                if y-1 >= 0 and board[x][y-1] == opposite_colour:
                    y_distance = -1
                    x_distance = 0
                    a = x
                    b = y-1
                    to_flip.append((a, b))
                    to_flip.append((x, y))
                    while 0 <= a  <= 7 and  0<= b <= 7:
                        a = a + x_distance
                        b = b + y_distance
                        to_flip.append((a, b))
                        if 0 <= a  <= 7 and  0<= b <= 7:
                            if board[a][b] == opposite_colour:
                                continue
                            if board[a][b] == actual_colour:       
                                legal_turn = True
                            if board[a][b] == "None   ":
                                break


                    if  x+1 <= 7 and y+1 <= 7 and board[x+1][y+1] == opposite_colour:
                        y_distance = 1
                        x_distance = 1
                        a = x+1
                        b = y+1
                        to_flip.append((a, b))
                        to_flip.append((x, y))
                        while 0 <= a  <= 7 and  0<= b <= 7:
                            a = a + x_distance
                            b = b + y_distance
                            to_flip.append((a, b))
                            if 0 <= a  <= 7 and  0<= b <= 7:
                                if board[a][b] == opposite_colour:
                                    continue
                                if board[a][b] == actual_colour:
                                    legal_turn = True
                                if board[a][b] == "None   ":
                                    break
                    if x-1 >= 0 and y-1 >=0 and board[x-1][y-1] == opposite_colour:
                        y_distance = -1
                        x_distance = -1
                        a = x-1
                        b = y-1
                        to_flip.append((a, b))
                        to_flip.append((x, y))
                        while 0 <= a  <= 7 and  0<= b <= 7:
                            a = a + x_distance
                            b = b + y_distance
                            to_flip.append((a, b))
                            if 0 <= a  <= 7 and  0<= b <= 7:
                                if board[a][b] == opposite_colour:
                                        continue
                                if board[a][b] == actual_colour:
                                        legal_turn = True
                                if board[a][b] == "None   ":
                                        break
                    if x+1 <= 7 and y-1 >= 0 and board[x+1][y-1] == opposite_colour:
                            y_distance = -1
                            x_distance = 1
                            a = x+1
                            b = y-1
                            to_flip.append((a, b))
                            to_flip.append((x, y))
                            while 0 <= a  <= 7 and  0<= b <= 7:
                                a = a + x_distance
                                b = b + y_distance
                                to_flip.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:
                                    if board[a][b] == opposite_colour:
                                        continue
                                    if board[a][b] == actual_colour:
                                        legal_turn = True
                                    if board[a][b] == "None   ":
                                        break
                    if x-1 >= 0 and y+1 <= 7 and board[x-1][y+1] == opposite_colour:
                            y_distance = 1
                            x_distance = -1
                            a = x-1
                            b = y+1
                            to_flip.append((a, b))
                            to_flip.append((x, y))
                            while 0 <= a  <= 7 and  0<= b <= 7:
                                a = a + x_distance
                                b = b + y_distance
                                to_flip.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:
                                    if board[a][b] == opposite_colour:
                                        continue
                                    if board[a][b] == actual_colour:
                                        legal_turn = True
                                    if board[a][b] == "None   ":
                                        break
    print(legal_turn)
    return legal_turn


def ai_player_move(board, colour = "Light",  size = 8):
        """
        Docstring for ai_player_move
        
        :param board: The gameboard which is a 2d array 
        that represents the current game board  state in Ascii
        :param colour: The colour the ai is placing its counters 
        set to a default value of light
        :param size: This is the width and the length of the board 
        It is set to a default value of 8 for a 8x8 board.
        This function goes through every position on the board and 
        checks whether its empty if it is then it will search for the opposite colour 
        in a direction from the empty position if this is found then 
        it will keep searching in that direction to find the ai's own colour. 
        The most amount of flipped coordinates is the move actually played.
        """
        legal_turn = False
        current_longest_counter_flip = 0
        coord_list = []
        opposite_colour = "Dark   "
        best_move = ""
        for x in range(0,size):
            for y in range(0,size):
                 all_possible_flips_list = []
                 to_flip =[]
                 if colour == "Light":
                   opposite_colour = "Dark   "
                   actual_colour = "Light  "
                 elif colour == "Dark":
                    opposite_colour = "Light  "
                    actual_colour = "Dark   "
                 if board[x][y] == "None   ":
                    if x < 7:
                        if x+1 <= 7 and board[x+1][y] == opposite_colour :
                            go = True
                            to_flip_1 = []
                            y_distance = 0
                            x_distance = 1
                            a = x+1
                            b = y
                            to_flip_1.append((a, b))
                            to_flip_1.append((x, y))
                            while 0 <=a<=7 and 0<=b<=7 and board[a][b]==opposite_colour and go is True:
                                a = a + x_distance
                                b = b + y_distance
                                to_flip_1.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:
                                    if board[a][b] == actual_colour:
                                            go = False
                                            legal_turn = True
                                            all_possible_flips_list.append(to_flip_1)
                    if x-1 >= 0 and board[x-1][y] == opposite_colour:
                        go = True
                        to_flip_2 = []
                        y_distance = 0
                        x_distance = -1
                        a = x-1
                        b = y
                        to_flip_2.append((a, b))
                        to_flip_2.append((x, y))
                        while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour and go is True:
                                
                                a = a + x_distance
                                b = b + y_distance
                                
                                to_flip_2.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:

                                    if board[a][b] == actual_colour:
                                        go = False
                                        legal_turn = True
                                        all_possible_flips_list.append(to_flip_2) 
                    if y+1 <= 7 and board[x][y+1] == opposite_colour:
                            
                            go = True
                            to_flip_3 = []
                            y_distance = 1
                            x_distance = 0 
                            a = x
                            b = y+1
                            to_flip_3.append((a, b))
                            to_flip_3.append((x, y))
                            while 0<= a<=7 and 0<=b<=7 and board[a][b]==opposite_colour and go is True:
                                
                                a = a + x_distance
                                b = b + y_distance
                                
                                to_flip_3.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:
                                    if board[a][b] == actual_colour:
                                        go = False
                                        legal_turn = True
                                        all_possible_flips_list.append(to_flip_3)
                                  
                            
            
                    
                    if y-1 >= 0 and board[x][y-1] == opposite_colour:
                        to_flip_4 = []
                        y_distance = -1
                        x_distance=0
                        a = x
                        b = y-1
                        go = True
                        to_flip_4.append((a, b))
                        to_flip_4.append((x, y))
                        while 0<=a<=7 and 0<=b<=7 and board[a][b]==opposite_colour and go is True:
                            a = a + x_distance
                            b = b + y_distance
                            to_flip.append((a, b))
                            if 0 <= a  <= 7 and  0<= b <= 7:
                                if board[a][b] == actual_colour:
                                    go = False
                                    legal_turn = True
                                    all_possible_flips_list.append(to_flip_4)


                    if x+1 <= 7 and y+1 <= 7 and board[x+1][y+1] == opposite_colour:
                        to_flip_5 = []
                        y_distance = 1
                        x_distance = 1
                        a = x+1
                        b = y+1
                        go = True
                        to_flip_5.append((a, b))
                        to_flip_5.append((x, y))
                        while 0<=a<=7 and 0<= b<=7 and board[a][b]==opposite_colour and go is True:
                                a = a + x_distance
                                b = b + y_distance
                                to_flip_5.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:
                                    if board[a][b] == actual_colour:
                                        go = False
                                        legal_turn = True
                                        all_possible_flips_list.append(to_flip_5)
                    
                    if x-1 >= 0 and y-1 >= 0 and board[x-1][y-1] == opposite_colour:
                        go = True
                        to_flip_6 = []
                        y_distance = -1
                        x_distance = -1 
                        a = x-1
                        b = y-1
                        to_flip_6.append((a, b))
                        to_flip_6.append((x, y))
                        while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour and go is True:
                            
                            a = a + x_distance
                            b = b + y_distance
                            to_flip_6.append((a, b))
                            if 0 <= a  <= 7 and  0<= b <= 7:
                                if board[a][b] == actual_colour:
                                    legal_turn = True
                                    go =False
                                    all_possible_flips_list.append(to_flip_6)

                        
                    
    
                    if  x+1 <= 7 and y-1 >= 0 and board[x+1][y-1] == opposite_colour:
                            to_flip_7 = []
                            y_distance = -1
                            x_distance = 1 
                            a = x+1
                            b = y-1
                            to_flip_7.append((a, b))
        
                            go = True
                            while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour and go is True:
                                a = a + x_distance
                                b = b + y_distance
                                to_flip_7.append((a, b))
                                if 0 <= a  <= 7 and  0<= b <= 7:
                                    if board[a][b] == actual_colour:
                                        legal_turn = True
                                        go = False
                                        all_possible_flips_list.append(to_flip_7)
    
                    if  x-1>=  0  and y+1 <= 7 and board[x-1][y+1] == opposite_colour:
                        go = True
                        to_flip_8 = []
                        y_distance = 1
                        x_distance = -1 
                        a = x-1
                        b = y+1
                        to_flip_8.append((a, b))
                        to_flip_8.append((x, y))
                        while 0 <=a<=7 and 0<=b<=7 and board[a][b]==opposite_colour and go is True:
                            a = a + x_distance
                            b = b + y_distance
                            to_flip_8.append((a, b))
                            if 0 <= a  <= 7 and  0<= b <= 7:
                                if board[a][b] == actual_colour:
                                    legal_turn = True
                                    go = False
                                    all_possible_flips_list.append(to_flip_8)
                    length_flip = 0
                    for i in all_possible_flips_list:
                        if len(i) > length_flip:
                            length_flip = len(i)
                            to_flip = i
                    if len(to_flip) > current_longest_counter_flip:
                        current_longest_counter_flip = len(to_flip)
                        coord_list = to_flip
                        best_move = (y, x)
        if legal_turn is True:
            print(coord_list)
            print('The move taken was', best_move)
            for (i, j) in coord_list:
                if 0 <= i  <= 7 and  0<= j <= 7:
                   board[i][j] = actual_colour
        print(legal_turn)
        return legal_turn
def check_board_full(the_board, size = 8):
    """
    Docstring for check_board_full

    :param the_board: The gameboard which is a 2d array that represents the current game board state in Ascii
    :param size: This is the width and the length of the board
    It is set to a default value of 8 for a 8x8 board.
    The function takes the current game board iterates through each index.
    if None is found it means that every position on the board has not been taken and True can be returned 
    otherwise False if no space was labelled as 'None'
    """
    for x in range(0, size):
        for y in range(0, size):
            if the_board[x][y] == "None   ":
                return True
    return False


    





def simple_game_loop():
    """
    Docstring for simple_game_loop
    Runs a game loop intiliases the board keeps playing the two players move
    until there are no available moves or the move counter has run out.
    It takes it in turns with Dark having their go first.
    It returns the winning board.
    """
    print('Welcome to Othello')
    board2 = initialise_board()
    move_counter = 60
    current_colour = "Dark"
    opposite_colour = "Light"
    available_move = True
    print_board(board2)
    while move_counter > 0 and available_move is True:
        available_move1 = check_if_any_possible_move(board2, current_colour)
        available_move2 = check_if_any_possible_move(board2,opposite_colour)
        if available_move1 and available_move2 is False:
            print('No available moves')
            break
        if check_if_any_possible_move(board2, current_colour) is True :
            print('Darks turn')
            current_coords = cli_coords_input()
            players_move_1 = legal_move(current_colour, current_coords, board2)
            print('\n')
            if players_move_1 is True:
                print_board(board2)
                available_move = check_if_any_possible_move(board2, opposite_colour)
                move_counter = move_counter - 1
                if check_if_any_possible_move(board2, opposite_colour) is True:
                    print('Lights turn')
                    print('\n')
                    current_coords2 = cli_coords_input()
                    players_move_2 = legal_move(opposite_colour, current_coords2, board2)
                    if players_move_2 is True:
                        move_counter = move_counter - 1
                        print_board(board2)
    return board2

def check_win(game_board, size = 8):
    """
    Docstring for check_win
    
    :param game_board: The gameboard which is a 2d array that represents 
    the current game board state in Ascii.
    :param size: This is the width and the length of the board.
    It is set to a default value of 8 for a 8x8 board.
    Takes the current game board checks every space 
    and counts how many light or dark counters are on the game board
    now that the game has been won.
    """
    light_counter = 0
    dark_counter = 0
    for row  in range(0,size):
        for column in range(0,size):
            if game_board[row][column] == "Light  ":
                light_counter += 1
            elif game_board[row][column] == "Dark   ":
                dark_counter += 1
    if light_counter > dark_counter:
        light_string = 'Light won the game with ', light_counter,' disks on the board'
        return light_string
    if dark_counter > light_counter:
        dark_string = 'Dark won the game with ', dark_counter,' disks on the board'
        return dark_string
#game = simple_game_loop()
#check_win(game)