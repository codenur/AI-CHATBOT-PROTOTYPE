# -*- coding: cp1252 -*-
import sys
import random
from NUR import John
from NUR import AItime
from NUR import timer
from time import *
from threading import *
import threading
import json
from difflib import get_close_matches
from time import sleep
import time


def translate(w):
    w = w.lower()
    if w in data:
        print"\t"
        return data[w]
    
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input("I think you mean %s instead? \n Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if ans == "Y" or ans=="y":
            print" "
            return data[get_close_matches(w, data.keys())[0]]
        elif ans == "N" or ans=="n":
            
            return "i don't think so,it exists"

        else:

            return "Sorry ,i didn't get it"
    else:

        return "The term does not exist"
    


"""    
def sentns(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        return data[get_close_matches(w, data.keys())[0]]     
        #print("%s")
        
       
    else:
       # return "The term does not exist."

        return "Sorry ! I didn't get you, ask me clearly/properly "    
"""




def p1():
    
    naz=open("answer.txt",'r')
    lines=naz.readlines() #print "JOHN ",":\t"
    print "\t", lines[0],"\t",lines[1],"\t",lines[2]
    return""


def p2():
    z=qw.split(',')
    for i in z:
        if i in t:
            print "\t",i,Q
            
            #print "JOHN ",":\t"
            #print "\t",i,Q
    return""

def p3():
    naz=open("answer.txt",'r')
    lines=naz.readlines()
    
    #print "JOHN ",":\t"
    print  "\t", lines[3]
    return""

def p4():
    #timer.typing2()
    print  "\t",AItime.time()
    return" "


data = json.load(open("db.json"))
#data1= json.load(open("db1.json"))
naz=open("answer.txt",'r')
name=['nur','NUR','Nur','Rohan','ROHAN','rohan']
q=["WHO MADE YOU ?",'WHO MADE YOU?',"WHO'S YOUR OWNER?","WHO CREATED YOU ?","OWNER NAME ?","OWNER","who made you ?","who's your owner?","who s your owner? ", "owner name?","owner","who made you?","who are you?","WHO ARE YOU?","who are you","WHO are YOU","who made you","whos your owner"
"owner name","who made you?","who is your owner?","who made you?","who is your owner ?","who is your owner","who created you?","who's your owner","owner name","who created you","WHO'S YOUR OWNER","who is your owner","who's your owner"]
t=["hi","HI","hey","HEY","Hey","HELLO","Hi","hello","hi john","HI john","hi JOHN",'HI JOHN',"HI JOHN",'hey','HEY','hey john','hey JOHN','HEY john','HEY JOHN','hello john','HELLO john','HELLO john','hello john','HELLO JOHN']
love=["LOVE","love","CRUSH","crush"]
p=['do you love somebody else?','DO YOU LOVE SOMEBODY ELSE?','DO YOU LOVE SOMEBODY ELSE','do you love somebody else','do you love someone','do you love somebody','are you in love?','are you in love ?','ARE YOU IN LOVE?','ARE YOU IN LOVE ?']
time1=["What time is it?","What’s the time?","Could you tell me the time?","Do you know what time it is?","WHAT TIME IS IT?","WHAT’S THE TIME?","COULD YOU TELL ME THE TIME?","DO YOU KNOW WHAT TIME IT IS?","What time is it","What’s the time","Could you tell me the time","WHAT TIME IS IT","WHAT’S THE TIME,WHAT IS THE TIME","COULD YOU TELL ME THE TIME","DO YOU KNOW WHAT TIME IT IS","WHAT TIME IS IT?","WHAT’S THE TIME?","COULD YOU TELL ME THE TIME?","DO YOU KNOW WHAT TIME IT IS?","WHAT TIME IS IT?","WHAT’S THE TIME?","COULD YOU TELL ME THE TIME?","DO YOU KNOW WHAT TIME IT IS?","WHAT TIME IS IT","WHAT’S THE TIME","COULD YOU TELL ME THE TIME","WHAT TIME IS IT","WHAT’S THE TIME,WHAT IS THE TIME","COULD YOU TELL ME THE TIME","DO YOU KNOW WHAT TIME IT IS","what time is it?","what’s the time?","could you tell me the time?","do you know what time it is?","what time is it?","what’s the time?","could you tell me the time?","do you know what time it is?","what time is it","what’s the time","could you tell me the time","what time is it","what’s the time,what is the time","could you tell me the time","do you know what time it is","WHAT IS THE TIME?","WHAT IS THE TIME ?","what is the time?","What is the time?","What is the time ?","Could you tell me the time ?","Do you know what time it is ?","WHAT TIME IS IT ?","WHAT’S THE TIME ?","COULD YOU TELL ME THE TIME ?","DO YOU KNOW WHAT TIME IT IS ?"]
y=["what","is","are","?","WHAT","What","IS","ARE","an","AN","?",'a',"A"]

#alll=q,t,love,p

sys.stderr.write("\t\tHELLO,I AM JOHN \n\n\t _____A COMPUTER PROGRAM_____\n")

lines=naz.readlines()

print""

print"YOUR NAME \n"


Q=input()
if Q in name:
    print"WELCOME Again Sir"
else:
    print "Hello\t",Q


try:

    while True:
        
        print"======================================================" 
        qw=input()
        print"======================================================"
        
        #John.John()
        
        time.sleep(4)

        if qw in q and qw not in t and qw not in p:
            
            print p1()

        elif qw in t and qw not in q and qw not in p:
            print p2()


        elif qw in p and qw not in q and qw not in t:
            print p3()

        elif qw in time1:
            print p4()

        elif qw=='date':
            print"\t",AItime.date()

        elif qw:
            
            split_word=qw.split(',')
            l=len(split_word)
            for i in split_word:
                if i in q and i not in t and i not in p:
                    print p1()
                elif i in t and i not in q and i not in p:
                    print p2()
                    continue
                elif i in p and i not in q and i not in t:             # and qw not in p and qw not in q and qw not in t
                    print p3()
                elif i in time1 and i not in q and i not in t and i not in p:
                    print p4()
                elif l==1:
                    output = translate(qw)      #"Should laptops be allowed in classrooms ?"
                    if type(output) == list:
                        for item in output:
                            print"\t",item
                    else:
                        print "\t",output
        
                        
        else:
            print" "
            
                
                    
                    
    else:
        
           
        
        print" "

    print" "
    
         
except NameError:
    sys.stderr.write("NAMEEROOR")
    
except SyntaxError:
    sys.stderr.write("SYNTAXERROR")
    
