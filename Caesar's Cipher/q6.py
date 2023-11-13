import q5
def cipher(string_to_encrpyt, shift_count):
  """
  Encrypts the given string by shifting the characters in the string by a specified number of positions.
  
  Precondition: 
  - string_to_encrypt: The string to be encrypted. Can contain both alphabetic and non-alphabetic character
  - shift_count: Must be an Integer
                 Specifies the number of shift and direction of the shift
                 Positive value shifts characters to the right
                 Negative value shifts characters to the left
                 
  Postcondition: 
  - Returns a string that is the encrypted version of the input string 
  """
  assert isinstance(string_to_encrpyt, str), "Input must be a string"
  assert isinstance(shift_count, int), "Shift count must be an integer"
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shifted_alphabet = q5.shift(
      alphabet, shift_count
  )  #Shifts alphabet by shift_count (Use shift function from q5.py module)
  encrypted_string = ""

  for letter_in_string in string_to_encrpyt:
    if letter_in_string.isalpha():  #Checks if letter is alphabetic
      upper_case = letter_in_string.isupper(
      )  #If the current letter is in uppercase. Saves it in a variable
      index = alphabet.index(letter_in_string.lower())
      shifted_letter = shifted_alphabet[index]
      if upper_case:  # If the current letter is in uppercase, uppercase the shifted letter before adding to the encryted string
        encrypted_string += shifted_letter.upper()
      else:
        encrypted_string += shifted_letter
    else:  # If the current letter is not alphabetic
      encrypted_string += letter_in_string
  return encrypted_string