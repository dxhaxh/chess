# chess
This is a self made, fully functioning(yes you can castle, yes there is en passant, yes castling through checks has been restricted as per regular chess rules, yes a player cannot put themselves in check and must stop a check if they are in check as per regular chess rules) chess game that can be played with two players. When the game ends, the result is printed on the console and there are no more possible moves since the game is over. 

To play the game, run the main file.   
To move a piece, click on it and drag it to the desired square. Possible squares to move a piece are highlighted.   
To change the theme press t.   
To restart the game press r.   
When a piece is selected, possible move squares are highlighted(in red). The last move is also highlighted(in yellow)

![image](https://github.com/user-attachments/assets/fc35f4c5-3ead-497a-bb45-cc6d03ed4703)   
![image](https://github.com/user-attachments/assets/25ae074c-6448-4894-a373-47b3ec458e08)   

Here only valid move for the black biship is to defend check   
![image](https://github.com/user-attachments/assets/a7e1743e-ca8d-4517-896a-90ed63b4e0e5)   

Here the queen cannot move to a different column, otherwise the king would be in check because of the black rook   
![image](https://github.com/user-attachments/assets/aaf1222f-7045-46af-b221-35bfbcecf696)   

Here we can see that en passant is properly implemented, the white pawn should have the opportunity to capture diagonaly to the right since we the black pawn to it's right moved 2 squares as it's first move. The black pawn on the left should not be able to be captured on this turn since it did not perform the last move.   
![image](https://github.com/user-attachments/assets/f717ee09-aba7-43ce-9ce0-0d0a165eef31)



Themes:   
![image](https://github.com/user-attachments/assets/372903d5-611f-4694-b9fc-7713e022d613)   
![image](https://github.com/user-attachments/assets/ba0b1fbd-cf7b-4045-ba19-b6e069bbf5c8)



