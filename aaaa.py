#Preselectedaaaa
import time
print("hello! It's rock-paper-scissors time")
time.sleep(2)
jan = input("-- Please enter the number --  \n 1. rock \n 2. scissors \n 3. paper  ")
time.sleep(1)
print('You chose number ' + str(jan) +":")

#Game start call
time.sleep(2)
print("Rock, ")
time.sleep(1)
print("Paper,")
time.sleep(1)
print("Scissors,")
time.sleep(1)
print("Go!!")
time.sleep(1)


import random
a = 'rock'
b = 'scissors'
c = 'paper'
cpu = [a , b , c]
random_cpu = random.choice(cpu)
bout = str(jan) + random_cpu
time.sleep(2)
#print(bout)

if bout == '1' + a or bout == '2' + b or bout == '3' + c :
	print("I chose " + random_cpu)
	print('draw!!')

elif bout == '1' + b or bout == '2' + c or bout == '3' + a :
	print("I chose " + random_cpu)
	print('Your win!!')

elif bout == '1' + c or bout == '2' + a or bout == '3' + b :
	print("I chose " + random_cpu)
	print('Your defeat...')

else :
	print("Choose one of 1,2,3 !!!!")
