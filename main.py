import animation
import time
import random
import array
from termcolor import colored
@animation.wait('bar')
def long_running_function():
    time.sleep(5)
    return
  
wheel = ('-', '/', '|', '\\')
@animation.wait(wheel)
def spin():
    time.sleep(5)
    return    
    
def passman():
	return password()
def sleep():
	time.sleep(2)
def password():
	max_len=int(input(colored("length of the password:","white")))
	mypass=""

	lower_charecters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
	
 	                    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
	
 	                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
	
 	                    'z']
	DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	
 	                   
	UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
	
 	                    'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
	
 	                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
	
 	                    'Z'] 
 	
	SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
	
 	          '*', '(', ')', '<','&']

                      
	all=SYMBOLS+UPCASE_CHARACTERS+DIGITS+lower_charecters                               
                                                                  
	for i in range(max_len):
		mypass+=random.choice(all)
	LIST=list(mypass)
	random.shuffle(LIST)
	mypass=''.join(LIST)
	password=""
	sleep()
	print(colored("Building up your password....","white"),end="")
	spin()
	
	for i in mypass:
		password+=i
	return password

	
def add(username,password,file_name):
		myfile=open(file_name,"a")
		dic={}
		dic[username]=password
		myfile.write(str(dic))
		myfile.write("\n")
		myfile.close()
			
def new_user(name,file_name):
	print(colored("\n_________________________________________\nHi welcome to your secret password manager....\n***am ayyappan your new manager***\n***Experiance the real privacy***\n_________________________________________","white"))
	sleep()
	print(colored("Building up your secret space","white"))
	long_running_function()
	sleep()
	print(colored("Hey ","white"),name)
	sleep()
	print(colored("Your system is crearted","white"))
	sleep()
	print(colored("eg:Facebook,Instagram,Bank,Amazon,ATM pin etc...\nEnter the name for the password:","white"),end="")
	assign=input()
	passw=password()
	print(assign," = ",passw)
	add(assign,passw,file_name)
	
def old_user(name,file_name):
	print(colored("Welcome back","white"),name.upper())
	print(colored("Retreving your filess......","white"),end="")
	spin()
	print(colored("Done.","cyan"))
	options=input(colored("1.Create new password	2.Acess old passwords\nEnter the option:","white"))
	if options=="1":
		print(colored("eg:Facebook,Instagram,Bank,Amazon,ATM pin etc...\nEnter the name for the password:","white"),end="")
		assign=input()
		passw=passman()
		print(assign," = ",passw)
		add(assign,passw,file_name)
	elif options =="2":
		print(colored("datas\n________________\n","white"))
		dic={}
		l={}
		myfile=open(file_name,'r')
		lines=myfile.readlines()
		for line in lines:
			l=eval(line)
			for username, password in l.items():
				print(colored(username,"cyan"))
				print("________________")
				dic[username]=password
		file_acess=input(colored("Enter the name name from above data for retriving the password\nEnter the name:","white"))
		usernames=dic.keys()
		if file_acess in username:
			val=dic[file_acess]
			print(colored("Enjoy the privacy....","white"),end="")
			spin()
			print(file_acess,"=",val)
		else:
			print(colored("The name not in the data try again()","red"))	
	
	
def main():
   linux='''
	_nnnn_
        dGGGGMMb
       @p~qp~~qMb		███████████████████████████████████████
       M|@||@) M|		█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
       @,----.JM|           	█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░░░░░▄▀░░█
      JS^\__/  qKL	        █░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
     dZP        qKRb	      	█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
    dZP          qKKb		█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
   fZP            SMMb		█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
   HZM            MMMM   	█░░▄▀░░░░░░░░░░█░░▄▀░░██░░░░░░██░░▄▀░░█
   FqM            MMMM		█░░▄▀░░█████████░░▄▀░░██████████░░▄▀░░█
 __| ".        |\dS"qML		█░░▄▀░░█████████░░▄▀░░██████████░░▄▀░░█
 |    `.       | `' \Zq		█░░▄▀░░█████████░░▄▀░░██████████░░▄▀░░█
_)      \.___.,|     .'		█░░░░░░█████████░░░░░░██████████░░░░░░█
\____   )MMMMMP|   .'		███████████████████████████████████████
     `-'       `--'                                        
                                                              | PASSWORD MANAGER
                                                              | CREATED BY DCHACKZz
    
    
    
    
'''
   for i in linux:
     	print(colored(i,"white"),end="")
     	time.sleep(.0015)
   
   
   details='''
                           Hello this is an important program
                                   Craeted by DCHACKZzz
                                      
                                       
====================================================================================================
====================================================================================================


                                       Privacy matters
____________________________________________________________________________________________________
                          Dont use stupid passwords anymore
               eg:(1234,Your_name,Your pet name,mobile number,common words,etc...)
_____________________________________________________________________________________________________
_____________________________________________________________________________________________________	 
                   The name you are going to enter is super important
                You can't recover the passwords if you don't Remember
                   #######Try to enter your REAL_NAME########
                                               '''
                                               
   for i in details:
   	print(colored(i,"white"),end="")
   	time.sleep(.0005)
   name=input(colored("\nEnter your name  ","white"))
   file_name=name+".txt"
   try:
   	file=open(file_name,'r')
   	file.close()
   	old_user(name,file_name)
   except:
   	file=open(file_name,'w')
   	file.close()
   	new_user(name,file_name)
main()
