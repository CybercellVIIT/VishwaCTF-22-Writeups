
1.	Here you are given with a bunch of bar codes and QR codes, all of them have a label except a “Maxi Code”. Crop that maxi code
2.	![image](https://user-images.githubusercontent.com/55281657/159540007-07f8c7b3-e8f0-409c-9bd1-ebedb9f87cca.png)

3.	Use an online maxi code reader and after scanning you’ll get “zippy share” link download the zip file there.
4.	That file is password encrypted ,use a normal alphabet wordlist to brute force the pass.
5.	There you’ll see 50,000 text files, now u have to find the file which has the flag
6.	You open any random file, you’ll see some random text. Only one file looks blank.
7.	So how do you find it? Just sort the files with size, the file with lowest size looks blank but isn’t.
8.	If you select the blank space, it come out to be “whitespace” code
9.	Use a whitespace decoder and there is the flag. vishwactf{justbecauseucantseeitdoesntmeanitsnotthere}
![image](https://user-images.githubusercontent.com/55281657/159540022-d476d2b7-ea25-4382-b9c3-c8e100b72d98.png)
