# Solve the preprocessed result with https://www.boxentriq.com/code-breaking/cryptogram

import string


def preprocess():

    with open('ciphertext.txt', 'r', encoding = 'utf-8') as f:
        ciphertext = f.read()

    keep = [' ', '{', '}', '.', ',', '!', '_', '?', '\'']
    replace = {}

    symbols = set(ciphertext) - set(keep) - set(replace.keys())
    table = str.maketrans(''.join(symbols), string.ascii_letters[:len(symbols)])

    processed = ciphertext.translate(table)

    for before, after in replace.items():
        processed = processed.replace(before, after)

    with open('table-1.txt', 'w', encoding = 'utf-8') as f:
        before, after = zip(*table.items())
        f.write(''.join([chr(c) for c in before]))
        f.write('\n')
        f.write(''.join([chr(c) for c in after]))

    with open('preprocessed.txt', 'w', encoding = 'utf-8') as f:
        f.write(processed)


def get_final_table():

    with open('table-1.txt', 'r', encoding = 'utf-8') as f:
        table_1 = str.maketrans(f.readline().strip(), f.readline().strip())

    # You need to write the second table to table-2.txt first after cracking the preprocessed cipher
    with open('table-2.txt', 'r', encoding = 'utf-8') as f:
        table_2 = str.maketrans(f.readline().strip(), f.readline().strip())

    table_final = {}

    for k in table_1.keys():
        table_final[chr(k)] = chr(table_2[table_1[k]])
    
    with open('table-final.txt', 'w', encoding = 'utf-8') as f:
        before, after = zip(*table_final.items())
        f.write(''.join(before))
        f.write('\n')
        f.write(''.join(after))


if __name__ == "__main__":

    preprocess()
    # get_final_table()