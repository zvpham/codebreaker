alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

# prerequisite - shift is an integer
# shifts the alphabet by shift
def encode_ceasar_cipher(message, shift):
  
  shifted_alphabet = [""] * 26
  encoded_message = ""
  
  for i in range(26):
    if i - shift <= -1:
      shifted_alphabet[i - shift + 26] = alphabet[i]
    else:
      shifted_alphabet[i - shift] = alphabet[i]
      
  for letter in message:
    if letter in alphabet:
      encoded_message += shifted_alphabet[alphabet.index(letter)]
    else:
      encoded_message += letter
  return encoded_message

def decode_ceasar_cipher(message, shift):
  shifted_alphabet = [""] * 26
  decoded_message = ""
  
  for i in range(26):
    if i - shift <= -1:
      shifted_alphabet[i - shift + 26] = alphabet[i]
    else:
      shifted_alphabet[i - shift] = alphabet[i]
      
  for letter in message:
    if letter in alphabet:
      decoded_message += alphabet[shifted_alphabet.index(letter)]
    else:
      decoded_message += letter
  print(decoded_message)

def encode_vignere_cipher(message, key):
  count = 0
  encoded_message = ""
  index = -1
  
  for letter in message:
    if letter in alphabet:
      if alphabet.index(letter) + alphabet.index(key[count]) > 25:
          index = alphabet.index(letter) + alphabet.index(key[count]) - 26
      else:
          index = alphabet.index(letter) + alphabet.index(key[count])
      encoded_message += alphabet[index]
      print(f"{key[count]} + {alphabet[index]} + {letter}")
      if count >= len(key) - 1:
        count = 0
      else:
        count += 1
    else:
      encoded_message += letter
      
    
  return encoded_message
       
shift = int(input("how much do you want to shift "))

file1 = open('message.txt', 'r')
message = file1.read().lower()

message.lower()
"""
cipher_text = encode_ceasar_cipher(message, shift)
print("")
print(cipher_text)
print("")
decode_ceasar_cipher(cipher_text, shift)
"""
print("test")
print(encode_vignere_cipher(message, "key"))