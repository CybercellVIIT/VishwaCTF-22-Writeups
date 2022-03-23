## One Way Enigma
## Auther:- (Sanjivan Pal and Ankit Kumar)

## Category
Reversing-(medium) 

## Challenge Description:
I was working on a school project to write an encryption program.
However, being the lazy person I am, I only implemented the encryption part, and now I have no idea how to reverse it.
Can you help in reversing the encryption?
If you succeed, you'll get the flag by decrypting "2HJZ0C7K}VRH9}JB{HHB0VHDHU69ILMIBO}6U2KH7M53".

## Challenge Files:
>>> OneWayEnigma.py
>>> machine.py

## Flag: VISHWACTF{4SSYM37R1C_3NCRYP710N_W17H_3NI6M4}

## Hints: If you observe carefully, you already have part of the flag.

## Method to Solve:
1. First of all, the first 10 character of the flag are known due to the common FLAG_FORMAT. Thus, the settings used for encryption can be found out by brute-force.
2. After this, one may choose to continue to use the brute force method to find the whole flag. This may take some time, but should be possible.
3. One can also choose to actually reverse the encryption by writing their own decryption function.