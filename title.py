from colorama import Fore
from colorama import Style

title = "\nWelcome to McMcT Project :-)"
print(Fore.GREEN + title.upper())
print(Style.RESET_ALL)

import unicode as u
titlestr1 = "McMcT"
titlestr2 = "Function Nr 1"
aStr = 'Name0, Location0, Address0, Price0'
aStr = aStr.replace(',', '\u5f61', 3)
ul = u.unilist
ul.append(ul[0])
mcmct = ul[0] + ul[2] + " " + ul[0] + ul[2] + " " + ul[-9]
einString = ""
# posparam = string des Titels
def title1(titlestr):
    print("\n\n")
    print(32*ul[10]) 
    print(32*ul[21]) 
    print(titlestr.center(60))
    print(32*ul[21])
    print(32*ul[13])

def title2(titlestr):
    print("\n\n")
    print(32*ul[21]) 
    print(titlestr.center(60))
    print(32*ul[21]) 
    
def title3(titlestr):
    print("\n\n")
    print(titlestr.center(60))
    print(32*ul[13])
    
def block(titlestr):
    print("\n\n")
    print(64*ul[25])
    print(ul[25]+62*ul[26]+ul[25])
    print(ul[25]+ul[26]+60*ul[27]+ul[26]+ul[25])   
    print(ul[25]+ul[26]+ul[27]+titlestr.center(55)+ul[27]+ul[26]+ul[25])
    print(ul[25]+ul[26]+60*ul[27]+ul[26]+ul[25]) 
    print(ul[25]+62*ul[26]+ul[25])
    print(64*ul[25])  
    
def block2(titlestr):
    print("\n\n")
    print(64*ul[25])
    print(ul[25]+62*ul[26]+ul[25])
    print(ul[25]+ul[26]+60*ul[27]+ul[26]+ul[25])   
    print(titlestr.center(55))
    print(ul[25]+ul[26]+60*ul[27]+ul[26]+ul[25]) 
    print(ul[25]+62*ul[26]+ul[25])
    print(64*ul[25])  
    
def block3(titlestr):
    w = 64
    m = 4
    print("\n\n")
    print((64*ul[25]).center(60))
    print((m)*" " + (w-2*m)*ul[26])
    print((2*m)*" " + (w-4*m)*ul[27])   
    print(titlestr.center(60))
    print((2*m)*" " + (w-4*m)*ul[27])   
    print((m)*" " + (w-2*m)*ul[26])
    print(64*ul[25])  

title1(mcmct)
title2(mcmct)
title3(mcmct)
block3(mcmct)
