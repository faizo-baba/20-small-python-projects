print ("welcome to password genrater")
import random as r

l_list = ["a","A","b","B","c","C","d","D","e","E","f","F"]
n_list = [1,2,3,4,5,6,7,8,9]
s_list = ["!","@","$","%","&","*"]

user_l = int (input("enter the number of letters u want in ur password\n"))
user_n = int (input(f"enter the number of numbers u want in ur password\n"))
user_s = int (input(f"enter the number of symbols u want in ur password\n"))

password_list = []
for letters in range(user_l) :
    password_list.append(r.choice(l_list))

for numbers in range(user_n) :
    password_list.append(r.choice(n_list))

for symbols in range(user_s) :
    password_list.append(r.choice(s_list))

r.shuffle(password_list)
print (password_list)

password = ""
for char in password_list :
    password += str(char) 

print (f"your password is {password}")