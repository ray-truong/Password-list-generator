#!/usr/bin/env python3
import os
from pathlib import Path

months =  ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
seasons = ['Summer', 'Spring', 'Autumn', 'Fall', 'Winter']


passwords = []

def print_passwords():
    for i in passwords:
        print(i)

def initiate_passwords():
    loop = True
    while loop == True:
        y_or_n = input('\nDo you want to add months to the list (Y/N)>> ')
        if y_or_n.lower() == 'y':
            passwords.extend(months)
            loop = False
        if y_or_n.lower() == 'n':
            loop = False
    loop = True
    while loop == True:
        y_or_n = input('\nDo you want to add seasons to the list (Y/N)>> ')
        if y_or_n.lower() == 'y':
            passwords.extend(seasons)
            loop = False
        if y_or_n.lower() == 'n':
            loop = False 
    loop = True
    while loop == True:
        y_or_n = input('\nDo you want to add passwords from a file (Y/N)>> ')
        if y_or_n.lower() == 'y':
            name = input('Please input the file you wish to read from: ')
            current_working_directory = os.getcwd()
            input_file = Path(os.path.join(current_working_directory, name)) 
            if input_file.is_file():
                with open(input_file, 'r') as file:
                    for line in file:
                        current_line = line.strip().split('\n')
                        passwords.extend(current_line)
                loop = False
            if not input_file.is_file():
                loop2 = True
                while loop2 == True:
                    y_or_n = input('\nThat file doesn\'t exist, do you want to read from a different file file (Y/N) >> ')
                    if y_or_n.lower() == 'y':
                        loop2 = False
                    if y_or_n.lower() == 'n':
                        loop2 = False
                        loop = False
        if y_or_n.lower() == 'n':
            loop = False

def add_words():
    new_word_list = []
    loop = True
    while loop == True:
        y_or_n = input('\nDo you want to another word to your list (Y/N)>> ')
        if y_or_n.lower() == 'y':
            new_word = input('Add new word: ')
            new_word_list.append(new_word)

        if y_or_n.lower() == 'n':
            loop = False
    if len(new_word_list) != 0:
        passwords.extend(new_word_list)
        print('New words added:\n')
        for i in new_word_list:
            print(i)
            

def lowercase_passwords():
    loop = True
    while loop ==  True:
        y_or_n = input('\nDo you want to include lowercase words (Y/N)>> ')
        if y_or_n.lower() == 'y' or y_or_n.lower() == 'n':
            loop = False
    
    if y_or_n.lower() == 'y':
        lowercases = []
        for i in passwords:
            lowercases.append(i.lower())
        passwords.extend(lowercases)

def append_words():
    appended_wordlist = [] 
    loop = True
    while loop == True:
        y_or_n = input('\nDo you want to append anything to your passwords (Y/N)>> ')
        if y_or_n.lower() == 'y':
            end_of_word = input('Add this to the end of your words: ')
            for i in passwords:
                appended_wordlist.append(i + end_of_word)

        if y_or_n.lower() == 'n':
            loop = False

    if len(appended_wordlist) != 0:
        passwords.extend(appended_wordlist)

def save_wordlist():
    loop = True
    while loop == True:
        y_or_n = input('\nDo you want to save this wordlist as a file (Y/N)>> ')
        if y_or_n.lower() == 'y':
            name = input('\nPlease input name of passwords file>> ')
            current_working_directory = os.getcwd()
            output_file = os.path.join(current_working_directory, name)
            loop = False
            with open(output_file, 'w') as file:
                for i in passwords:
                    file.write(i + '\n')
        if y_or_n.lower() == 'n':
            loop = False


def main():
    initiate_passwords()
    print_passwords()
    add_words()
    lowercase_passwords()
    print_passwords()
    append_words()
    print_passwords()
    save_wordlist()
    length = len(passwords)
    print("The size of your password list is " + str(length))


if __name__ == "__main__":
    main()
