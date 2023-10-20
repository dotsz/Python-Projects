import q1

def prompt_for_1_to_9():
  """
  Prompts the user to enter an integer from 1 to 9

  Precondition:
  None.

  Postcondition:
  - Returns an integer representing the user's input if it is between 1 and 9.

  """
  disk_number = input("Enter an integer from 1 to 9: ")
  disk_number = disk_number.strip('\'"') #Removes quotations on input, for cases where input is a string with quotation i.e. ("1", "0")
  
  is_it_valid = q1.is_1_to_9(disk_number) 
  
  if is_it_valid is True: #base case, returns the input as integer type if it is valid (= 1 to 9), stops the recursion.
    return int(disk_number)
    
  else: #recursive case, calls prompt_for_1_to_9 when the input is invalid (!= 1 to 9)
    print("Invalid input.")
    return prompt_for_1_to_9() 
    # needs to return the value of prompt_for_1_to_9, otherwise the value would be 'None', which also breaks the next recursion as none value is passed

  
  
    
  