Epistemus: This image goes hard, feel free to run diagnostics.
 
![img](https://github.com/CybercellVIIT/VishwaCTF-22-Writeups/blob/main/Forensics/Epistemus/patrick.jpg)
Here, we are given a photo of Patrick that seems to have a github link hiding in plain sight
We use stegsolve to accurately identify the link

![image](https://user-images.githubusercontent.com/55281657/159537515-55cdc996-e224-4b56-bbed-1d096cf60576.png)

 
The GitHub Repository contains one file to lead challengers astray and two important files to complete the challenge:
![image](https://user-images.githubusercontent.com/55281657/159537774-0f29fd61-176a-4e6c-9e78-7ebbdfafbe05.png)

 
README.md contained the following line of text:
Arire tbaan tvir lbh hc Arire tbaan yrg lbh qbja Arire tbaan eha nebhaq naq qrfreg lbh Arire tbaan znxr lbh pel Arire tbaan fnl tbbqolr Arire tbaan gryy n yvr naq uheg lbh
 
Since it looks like the output of a well-known substitution cipher (ROT13), I decided to use the tool CyberChef by the GCHQ and immediately found out that this … is indeed a Rickroll

The something_in_the_way.rar file needs some password to extract the files within, but we do not seem to have that
There is another file named rightplace?.txt that contains:
I dｏｎ't ｔhiｎk tｈⅰs iｓ the ｒｉght plaｃe to be sｅaｒcｈіｎg ｆｏｒ ａｎｙtｈiｎg. Nothing bｕt emptiｎesｓ aｎｄ ⅴoіd. Liｔerally， ａ wastｅ οｆ time

At first look, it looks like some gibberish, but this is a classic case of Homoglyph Steganography.
Using the link: http://holloway.co.nz/steg/
![image](https://user-images.githubusercontent.com/55281657/159537843-01bbceec-cef1-45d4-9424-ddd6e47d6095.png)
![image](https://user-images.githubusercontent.com/55281657/159537874-73f501d6-bebd-41cc-9fe3-0fa34dd8a1a2.png)

 
 
This is indeed the password for the .rar file
After extracting, we find multiple copies of a file
One specific text file has the info we need, i.e,
Bomb – copy(69) ,we just have to ctrl F the file for ‘flag’ and voila
VishwaCTF{th1ng$_a43_n0t_wh4t_th3y_4lw4y$_$33m}
![image](https://user-images.githubusercontent.com/55281657/159537960-4bdb20f5-322e-4b5b-9143-9c61befd6c82.png)

 

















