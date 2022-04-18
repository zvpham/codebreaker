alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
is_capital = []
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
  return decoded_message

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
      #print(f"{key[count]} + {alphabet[index]} + {letter}")
      if count >= len(key) - 1:
        count = 0
      else:
        count += 1
    else:
      encoded_message += letter
  return encoded_message

def decode_vignere_cipher(message, key):
  count = 0
  decoded_message = ""
  index = -1
  
  for letter in message:
    if letter in alphabet:
      if alphabet.index(letter) - alphabet.index(key[count]) < 0:
          index = alphabet.index(letter) - alphabet.index(key[count]) + 26
      else:
          index = alphabet.index(letter) - alphabet.index(key[count])
      decoded_message += alphabet[index]
      #print(f"{key[count]} + {alphabet[index]} + {letter}")
      if count >= len(key) - 1:
        count = 0
      else:
        count += 1
    else:
      decoded_message += letter
  return decoded_message

def capital_letter(text):
  count = 0
  capitalized_text = ""
  for letter in text:
    if is_capital[count] == 1:
      capitalized_text += letter.upper()
    else:
      capitalized_text += letter
    count += 1
  return capitalized_text

message = input("type a message you want encoded: ")
for letter in message:
  if letter == letter.upper():
    is_capital.append(1)
  else:
    is_capital.append(0)


shift = int(input("how much do you want to shift: "))
key =  input("what is the key: ")
print("")

message = message.lower()
ceasar_cipher_text = capital_letter(encode_ceasar_cipher(message, shift))
ceasar_decoded_message = capital_letter(decode_ceasar_cipher(ceasar_cipher_text, shift))

vignere_cipher_text = capital_letter(encode_vignere_cipher(message, key))
vignere_decoded_message = capital_letter(decode_vignere_cipher(vignere_cipher_text, key))


file1 = open('message.txt', 'w')
file1.write(f"original message: {capital_letter(message)}\n")
file1.write(f"Ceasar cipher with a shift of {shift}: {ceasar_cipher_text} \nDecoded cipher: {ceasar_decoded_message}\n")
file1.write(f"\noriginal message: {capital_letter(message)}\n")
file1.write(f"Vignere cipher with a key of {key}: {vignere_cipher_text} \nDecoded cipher: {vignere_decoded_message}\n")
file1.close

file1 =  open('message.txt', 'r')
print(file1.read())
file1.close()