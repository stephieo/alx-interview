#!/usr/bin/python3
"""This module contains the solution to the utf validation problem
"""

def validUTF8(data):
    """ Determine if data set represents a valid UTF-8 encoding  """
    bytes_to_process = 0

    for byte in data:
        if bytes_to_process == 0:
            if byte >> 5 == 0b110:
                bytes_to_process = 1
            elif byte >> 4 == 0b1110:
                bytes_to_process = 2
            elif byte >> 3 == 0b11110:
                bytes_to_process = 3
            elif (byte >> 7) == 0:
                continue 
            else:
                return False 
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
