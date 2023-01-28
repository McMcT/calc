import math
import title as ti


print(6*"\n")
print("***********************************")
welcomeMcMcT = "Willkommen im McMcT Projekt"
print("***********************************")
print(1*"\n")

ti.title1(welcomeMcMcT)

nullswitch = False
hello = "Willkommen im McMcT Projekt"

funcList = ["Funktionen", "Währungsrechner","Dreiecks-Geometrie","Vektorberechnung"]
#while(True)

funcMenu =    '''
            1 - ''' + funcList[0] + '''
            2 - ''' + funcList[1] + '''
            3 - ''' + funcList[2] + '''
            4 - ''' + funcList[3] + '''
    
    '''

ti.block3(funcMenu)
operation = int (input("Bitte wählen Sie ein Funktion(1-4) des McMcT-Taschenrechners aus:  "))



#Auswahl 

match operation:
    
    case 1:
        print ("Viel Spass beim "+ funcList[0])
        
    case 2:
        print ("Viel Spass beim "+ funcList[1])

    case 3:
        print ("Viel Spass beim "+ funcList[2])

    case 4:
        print ("Viel Spass beim "+ funcList[0])
    
    case _:
        print ("Sie haben ein falsches Zeichen eingegeben....lernen Sie bitte ordentlich tippen...sorry :)")
        
if(nullswitch == True):
    print("Der McMcT ist aufgrund dieser inakzeptablen Operation explodiert - Kawuuum!")
else:
    print ("Danke für die kompetente Verwendung unseres McMcT :)")
        
# Berechnung mit ende beenden wollen, oder ob sie mit start eine neue Rechnung starten wollen.
