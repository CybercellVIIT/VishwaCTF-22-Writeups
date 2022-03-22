Here we are given with a .pcap file, which is a Wireshark file. Opening it we see a lot of traffic, now ignoring the UDP and TCP, focus on the http…
There’s an application form, right click and follow its TCP stream. There you’ll see a password, which has some %3d at the end, aah looks like a URL.
Now use an URL decoder and you’ll see a text with “==” at the end, aha looks like base64.
Decode the base64 and here you are with the flag. 
vishwactf{KN1Z6PXVy9}

![image](https://user-images.githubusercontent.com/55281657/159540913-f2bdb800-a44e-4aa3-8c1b-b6da01ed13ca.png)

