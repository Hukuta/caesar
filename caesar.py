#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Odarchenko N.D.'

my_symbols = 'abcdefghijklmnopqrstuvwxyz'
letters = my_symbols.upper() + my_symbols


def caesar_encode(message, key):
    translated = ''
    # run the encryption code on each symbol in the message
    for symbol in message:
        if symbol in letters:
            # get the number of the symbol
            num = letters.find(symbol) - key

            if num < 0:
                num += len(letters)

            # add number's symbol at the end of translated
            translated += letters[num]
        else:
            # just add the symbol without encrypting
            translated += symbol

    return translated


mess = 'The Spartans came to Rome! Rome is in danger.'
encoded = caesar_encode(mess, 7)
decoded = caesar_encode(encoded, -7)
print('\r\nEncoded Message:\r\n%s\r\nDecoded Message:\r\n%s\r\n' % (encoded, decoded))


def symbol_statistics(book, symbols_lower):
    stat = dict()
    for symbol_lower in symbols_lower:
        stat[symbol_lower] = 0

    for symbol in book:
        symbol = symbol.lower()

        if symbol in symbols_lower:
            stat[symbol] += 1

    return sorted(stat.items(), key=lambda x: x[1], reverse=True)

with open('gpl.txt', 'r') as read_file:
    some_text = read_file.read()
normal_statistics = symbol_statistics(some_text, my_symbols)


def hack_caesar(message):
    key_matches = {}
    for key in range(1, len(letters) - 1):
        key_stat = symbol_statistics(caesar_encode(message, key), my_symbols)
        key_matches[key] = 0
        for symbol_num in range(0, len(normal_statistics)):
            if key_stat[symbol_num][0] == normal_statistics[symbol_num][0]:
                key_matches[key] += 1

                #return key, caesar_encode(message, key)
    best_matches = sorted(key_matches.items(), key=lambda x: x[1], reverse=True)
    best_matches_count = best_matches[0][1]
    hacked_messages = []
    for key, cnt in best_matches:
        if cnt != best_matches_count:
            break
        hacked_messages.append((key, caesar_encode(message, key)))
    return hacked_messages

words_dictionary = [' is ', 'the ', ' to ', ' are ']
for key, message in hack_caesar(encoded):
    message_lowercase = message.lower()
    # checking by dictionary
    for word in words_dictionary:
        if word in message_lowercase:
            print('Hacked message: %s\r\n with key: %s\r\n' % (message, key))
            break