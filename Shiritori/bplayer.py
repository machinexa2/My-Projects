#BOT PlAYING SHITORI, PROVIDE HIM A BIG DICTIONARY AND SEE HOW MUCH CAN HE GUESS BEFORE RUNNING OUT OF WORDS
import random
from time import *
import shitori
import sys
import os
filepath = "/usr/share/dirb/wordlists/common.txt"

if len(sys.argv) == 2:
    filepath = sys.argv[1]

if os.path.exists(filepath):
    wordlist_old = [line.rstrip('\n') for line in open(filepath)] #oneliner yeah
    wordlist_new = [word for word in wordlist_old if len(word) >= 3 and not '_' in word and not '-' in word and not '.' in word and not '~' in word and not '1' in word and not '2' in word and not '3' in word and not '4' in word and not '5' in word and not '6' in word and not '7' in word and not '8' in word and not '9' in word and not '0' in word] #oneliner MORE YEAH
#
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
            sleep(0.2)
            wordlist.remove(rnd)
            count += 1
        else:
            status = False
            print(f"Bot played {count} number of times before running out of words")
obj = shitori.SHITori()
bot_player(wordlist_new)
