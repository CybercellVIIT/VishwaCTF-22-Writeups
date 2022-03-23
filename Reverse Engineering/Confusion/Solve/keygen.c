#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int bytes[] = {0xff98ffb1,0xff9cffa0,0xff99ffb8,0xffe0ffa2,
			   0xffb2ffe2,0xffff};

int main(void) {
	short temp[11];
	int pass[11];
	FILE *fd;
	char *name;
	size_t len;
	
	srand(time(NULL));
	
	len = rand() % 0x10 + 5;
	
	if (!(name = malloc(len+1))) {
		fprintf(stderr, "malloc failed\n");
		return 1;
	}
	
	for (size_t i = 0; i < len; ++i) {
		name[i] = rand() % 2 ? 0x41 : 0x61;
		name[i] = name[i] + rand() % 0x1a;
	}
	
	name[len] = 0;
	
	for (short i = 0, *p = (short *) bytes; i < 11; ++i, ++p) {
		temp[i] = (~(*p - i))^i;
	}
	
	for (int i = 0; i < 11; ++i) {
		pass[i] = temp[i] ^ len;
	}
	
	if (!(fd = fopen("pass.txt", "wb"))) {
		fprintf(stderr, "error opening file\n");
		return 1;
	}
	
	fprintf(fd, "continue\n%s\n", name);
	
	for (int i = 0; i < 11; ++i) {
		fprintf(fd, "%d\n", pass[i]);
	}
	
	if (fclose(fd) == EOF) {
		fprintf(stderr, "error closing file\n");
		return 1;
	}
	
	free(name);
	
	return 0;
}