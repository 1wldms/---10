



if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'{cipher_text=}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'{decipher_text=}')