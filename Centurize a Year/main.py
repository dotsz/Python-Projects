# Use comments to manage which of your code files to run

import q1
import q2
import q3
import q4

# You may add code below here to do your own tests of your functions

year = int(input('Enter a year: '))
print("The Year {} is... \n...the year of the {}".format(
    year, q1.get_year_animal(year)))

if q2.is_leapyear(year):
  print('...is a leap year')
else:
  print('...not a leap year')

if q3.is_year_lucky(year):
  print('...a lucky year')
else:
  print('...not a lucky year')

print(q4.centurize_year(year))
