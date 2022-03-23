from z3 import *

def char_transform(c):
	return ((c >> 7) * 0x1b ^ c * 2) & 0xff

def reverse_shuffle(input_bytes):

	mappings = {0: 29, 1: 34, 2: 13, 3: 18, 4: 15, 5: 20, 6: 35, 7: 28, 8: 19, 9: 12, 10: 21, 11: 14, 12: 3, 13: 8, 14: 25, 15: 30, 16: 1, 17: 6, 18: 9, 19: 2, 20: 31, 21: 24, 22: 7, 23: 0, 24: 5, 25: 10, 26: 17, 27: 22, 28: 27, 29: 32, 30: 11, 31: 4, 32: 23, 33: 16, 34: 33, 35: 26}
	mappings = {v:k for k,v in mappings.items()}

	out = [None] * len(input_bytes)
	for orig, new in mappings.items():
		out[new] = input_bytes[orig]

	return out

def reverse_num_combine(input_bytes, nums):

	# The known output values
	n_out = [input_bytes[nums[i]] for i in range(6)]

	# The unknown input_bytesut values that produce the output
	n = [BitVec(f"n{i}", 32) for i in range(6)]

	s = Solver()
	s.add(input_bytes[nums[0]] == char_transform(n[4]) ^ char_transform(n[0]) ^ n[0] ^ n[2] ^ char_transform(n[2]))
	s.add(input_bytes[nums[1]] == char_transform(n[5]) ^ char_transform(n[1]) ^ n[1] ^ n[3] ^ char_transform(n[3]))
	s.add(input_bytes[nums[2]] == char_transform(n[0]) ^ n[4])
	s.add(input_bytes[nums[3]] == char_transform(n[1]) ^ n[5])
	s.add(input_bytes[nums[4]] == char_transform(n[2]) ^ char_transform(n[0]) ^ n[0])
	s.add(input_bytes[nums[5]] == char_transform(n[3]) ^ char_transform(n[1]) ^ n[1])

	if s.check() == sat:

		m = s.model()
		final_nums = [int(str(m[e])) for e in n]

		for i in range(6):
			input_bytes[nums[i]] = final_nums[i]
		return input_bytes

def reverse_combine(input_bytes):

	nums = [
		[0,1,2,6,12,18],
		[3,4,5,11,17,23],
		[7,8,9,13,14,15],
		[10,16,22,28,29,35],
		[19,20,24,25,26,30],
		[21,27,31,32,33,34]
	]

	for n in nums[::-1]:
		input_bytes = reverse_num_combine(input_bytes, n)
	return input_bytes

if __name__ == '__main__':
	
	target = bytes.fromhex("ed1fb0b0569a444609bc06833f938752ff032f9ff8cd5df249ae844de82c8d58b6a271b6")
	print(target)

	for _ in range(16):
		target = reverse_shuffle(target)
		target = reverse_combine(target)

	
	print("".join(map(chr, target)))
	# VishwaCTF{rev3rs1bl3_and_1nv3rtibl3}
