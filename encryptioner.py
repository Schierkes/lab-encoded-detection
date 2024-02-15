import os
import sys
import math

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)):
        yield chr(c)
    yield chr(ord(c2))

azalphabet = [ a for a in char_range('A', 'Z') ]

def byteshift(mode, key, text):
    alphabet = [a for a in char_range('\0', '\xff')]
    key_ints = [alphabet.index(k) for k in key]
    key_length = len(key)
    alphabet_length = len(alphabet)

    shift_text = []
    for i in range(0, len(text)):
        c = text[i]
        c_index = alphabet.index(c)
        key_shift = key_ints[i % key_length]
        if mode == 'enc':
            shift_index = (c_index + key_shift) % alphabet_length
        elif mode == 'dec':
            shift_index = (c_index - key_shift + alphabet_length) % alphabet_length
            
    shift_text.append(alphabet[shift_index])
    return shift_text

def main():
    print("What'll it be, Mr. Bond?")
    modeSel = input()
    print("Excellent choice, Mr. Bond. The key?")
    keySel = input()
    f = open(keySel, "rb").read(-1)
    print("Your last choice, Mr. Bond. What is the block of text?")
    textTo = input()
    Passon = open(keySel, "rb").read(-1)
    
    shifted = byteshift(modeSel, f, Passon)

    print(shifted)
    
if __name__ == "__main__":
    main()
