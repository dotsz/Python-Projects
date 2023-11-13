def num_letters(strng, letter):
  """
  Counts the number of times a specified letter or set of letters appears in a given string. 
  The comparison is case-insensitive.

  Precondition: 
  - strng: a string to search within.
  - letter: a string containing the letter(s) to count.

  Postcondition: 
  - Returns the number of times the specified letter(s) appear in the string.
  """
  assert isinstance(strng, str), "Input should be a string"
  assert isinstance(letter, str), "Input should be a string"
  unique_letters = set(letter.lower())  # creates a list of unique letters from the 'letter' variable
  english_alphabet = 'abcdefghijklmnopqrstuvwxyz' 
  counter = 0
  for current_letter_in_string in strng:
    if current_letter_in_string.lower() in english_alphabet:
      for current_letter_in_letter in unique_letters:
        if current_letter_in_string.lower() == current_letter_in_letter.lower():
          counter += 1
    else:
      raise AssertionError("String must not contain non-letter")
  return counter