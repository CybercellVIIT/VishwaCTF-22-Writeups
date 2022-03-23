            

# Take Your Time

# Author: - (Ayush Shende and Chirag Maski)

## Question description

We recieved this file, our analysts believe it is too random to be sovled. Can you do anything with this?

## Solution

We are given an executable that asks us to enter three numbers and see if we get the correct answer.

![[Pasted image 20220323133720.png]]
If we examine the program in IDA, we can see that the random number generator is seeded using the current time. So if we know how the numbers are generated, then we can accurately predict what the correct guesses are.

![[Pasted image 20220323133727.png]]

After further investigation, we see that the numbers are generated in a predictable way and we can imitate the process using our own C program.

![[Pasted image 20220323133733.png]]

Next we can run both our program, and the provided executable at the same time so they both have the same time seeds.

./sol && ./revme

This prints out the current time, followed by the three numbers, which we can type in and "guess" correctly.

![[Pasted image 20220323133740.png]]
### Flag

t!m3_!5_m0n3y