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

  # creates a list of unique letters from the 'letter' variable
  unique_letters = set(letter.lower())
  english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
  counter = 0
  index = 0
  while index < len(strng):
    if strng[index].lower() in english_alphabet:
      if strng[index].lower() in unique_letters:
          counter += 1
    else:
      raise AssertionError("String must not contain non-letter")
    index += 1
  return counter