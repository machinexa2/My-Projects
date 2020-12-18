import os
import random
import sys
from time import *

class SHITori:

    def __init__(self):
        self.game_over = False
        self.temp_words = []

    def play(self, word: str):
        if len(self.temp_words) == 0:
            self.temp_words.append(word)
            return self.temp_words
        else:
            if self.temp_words[-1][-1] == word[0]:    
                if self.temp_words.count(word) == 0:
                    self.temp_words.append(word)
                    return self.temp_words
                else:
                    self.game_over = True
                    return "GAME OVER!!!"
            else:
                self.game_over = True
                return "GAME OVER!!!"
    def restart(self):
        self.temp_words = []
        self.game_over = False
        return "GAME RESTARTED!!!"

obj = SHITori()

assert obj.game_over  == False
assert obj.play("apple") == ["apple"]
assert obj.temp_words == ["apple"]
assert obj.play("ear") == ["apple", "ear"]
assert obj.play("rhino") == ["apple", "ear", "rhino"]
assert obj.play("ocelot") == ["apple", "ear", "rhino", "ocelot"]
assert obj.game_over is False
assert obj.play("oops") == "GAME OVER!!!"
assert obj.game_over is True
assert obj.temp_words == ["apple", "ear", "rhino", "ocelot"]

assert obj.restart() == "GAME RESTARTED!!!"
assert obj.temp_words == []
assert obj.game_over is False
assert obj.play("hostess") == ["hostess"]
assert obj.game_over is False
assert obj.play("stash") == ["hostess", "stash"]
assert obj.play("hostess") == "GAME OVER!!!"
assert obj.temp_words == ["hostess", "stash"]
obj.restart()





