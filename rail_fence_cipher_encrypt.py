r"""Encrypt a Civil War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messages

Example text to encrypt:  'Buy more Maine potatoes'

Rail fence style:  B Y O E A N P T T E
                    U M R M I E O A O S

Read zig-zag:      \/\/\/\/\/\/\/\/\/\/

Encrypted:  BYOEA NPTTE UMRMI EOSOS

"""
#------------------------------------------------------------------------------
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Buy more Maine potatoes
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------

def text_to_letter(plaintext):
    words = list(plaintext.split(" "))
    letters = [letter for word in words for letter in word.upper()]
    return letters

def rail_fence(plainletter):
    '''
    railfence = [[],[]]

    for i in range(len(plainletter)):
        if i % 2 == 0:
            railfence[0].append(plainletter[i])
        else:
            railfence[1].append(plainletter[i])
    railfence = railfence[0] + railfence[1]
    if "\n" in railfence:
        railfence.remove("\n")
    return railfence'''

    evens = plainletter[::2]
    odds = plainletter[1::2]
    railfence = evens + odds
    if "\n" in railfence:
        railfence.remove("\n")
    return railfence

def encrypt_text(railfence,plainletter):
    text = ""
    for i in range(len(plainletter)//5):
        temptext = ""
        temptext += "".join(railfence[i*5:(i+1)*5])
        text += temptext + " "
    return text

def main():
    plainletter = text_to_letter(plaintext)
    railfence = rail_fence(plainletter)
    print(railfence)
    encrypted_text = encrypt_text(railfence,plainletter)
    print(encrypted_text)

if __name__ == '__main__':
    main()