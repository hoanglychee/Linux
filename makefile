
test: test-libmymath.o mymath.a
	gcc -o test test-libmymath.o libmymath.a
test-libmymath.o: test-libmymath.c libmymath.h
	gcc -c test-libmymath.c
mymath.a: giaithua.o tongchan.o tongle.o luythua.o
	ar crv mymath.a giaithua.o tongchan.o tongle.o luythua.o

