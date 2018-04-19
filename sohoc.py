a = float (input ('a = '))
b = float (input ('b = '))
c = raw_input ('Phep toan:')
if (c == "+"):
	print ('a+b='), a+b
else:
	if(c == "-"):
		print ('a-b='), a-b
	else:
		if(c == "*"):
			print ('a*b='), a*b
		else:
			if(c == "/"):
				print ('a/b='), a/b
			else:
				if(c == "%"):
					print ('a%b='), a%b
				else:
					print ('a**b='), a**b
