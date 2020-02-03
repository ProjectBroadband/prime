a = input ("\n\nCheck which number?\n\n")
a = int(a)
for b in range (2, a):
	if (a % b == 0):
		print ("\n\nNo", a,"is not a prime number.\n\n")
		raise SystemExit
print ("\n\nYes", a,"is a prime number.\n\n")

