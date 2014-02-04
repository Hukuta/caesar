#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Odarchenko N.D.'


def caesar_encode(message, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
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


mess = 'The Spartans came to Rome!'
encoded = caesar_encode(mess, 7)
decoded = caesar_encode(encoded, -7)
print('\r\nEncoded Message:\r\n%s\r\nDecoded Message:\r\n%s\r\n' % (encoded, decoded))