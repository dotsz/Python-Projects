def make_times_table(number):
  """
  Creates a times table from the input number
  Precondition: number is an integer and must be greater than 0.
  Postcondition: returns a list of numbers that are the product of the number and each number from 1 to 10.
  """
  assert isinstance(number, int), "number must be an integer"
  # if the input is less than 0, return empty [] 
  # else make a 2-dimension list using nested list comprehension
  # each index is composed of product of the input and each number from 1-10 
  return [] if number < 0 else [[i*j for j in range(number + 1)] for i in range(number + 1)]