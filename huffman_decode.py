def huffman_decode(encoded_text, codes):
    reverse_codes = {code: char for char, code in codes.items()}
    decoded_text, temp_code = "", ""

    for bit in encoded_text:
        temp_code += bit
        if temp_code in reverse_codes:
            decoded_text += reverse_codes[temp_code]
            temp_code = ""

    print(decoded_text)

if __name__ == "__main__":
    codes = {
        ' ': '1011',
        '.': '1110',
        'D': '1000',
        'c': '000',
        'd': '001',
        'e': '1001',
        'i': '010',
        'm': '1100',
        'n': '1010',
        'o': '1111',
        's': '011',
        'u': '1101',
    }
    encoded_text = "100011110001001101000111111011001010011000010110011010111110"
    huffman_decode(encoded_text, codes)
