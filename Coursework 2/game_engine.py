from Components import initialise_board, print_board, legal_move
import logging 

def main():
    logging.basicConfig(filename="file.log", level= logging.DEBUG,
    format = "%(asctime)s %(levelname)s %(message)s", datefmt = "")
    logging.basicConfig(filename="info.log", level= logging.INFO, 
    format = "%(asctime)s %(levelname)s %(message)s", datefmt = "")
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An error")
    logging.exception("an exception")
    logging.critical("A message of CRITICAL severity")
    

if __name__ == "__main__":
    main()

logger = logging.getLogger(__name__)
def cli_coords_input():
    """
    Takes the inputs of the x and y coordinate
    the user wants and returns them as
    a list that can be plugged into the legal move
    """

    try: #in case
        x = int(input('enter the x coordinate you want'))
        y = int(input('enter the y coordinate you want'))
    except ValueError: #if an integer isnt entered the error
        #should be caught
        logger.exception("Wrong data type")


    coord_list = [x,y] #take both inputs and puts them into a list
    return coord_list #returns the coord_list so that it
    #can be used by legal_turn

def check_if_any_possible_move(board,colour, size =8):
    """
    Docstring for check_if_any_possible_move
    
    :param board: The gameboard which is a 2d array that represents
    the current game board state
    in Ascii
    :param colour: The colour that's currently being checked
    to have any available moves to play
    :param size: This is the width and the length of the board.
    It is set to a default value of 8 for a 8x8 board
    This function checks through every space on the board to find empty ones.
    It then checks for an adjacent space with an opponent counter
    then it checks for the colour
    given in the same direciton of opposite one if not true return
    """
    # return(True)
    to_flip = []
    legal_turn = False
    opposite_colour = ""
    actual_colour = ""
    if colour == "Light":
        opposite_colour = "Dark   "
        actual_colour = "Light  "
    elif colour == "Dark":
        opposite_colour = "Light  "
        actual_colour = "Dark   "
    for x in range(0,size): # we have to check every space on the board
        for y in range(0,size):
            if board[x][y] == "None   ":
                if x+1 <= 7 and board[x+1][y] == opposite_colour:
                    #same logic for each direction possible in each move
                    y_distance = 0
                    x_distance = 1
                    a = x+1
                    b = y
                    while 0 <= a  <= 7 and  0<= b <= 7:
                        a = a + x_distance
                        b = b + y_distance
                        to_flip.append((a, b))
                        if 0 <= a  <= 7 and  0<= b <= 7:
                            if board[a][b] == opposite_colour: #keeps looping if its oppposite colour as we havent found confirmation it is a legal move yet
                                continue
                            if board[a][b] == actual_colour: #if the users colour is found before an empty space 
                                legal_turn = True
                            if board[a][b] == "None   ": #if there is an empty space before the actual colour it wont count as a legal move
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
    return legal_turn #returns the boolean value which determines
#whether there is a move to be played


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
        legal_turn = False #as a move has not been made yet so the legal turn
        current_longest_counter_flip = 0 #counter for the longest length flip 
        coord_list = [] #list for the tuple coordinates
        #that will get flanked
        opposite_colour = "Dark   "
        best_move = "" #assigning variables so that they can be changed later on
        for x in range(0,size): #every position on the board
            #is checked with a nested loop
            for y in range(0,size):
                 all_possible_flips_list = [] #This list stores every
                 #possible direction this space can flip coordinates
                 if colour == "Light": #same logic to select the Two diffrent colours
                    #as the game board has space padding on Dark and Light
                   opposite_colour = "Dark   "
                   actual_colour = "Light  "
                 elif colour == "Dark":
                    opposite_colour = "Light  "
                    actual_colour = "Dark   "
                 if board[x][y] == "None   ": #The space has to be empty to play a move on it
                    if x+1 <= 7 and board[x+1][y] == opposite_colour:
                        #same logic of legal turn for each direction for each coordinate
                        go = True #boolean which is true
                        #while the loop of checking counters to be flipped
                        to_flip_1 = [] #make a list for each individual direction 
                        y_distance = 0
                        x_distance = 1
                        a = x+1
                        b = y
                        to_flip_1.append((a, b)) #add the counter of opposite
                        #colour to the flipped list
                        to_flip_1.append((x, y)) #adding the coordinate being
                        #played to the list to flip this done
                        while 0 <=a<=7 and 0<=b<=7 and board[a][b]==opposite_colour and go is True:
                            #while the coordinates are still opposite
                            #colour and Light hasnt been found
                            a = a + x_distance
                            b = b + y_distance #increase the coordinate in the direction
                            #that the initial opposite colour was found
                            #so we can look for a valid move to take
                            to_flip_1.append((a, b)) #if it is an opposite counter to be flipped
                            if 0 <= a  <= 7 and  0<= b <= 7: #checking whether the next coordinates
                                #are legally in the board
                                if board[a][b] == actual_colour: #checks whether their is
                                    #one of their own counters in the same direction
                                    #making it a valid move
                                        go = False #boolean changed as the loop should end
                                        #as no more counters need to be flipped as it is one of their own
                                        legal_turn = True #We now know that their is a legal move
                                        #so we can set legal turn to true
                                        all_possible_flips_list.append(to_flip_1) #add the list of counters flipped
                                        #to the right to list of all directions flipped
                                        #in the same row to the list of all possible flips on this
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
                    length_flip = 0 #sets up a variable which tracks the length of each direction of a flip
                     to_flip = []
                    for i in all_possible_flips_list: #iterates through the list of coordinates of all possible moves
                        if len(i) > length_flip: #if the current length of coordinates is longer than the longest so far
                            length_flip = len(i) #then that is the new longest flip length
                            to_flip = i #the list of coordinates to actuall flip now change to the current one as it is the longest so far on this coordinate
                    if len(to_flip) > current_longest_counter_flip: #if the longest list of this coordinate is longer than any  
                        current_longest_counter_flip = len(to_flip)
                        coord_list = to_flip #the overall longest list to flip is set to the last one of the current coordinate
                        best_move = (y, x) # due to the index 

        if legal_turn is True: #If their is legal move on the board
            print(coord_list) #debugging
            print('The move taken was %', best_move)
            for (i, j) in coord_list: #iterates through the coordinate list 
                #which is the longest flips in a direction 
                if 0 <= i  <= 7 and  0<= j <= 7: #checks that the coordinates selected are in range of the board
                   board[i][j] = actual_colour #sets the indexs that match with the coordinates on the board to the Ais colour
        print(legal_turn) #debugging
        logger.info("This was the move the ai took", best_move)
        logger.info("this was the list of coordinates the ai flipped", coord_list)
        return legal_turn
def check_board_full(the_board, size = 8):
    """
    Docstring for check_board_full

    :param the_board: The gameboard which is a 2d array that 
    represents the current game board state in Ascii
    :param size: This is the width and the length of the board
    It is set to a default value of 8 for a 8x8 board.
    The function takes the current game board iterates through each index.
    if None is found it means that 
    every position on the board has not been taken 
    and True can be returned 
    otherwise False if no space was labelled as 'None'
    """
    for x in range(0, size): #iterate through every position on the board with a nested loop
        for y in range(0, size):
            if the_board[x][y] == "None   ": #If there is an empty space return true
                #if not return false
                return True
    return False


    





def simple_game_loop():
    """
    Docstring for simple_game_loop
    Runs a game loop intiliases the board keeps playing 
    the two players move
    until there are no available moves 
    or the move counter has run out.
    It takes it in turns with Dark having their go first.
    It returns the winning board.
    """
    print('Welcome to Othello')
    board2 = initialise_board() #makes the game board to be used in the board
    move_counter = 60 #60 total moves as the game starts 
    #with 60 available spaces on the board
    current_colour = "Dark" 
    opposite_colour = "Light"
    available_move = True #intially sets available move to true
    print_board(board2) #So that the users can see the board before hand
    while move_counter > 0 and available_move is True: #the players should keep playing while the 
        available_move1 = check_if_any_possible_move(board2, current_colour) #check if the 
        #current colour has any moves that 
        available_move2 = check_if_any_possible_move(board2,opposite_colour) 
        #check if the other player has any moves available
        if available_move1 and available_move2 is False: 
            #If both are false then the game loop should be over
            print('No available moves')
            break
        if check_if_any_possible_move(board2, current_colour) is True: #If there are available moves
            #for dark they can play
            print('Darks turn') #lets the players know whos turn it is
            current_coords = cli_coords_input() #Takes darks given coordinates
            logging.info(f"darks coordinate given {current_coords}")
            players_move_1 = legal_move(current_colour, current_coords, board2) 
            #checks if legal move then plays it for the coordinates dark player gave
            print('\n')
            if players_move_1 is True: #if the players turn was legal
            #a move should be taken of the move counter
                move_counter = move_counter -1
            print_board(board2) #print out the board now that the dark players turn is over
            available_move = check_if_any_possible_move(board2, opposite_colour) 
            #checks if the opposite colour has any moves available.
            if check_if_any_possible_move(board2, opposite_colour) is True: 
                #if it is true then Light can select their move
                print('Lights turn')
                print('\n') #makes a gap between the announcement of the board
                current_coords2 = cli_coords_input() #take white players coordinates
                logging.info(f"light's coordinate given {current_coords2}")
                players_move_2 = legal_move(opposite_colour, current_coords2, board2) #check whether the players move 
                if players_move_2 is True: #if light successfully played their move 
                    move_counter = move_counter - 1 #decrease the move counter 
                print_board(board2) #print the board out now that the light player 
    return board2 #return the finished board now that the game is over 
#so that it can be calculated who won.

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
    light_counter = 0 #both light and dark counters
    #are set to zero before they are counted
    dark_counter = 0
    for row  in range(0,size):
        for column in range(0,size): #iterate through 
            if game_board[row][column] == "Light  ": #if the coordinate or 2d index is equal to light 
                #then the light counter that should be increased
                light_counter += 1
            elif game_board[row][column] == "Dark   ": #if a coordinate is equal to Dark 
                #then the dark counter should be increased 
                dark_counter += 1
    if light_counter > dark_counter: #if more light counters are counted 
        #on the board then it return a string announcing light as the winner
        light_string = 'Light won the game with ', light_counter,' disks on the board'
        return light_string
    if dark_counter > light_counter: #if dark has more counters 
        #then a string should be returned announcing dark as the winner.
        dark_string = 'Dark won the game with ', dark_counter,' disks on the board'
        return dark_string

if __name__ == "__main__":

   game = simple_game_loop()

   check_win(game)
