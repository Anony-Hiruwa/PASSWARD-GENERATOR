# CODE BY HIRUWA
import string
import random
import time
from os import system as sys

sys("clear")

def rer() :


    print( '\033[1;32m' "____   _    ____ ____     ____ _____ _   _" )
    time.sleep( 0.5 )
    print( "|  _ \ / \  / ___/ ___|   / ___| ____| \ | |" )
    time.sleep( 0.5 )
    print( "| |_) / _ \ \___ \___ \  | |  _|  _| |  \| |" )
    time.sleep( 0.5 )
    print( "|  __/ ___ \ ___) |__) | | |_| | |___| |\  |" )
    time.sleep( 0.5 )
    print( "|_| /_/   \_\____/____/   \____|_____|_| \_|" )
    time.sleep( 0.5 )

    print("")
    print('\033[93m' " << TOOL BY HIRUWA >>".center( 50 ) )
    print( "" )
    time.sleep(0.5)
    print('\033[93m' "<==DARK CRIME TEAM==>".center( 50 ) )
    print( "" )
    time.sleep(0.5)
    input( "PRESS ENTER KEY TO CONTINUE THIS TOOL" )
    print( "" )
    time.sleep(0.3)
    print( "SUCCESFULLY !! THIS TOOL WAS RUNNING......." )
    time.sleep( 0.6 )
    print( "LOADING........" )
    time.sleep( 2 )

    if __name__ == "__main__" :
     s1 = string.ascii_lowercase
     s2 = string.ascii_uppercase
     s3 = string.digits
     s4 = string.punctuation
     time.sleep( 1 )
     print( "" )
     plen = int( input('\033[32m' "Enter password length ( Ex : 10 ) : " ) )
     print( "" )
     print( "GENERATING YOUR PASSWORD WAIT 1 SECOND !!........" )
     time.sleep( 1 )
     s = []
     s.extend( list( s1 ) )
     s.extend( list( s2 ) )
     s.extend( list( s3 ) )
     s.extend( list( s4 ) )
     print( "" )
     print( "Your password is  " )
     print( "👇👇👇👇👇" )
     print( "".join( random.sample( s,plen ) ) )
     print( "\033[93m" )
     print( "<<--ENJOY THIS TOOL-->>".center( 49 ) )
     print( "<<--TOOL BY HIRUWA-->>".center( 50 ) )
     print("")
     print( "[1] EXIT\n[2] RERUN" )
     print("")
     re=int(input("Enter your choice like ( 1 or 2 ) : "))
     if re == 1 :
         print("EXITING PASS GEN TOOL...........")
         exit()
     else:
         print(rer())
rer()
