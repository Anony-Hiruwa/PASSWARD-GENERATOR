# CODE BY HIRUWA
import string
import random
import time

# banner
def banner():
	print('\033[1;32m' "____   _    ____ ____     ____ _____ _   _")
	time.sleep(1)
	print("|  _ \ / \  / ___/ ___|   / ___| ____| \ | |")
	time.sleep(1)
	print("| |_) / _ \ \___ \___ \  | |  _|  _| |  \| |")
	time.sleep(1)
	print("|  __/ ___ \ ___) |__) | | |_| | |___| |\  |")
	time.sleep(1)
	print("|_| /_/   \_\____/____/   \____|_____|_| \_|")
	time.sleep(1)
banner ()

#print
print("")
print("<<TOOL BY HIRUWA 🇱🇰>>".center(50))
print("")
print("<==DARK CRIME TEAM==>".center(50))

#main
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
#    s3 = string.digits
#    s4 = string.punctuation
    time.sleep(1)
    print("" )
    plen = int(input("Enter password length (Ex : 10 ) :\n")) 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
#    s.extend(list(s3))
#    s.extend(list(s4))
    print(  "Your password is : ")
    print("")
    print("".join(random.sample(s, plen)))
    
#print
    print("<<--ENJOY THIS TOOL 🇱🇰-->>".center(50))
    print("<<--TOOL BY HIRUWA 🇱🇰-->>".center(50))