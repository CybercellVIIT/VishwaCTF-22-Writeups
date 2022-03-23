            

# Brutal Taskmaster

# Author: - (Ayush Shende and Chirag Maski)

## Question description

**Anthony "Tony" Masters** (Taskmaster) has given you a task to find the flag. Let’s see if you can get it done.

## Solution

Compiling **_task.ll_** in ELF format using clang with the following command

```

_clang task.ll -mllvm -W -g -W1,-pie -o task_

```

After compiling the task.ll with clang, we run executable file and type string as _0123456789,_ but receive fail notification as below:

![[Pasted image 20220323130931.png]]
Let’s open **_task_**![[Pasted image 20220323130941.png]]in Ghidra.

Pseudo code for check() function.

![[Pasted image 20220323130948.png]]
We easy conclude that the return value( initially, its value is 1) of this function depends input string and what string:

· if it's 1 then all elements of input must satisfy above equation( choose this case)

· if it's 0, we will have a lot's of potential input which can happen( ignore this case)

main() function

![[Pasted image 20220323130954.png]]
![[Pasted image 20220323130959.png]]
-   As mentioning above, I guess that the return value of check() function is 1, so I will pay my attention to the second branch of program: each element of input will be XOR-ed secret string before printing to screen.
-   Because there are no additional hints about original flag, so I brute-forced all possible characters of flag( in range 32-127, in ASCII). We also noticed that, when I have the first character of input, I easily can get its original form( xor with secret[i]) and second character's original form( xor with what[i])

This is the sample script which will do the brute forcing.

_secret = 'B\n|_"\x06\x1bg7#\\F\n)\t0Q8_{Y\x13\x18\rP'_

_what = "\x17/'\x17\x1dJy\x03,\x11\x1e&\nexjONacA-&\x01LANH'.&\x12>#'Z\x0fO\x0b%:(&HI\x0cJylL'\x1emtdC"_

_alphabet =[]_

_for i in range(30, 127):_

 _alphabet.append(i)_

_flag = [0]*56_

_for i in alphabet:_

 _print( 'i = ', chr(i))_

 _flag[0] = i_

 _for j in range(0, len(flag) – 1):_

 _#flag[i] ^ secret_

 _tmp = flag[j] ^ ord(secret[j %len(secret)])_ 

 _#ori_flag[i] ^ what --> ord_flag[i + 1]_

 _ori_flag_i_1 = tmp ^ ord(what[j])_ 

 _flag[j + 1] = ori_flag_i_1 ^ ord(secret[(j + 1) % len(secret)])_

 _print('flag{', end='')_

 _for k in flag:_

 _print(chr(k), end='')_

 _print('}')_

 _print('\n**********************************************************\n')_

_print()_

Sensible xor is found as i=7.

### Flag

7h15_f14g_15_v3ry_v3ry_l0ng_4nd_1_h0p3_th3r3_4r3_n0_7yp0