def initialise_board(size = 8):
    """
    Docstring for initialise_board
    
    :param size:This is the width and the length of the board It is set to a default value of 8 for a 8x8 board 
    Takes the size of the board desired  It creates an empty 2d array of that size and fills the middle spaces with Light and Dark and the rest with None.
    It then returns this now set up game board
    """
    board_list = [["","","","","","","",""],["","","","","","","","",],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""],["","","","","","","",""]]
    for i in range(0,size):
        for x in range(0,size):
    

            if  i == 3 and x == 3:
                board_list[i][x] = "Light  "
            
            elif i == 3 and x == 4:
                board_list[i][x] = "Dark   "
            
            elif i ==4 and x == 3:
                board_list[i][x] = "Dark   "
            elif i == 4 and x == 4:
                board_list[i] [x] = "Light  "
            else:
                board_list[i][x] =  "None   "

          
    
    return(board_list)
    
def print_board(board):
    """
    Docstring for print_board
    
    :param board: The gameboard which is a 2d array that represents the current game board  state in Ascii
    It iterates through each index of the board and prints them out to make it easy to see where counters are and what colour each square of the board is 
    """
    for i in range(0, len(board)):
        print(board[i]) 

   
def switch_colour(colour):
    """
    Docstring for switch_colour
    
    :param colour: The colour as a string of the player who last played
    It takes the colour of the player and uses an if statement to return the other players colour
    """
    if colour == "Light":
        return("Dark")
    else:
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
    legal_turn = False 
    y = int(coordinate[0])
    x = int(coordinate[1])
    
    print(x)
    print(y)
    print(board[x])
    print(board[x][y])
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

                # for i in range(x+1, size):
                #     if board[i][y] == actual_colour:
                #         for z in range(x, i):
                #             board[z][y] = actual_colour
                #         board[x][y] = actual_colour
                            
                #         legal_turn = True
                
        if x-1 >= 0 and board[x-1][y] == opposite_colour:

            
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
            # for row in range(0, x):
            #     print(board[row][y])
            #     if board[row][y] == actual_colour:
            #         print('This is for the backwards row')
            #         print(board[row][y])
            #         print(opposite_colour)
            #         for found_row in range(row, x):
            #             board[found_row][y] = actual_colour
            #             legal_turn = True
            #         board[x][y] = actual_colour

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
                    
                # for column in range(y+1, size):
                #     if board[x][column] == opposite_colour:
                #         print(column)
                #         print()
                #         for found_column in range(y, column+1):
                #             print(found_column)
                #             board[x][found_column] = actual_colour
                #             legal_turn = True
                #         board[x][y] = actual_colour
        
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
            # for back_column in range(0, y):
            #     print(back_column)
            #     print(board[x][back_column])
            #     if board[x][back_column] == opposite_colour:
            #         for found_back_column in range(back_column, y):
            #             print('We have found oppos')
            #             board[x][found_back_column] = actual_colour
            #             legal_turn = True

            #         board[x][y] = actual_colour
        
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
            # # for diag_row_back in range(0,x-1):
            # #     for diag_column_back in range(0, y-1):
            # #         if board[diag_row_back][diag_column_back] == actual_colour:
            # #             for found_diag_row_back in range(diag_row_back, x):
            # #                 for found_diag_column_back in range(diag_column_back, y):
            # #                     board[found_diag_row_back][found_diag_column_back] = actual_colour
            # #                     legal_turn = True
            # #             board[x][y] = actual_colour


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
                
                
                # for diag_row_front in range(x+1,size):
                #     for diag_column_back2 in range(0, y-1):
                #         if board[diag_row_front][diag_column_back2] == actual_colour:
                #             for found_diag_row_front in range(x, diag_row_front):
                #                 for found_diag_column_back2 in range(diag_column_back2, y):
                #                     board[found_diag_row_front][found_diag_column_back2] = actual_colour
                #                     legal_turn = True
                #             board[x][y] = actual_colour
        
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
                
                # for diag_row_back2 in range(0,x-1):
                #     for diag_column_up in range(y+1, size):
                #         if board[diag_row_back2] [diag_column_up] == actual_colour:
                #             for found_diag_row_back in range(diag_row_back2, x):
                #                 for found_diag_column_up in range(y, diag_column_up):
                #                     board[found_diag_row_back][found_diag_column_up] = actual_colour
                #                     legal_turn = True
                #             board[x][y] = actual_colour
        

        print(legal_turn)
        return(legal_turn)





 







        
        




        
                
                







    
                    





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