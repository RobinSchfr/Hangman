import hangmanAscii


class Console:
    game = None

    def __init__(self, game):
        self.game = game
        self.main()

    def draw(self):
        print(hangmanAscii.asciis[9 - self.game.fails])
        print('\nUnbenutzte Buchstaben: ' + self.printChars(self.game.unusedChars))
        print('Benutzte Buchstaben: ' + self.printChars(self.game.usedChars))
        print('Wort: ' + self.game.wordWithUnderscores)
        guess = input("Tipp: ").lower()
        msg = self.game.guess(guess)
        self.message(msg)
        print('-' * 40 + '\n')

    def printChars(self, charList):
        chars = ''
        for char in charList:
            chars += char + ' '
        return chars

    def message(self, msg):
        if msg == 1:
            print('Wort gefunden!')
        if msg == 2:
            print('Richtiger Buchstabe!')
        if msg == -1:
            print('Falsches Wort!')
        if msg == -2:
            print('Falscher Buchstabe oder ungültige Eingabe!')

    def main(self):
        # print(self.game.word)
        while self.game.isRunning():
            self.draw()
        print('Spiel beendet! - Das Wort lautet: ' + self.game.word)