import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase

def alphabet_position(letter):
  if letter.islower():
    return lower.index(letter)
  else:
    return upper.index(letter) 

def rotate_character(char, rot):

  new_index = (alphabet_position(char) + rot) % 26
  if char.islower():
    return lower[new_index]
  else:
    return upper[new_index]

def encrypt(text, rot):
  new_string = ''

  for char in text:
    if char.isalpha():
      new_string = new_string + rotate_character(char, rot)
    else:
      new_string = new_string + char

  return new_string
