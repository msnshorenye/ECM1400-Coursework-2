---
title: "ECM1400-Coursework-2"
author: "Matthew Shore-Nye"
version: "3.0"
product: "Othello/reversi game"
---

# ECM1400-Coursework-2

Module 1: Components.py


1. intialise_board()

   1.1 flow chart
   
   <img width="1259" height="655" alt="image" src="https://github.com/user-attachments/assets/d2cb094a-e9cc-4a48-896d-88e79b8e4045" />

   1.2 Code function
   
   It creates a 2d array with 8 lists with 8 values in them if they are at the starting coordinates so that it can be returned and used as the board for the othello game.
   
   1.3 Explanation
   
   I chose to make a 2d array and then use a nested loop then iteration to pick out the exact coordinate that start with the intial othello game (the middle 4). This sets up the board to be interacted with if you make the output of the function a variable.

2. print_board()

   

      2.1 flow chart

      <img width="504" height="492" alt="image" src="https://github.com/user-attachments/assets/8d07c6f8-bd15-47cf-bd4f-31ec17f87f4c" />

     2.2 Code Function
     It iterates through each row of the board and prints it out.

     2.3 Explanation
   It iterates through each row to print out the board in a readable state so that the user can see what happens after each move is played allowing them to inform each of their moves. 

3. switch_colour()

   3.1 flow chart

   <img width="410" height="505" alt="image" src="https://github.com/user-attachments/assets/6d97eeb2-7aee-4d93-ba7c-ae94ecf1d7ad" />

   3.2 Code function
   Accepts a players colour and switches it to the opposite.

   3.3 Explanation
   This can be used before a turn in a game loop to allow players to play one after the other.

4. Legal_move()


   4.1 flow chart

     <img width="959" height="1152" alt="image" src="https://github.com/user-attachments/assets/41f56a98-986b-4ebb-97af-b3328016f5fc" />
     <img width="892" height="988" alt="image" src="https://github.com/user-attachments/assets/27c9b9ed-844f-4708-a7b8-19f81a86db67" />


 4.2 Code function 
   It takes the current players entered coordinates checks if that it is a valide othello move in any direction and changes the colour of the coordinates in that direction if it is valid overflank. It returns a boolean that indicates whether the coordinate is a legal move.

4.3 Explanation
I chose this approach as it takes the exact coordinates possible and makes sure they are the only ones appended and that it works for every direction which should be overflanked. The use of a legal turn boolean also makes it useful in telling whether the current player has made a valid move.

Module 2: game_engine.py

1. cli_coords_input()

   1.1 flow chart

   <img width="264" height="636" alt="image" src="https://github.com/user-attachments/assets/d3acc4e4-e765-4945-bd54-0080c0aa22b5" />

2. check_win()


3. Simple_game_loop()
   


5. Check_any_possible_moves()
   
      
