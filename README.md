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
 2.1 flow chart

   <img width="339" height="622" alt="image" src="https://github.com/user-attachments/assets/81e6f2ea-f365-4b4d-bc58-15282caa7c15" />


4. Simple_game_loop()
   4.1 flow chart

   
   <img width="424" height="745" alt="Screenshot 2025-12-13 161050" src="https://github.com/user-attachments/assets/f2c3cfea-52c6-401c-b595-3010a2fd684e" />
<img width="472" height="552" alt="Screenshot 2025-12-13 161056" src="https://github.com/user-attachments/assets/810e9557-5c35-4098-8482-f246c789efae" />

5.check_board_full 


5.1 flowchart


<img width="332" height="651" alt="image" src="https://github.com/user-attachments/assets/aab8e076-b8b0-4deb-af9f-8b78b2c605c7" />



6. Check_any_possible_moves() 
   6.1 flowchart


   <img width="420" height="707" alt="image" src="https://github.com/user-attachments/assets/b5c2e9a0-5171-4ed5-8ce0-affa29da5769" />
   <img width="415" height="730" alt="image" src="https://github.com/user-attachments/assets/d158f195-a85b-4771-85c4-6be6ac28c08e" />



7. Ai_player_Move


8. Main program
 
   8.1 flowchart

   <img width="144" height="302" alt="image" src="https://github.com/user-attachments/assets/cfde6234-439c-4704-87d8-6634b8fcbb20" />


Module: flask_server_ai_player.py


1. index()

   1.1 flowchart

   <img width="182" height="340" alt="image" src="https://github.com/user-attachments/assets/8894d2f7-4143-493c-998e-9de83bef9927" />

   
2. get_move()

   2.1 flowchart

       <img width="548" height="681" alt="image" src="https://github.com/user-attachments/assets/08331765-8c95-426b-b85e-433046f418cc" />
        <img width="601" height="748" alt="image" src="https://github.com/user-attachments/assets/29ba813a-e334-4c76-9111-b94387b83e61" />


4.  save_board()

5. Load_board()

6. main program
   
   

   
   
      
