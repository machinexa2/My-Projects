import random
from time import *
import shitori
import sys
import os
filepath = "all_words_in_world"

if len(sys.argv) == 2:
    filepath = sys.argv[1]

if os.path.exists(filepath):
    wordlist_old = [line.rstrip('\n') for line in open(filepath)] 
    wordlist_new = [word for word in wordlist_old if len(word) >= 3 and not ' ' in word] 

def bot_player(wordlist: list) -> None: 
    status = True
    count = 0
    rnd = random.choice(wordlist)
    while status == True:
        if count >=1:
            for i in wordlist:
                rnd = i
                if rnd[0] == temp[-1][-1]:
                    break
        temp = obj.play(rnd)
        os.system("clear") 
        if temp != "GAME OVER!!!":
            print(f"The wordlist is {temp}")
            sleep(0)
            wordlist.remove(rnd)
            count += 1
        else:
            status = False
            print(f"Bot played {count} number of times before running out of words")
obj = shitori.SHITori()
bot_player(wordlist_new)
