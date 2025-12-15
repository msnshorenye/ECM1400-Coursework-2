from flask import Flask, request
from flask import render_template
from Components import initialise_board
from Components import print_board
from Components import legal_move
from Components import switch_colour
from game_engine import check_win
from game_engine import check_if_any_possible_move
from game_engine import ai_player_move
import json
app = Flask(__name__)
current_player = "Light"

move_counter = 60
g_b_2 = initialise_board()

@app.route('/')
@app.route('/index', methods = ['GET','POST'])
def index():
   g_b  = initialise_board()

   game_b = print_board(g_b)
   return render_template('Othello Board.html',game_board = g_b)
@app.route('/move', methods = ['GET', 'POST'])

def get_move():
   if request.method == 'GET':
      global current_player
      global move_counter
      print('This is the game board')
      print_board(g_b_2)

      tmp = switch_colour(current_player)
      current_player = tmp
      x = request.args.get('x', type=int)
      print(x)
      y = request.args.get('y', type=int)
      print(y)
      coord_list = [x-1, y-1]
      
      any_moves = check_if_any_possible_move(g_b_2, current_player)
      print('This is the value for the any possible moves check', any_moves)
      if move_counter > 0 and any_moves == True:
         move = legal_move(current_player,coord_list,g_b_2)
         print_board(g_b_2)
         if move == True:
            return{'status': 'success', 'player' : switch_colour(current_player), 'board': g_b_2}
         
         else:
            return{'status': 'fail', 'message': current_player}
      else:

         return{'finished': check_win(g_b_2), 'board': g_b_2}
      
      

@app.route('/save', methods= ['GET', 'POST'])

def save_board():
   if request.method == 'GET':
      return{'board': g_b_2}
@app.route('/load', methods = ['GET', 'POST'])
def load_board():
   if request.method == 'POST':
      b = request.get_data(as_text = True)
      b_2 = json.loads(b)
      return render_template('Othello Board.html', game_board = b_2)
if __name__ == '__main__':
   app.run()
