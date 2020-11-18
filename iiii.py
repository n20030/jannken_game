#Preselected
import time

def sl1():
	time.sleep(1)

def sl2():
	time.sleep(2)



print("hello! It's rock-paper-scissors time")
sl1()
jan = input("-- Please enter the number --  \n 1. rock \n 2. scissors \n 3. paper  ")
sl1()
print('You chose number ' + str(jan) +":")

#Game start call
sl2()
print("Rock, ")
sl1()
print("Paper,")
sl1()
print("Scissors,")
sl1()
print("Go!!")
sl1()


def chose_cpu():
	print("I chose " + random_cpu)

import random
a = 'rock'
b = 'scissors'
c = 'paper'
cpu = [a , b , c]
random_cpu = random.choice(cpu)
bout = str(jan) + random_cpu
sl2()
#print(bout)

if bout == '1' + a or bout == '2' + b or bout == '3' + c :
	chose_cpu()
	print('draw!!')

elif bout == '1' + b or bout == '2' + c or bout == '3' + a :
	chose_cpu()
	print('Your win!!')

elif bout == '1' + c or bout == '2' + a or bout == '3' + b :
	chose_cpu()
	print('Your defeat...')

else :
	print("Choose one of 1,2,3 !!!!")