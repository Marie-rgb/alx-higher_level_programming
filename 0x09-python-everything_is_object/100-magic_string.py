#!/usr/bin/python3
def magic_string(kenya=[0]):
    kenya[0] = kenya[0] + 1
    return ("Nairobi, " * kenya[0])[:-2]
