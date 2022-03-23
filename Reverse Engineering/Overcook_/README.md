## Overcook 
## Auther:- (Ankit Kumar and Sanjivan Pal)

## Category
Reversing-buffer overflow-(medium) 

## Challenge Description:
Alright, this time you’ll need to control some numerical representations. Can you get the flag from this program?

## Challenge Files:
>>> vuln

## Flag: 
VishwaCTF{r3vers1ng_dud3}

## Hints: 
Try using gdb to print out the stack once you write to it! (not to be given)

## Method to Solve:
1. check for the functions in the program there u will find printflag() function (by using objdump -d vuln)
2. then find the point of overflow for the program. (by using pwn lib- cyclic func i.e=62)
3. then find adress of printflag() function and try to return it by oveflowing stack (\x3c\x62\x55\x56)
4. then u will get some numbers that are the ascii values of flat letters (i.e 114 051 118 101 114 115 049 110 103 095 100 117 100 051)
5. convert it to string and u will get the flag (i.e r3vers1ng_dud3)


