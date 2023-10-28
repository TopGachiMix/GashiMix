from random import randint

user = int(input("угадай число от 1 до 5"))
comp = randint(1,5)

if user == comp:
    print('ты выйграл')
else:
    print('лузер')