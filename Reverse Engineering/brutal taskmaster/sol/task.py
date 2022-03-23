secret = 'B\n|_"\x06\x1bg7#\\F\n)\t0Q8_{Y\x13\x18\rP'
what = "\x17/'\x17\x1dJy\x03,\x11\x1e&\nexjONacA-&\x01LANH'.&\x12>#'Z\x0fO\x0b%:(&HI\x0cJylL'\x1emtdC"
alphabet =[]

for i in range(30, 127):
	alphabet.append(i)

flag = [0]*56
for i in alphabet:
	print( 'i = ', chr(i))
	flag[0] = i
	for j in range(0, len(flag) - 1):
		tmp = flag[j] ^ ord(secret[j %len(secret)])		#flag[i] ^ secret
		ori_flag_i_1 = tmp ^ ord(what[j])				#ori_flag[i] ^ what --> ord_flag[i + 1]
		flag[j + 1] = ori_flag_i_1 ^ ord(secret[(j + 1) % len(secret)])
	print('flag{', end='')
	for k in flag:
		print(chr(k), end='')
	print('}')
	print('\n**********************************************************\n')
print()

