Heading: Money money money

Writeup:
1.	The zip file money.zip has a password so we will have to find the password somehow
2.	We start with the richies.jpeg file, it is a message in numbers which will have to be converted into text. After researching a bit we get it is a sms phone tap code cipher.
3.	After decoding it using online tool SMS Phone Tap Code Cipher (Multitap Mode) - Online Decoder, Translator (dcode.fr) we get :
IN THE LAST YEAR I INVESTED IN HUNDRED DOGECOIN GOLD AND GOT HUGE PROFITS. HAVE A LOOK AT SOME OF MY TRANSACTIONS. IF YOU ARE STUCK, YOU HAVE EVERYTHING YOU NEED LOOK CLOSELY
4.	Now we can understand we have to find a transaction of 100 dogecoin gold somewhere which can lead us further but where to find these transaction? The message says everything is given to us.
5.	So we check the richies.jpeg file and strings it we see there is a index.jpeg hidden in it. We unzip richies.jpeg to get this image
6.	![image](https://user-images.githubusercontent.com/55281657/159769163-5b21fd70-0d67-4191-bdef-11ea9f488201.png)

 
6.	After reverse searching this image on google images we get that this is a logo for the site Ethereum (ETH) Blockchain Explorer (etherscan.io)
7.	Now we have to look for the correct transaction so in the search bar we put dogecoin gold as search filter and see this:

![image](https://user-images.githubusercontent.com/55281657/159769206-e39ea7a0-2d06-4b1d-bb74-4079a1f7553c.png)
![image](https://user-images.githubusercontent.com/55281657/159769243-e6730db9-8261-4820-a9da-2bbdf6b413ae.png)

 
8.	Here we have 3 transactions in last year with 100 dogecoin gold transferred we check each transaction one by one. In the last transaction we get this in the comments section:
 
9.	Here we can see author is trying to hint that the password to the zip file we need is the name of 2 people owning a cryptocurrency company.
10.	By this chat we can understand that this company as in some leaks offshore and that it is based in Barbados. So we search on google offshore leaks and find this site: ICIJ Offshore Leaks Database
11.	Here we can search for a company in the entire offshore leaks database. We know that the company we are looking for is a cryptocurrency company so we search it and find one company that matches our criteria
 
12.	Inside this we get the name of two directors
13.	![image](https://user-images.githubusercontent.com/55281657/159769290-72287e04-f388-4a98-b1d3-ed14075e726a.png)

 
13.	So the 2 people are Esper and Louis so we try both combinations i.e ESPER_LOUIS and LOUIS_ESPER. The second one is the correct one and we get the image money.jpeg from the zip file.
14.	The image is nothing special but after some stegnography, we use steghide to extract any possible data and get the file flag.txt.
15.	The flag is VishwaCTF{d0nt_l00k_@_my_m0n3y$}
