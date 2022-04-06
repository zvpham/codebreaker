alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

# prerequisite - shift is an integer
# shifts the alphabet by shift
def encode_ceasar_cipher(message, shift):
  
  shifted_alphabet = [""] * 26
  encoded_message = ""
  
  for i in range(26):
    if i + shift >= 26:
      shifted_alphabet[i + shift - 26] = alphabet[i]
    else:
      shifted_alphabet[i + shift] = alphabet[i]
      
  for letter in message:
   encoded_message += shifted_alphabet(alphabet.getindexof("letter"))

shift = int(input("how much do you want to shift "))

file1 = open('message.txt', 'r')
message = file1.read()

encode_ceasar_cipher(message, shift)