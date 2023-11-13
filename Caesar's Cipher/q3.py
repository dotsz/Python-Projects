import q2
def num_vowels(text):
  """
  Counts the number of vowels in the given string. The letter 'y' is counted as a vowel, except 
  when it is the first letter of a word and there are other vowels in the word.

  Precondition: 
  - text: a string to search within. The string should contain only letters.

  Postcondition: 
  - Returns the number of vowels in the string.
  """
  assert isinstance(text, str), "Input should be a string"
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel_counter = 0
  y_counter = 0

  for current_vowel in vowels:  # counts the vowels in the string
    vowel_counter += q2.num_letters(text, current_vowel)  # Count each vowel in the text using the num_letters function from q2
  y_counter += q2.num_letters(text, 'y')
  if text[0].lower(
  ) == 'y' and vowel_counter != 0:  # 'y' does not count as vowel if it's the first letter in the string with other vowels
    y_counter -= 1
  return vowel_counter + y_counter