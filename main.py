import argparse

def get_original_text():
    with open('plain.txt', 'r') as f:
        for line in f:
            input_text = line
            return input_text
        
def get_shift_amount():
    parser = argparse.ArgumentParser(description='Shift 숫자를 입력받는 예제')
    parser.add_argument('--shift', type=int, required=True, help='문자를 이동할 숫자')
    args = parser.parse_args()
    return args.shift

def remove_nonletters(input_text):
    result = []
    for word in input_text:
        if word.isalpha():
            result.append(word)
    input_text = ''.join(result)
    
    return input_text

def cipher(text, shift_amount):
    
    # 5 단어씩 나누기, 아직 cipher 하기 전
    result = []
    for i in range(0, len(text), 5):
        split = text[i:i+5]
        result.append(split)
    text = ' '.join(result)
    
    return text

def decipher(text, shift_amount):
    
    #암호화 코드 붙이기
    text = text.replace(' ','')
    return text



if __name__ == '__main__':
    original_text = get_original_text()
    shift_amount = get_shift_amount()
    text_letter_only = remove_nonletters(original_text)
    cipher_text = cipher(text_letter_only, shift_amount)
    print(f'{cipher_text=}')
    decipher_text = decipher(cipher_text, shift_amount)
    print(f'{decipher_text=}')