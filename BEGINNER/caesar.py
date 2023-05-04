alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
#     cipher_text = ""
#     for l in text:
#         i = alphabet.index(l)
#         new = i + shift
#         if new > 25:
#             new = new - 26
#             l = alphabet[new]
#         else:
#             l = alphabet[new]
#         cipher_text += l
#     print(f"The encoded text is {cipher_text}")
#
#
# def decrypt(text, shift):
#     decipher_text = ""
#     for letter in text:
#         i = alphabet.index(letter)
#         new = i - shift
#         if new < 0:
#             new = new + 26
#             letter = alphabet[new]
#         else:
#             letter = alphabet[new]
#         decipher_text += letter
#     print(f"The decoded text is {decipher_text}")
#
#
# if direction == 'encode':
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)
def caesar(direction, text, shift):
    decode_text = ""
    encode_text = ""
    # for letter in text:
    #     ind = alphabet.index(letter)
    if shift > 26:
        shift = shift % 26
    if direction == 'encode':
        for letter in text:
            if letter in alphabet:
                ind = alphabet.index(letter)
                ind1 = ind + shift
                if ind1 > 25:
                    ind1 -= 26
                letter = alphabet[ind1]
                encode_text += letter
            else:
                encode_text += letter
        print(f"The encoded text is {encode_text}")
    elif direction == 'decode':
        for letter in text:
            if letter in alphabet:
                ind = alphabet.index(letter)
                ind2 = ind - shift
                if ind2 < 0:
                    ind2 += 26
                letter = alphabet[ind2]
                decode_text += letter
            else:
                decode_text += letter
        print(f"The decoded text is {decode_text}")


caesar(direction, text, shift)

# def caesar(start_text, shift_amount, cipher_direction) :
# end text =
# for letter in start text:
# = alphabet. index(letter)
# position
# if cipher_direction
# == "decode":
# shift amount -1
# new_position
# = position + shift_amount
# 1
# end _ text += alphabet [new_position]
# print (f" The {cipher_direction}d text is {end _ text}" )
