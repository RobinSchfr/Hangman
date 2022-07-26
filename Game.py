import random
import string


class Game:
    word = None
    wordWithUnderscores = None
    fails = None
    usedChars = None
    unusedChars = None
    running = None

    def __init__(self):
        self.word = self.pickRndWord()
        self.wordWithUnderscores = '_' * len(self.word)
        self.fails = 0
        self.usedChars = []
        self.unusedChars = list(string.ascii_lowercase)
        self.running = True

    def guess(self, char):      # Either a single char or an entire word but no substrings
        if self.running:
            if len(char) == len(self.word):
                if char == self.word:
                    self.wordWithUnderscores = char
                    self.running = False
                    return 1
                else:
                    self.fails += 1
                    return -1

            if char in self.word and char in self.unusedChars and len(char) == 1:
                self.reorderLists(char)
                i = 0
                index = -1
                while i < self.word.count(char):
                    index = self.word.index(char, index + 1)
                    self.wordWithUnderscores = self.wordWithUnderscores[:index] + char + self.wordWithUnderscores[index + 1:]
                    i += 1
                if self.wordWithUnderscores == self.word:
                    self.running = False
                    return 1
                return 2

            else:
                self.reorderLists(char)
                self.fails += 1
                return -2

    def isRunning(self):
        if self.fails > 9:
            self.running = False
        return self.running

    def reorderLists(self, char):
        if self.unusedChars.count(char) > 0:
            self.unusedChars.remove(char)
            self.usedChars.append(char)
            self.usedChars.sort()

    def pickRndWord(self):
        with open('wordlist.txt', 'r') as f:
            words = f.readlines()
            # result = list(filter(lambda x: len(x) == 11, result))
            word = words[random.randint(0, len(words) - 1)]
            word = word[:-1]    # cut off the \n
            return word