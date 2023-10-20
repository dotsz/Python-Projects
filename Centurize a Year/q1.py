def get_year_animal(year):
  """
  returns zodiac sign for the given year
  """
  remainder = year % 12
  if remainder == 0:
    zodiac_sign = 'Monkey'
  elif remainder == 1:
    zodiac_sign = 'Rooster'
  elif remainder == 2:
    zodiac_sign = 'Dog'
  elif remainder == 3:
    zodiac_sign = 'Pig'
  elif remainder == 4:
    zodiac_sign = 'Rat'
  elif remainder == 5:
    zodiac_sign = 'Ox'
  elif remainder == 6:
    zodiac_sign = 'Tiger'
  elif remainder == 7:
    zodiac_sign = 'Rabbit'
  elif remainder == 8:
    zodiac_sign = 'Dragon'
  elif remainder == 9:
    zodiac_sign = 'Snake'
  elif remainder == 10:
    zodiac_sign = 'Horse'
  elif remainder == 11:
    zodiac_sign = 'Goat'
  return zodiac_sign
