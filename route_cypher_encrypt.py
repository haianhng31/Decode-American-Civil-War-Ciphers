import sys
import random

'''plaintext = 'We will run the batteries at Vicksburg the night of April 16 and process to Grand Gulf where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter.'
codewords = {'Batteries': 'HOUNDS', 'Vicksburg': 'ODOR', 'April':'CLAYTON', '16': 'SWEET',
             'Grand':'TREE', 'Gulf':'OWL', 'Forts':'BAILEY','River':'HICKORY', '25':'MULTIPLY',
             '29':'ADD', 'Admiral':'HERMES','Porter':'LANGFORD'}'''

plaintext = 'Yeu Hai Anh. She ate and left no crumps. I mean the ideas of this post. It reenforces the suffering of women rather than challenging and smashing it.'
codewords = {'Yeu':'HATE','ate':'DIE','ideas':'BOOBIES','suffering':'FLOWER','smashing':'BIRD','women':'CAR'}

codewords_upper = {key.upper(): value.upper() for key, value in codewords.items()}

def prep_text(plaintext):
    # convert to upper case, delete the and replace by code words
    replaced_text = []
    words = list(plaintext.replace(".", "").replace(",", "").split())
    for word in words:
        word = word.upper()
        if word in codewords_upper.keys():
            word = codewords_upper[word]
        replaced_text.append(word)
    print('The replaced message is: {}'.format(replaced_text))
    return replaced_text

def get_row_col(replaced_text):
    factors = [i for i in range(2,len(replaced_text)) if len(replaced_text) % i == 0]
    print("Message's length is: {}".format(len(replaced_text)))
    print('Factors of length of the message are: {}'.format(factors))
    rows = int(input('Type number of rows: '))
    cols = int(input('Type number of columns: '))
    if int(cols*rows) != int(len(replaced_text)):
        print('\nError: Problem with keys. Terminating', file = sys.stderr)
        sys.exit(1)
    return rows, cols

def add_dummy_words(replaced_text, cols):
    dummy_words = ['LOVE', 'HATE', 'ENEMY', 'LOVER', 'LAPTOP', 'GUN', 'FILLER', 'ROSE', 'VIOLET', 'PINK', 'BARBIE','BOMB','DIVORCE']
    for i in range(cols):
        replaced_text.append(random.choice(dummy_words))
    print('The message with dummy words is: {}'.format(replaced_text))
    return replaced_text

def turn_to_matrix(full_text,rows,cols):
    text_matrix = [[] for _ in range(rows+1)]  # Create a list of empty lists for each row
    for r in range(rows+1): #7
        for c in range(cols): #6
            text_matrix[r].append(full_text[r*cols + c%cols])
    #print('The message matrix is:\n{}'.format(text_matrix))
    print('The message matrix is:\n{}'.format('\n'.join(map(str, text_matrix))))

    return text_matrix

def get_key(text_table):
    while True:
        key_candidate = input('Type keys here: ')
        key_lst = [int(number) for number in key_candidate.split(" ")]
        cols = len(text_table[0])
        if len(key_lst) != cols or max(key_lst) > cols or min(key_lst) < -cols or 0 in key_lst:
            print('\nError: Problem with keys. Try again', file = sys.stderr)
        else:
            break
    print('Keys accepted = {}'.format(key_lst))
    return key_lst

def encrypt(text_matrix,keys):
    encrypted = ""
    for key in keys:
        index = abs(key) - 1
        if key < 0:
            encrypted += ' '.join(text_matrix[i][index] for i in range(len(text_matrix)-1,-1,-1)) + ' '
        if key > 0:
            encrypted += ' '.join(text_matrix[i][index] for i in range(len(text_matrix))) + ' '
    print('The encrypted message is: {}'.format(encrypted))
    return encrypted
def main():
    print('The initial message is: {}'.format(plaintext))
    replaced_text = prep_text(plaintext)
    rows, cols = get_row_col(replaced_text)
    full_text = add_dummy_words(replaced_text,cols)
    text_matrix = turn_to_matrix(full_text,rows,cols)
    keys = get_key(text_matrix)
    encrypted_text = encrypt(text_matrix,keys)

if __name__ == '__main__':
    main()