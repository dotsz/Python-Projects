def is_1_to_9(disk_number):
  """
  Checks if disk_number is either an integer or a string representation of integers 1 to 9
  
  Precondition: 
  - Should be a single value input
  
  Postcondition:
  - Returns True if the disk_number is either an integer or a string representation of integers 1 to 9
  - Returns False otherwise
  
  """
  if isinstance(disk_number, str) and disk_number.isnumeric(): #checks if the input is of numerical value
      disk_number = int(disk_number) # converts input into an int
  return isinstance(disk_number, int) and 1 <= disk_number <= 9


  