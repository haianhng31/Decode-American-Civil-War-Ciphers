r"""Decrypt a Civil War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messages

Example plaintext:  'Buy more Maine potatoes'

Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S

Read zig-zag:      \/\/\/\/\/\/\/\/\/\/

Ciphertext:  BYOEA NPTTE UMRMI EOSOS

"""
import math
import itertools

#------------------------------------------------------------------------------
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES

"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------
def prep_ciphertext(ciphertext): # String -> String
    # remove white space
    return "".join(ciphertext.split())

def decrypt(text):
    railfence = ""
    if len(text)%2 == 0:
        for i in range(0,len(text)//2):
            railfence += text[i].lower() + text[i + len(text)//2].lower()
    else:
        for i in range(0,(len(text)+1)//2):
            railfence += text[i].lower() + text[i + len(text+1) // 2].lower()
    return railfence


def main():
    prepciphertext = prep_ciphertext(ciphertext)
    plaintext = decrypt(prepciphertext)
    print(plaintext)

if __name__ == '__main__':
    main()