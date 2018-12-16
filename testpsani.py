f = open ("Hello.txt", "a+")
for i in range(10):
    f.write("This is line %d\r\n" % (i+1))
f.close()

#f = open ("Hello.txt", "r")
#if f.mode == 'r':
#	cont = f.read()
#	print(cont)