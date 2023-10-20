def centurize_year(year):
  century = 0
  
  if year <0:
    year = -year
    era  = 'BCE'
  else: 
    era = 'ACE'
    
  if year >= 0 and year <=99:
    century = (year / 100) + 1
  elif year % 99 == 0:
    century = year / 100
  elif year % 99 != 0:
    century = (year / 100) + 1
  century = int(century)
  
  if century % 100 > 9 and century % 100 < 21:
    suffix = 'th'
  else:
    last_digit = century % 10
    if last_digit == 1:
      suffix = "st"
    elif last_digit == 2:
      suffix = 'nd'
    elif last_digit == 3:
      suffix = 'rd'
    else:
      suffix = 'th'
  
  return str(century) + suffix + ' century ' + era