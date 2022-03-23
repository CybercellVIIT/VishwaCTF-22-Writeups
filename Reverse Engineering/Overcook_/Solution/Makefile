all: elf32

target: elf32
elf32: vuln.c
	gcc -O0 -fno-builtin -fno-stack-protector -m32 -Wall -std=c11 -ggdb -z execstack -o vuln vuln.c

target: clean
clean: vuln
	rm vuln

