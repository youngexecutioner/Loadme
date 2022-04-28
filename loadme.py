# Code By Young_Executioner
# Import Modules
import pyfiglet
from termcolor import colored
import os
import sys
import base64
# Functions
def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
def encode_base64(text):
        encodedBytes = base64.b64encode(text.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        print(colored("Output : " + encodedStr))


morseAlphabet ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/"
        }

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())


testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "

    # parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code, positionInString = 0):
        
        if positionInString < len(code):
            morseLetter = ""
            for key,char in enumerate(code[positionInString:]):
                if char == " ":
                    positionInString = key + positionInString + 1
                    letter = inverseMorseAlphabet[morseLetter]
                    return letter + decodeMorse(code, positionInString)
                
                else:
                    morseLetter += char
        else:
            return ""
        
    #encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message):
        encodedMessage = ""
        for char in message[:]:
            encodedMessage += morseAlphabet[char.upper()] + " "
                
        return encodedMessage 
def decodeBase64(text):

    decodedBytes = base64.b64decode(text)
    decodedStr = str(decodedBytes, "utf-8")
    print(colored("Output : " + decodedStr))       
    
# Code   
WelcomeText1 = colored(pyfiglet.figlet_format("LoadMe Decoder" , font="slant") ,"green" , attrs=['reverse' , 'blink'])
welcomeText2 = colored('Welcome To LoadMe Decoder!', 'green', attrs=['reverse'])
print(WelcomeText1)
print(welcomeText2)
print(colored('This Tool Was Writen By YOUNG_EXECUTIONER' , 'green' , attrs=['reverse']))
opts1 = colored("**************************\n1-Encode\n2-Decode\n**************************", 'red')
print(opts1)
cop1 = int(input("Choose Option : "))
if cop1 == 1:
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    opts2 = colored("**************************\n1-Base64\n2-Morse\n**************************", 'red')
    print(opts2)
    cop2 = int(input("Choose Option : "))
    if cop2 == 1:
        to_base64 = input("Enter The Normal Text : ")
        encode_base64(to_base64)
    elif cop2 == 2:
        to_morse = input("Enter The Normal Text : ")
        print(colored("Output : " + encodeToMorse(to_morse) , "green"))
        
    else:
        delete_last_line()
        delete_last_line()
        delete_last_line()
        delete_last_line()
        delete_last_line()
        err1 = colored("**************************\nInvalid Option!\nExiting..\n**************************", 'red')
        print(err1)    
        
        
        
        

            
elif cop1 == 2:
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    opts3 = colored("**************************\n1-Base64\n2-Morse\n**************************", 'red')
    print(opts3)
    cop3 = int(input("Choose Option : "))
    if cop3 == 1:
       from_base64 = input("Enter The Normal Text : ")
       decodeBase64(from_base64)
    elif cop3 == 2:
        from_morse = input("Enter The Normal Text : ")
        print(colored("Output : " + decodeMorse(from_morse) , "green"))
    else:
        delete_last_line()
        delete_last_line()
        delete_last_line()
        delete_last_line()
        delete_last_line()
        err1 = colored("**************************\nInvalid Option!\nExiting..\n**************************", 'red')
        print(err1)    
else:
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    delete_last_line()
    err1 = colored("**************************\nInvalid Option!\nExiting..\n**************************", 'red')
    print(err1)



