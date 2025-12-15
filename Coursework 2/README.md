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

   1.2 code function Takes the players input for the two coordinates and puts them into a list and returns that list

   1.3 Its designed this way so that it can be passed as a single parameter and its output can be put straight into the legal move function. 

3. check_win()
 2.1 flow chart

   <img width="339" height="622" alt="image" src="https://github.com/user-attachments/assets/81e6f2ea-f365-4b4d-bc58-15282caa7c15" />


  2.2 Code function: This function iterates through every space on the finished game board after the game has been played and checks if spaces are black or white and adds them to a counter for each. The counter with highest number is the winner and the function will return a winning message for the player with the highest counter

  2.3 Explanation: This function is written so that a winner is calculated and can be outputted to complete the requirements of the game

  

3. Simple_game_loop()
   3.1 flow chart

   
   <img width="424" height="745" alt="Screenshot 2025-12-13 161050" src="https://github.com/user-attachments/assets/f2c3cfea-52c6-401c-b595-3010a2fd684e" />
<img width="472" height="552" alt="Screenshot 2025-12-13 161056" src="https://github.com/user-attachments/assets/810e9557-5c35-4098-8482-f246c789efae" />

   3.2 Code Function: It Allows the player to take turns placing discs until conditions are met which means no more counters are able to be placed; It loops between each player until a move cant be played. It returns the winning board function to be checked through 

   3.3 Explanation This allows for a text based coordinate input system which runs the entirety of all in one function which streamlines the main program to incredibly simple code

4.check_board_full 


4.1 flowchart


<img width="332" height="651" alt="image" src="https://github.com/user-attachments/assets/aab8e076-b8b0-4deb-af9f-8b78b2c605c7" />

4.2 Code Function 
Iterates through each space in the board in a nested board to check if there is any availavble spaces. It returns False if there are none and True if there is 

4.3 Explanation
This function was more of a debugging function while I was still developing the Check_any_possible_move and wanted to test playing through full games which wouldn't haven't ended with a winner otherwie.


5. Check_any_possible_moves() 
   5.1 flowchart


   <img width="420" height="707" alt="image" src="https://github.com/user-attachments/assets/b5c2e9a0-5171-4ed5-8ce0-affa29da5769" />
   <img width="415" height="730" alt="image" src="https://github.com/user-attachments/assets/d158f195-a85b-4771-85c4-6be6ac28c08e" />
   (The flowchart shows the logic for every nested loop for each coordinate in the game board)

    5.2 Code Function This function checks every space in a nested loop with a given players colour checks if it is empty then checks whether in each direction there is an opposite colour and then there own colour without any empty spaces in between the boolean returned is set to true else it is False and there arent more moves available for this paticular player at t

    5.3  This is used in many other functions like the game loop and get move to check that the game continue as if there are no available moves for both players


5. Ai_player_Move


   5.1 Flowchart

   <img width="582" height="705" alt="image" src="https://github.com/user-attachments/assets/7fef8796-5263-40dc-836c-64d08077d7e3" />
   <img width="543" height="700" alt="image" src="https://github.com/user-attachments/assets/48182ef3-6f3c-43e2-98d8-f26241a58a73" />


   5.2 code function
       checks through every space on the board it sees how many directions one counter can flank keeping them in an indvidual list to each direction the largest coordinate from that list is compared to the largest move so far in the entire board if it is larger it will become the coordinates to change if not it moves on to checking the next space after every space has been checked the longest list of coordinates are turned into the ai discs.

   5.3 Explanation The idea of the ai is that it picks the move that flips the most counters possible although there is a small issue of it not flipping multiple directions at once but other than that in single directions it works well in automating the second player.


6. Main program
    
 
   6.1 flowchart

   <img width="144" height="302" alt="image" src="https://github.com/user-attachments/assets/cfde6234-439c-4704-87d8-6634b8fcbb20" />

   6.2 Code Function It calls the main game loop function and then takes the finished game board once the game has been played and puts it through the check win function to output the winner finishing the game.

   6.3 This is the code that actually runs the instance of the  game the players actually play when the python module is run 


Module: flask_server_ai_player.py


1. index()

   1.1 flowchart

   <img width="182" height="340" alt="image" src="https://github.com/user-attachments/assets/8894d2f7-4143-493c-998e-9de83bef9927" />


    1.2 Code Function Intialises a board and uses that in the render of the template. When the webpage is opended the template is rendered with a starting game board
   1.3 This index function loads up the page intially so that the user can interact with the tile buttons and play their cards and start the game on a web based GUI.
   
3. get_move()

   2.1 flowchart
<img width="548" height="681" alt="Screenshot 2025-12-13 235514" src="https://github.com/user-attachments/assets/d1e5dff3-bba7-46f4-8876-0e269594a79d" />
<img width="601" height="748" alt="Screenshot 2025-12-13 235553" src="https://github.com/user-attachments/assets/000319ed-461e-43ee-bd6a-067ba196800b" />

2.2 Code function It gets the url on the tile button click and request the boards X and y values from that tile It uses those coordinates to play the players turn with legal turn 

2.3 It plays the game with the coordinates the user has clicked on then it plays the AI players turn If both cant play the game ends. This means both the player and the ai play a turn on one click. 

4.  save_board()

   
    4.1 Flowchart

    <img width="556" height="739" alt="image" src="https://github.com/user-attachments/assets/71149f34-4446-45ae-88e0-31dd9105dc7e" />
    <img width="567" height="537" alt="image" src="https://github.com/user-attachments/assets/1a6fb0e6-0d9c-41a7-95f6-06ddcd27ed45" />

    4.2 Code function On click it sends the current board in a json format return {board: the board} and then it is saved as an item in javascript local storage not a json file as a file is not able to be loaded into 
 
    4.3 It is function that returns the current game board in json when the button is clicked despite the troubles with recieving the board back in the correct form it now works entirely correctly.
5. Load_board()
   
   5.1 flowchart

   <img width="293" height="537" alt="image" src="https://github.com/user-attachments/assets/88017fbc-600b-446d-b8e7-d17dab6184f8" />
   

   5.2 Code Function
      Gets the saved plain text version saved in the template converts it into a useable format and uses json loads to return it back to the format of a game board in my game. The template is then rerendered with this new game board. 

   5.3 Intially I tried to use Node.js to write and save to files but reading and writing was not accessible for the website GUI. I had to instead Use Jsonify to save the string in Local storage (Not just a plain Json file thats accessed through Node.js a Json  then instead of Node,js use text with a json header
   The html has to be updated to the current one with the board once the text has been given back to the flask server then on 

depository handele for the project https://github.com/msnshorenye/ECM1400-Coursework-2 
   
   

   
   
      
