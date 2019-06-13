6_Wait_for_a_break.ipynb
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import time
import webbrowser

def new_game():
    i = 0
    while i < 3:
        #print(i)
        i = i + 1
        webbrowser.open("https://www.youtube.com/watch?v=fRh_vgS2dFE&list=PLx0sYbCqOb8Q_CLZC2BdBSKEEB59BOPUM")
        time.sleep(10)

    
new_game()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Function_exercises.ipynb
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Type your code here
def my_function(number):
    if (type(number) != int or number < 0 ): print(None)
    else:
        a = number+5
        print (a)
        return a
		
my_function(66)
my_function(55)
my_function("None")
my_function('5+4')

###################################################################

# Type your code here
def my_function(left, right):
    if (type(left and right) != int or left and right < 0 ): print(None)
    else:
        a = left*right
        print (a)
        return a
        
my_function(1114, 632)
###################################################################
# Type your code here
def my_function(left, right):
    if (type(left and right) != int or left and right < 0 ): print(None)
    else:
        a = (left*2)+(right*2)
        print (a)
		return a

my_function(1, 3)

###################################################################
Function_exercises.ipynb
# Functions Exercise 4
проверка не правильная 

def my_function(number):
    if (type(number) != int or number < 0 ): print(None)
    else:
        a = math.pi * number * number
        print (a)
        return a
###################################################################

# Type your code here
import math
def my_function(x):
    try:
        x=float(x)
        print(x)
        
        a = (math.pow(x, 4))-12*(math.pow(x, 3))+13*(math.pow(x, 2))+11
        print (a)
        return a
    
    except ValueError:
        print('None')
    
###################################################################

	
import math
def my_function(x):
    a = (math.sin(x))-(math.cos(x))+((math.cos(x))*(math.sin(x)))
    print (a)
    return a
	
###################################################################

# Type your code here
import math
def my_function(x):
    a = (math.sin(x))-(math.cos(x))+((math.cos(x))*(math.sin(x)))
    print (a)
    return a
	
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
####
import random
import math

def input_guess(guess):
    # Основная программа
    num = int(guess)
    print("Guess was {}".format(num))
    # Удалите следующую строку после того, как добавите ваш код
    if num == secret_number: 
        print ('!Correct!') 
        return True
    elif num < secret_number : print ('!Lower!') 
    else : print ('!Higher!') 

import random
####
def new_game():
    # Инициализируйте глобальные переменные, используемые в коде, здесь
    global secret_number
    secret_number = random.randrange(0, 100)
    print (secret_number)
    return secret_number
    
new_game()

####

new_game()
print (secret_number)
i = 7
while i > 0 :
    print ('Number of remaining guesses is ' + str(i))
    num1 = input()
    if input_guess(num1):
        break
    i -=1
print ("Good bye!")
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import random
def new_comp():
    comp = random.randrange(0, 5)
    print (comp)
    return comp

def name_to_number():
    
    name=input()
    
    if name == "rock": return 1
    elif name == "Spock": return 2
    elif name == "paper": return 3
    elif name == "lizard": return 4
    elif name == "scissors": return 5
    else: print ('wrong name')


def new_game():
    comp =new_comp()
    my = int(name_to_number())
    #my=int(input())
    if ((comp > my) and ((my+1)==comp or (my+2)==comp)) or ((comp < my) and ((comp-1)==my or (comp-2)==my) or (comp+2) < my):
        print("conp win!")
    else: print("you win!")    
    return

new_game()







