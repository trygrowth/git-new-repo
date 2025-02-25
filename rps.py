import random
choices = ('r','p','s')
emojis = {'r':'🪨','p':'📃','s':'✂️'}
while True:
    my_choice = int(input('Rock, paper, scissors (r/p/s)')).lower()
    if my_choice not in choices:
        print('Enter a valid choice!!!!!')
        continue

    computer_choice = random.choice(choices) 

    print(f'your choice {emojis[my_choice]}')
    print(f'computer choice {emojis[computer_choice]}')
    if my_choice == computer_choice:
        print('tie!!')
    elif( 
        (my_choice == 'r' and computer_choice == 's') or
        (my_choice == 's' and computer_choice == 'p') or
        (my_choice == 'p' and computer_choice == 'r')):
                print('you win')
    else:
          print('you lose')
    should_comtinue = input('continue? (y/n)').lower()
    if should_comtinue == 'n':
      break