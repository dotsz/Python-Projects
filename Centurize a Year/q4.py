def centurize_year(year):
  """
  returns which century the given year is in
  """
  century = 0
  #section for checking which era the year is in
  if year < 0:
    year = -year
    era = 'BCE'
  else:
    era = 'ACE'

  century = year // 100 + 1 # finds the century (╯°□°)╯︵ ┻━┻ 

  #section for concatenation of th, st, nd and rd
  if century % 100 > 9 and century % 100 < 21:
    suffix = 'th'
  else:
    if century % 10 == 1:
      suffix = "st"
    elif century % 10 == 2:
      suffix = 'nd'
    elif century % 10 == 3:
      suffix = 'rd'
    else:
      suffix = 'th'

  return str(century) + suffix + ' century ' + era
