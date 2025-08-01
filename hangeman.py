import random as r

# ASCII art for hangman stages
hangman_stages = [
"""
+---+
| |
|
|
|
|
=========
""",
"""
+---+
| |
O |
|
|
|
=========
""",
"""
+---+
| |
O |
| |
|
|
=========
""",
"""
+---+
| |
O |
/| |
|
|
=========
""",
"""
+---+
| |
O |
/|\\ |
|
|
=========
""",
"""
+---+
| |
O |
/|\\ |
/ |
|
=========
""",
"""
+---+
| |
O |
/|\\ |
/ \\ |
|
=========
"""]

list = ["cricket","football","basketball","games","vallyball","bidmintan","hockey"]
lives = 6

computer_choice = r.choice(list)

#print (computer_choice)

#todo 1
place_holder = ""
l_letter = len(computer_choice)
for i in range (l_letter):
    place_holder += "-"

print (place_holder)
game_over = False

correct_letters = []
while not game_over :
    user_choice = input("guess the latter: ")
#todo 2nd
    
    display = ""
    for letter in computer_choice :
 
        if user_choice == letter :
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters :
            display += letter
        else :
            display += "-"

    print (display)

    if user_choice not in computer_choice:
        lives -= 1 
        if lives == 0 :
            game_over = True
            print ("game over you lose")


    if "-" not in display :
        game_over = True
        print ("you won")

    print (hangman_stages[lives])
        
