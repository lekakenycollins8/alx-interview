#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """validate utf8 data using bitwise operations"""
    n_bytes = 0
    for num in data:
        num = num & 0xFF
        if n_bytes == 0:
            if num >> 7 == 0:
                continue
            elif num >> 5 == 0b110:
                n_bytes = 1
            elif num >> 4 == 0b1110:
                n_bytes = 2
            elif num >> 3 == 0b11110:
                n_bytes = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            n_bytes -= 1
    return n_bytes == 0
