from random import randint
def play_level(width):
    given_number = input('select number ')
    secret_number = randint(1, width)
    if given_number == secret_number:
        print('yay')
    else:
        second_guess = input('try again')
        if second_guess == secret_number:
            print('yay')


        else:
            print('answer is {}'.format(secret_number))

for level in range(1,1000000000):
    play_level(level * 5)