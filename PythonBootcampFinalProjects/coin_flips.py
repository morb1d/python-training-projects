# File coin_flips.py

"""
Write some code that simulates flipping a single coin however many times the user decides. 
The code should record the outcomes and count the number of tails and heads.
"""
from random import randint

# randint = 0 <- tail
# randint = 1 <- head
count_of_tails = 0
count_of_heads = 0
keep_playing = 1

while (keep_playing):
    coin_flip = randint(0,1)
    
    if coin_flip == 0: 
        print('Tail tossed')
        count_of_tails += 1
    else:
        print('Head tossed')
        count_of_heads += 1 

    user_continue_decision = input("\nDo you want to continue (Y/N): ") 

    if user_continue_decision == "N": keep_playing = 0

print('# of tails tossed: ',count_of_tails,'\n# of heads tossed: ',count_of_heads)