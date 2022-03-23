            

# Betting Game

# Author: - (Ayush Shende and Chirag Maski)

## Question description

Try your luck to get the flag.

## Solution

We are given an ELF and a .py file named game and sage.py respectively.

On running game we see game instructions:

![[Pasted image 20220323130725.png]]
While playing, we notice it is almost impossible to earn the flag amount. So we give the player a hint in the form of sage.py

when we run sage.py it says “The biggest clue lies in your input” and asks for input.

Let’s try some random input.

![[Pasted image 20220323130738.png]]

It’s saying “t@k3_f3w_5t3p5_b@<k”.

If we look into code we can see a weird looking string and some functions. Let’s try to input that string.

![[Pasted image 20220323130745.png]]
Hmm, so the output was same.

We reversed those functions and tried to print the output given by functions we get:-

![[Pasted image 20220323130754.png]]

So we got the hint which is “try_thinking_negatively”.

The flag amount can be earned directly in one bet if the player bets negative amount (hence the hint try_thinking_negatively) only this time we have to guess incorrectly (which is pretty easy).

![[Pasted image 20220323130800.png]]

### Flag

$tr!k3_!t_lu<ky