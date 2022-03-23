## Is This Even Hashing
## Auther:- (Sanjivan Pal and Ankit Kumar)

## Category
Reversing-(medium) 

## Challenge Description:
My manager thinks open source hashing functions are trash. Wants me to use this program he wrote for hashing. Can you help me show him that this isn't a good idea? Just crack this hash maybe "496838097359601664".

## Challenge Files:
>>> isThisEvenHashing2.exe

## Flag: vishwaCTF{961794786}

## Hints: Try to learn how the code works form the inside. That's all.

## Method to Solve:
1. Use ghidra to decompile
2. Observe the combination of reversible functions used in place of hash.
3. Write reverse functions for the same, i.e, bit-shift again and find modular multiplicative inverse.
4. Reverse the hash using above functions.