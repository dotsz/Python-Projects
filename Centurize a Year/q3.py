import q2

def is_year_lucky(year):
  """
  returns whether or not the given year is a lucky year
  """
  return q2.is_leapyear(year) and (year%7 == 0 or year%13 == 0)