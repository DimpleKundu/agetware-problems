def caesar_cipher(message, shift, encode=True):
    result = []
    shift = shift if encode else -shift
    
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    
    return ''.join(result)


message =input("enter a string to encode: ")
shifts = int(input("enter number of shifts: "))
encoded_message = caesar_cipher(message, shifts)  # Encoding
decoded_message = caesar_cipher(encoded_message, shifts, encode=False)  # Decoding

print("Encoded:", encoded_message)
print("Decoded:", decoded_message)
