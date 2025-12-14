def initialise_board(size = 8):
    """
    Docstring for initialise_board
    
    :param size:This is the width and the length of the board It is set to a default value of 8 for a 8x8 board 
    Takes the size of the board desired  It creates an empty 2d array of that size and fills the middle spaces with Light and Dark and the rest with None.
    It then returns this now set up game board
    """
    board_list = [["","","","","","","",""],["","","","","","","","",],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]] #8 by 8 2d array
    for i in range(0,size): #for loop for all x coordinates
        for x in range(0,size): #for loop for all y coordinates in the 2d array
    

            if  i == 3 and x == 3: # checks for coordinate (3, 3)
                board_list[i][x] = "Light  " #Makes it equal to the string light representing the light counter
            
            elif i == 3 and x == 4: #checks for coorrdinate()
                board_list[i][x] = "Dark   " 
            
            elif i ==4 and x == 3:
                board_list[i][x] = "Dark   "
            elif i == 4 and x == 4:
                board_list[i] [x] = "Light  " 
            else: #if it is not one of the specific centre coordinates at the start of the game then it should not be played
                board_list[i][x] =  "None   " #every other coordinate should be set to empty

          
    
    return(board_list) #returns the gam board 2d list so that it can be used and changed in the othello game
    
def print_board(board):
    """
    Docstring for print_board
    
    :param board: The gameboard which is a 2d array that represents the current game board  state in Ascii
    It iterates through each index of the board and prints them out to make it easy to see where counters are and what colour each square of the board is 
    """
    for i in range(0, len(board)): #iterates through the 8 rows in the board
        print(board[i]) #prints out each row

   
def switch_colour(colour):
    """
    Docstring for switch_colour
    
    :param colour: The colour as a string of the player who last played
    It takes the colour of the player and uses an if statement to return the other players colour
    """
    if colour == "Light": #selection if the colour is the light player it should return the next players colour Light
        return("Dark") 
    else: #If the player's colour given is not light the next colour should be light
        return("Light") 

def legal_move(colour, coordinate, board, size = 8): 
    """
    Docstring for legal_move
    
    :param colour: The colour of the player who has inputted the move they want to play.
    :param coordinate: Set of coordinates obtain from the player from input statements or cli_coordnates_input that are used to check whether 
    :param board: The gameboard which is a 2d array that represents the current game board  state in Ascii
    :param size: This is the width and the length of the board It is set to a default value of 8 for a 8x8 board
    It checks whether the move is legal and then flips the counters in the directions which their is an opposition counter and then one of the players own colours.
    It checks this for every direction possible 
    """
    legal_turn = False #Legal turn is set to false intially as a legal move has not been found yet
    y = int(coordinate[0]) #Takes the list inputted by the player 
    #and switchest the index around to get x and y as the first indexx as a 3d 
    x = int(coordinate[1])

    if colour == "Light": #same logic as switch colour within the legal move function 
        opposite_colour = "Dark   "
        actual_colour = "Light  "
    elif colour == "Dark":
        opposite_colour = "Light  "
        actual_colour = "Dark   "

    
    if board[x][y] == "None   ": # For a move to be made the position has to be none otherwise it already has an assigned counter

        if x+1 <= 7 and board[x+1][y] == opposite_colour: #all adjacent directions coordinates within the size of the board are checked with selection
        #and that direction is on the board
        # if they are equal to opposite_colour 
        # then the move can be checked whether there is a playable move

                y_distance = 0  #an x and y distance are set to the direction of the coordinates being checked
                x_distance = 1 #checking to the right in the same row so 0 and 1 are the values
                a = x+1 #a and b are the values of the coordinates being added ib
                b = y
                to_flip = [] #list created so that coordinates found that should be flipped can be saved 
                to_flip.append((a, b)) #these coordinates which are the opposite of the players are the first appe
                while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                    #While the coordinates are in the bounds of the board and the counters are opposite colour the code should loop
                    a = a + x_distance #we add x distance and y distance to the coordinate
                    #so that we get the next counter in that direction
                    b = b + y_distance
                    to_flip.append((a, b)) #if it is equal to opposite colour the new coordinate 
                    if 0 <= a  <= 7 and  0<= b <= 7: #checks that the new coordinate is also within the boards coordinates
                        if board[a][b] == actual_colour: #if the next coordinate is equal to the players colour it means we can stop flipping coordinates
                            for (i, j) in to_flip: #for each tuple coordinate in the list
                                board[i][j] = actual_colour #the coordinates of the tuple 
                                legal_turn = True #legal turn can be set to true as a move has been made
                            board[x][y] = actual_colour
                            #while loop will stop as board[a][b]

                
        if x-1 >= 0 and board[x-1][y] == opposite_colour: #same logic for each direction

            
            y_distance = 0
            x_distance = -1 
            a = x-1
            b = y
            to_flip = []
            to_flip.append((a, b))
            while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                    
                    a = a + x_distance
                    b = b + y_distance
                    to_flip.append((a, b))
                    if 0 <= a  <= 7 and  0<= b <= 7:
                        if board[a][b] == actual_colour:
                            for (i, j) in to_flip: 
                                board[i][j] = actual_colour
                                legal_turn = True
                            board[x][y] = actual_colour


        if y+1 <= 7 and board[x][y+1] == opposite_colour :
                
                y_distance = 1
                x_distance = 0 
                a = x
                b = y+1
                to_flip = []
                to_flip.append((a, b))
                while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                    
                    a = a + x_distance
                    b = b + y_distance
                    to_flip.append((a, b))
                    if 0 <= a  <= 7 and  0<= b <= 7:
                        if board[a][b] == actual_colour:
                            for (i, j) in to_flip: 
                                board[i][j] = actual_colour
                                legal_turn = True
                            board[x][y] = actual_colour
                    

        
        if  y-1 >= 0 and board[x][y-1] == opposite_colour:

            y_distance = -1
            x_distance = 0 
            a = x
            b = y-1
            to_flip = []
            to_flip.append((a, b))
            while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                
                a = a + x_distance
                b = b + y_distance
                to_flip.append((a, b))
                if 0 <= a  <= 7 and  0<= b <= 7:
                    if board[a][b] == actual_colour:
                        for (i, j) in to_flip: 
                            board[i][j] = actual_colour
                            legal_turn = True
                        board[x][y] = actual_colour
        
        if x+1<=7 and y+1 <=7 and board[x+1][y+1] == opposite_colour:
                y_distance = 1
                x_distance = 1 
                a = x+1
                b = y+1
                to_flip = []
                to_flip.append((a, b))
                while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                    
                    a = a + x_distance
                    b = b + y_distance
                    to_flip.append((a, b))
                    if 0 <= a  <= 7 and  0<= b <= 7:
                        if board[a][b] == actual_colour:
                            for (i, j) in to_flip: 
                                board[i][j] = actual_colour
                                legal_turn = True
                            board[x][y] = actual_colour
        
        if x-1 >= 0 and y-1 >=0 and board[x-1][y-1] == opposite_colour :
            
            y_distance = -1
            x_distance = -1 
            a = x-1
            b = y-1
            to_flip = []
            to_flip.append((a, b))
            while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                
                a = a + x_distance
                b = b + y_distance
                to_flip.append((a, b))
                if 0 <= a  <= 7 and  0<= b <= 7:
                    if board[a][b] == actual_colour:
                        for (i, j) in to_flip: 
                            board[i][j] = actual_colour

                
                    
                        board[x][y]  = actual_colour
                        legal_turn = True

        if x+1 <=7 and y-1 >= 0 and board[x+1][y-1] == opposite_colour :
                
                 
                y_distance = -1
                x_distance = 1 
                a = x+1
                b = y-1
                to_flip = []
                to_flip.append((a, b))
        
                while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour:
                    
                    a = a + x_distance
                    b = b + y_distance
                    to_flip.append((a, b))
                    if 0 <= a  <= 7 and  0<= b <= 7:
                        if board[a][b] == actual_colour:
                            for (i, j) in to_flip: 
                                board[i][j] = actual_colour

                        
                            board[x][y]  = actual_colour
                            legal_turn = True
                
                
        
        if x-1>= 0 and y+1 <= 7 and board[x-1][y+1] == opposite_colour:
                
                
                 
                y_distance = 1
                x_distance = -1 
                a = x-1
                b = y+1
                to_flip = []
                to_flip.append((a, b))
                while 0 <= a  <= 7 and  0<= b <= 7 and board[a][b] == opposite_colour :
                    
                    a = a + x_distance
                    b = b + y_distance
                    to_flip.append((a, b))
                    if 0 <= a  <= 7 and  0<= b <= 7:
                        if board[a][b] == actual_colour:
                            for (i, j) in to_flip: 
                                board[i][j] = actual_colour

                    
                        
                            board[x][y]  = actual_colour
                            legal_turn = True
                
        

        print(legal_turn)
        return(legal_turn) #return the boolean value whether





 







        
        




        
                
                







    
                    





board = initialise_board()   
p_board = print_board(board)
# print(board[2][3])
p1 =legal_move("Dark",[2,3],board)
print(p1)
print_board(board)

# print
# p2 = legal_move("Light",[2,2],board)
# print_board(board)
# #p3 = legal_move("Dark",[1,2],board)
# #print_board(p3)
# #p4 = legal_move("Light",[1,1],board)
# #print_board(p4)
# p3 = legal_move("Dark", [3,2],board)
# print_board(board)
# p7 = legal_move("Light", [4,2], board)
# print_board(board)
# p8 = legal_move("Dark", [4,1], board)
# print_board(board)
# p9 = legal_move("Light", [3,5], board)
# print_board(board)
# p10 = legal_move("Dark",[5,4], board)
# print_board(board)
# p11 = legal_move("Light",[4,5],board)
# print_board(board)
# p12 = legal_move("Dark", [3,1],board)
# print_board(board)
# p13 = legal_move("Light",[2,2],board)
# print_board(board)
# p14 = legal_move("Dark",[2,1],board)
# print_board(board)