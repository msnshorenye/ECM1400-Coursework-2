import json
from flask import Flask, request
from flask import render_template
from Components import initialise_board
from Components import print_board
from Components import legal_move
from Components import switch_colour
from game_engine import check_win
from game_engine import check_if_any_possible_move
from game_engine import ai_player_move
from game_engine import check_board_full
import logging
from game_engine import main
app = Flask(__name__) # making a flask server called app
Current_Player = "Dark" #starting player should be set to Dark
Light = "Light"
move_counter = 60 #set up the maxium move count to 60
g_b_2 = initialise_board() #make the board to render the template
logger = logging.getLogger(__name__)
@app.route('/')
@app.route('/index', methods = ['GET','POST']) 
def index():
    """
    Makes the template using render template by intialising a game board and then using it as board with the html template 
    This function is called when the template and the flask framework web server is loaded. 
    """
    g_b  = initialise_board() #make the board
    return render_template('Othello Board.html',game_board = g_b) #makes the template when the web server is opened up
@app.route('/move', methods = ['GET', 'POST'])

def get_move():
   """
   Docstring for get_move

   """
   if request.method == 'GET': #if the re
      global Current_Player #making current player global so that It can be used in the get move function
      global move_counter #making move counter global so that it can be decreased in the get move function 
      print('This is the game board')
      print_board(g_b_2) 

      #tmp = switch_colour(current_player)
      #current_player = tmp
      x = request.args.get('x', type=int) #getting the x coordinate that has been clicked by the player
      print(x)
      y = request.args.get('y', type=int) #getting the y coordinate that has been clicked by the player
      print(y)
      coord_list = [x-1, y-1] #zero indexing means the coordinates
      logging.info(F"Dark coordinates played {x} and {y}")
      any_moves = check_if_any_possible_move(g_b_2, Current_Player) #checks if their are any possible moves to be made by the current playerr
      board_full = check_board_full(g_b_2) #checking if the board is full so that a move can be played
      print('This is the value for the any possible moves check', any_moves)
      if move_counter > 0 and any_moves is True and board_full is True: #if all the game conditions 
         move = legal_move(Current_Player,coord_list,g_b_2) 
         any_moves = check_if_any_possible_move(g_b_2, Light) #function call to make sure the ai can play a move on the board
         if any_moves is True: #if there is an available 
            ai_move = ai_player_move(g_b_2)
            if move is True and ai_move is True:
               return{'status': 'success', 'player' : switch_colour(Current_Player), 'board': g_b_2}
            
            if any_moves is True and ai_move is False: #If the ai cant make a move but their is an available move their should be a turn played
               return{'status': 'success', 'player' : switch_colour(Current_Player), 'board': g_b_2}
            else:
               return{'status': 'fail', 'message': Current_Player}
         else:
             return{'finished': check_win(g_b_2), 'board': g_b_2} 
      else:
          return{'finished': check_win(g_b_2), 'board': g_b_2}  #if their are no more moves allowed or avaliable or the board is full
         #the game is finished so it returns the board and winner to the html template
@app.route('/save', methods= ['GET', 'POST'])
def save_board():
   """
   Docstring for save_board
   returns the current gameboard on click of the html save button
   """
   if request.method == 'GET':
      return{'board': g_b_2} #returns the game board so that it can be saved in a json Stringfy data type
@app.route('/load', methods = ['GET', 'POST'])
def load_board():
   """
   Docstring for load_board
   Gets data as text of the saved game boardon click of the load button 
   and then uses Json loads  
   to format the gameboard back into a 2d list 
   so that it can be used in the render template function. 
   """
   if request.method == 'POST':
      b = request.get_data(as_text = True) #gets the game board
      b_2 = json.loads(b)
      return render_template('Othello Board.html', game_board = b_2)
if __name__ == '__main__':
   app.run()
