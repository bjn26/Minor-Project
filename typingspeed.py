from time import *
import random as r

def mistake(strtest,usertest):
    error=0
    for i in range(len(strtest)):
        try:
            if strtest[i]!=usertest[i]:
                error=error+1
        except:
            error=error+1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

test="Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems."\
    ,"My name is xyz.What is yours?","welcome to the typing test!It is fun."
test1=r.choice(test)
print("-----typing speed-----")
print(test1)
print()
time_1=time()
testinput=input(" Enter: ")
time_2=time()

print("Speed : ",speed_time(time_1,time_2,testinput),"w/sec")
print("error : ",mistake(test1,testinput))