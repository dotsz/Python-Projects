def solve_hanoi(disk_number, source_tower, target_tower):
  """
  Solve the Towers of Hanoi puzzle for a given number of disks.

  Preconditions:
  - disk_number: Must be a positive integer representing the number of disks.
  - source_tower: Must be an integer representing the source tower (1, 2, or 3).
  - target_tower: Must be an integer representing the target tower (1, 2, or 3).

  Postconditions:
  - Returns a string representing the sequence of moves required to solve the Towers of Hanoi puzzle.

  """
  assert isinstance(disk_number, int) and disk_number > 0, "The number of disks must be a positive integer."
  assert source_tower in [1, 2, 3], "Source tower number must be 1, 2, or 3."
  assert target_tower in [1, 2, 3], "Target tower number must be 1, 2, or 3."
    
  if disk_number == 1:
    return f"Move disk 1 from tower {source_tower} to tower {target_tower}.\n"
  else:
    spare_tower = 6 - source_tower - target_tower 
    step1 = solve_hanoi(disk_number - 1, source_tower, spare_tower)
    step2 = f"Move disk {disk_number} from tower {source_tower} to tower {target_tower}.\n"
    step3 = solve_hanoi(disk_number - 1, spare_tower, target_tower)
    
    return f"{step1}{step2}{step3}"
