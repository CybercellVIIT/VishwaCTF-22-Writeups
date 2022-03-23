**Language:** C/C++
**Platform:** Windows
**Difficulty:** 3.0

---

**Tools:** CFF Explorer, IDA, x64dbg

---
**Summary**

Simple keygen that takes a username and creates a password the user must enter, the Username has already been given to the user, all the user had to do was reverse engineer the program, and based on the Username find the suitable Password. There are multiple debugger checks that will force the application to exit if it is being debugged.

**Analysis**

The main function is found by finding the `_cexit` function. This is the function
that returns control from the user code back to the C runtime environment. The function call at instruction `14000310b` seen below is the main function.

```md
       1400030f6 e8 93 0a        CALL       API-MS-WIN-CRT-RUNTIME-L1-1-0.DLL::__p___argv
                 00 00
       1400030fb 48 8b 18        MOV        RBX,qword ptr [RAX]
       1400030fe e8 85 0a        CALL       API-MS-WIN-CRT-RUNTIME-L1-1-0.DLL::__p___argc
                 00 00
       140003103 4c 8b c7        MOV        R8,RDI
       140003106 48 8b d3        MOV        RDX,RBX
       140003109 8b 08           MOV        ECX,dword ptr [RAX]
       14000310b e8 f0 e1        CALL       main				<-----------------
                 ff ff
       140003110 8b d8           MOV        EBX,EAX
       140003112 e8 05 07        CALL       FUN_14000381c
                 00 00
       140003117 84 c0           TEST       AL,AL
       140003119 74 55           JZ         LAB_140003170
       14000311b 40 84 f6        TEST       SIL,SIL
       14000311e 75 05           JNZ        LAB_140003125
       140003120 e8 6f 0a        CALL       API-MS-WIN-CRT-RUNTIME-L1-1-0.DLL::_cexit
                 00 00
```

Inside main there are three debugger checking functions. These are found at `14000138c`, `14000139f`, and `1400013ef`. If the user wants to bypass the logic checks for the presence of a debugger, the zflag needs to be set to 1, 1, and 0 respectively for the logic checks at addresses `14000138c`, `14000139f`, and `1400013ef`.

The program then prompts the user to either enter *'continue'* or *'rules'* to either continue or see a list of rules. Entering continue will take the user to a function called at address `140001591`. The function starts at address `140002120` and is the function that generates the key, prompts the user for their name and password, and checks if the password is valid. Another debugger check occurs at `140002157`. This requires the zflag set to 1 to bypass. The console screen is cleared and the username is prompted for their username. Data is encountered at `1400021dc` to `140002201` that is the base data used to generate the password.
```md
       1400021dc c7 45 db        MOV        dword ptr [RBP + -0x25]=>local_88[4],0xff9cffa0
                 a0 ff 9c ff
       1400021e3 c7 45 e7        MOV        dword ptr [RBP + -0x19]=>local_78[0],0xffb2ffe2
                 e2 ff b2 ff
       1400021ea c7 45 d7        MOV        dword ptr [RBP + -0x29]=>local_88[0],0xff98ffb1
                 b1 ff 98 ff
       1400021f1 c7 45 e3        MOV        dword ptr [RBP + -0x1d]=>local_88[12],0xffe0ffa2
                 a2 ff e0 ff
       1400021f8 b8 ff ff        MOV        EAX,0xffff
                 00 00
       1400021fd 66 89 45 eb     MOV        word ptr [RBP + -0x15]=>local_78[4],AX
       140002201 c7 45 df        MOV        dword ptr [RBP + -0x21]=>local_88[8],0xff99ffb8
                 b8 ff 99 ff
```

A loop is then entered that will begin the process of transforming the data from the assembly above.

```md
                             encrypt_sub 
       140002210 0f b7 0a        MOVZX      ECX,word ptr [RDX]=>local_88
       140002213 66 2b c8        SUB        CX,AX
       140002216 66 f7 d1        NOT        CX
       140002219 66 33 c8        XOR        CX,AX
       14000221c 66 89 0a        MOV        word ptr [RDX]=>local_88,CX
       14000221f ff c0           INC        EAX
       140002221 48 8d 52 02     LEA        RDX=>local_88[2],[RDX + 0x2]
       140002225 83 f8 0b        CMP        EAX,0xb
       140002228 72 e6           JC         encrypt_sub

```

The loop takes 2 byte chunks from the data "buffer" and subtracts it from the index of the loop, toggles every bit, xor's it with the index of the loop, and then places the value back in the same portion of the data "buffer." This is done 11 times.

A loop is then entered that prompts the user for the password. The input stream accepts an integer value as input. This is done 11 times.

The final transform is taking the values from the "encryption" loop and xor'ing each 2 byte zero extended chunk by the length of the username entered. A comparison is performed with the input password integers, if the two values are not equal a counter is incremented.

Note, the 2 byte chunks start at index 0 and incremented to the next 2 byte chunk. The input password integers are indexed by their order in the password prompting above. The counter is checked after all the comparisons are performed and if it is zero the success message is output to the user.