Step 1: Convert the given id_rsa file to hash file. (use the ssh2john.py for the same)
Command: pyhton3 ssh2john.py id_rsa.idrsa.docx > hash
Step 2: Use john the ripper to find the flag from hash file. (Use rockyou.txt as wordlist)
Command: john -w=(Path of rockyou.txt) hash

![image](https://user-images.githubusercontent.com/53442472/159559783-c6707ab0-3a77-434c-a787-5c886031cd05.png)

Flag: VishwaCTF{!!**john**!!}
