#!/bin/python3
#####################
#
#####################
import sys
import datetime as dt
print("Hello World!")
#defining a function
def PrintThis() :
	print("Print This")

PrintThis()
#plays with lists
gameList = ["Final Fantasy 7","Super Metroid","Monster Hunter"]
print(gameList)
print(gameList[1])
print(gameList[:2])
print(gameList[1:])
#For loop syntax in printing a list
for x in  gameList:
	print(x)

#while loops
i=1
while i < 10 :
	print(i)
	i+=1
print(dt.date.today().strftime("%m/%d/%Y"))

dt_string = dt.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

print("date and time =", dt_string)

print(sys.version)
print(sys.path)

sentence = "This is a Sentence"
print(sentence)
print(sentence.split())

for x in sentence.split() :
	print(x)

mychars = {"Orvac":60,"Aliah":50,"Dark" : 56}
print(mychars)
mychars['Brazeldo']=35
print(mychars)
print(mychars.get("Brazeldo"))
sys.exit()

