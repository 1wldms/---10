def get_original_text():
    with open('plain.txt', 'r') as f:
        for line in f:
            return
        
def get_shift_amount():
    return

def remove_nonletters(input_text):
    
    return

def cipher(text, shift_amount):
    return

def decipher(text, shift_amount):
    return


if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'{cipher_text=}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'{decipher_text=}')