def shift(string_to_shift, shift_count):
  """
  Shifts the characters in the given string to the right or left by a specified number of positions. 
  The direction of the shift is determined by the sign of the shift count (positive for right, negative for left).

  Precondition: 
  - string_to_shift: a string to be shifted.
  - shift_count: an integer indicating the number of positions to shift.

  Postcondition: 
  - Returns a string that is the shifted version of the first parameter.
  """
  assert isinstance(string_to_shift, str), "1st parameter should be a string"
  assert isinstance(shift_count, int), "2nd parameter should be a Int"
   
  shifted_string = string_to_shift
  
  if shift_count >= 0: # if shift count is positive, shift string to the right
    shift_count = shift_count % len(string_to_shift) 
    for _ in range(shift_count):
      shifted_string = string_to_shift[-1] + string_to_shift[:-1]
      string_to_shift = shifted_string
  elif shift_count < 0: # if shift count is negative, shift string to the left
    shift_count = -shift_count % len(string_to_shift)
    for _ in range(shift_count):
      shifted_string = string_to_shift[1:len(string_to_shift)] + string_to_shift[0]
      string_to_shift = shifted_string
  return shifted_string