Challenge Name : Chess


PROBLEM STATEMENT :


my friend Beaufort challenged me to solve a chess problem and also said that "In this game stability is the key. Can you find the final position in this: White-to-play    Mate-in-4
the pieces are on the board as follows:
white pieces                   
Kh8                                  
Qa3                                  
Rf1                                   
f2
black pieces
Kh2
Bb8 and Bh5
c3,f3,g4,f6

I believe a chessboard looks like this
Flag : vishwaCTF{EVERY_MOVE_MUST_HAVE_A_PURPOSE}
Solution : 
Hints to identify from the problem description :
“ Beaufort ”
“ Being stable is Key ”
“ Find the final position ”

Step 1 :
The word Beaufort means Beaufort cipher has been used in the challenge and if you see at beaufort cipher it requires two parameters: a key and a ciphertext to solve
Step 2 :
A image was provided along with the question so there must be a reason for that:


![image](https://user-images.githubusercontent.com/53442472/159557668-10902093-2f8e-4c7e-8abb-7bd22cffe0c8.png)

on close observing we see some characters written on every square of the board so we must analyse it in detail.

on analysing the image in stegolve we get the following values board :
![image](https://user-images.githubusercontent.com/53442472/159557797-ec02a510-87ae-4029-9657-fae6fcaafaf0.png)
Step 3 : 
Now solving the chess puzzle :
This is the optimum solution, why the other solutions are not optimum is written at the end of writeup
QC1         KH3
RH1+       Bh2
QF4          g3
Qxg3#
Then visit the second hint from description “Being stable is key”
This means after the solution all the pieces that are stable i.e. did not move constitute the key values
so the key becomes after reading the values from the squares with stable pieces:
key = VNW5H0TE408QWFYMUL6BBC7X
step 4 :
go to hint 3
Find the final position

since we have the final position and that we also have the key as the stable pieces position
whatever pieces remain must be the cipher text
another hint is that if we observe the image in stegsolve only 4 squares have 6  alphabetic characters only on them while every other squares have 4 alphanumeric charaters only in the right bottom values
![image](https://user-images.githubusercontent.com/53442472/159557920-30a45f59-d483-4137-acfe-9524282e8871.png)

also the final positions we read from image we get cipher text as :
ciphertext = RSSQVSCBBMSCSUBHTVYCQEQYS

Step 5 :
we know it has beaufort cipher 
we have the key and we also have cipher text
we solve it online we get :
![image](https://user-images.githubusercontent.com/53442472/159558102-aae96fce-4b86-4fe4-afc2-8f895ba27709.png)

message = EVERYMOVEMUSTHAVEAPURPOSE
we wrap it in flag format to get follow ready for submission
flag = vishwaCTF{EVERY_MOVE_MUST_HAVE_A_PURPOSE}



Explanation about why other moves are not optimal
Explanation 1 :
After Qc1 if king moves g2 then rook will move g1+ as white does not want to give his pawn so if in next move Kxf2 then Qe1# and it will be mate in 3 so problem criteria of mate in 4 not met and king goes back to h3 then it will take more than 4 moves to mate and again problem criteria not met

Explanation 2 :
if everything is right upto Qf4 and after that black can see that if queen takes bishop it is definetly checkmate and black is playing to avoid mate so he will try to support bishop and hence he will not play any other move than g3 to support bishop and will not waste any move on playing some random piece.

