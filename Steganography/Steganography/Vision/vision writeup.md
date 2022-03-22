Title: Vision

Flag: VishwaCTF{bl1nd3d_by_th3_col0r5}

![](piet.png "Piet Image")

Step 1 : we We will use the tool OurSecret which was provided in the #announcements channel on discord to extract data from given file.

OurSecret uses LSB replacement method for steganography and is a general purpose software that can be used for performing steganography for almost all file types like mp4,mp3,wav,png,jpg,bin and many more.

using Oursecret and uploading the image in it we directly get the output of piet png file
then we move to step 2


Step 2: In this png file, we can find suspicious color pixels at the edges of the image. The image is actually based on an esoteric programming language called piet. Also the person in the image is Piet Mondrian, a famous Dutch painter. We can use any [interpreter](https://www.bertnase.de/npiet/) to execute the script and get the flag.
