1.	The image given has errors and cannot be opened. It is a png image but given the extension bmp to confuse players
2.	First we have to rename the image as a png file
3.	Then also image is not openable because the header hex bits are wrong
4.	Use any hex editor to correct the header bits of the file(Use any png image to compare)
5.	Now the image is openable and is a QR code. Scan this QR code which has a link to a google drive folder.
6.	In that folder we have an image of a pirate.
7.	Download that image and use strings command on it.
8.	We see there is a weird string in the bottom (Second last line)
9.	It is a rot47 encrypted text
10.	Use any tool to decrypt the text. We get the flag flipped.
}su0id3t_si_5cisn3r0f{FTCawhsiV
11.	Reverse the flag and enter to solve.
