from idlist import*
file= open("result.txt","a")
fopen = open('att.txt',mode='r+')
fread = fopen.readlines()
for rollno in range(68):
	x =id[rollno]
	for line in fread:
		if x.lower() in line.lower():
			file.write(str(rollno+1))
			file.write(str(","))


