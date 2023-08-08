"""Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers means start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
"""

import sys

#==============================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple-quotes):
# ciphertext = """ REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW HEADING TO GONE TO SOUTH FILLER """
ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDANTS OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"""
#ciphertext = """ 16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"""

# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix:
ROWS = 6

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = """ -1 2 -3 4"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#==============================================================================

def validate_col_row(cipherlist):
    factors = []
    for i in range(2,len(cipherlist)):
        factors.append(i) if len(cipherlist)%i == 0 else None
    print(f"Length of cipher = {len(cipherlist)}")
    print("Acceptable number of rows/cols = {}".format(factors))
    if COLS*ROWS != len(cipherlist):
        print("\nError: Input columns & rows are not factors of cipher's length. Terminating program.", file = sys.stderr)
        sys.exit(1)

def key_to_int(key):
    # Turn keys into integers and check for validity
    key_list = [int(number) for number in key.split()]
    if len(key_list) != COLS or max(key_list) > COLS or min(key_list) < -COLS or 0 in key_list:
        print("\nError: Problem with keys. Terminating", file = sys.stderr)
        sys.exit(1)
    return key_list

def build_matrix(key_int, cipherlist):
    matrix = []
    for key in key_int:
        index = abs(key) - 1
        if key > 0:
            templist = [cipherlist[i] for i in range(index*ROWS,(index+1)*ROWS)]
            matrix.append(templist)
        if key < 0:
            templist = [cipherlist[i] for i in range((index+1) * ROWS - 1, index * ROWS - 1, -1)]
            matrix.append(templist)

    #for i in range(len(matrix)):
    #    matrix[i].remove(matrix[i][ROWS - 1])

    return matrix

def decrypt(matrix):
    plaintext = ""

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            plaintext += matrix[row][col] + " "
    return plaintext

def main():
    # Print decrypted plain text
    print(f"Ciphertext = {ciphertext}")
    print(f"Trying {COLS} columns.")
    print(f"Trying {ROWS} rows.")
    print(f"Trying keys = {key}.")

    # split elements into words
    cipherlist = [word for word in ciphertext.split()]
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int,cipherlist)
    plaintext = decrypt(translation_matrix)
    print(plaintext)

if __name__ == '__main__':
    main()