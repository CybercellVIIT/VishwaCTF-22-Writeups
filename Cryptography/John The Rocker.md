Writeup – John the Rocker

Step 1: Convert the given id_rsa file to hash file. (use the ssh2john.py for the same)
Command: pyhton3 ssh2john.py id_rsa.idrsa.docx > hash
Step 2: Use john the ripper to find the flag from hash file. (Use rockyou.txt as wordlist)
Command: john -w=(Path of rockyou.txt) hash
Process to follow:

![image](https://user-images.githubusercontent.com/53442472/159559265-de869313-07fc-45c6-83a5-3731696daf8c.png)


 

Flag: VishwaCTF{!!**john**!!}
