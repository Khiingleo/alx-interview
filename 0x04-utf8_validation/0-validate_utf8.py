#!/usr/bin/python3
"""
defines a function validUTF8
"""


def validUTF8(data):
    """
    determine if a given data represents a valid
    utf-8 encoding
    """
    # iterate through the data
    i = 0
    while i < len(data):
        # mask the integer to keep only the 8 least significant bits
        data[i] = data[i] & 0b11111111
        # check if the first bit is = 0
        if data[i] >> 7 == 0:
            i += 1
        # check if it is a two byte character
        elif (data[i] >> 5 == 0b110 and i + 1 < len(data)
              and data[i + 1] >> 6 == 0b10):
            i += 2
        # check if it is a three byte character
        elif (data[i] >> 4 == 0b1110 and i + 2 < len(data)
              and data[i + 1] >> 6 == 0b10 and data[i + 2] >> 6 == 0b10):
            i += 3
        # check if it is a four byte character
        elif (data[i] >> 3 == 0b11110 and i + 3 < len(data)
              and data[i + 1] >> 6 == 0b10 and data[i + 2] >> 6 == 0b10
              and data[i + 3] >> 6 == 0b10):
            i += 4
        else:
            return False

    return True
