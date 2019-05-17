#!/usr/bin/env python3
import random


def main():
    names_ru = ['La', 'Si', 'Do', 'Re', 'Mi', 'Fa', 'Sol']
    letters = [chr(ord('A') + x) for x in range(7)]
    names_to_letters = dict(zip(names_ru, letters))
    letters_to_names = dict(zip(letters, names_ru))

    while True:
        if random.choice([0, 1]) == 0:
            name = random.choice(names_ru)
            ans = input(name + '?')
            if ans.lower() == names_to_letters[name].lower():
                print('Correct!')
            else:
                print('Incorrect, right answer is: ' + names_to_letters[name])
        else:
            letter = random.choice(letters)
            ans = input(letter + '?')
            if ans.lower() == letters_to_names[letter].lower():
                print('Correct!')
            else:
                print('Incorrect, right answer is: ' + letters_to_names[letter])


if __name__ == '__main__':
    main()

